#!/usr/bin/env python

# Chamara64's PCSX2 custom configs addon for Batocera Linux

import os

if not os.path.exists("/userdata/system/custom.sh"):

	f = open("/userdata/system/custom.sh", "w+")
	f.write("#!/bin/bash")
	f.write("\n")
	f.write("cd /userdata/pcsx2_custom_configs")
	f.write("\n")
	f.write("python start.py")
	f.close()

else:

	with open('/userdata/system/custom.sh') as f:
		if not 'python /userdata/pcsx2_custom_configs/start.py' in f.read():
			f = open("/userdata/system/custom.sh", "a")
			f.write("\n")
			f.write("cd /userdata/pcsx2_custom_configs")
			f.write("\n")
			f.write("python start.py")
			f.close()


os.system("./start.py")

#raw_input("promt: ")
