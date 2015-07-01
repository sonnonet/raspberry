# Author: Jeonghoonkang, Wonsikko, Jungukchoi 

import datetime
import requests
import json


def get_last_value(server_url, metric, tags, start='10m-ago', aggregator='sum'):
	assert isinstance(server_url, str)
	assert isinstance(metric, str)
	assert isinstance(tags, dict)
	assert isinstance(start, str)
	assert isinstance(aggregator, str)

	url = 'http://%s/api/query?start=%s' % (server_url, start)
	url += '&m=%s:%s' % (aggregator, metric)
	if len(tags):
		url += '{'
		for (k, v) in tags.items():
			url += '%s=%s,' % (k, v)
		url = url[:-1] + '}'
	
	ret = requests.get(url=url)
	print ret
	if ret.ok:
		#ret = ret.json() # this line is not working. use below loads() rather than .json()
		data = json.loads(ret.text)
		assert isinstance(data, (list, tuple))
		dps = data[0]['dps']
		assert isinstance(dps, dict)  # 't' --> value
		if len(dps):
			max_time = sorted(dps.keys())[-1]
			value = dps[max_time]
			epoch = float(max_time)
			ts = datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')
			return (value, epoch, ts)

def start():
	print get_last_value('125.7.128.53:4242', 'rc1.co2.ppm', {'name': 'co2.001'})
