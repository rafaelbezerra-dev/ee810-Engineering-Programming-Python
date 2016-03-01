#!/bin/bash

traceroute github.com >> tr.txt
chmod +x rt_process.py
python rt_process.py
