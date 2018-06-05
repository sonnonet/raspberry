# 라즈베리파이 비콘 스캐너 만들기

```
### Raspberry pi Update ###

sudo apt-get update && sudo apt-get upgrade
sudo apt-get install libusb-dev libdbus-1-dev libglib2.0-dev libudev-dev libical-dev libreadline-dev
```

```
### BlueZ's Install ###

sudo wget www.kernel.org/pub/linux/bluetooth/bluez-5.11.tar.xz
sudo unxz bluez-5.11.tar.xz
sudo tar xvf bluez-5.11.tar
cd bluez-5.11
sudo ./configure --disable-systemd
sudo make
sudo make install

sudo apt-get install python-bluez

sudo shutdown -r now
```
```

### Beacon Scanner Install ###

git clone https://github.com/switchdoclabs/iBeacon-Scanner-
sudo chown pi iBeacon-Scanner-
sudo chgrp pi iBeacon-Scanner-
```
```
### 실행 ###

sudo python testblescan.py
```

![Data](https://raw.githubusercontent.com/jeonghoonkang/raspberry/master/img/iBeacon_Scanner.png)
