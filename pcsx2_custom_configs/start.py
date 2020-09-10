#!/usr/bin/env python

# Chamara64's PCSX2 custom configs addon for Batocera Linux

import os
import shutil

shutil.copy('./files/pcsx2Generator.py','/usr/lib/python2.7/site-packages/configgen/generators/pcsx2/pcsx2Generator.py')
shutil.copy('./files/pcsx2-custom-config','/usr/lib/python2.7/site-packages/configgen/generators/pcsx2/pcsx2-custom-config')

if not os.path.exists("games"):
	os.makedirs("games")

def ini_clone(pcsx2_ini, custom_config_ini_path, ini_filename):
	if not os.path.exists(custom_config_ini_path + ini_filename):
		if os.path.exists(pcsx2_ini + ini_filename):
			shutil.copy(pcsx2_ini + ini_filename, custom_config_ini_path + ini_filename)

for root, dirs, files in os.walk("/userdata/roms/ps2"):
	for thing in files:

		if(thing.endswith('.iso') or thing.endswith('.bin') or thing.endswith('.img') ):

			custom_config_path = "/userdata/pcsx2_custom_configs/games/"+ thing
			custom_config_ini_path = custom_config_path+"/inis/"
			pcsx2_ini = "/userdata/system/configs/PCSX2/inis/"

			if not os.path.exists(custom_config_path):
				os.makedirs(custom_config_ini_path)

			ini_clone(pcsx2_ini, custom_config_ini_path, "GSdx.ini")
			ini_clone(pcsx2_ini, custom_config_ini_path, "OnePAD.ini")
			ini_clone(pcsx2_ini, custom_config_ini_path, "PCSX2_ui.ini")
			ini_clone(pcsx2_ini, custom_config_ini_path, "PCSX2_vm.ini")
			ini_clone(pcsx2_ini, custom_config_ini_path, "spu2-x.ini")
			ini_clone(pcsx2_ini, custom_config_ini_path, "USBnull.ini")
			ini_clone(pcsx2_ini, custom_config_ini_path, "Dev9null.ini")
			ini_clone(pcsx2_ini, custom_config_ini_path, "FWnull.ini")

			shutil.copy("./files/pcsx2-custom-config", custom_config_path)
