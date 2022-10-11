#!/usr/bin/python3

import os,re,subprocess

#There should be 65535 ports


def check_port(port):
	proc = subprocess.Popen(["/usr/bin/curl -s portquiz.net:%s" % port, ""], stdout=subprocess.PIPE, shell=True)
	try:
		proc.communicate(timeout=1)
		return True
	except:
		return False
if __name__=='__main__':

	for port in range(1,7):
		if(check_port(port)):
			print(("{},").format(port),end="")
