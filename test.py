#!/usr/bin/python3

import os

#There should be 65535 ports

for i in range(1,3):
	print(i)
	url = str(("curl portquiz.net:{}").format(i))
	result = os.system(url)
	print(result)
