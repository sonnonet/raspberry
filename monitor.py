# -*- coding: utf-8 -*-
# monitor.py

import platform
import sys
import os
import time
import traceback
import requests


SERVER_ADDR = '211.184.76.80'

def query_last_data_point(plug_id):
	url = 'http://%s/api/raw_plug_last/?plug_id=%d' % (SERVER_ADDR, plug_id)
	
	try:
		ret = requests.get(url, timeout=10)
		if ret.ok:
			ctx = ret.json()
			if ctx['code'] == 0:
				return ctx['result']['time'], ctx['result']['value']

	except Exception:
		traceback.print_exc()

	return None


# test
plug_id = 900101
while True:
	ret = query_last_data_point(plug_id)
	if ret is not None:
		t, v = ret
		if t > time.time() - 30:
			dt = time.time() - t 
			print 'plug %d operate correctly. (%.1f seconds ago, %f watt)' % (plug_id, dt, v)

		else:
			print 'plug %d may be not connected to server. (%.1f seconds ago, %f watt)' % (plug_id, dt, v)

	else:
		print 'plug %d does not exists on server!' % plug_id

	time.sleep(3.0)