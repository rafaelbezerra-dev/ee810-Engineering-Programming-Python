
#!/bin/bash

cd /home/pi/Projects/GitHub/ee810/assignment_01/

#traceroute -m 20 github.com >> tr_github.txt
#python process.py tr_github.txt dt_github.txt

traceroute -m 20 jovemnerd.com.br >> tr_jovemnerd.txt
python process.py tr_jovemnerd.txt dt_jovemnerd.txt

traceroute -m 20 submarino.com.br >> tr_submarino.txt
python process.py tr_submarino.txt dt_submarino.txt

traceroute -m 20 sae.infnet.edu.br >> tr_infnet.txt
python process.py tr_infnet.txt dt_infnet.txt

traceroute -m 20 unesp.br >> tr_unesp.txt
python process.py tr_unesp.txt dt_unesp.txt
