#!/bin/bash

cd /home/pi/Projects/GitHub/ee810/assignment_01/
traceroute github.com >> tr.txt
chmod +x rt_process.py
python rt_process.py
