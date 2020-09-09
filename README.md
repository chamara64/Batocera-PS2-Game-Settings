# Batocera PCSX2 custom-configs 

This script will automatically create separate configuration files for individual roms on the PCSX2 emulator for Batocera Linux, as well as make the games run with those game specefic settings through the EmulationStation front end menu, effectively putting an END to the pain of going through PCSX2 plugin and speed hack settings everytime you want to play a different game. 

# Installation
Step 1: copy the "pcsx2_custom_configs" folder to the root of the Batocera "SHARE" partition (along side the bios, roms, themes etc. directories). Thats it.

Step 2: There is no step two.

NOTE: If you haven't set up and configured the PCSX2 settings on your Batocera installation already, do that before continuing. 

# How to use
open the file manager (via the F1 key) and execute (usually by double clicking) the “start” file in the pcsx2_custom_configs directory once after a boot.  


# Configuring individual games

To change configurations on individual games, navigate via the Batocera’s file manager to the directory with the name of your game  eg: “pcsx2_custom_configs/games/Tekken 5.iso/” and execute the “pcsx2-custom-config” file in it to open the pcsx2 application. Changes in settings made here will not effect other games or the default pcsx2 settings in the system.
