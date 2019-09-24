#!/usr/bin/env bash

# Preparation enviornment
sudo mkdir /etc/interior_sensor_device/
sudo chown $USER:$USER /etc/interior_sensor_device/
# You must be inside the root folder of this project!
cp -r $(pwd)/* /etc/interior_sensor_device/

# Required
pip3 install -r /etc/interior_sensor_device/requirements.txt

# For systemd
sudo useradd -r -s /bin/false interior_sensor_device_user
sudo chown -R interior_sensor_device_user:interior_sensor_device_user /etc/interior_sensor_device
sudo chmod +x /etc/interior_sensor_device/start.py
sudo cp /etc/interior_sensor_device/systemd/interior_sensor_device.service /etc/systemd/system/interior_sensor_device.service

# Hints

printf "
#######################################################
# - Edit the start.py in /etc/interior_sensor_device  #
# - You may what to edit the user of the service.     #
#######################################################

# Let's start the service
sudo systemctl enable interior_sensor_device
sudo systemctl start interior_sensor_device
"