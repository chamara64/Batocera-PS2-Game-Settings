# Batocera PCSX2 custom-configs 
This script will automatically create separate configuration files for individual roms on the PCSX2 emulator for Batocera Linux, as well as make the games run with those game specific configurations through the EmulationStation front end menu, effectively putting an END to the pain of changing PCSX2 settings every time you want to switch to a different game. tested with 5.25 and 5.26.

# Installation
Step 1: copy the "pcsx2_custom_configs" folder to the root of the Batocera "SHARE" partition (along side the bios, roms, themes etc. directories). NOTE: If you haven't set up and configured the PCSX2 settings on your Batocera installation already, do that before continuing to step 2. 

Step 2: Execute the "install.py" file.

Step 3: That it you're done! There is no step 3.

# Configuring individual games
Navigate to "pcsx2_custom_configs/games/[your game]" directory and execute the “pcsx2-custom-config” file which will open up pcsx2. Changes in settings made here will not effect other games or the default pcsx2 settings in the system.

*Testing tip: The easiest way to test if individual settings works is to change a games color saturation or contrast*

# Uninstalling 
Delete the "pcsx2_custom_configs" directory 

and remove the following lines from the "system/custom.sh" file.

*cd /userdata/pcsx2_custom_configs*

*python start.py*

# known issue
if a game refuses to start and reverts back to the EmulaionStation menu, try deleting its folder in "pcsx2_custom_configs/games/" and start the game again.
