
#!/bin/bash

cd /home/pi/Projects/GitHub/ee810/assignment_01/

traceroute -m 20 github.com >> tr_github.txt
python process.py tr_github.txt dt_github.txt
python plot_cdf.py dt_github.txt output/github.png

traceroute -m 20 jovemnerd.com.br >> tr_jovemnerd.txt
python process.py tr_jovemnerd.txt dt_jovemnerd.txt
python plot_cdf.py dt_jovemnerd.txt output/jovemnerd.png

traceroute -m 20 submarino.com.br >> tr_submarino.txt
python process.py tr_submarino.txt dt_submarino.txt
python plot_cdf.py dt_submarino.txt output/submarino.png

traceroute -m 20 sae.infnet.edu.br >> tr_infnet.txt
python process.py tr_infnet.txt dt_infnet.txt
python plot_cdf.py dt_infnet.txt output/infnet.png

traceroute -m 20 unesp.br >> tr_unesp.txt
python process.py tr_unesp.txt dt_unesp.txt
python plot_cdf.py dt_unesp.txt output/unesp.png
