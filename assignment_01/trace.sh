
#!/bin/bash

cd /home/pi/Projects/GitHub/ee810/assignment_01/

traceroute -m 20 github.com >> tr_github.txt
python process.py tr_github.txt dt_github.txt

traceroute -m 20 jovemnerd.com.br >> tr_jovemnerd.txt
python process.py tr_jovemnerd.txt dt_jovemnerd.tx

traceroute -m 20 submarino.com.br >> tr_submarino.txt
python process.py tr_submarino.txt dt_submarino.txt
