# Batocera PCSX2 custom-configs 
This script will automatically create separate configuration files for individual roms on the PCSX2 emulator for Batocera Linux, as well as make the games run with those game specefic settings through the EmulationStation front end menu, effectively putting an END to the pain of changing PCSX2 settings everytime you want to switch to a different game. 


# Installation
Step 1: copy the "pcsx2_custom_configs" folder to the root of the Batocera "SHARE" partition (along side the bios, roms, themes etc. directories). 

 -> NOTE: If you haven't set up and configured the PCSX2 settings on your Batocera installation already, do that before continuing to step 2. 

Step 2: Execute the "install.py" file.

Step 3: That it youre done! There is no step 3.


# Configuring individual games
Navigate to "pcsx2_custom_configs/games/[your game]" directory and execute the “pcsx2-custom-config” file. Changes in settings made here will not effect other games or the default pcsx2 settings in the system.

# Uninstallation 
Simplay delete the "pcsx2_custom_configs" directory and the following lines from the "system/custom.sh" file

cd /userdata/pcsx2_custom_configs
python start.py
