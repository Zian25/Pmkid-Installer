# -*- coding: UTF-8 -*-
#!/bin/bash
import os, sys

print "Começando..."
os.system("apt-get update && apt-get upgrade && apt-get dist-upgrade && apt-get install libssl-dev && apt-get install libz-dev && apt-get install libpcap-dev && apt-get install libcurl4-openssl-dev")
os.system("clear")
print "Baixando" 
os.system("git clone https://github.com/ZerBea/hcxdumptool.git");
os.system("git clone https://github.com/ZerBea/hcxtools");
os.system("cd hcxdumptool && make && make install");
os.system("cd ..")
os.system("cd hcxtools && make && make install");
os.system("clear")
print "Concluido"


