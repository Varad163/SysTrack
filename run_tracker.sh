#!/bin/bash

cd /home/varad/Desktop/app_time_tracker
/usr/bin/python3 main.py track
systemctl --user start app-time-tracker
