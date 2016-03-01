#!/bin/bash

traceroute github.com >> /home/pi/Projects/GitHub/ee810/assignment_01/tr.txt
chmod +x rt_process.py
python rt_process.py
