# Batocera PCSX2 custom-configs 
This small add-on will enable Batocera Linux to keep separate configurations/settings for individual games on the PCSX2 emulator, as well as run those roms through the EmulationStation front end menu with thier own settings automatically loaded, effectively putting an END to the pain of changing PCSX2 settings every time you want to switch to a different game. tested with 5.25 and 5.26.

# Installation
Step 1: copy the "pcsx2_custom_configs" folder to the root of the Batocera "SHARE" partition (along side the bios, roms, themes etc. directories). NOTE: If you haven't configured the PCSX2 settings at least once on your Batocera installation already (File manager -> Applications-> Pcsx2), do that before continuing to step 2. 

Step 2: Start Batocera and execute the "install.py" file in the "pcsx2_custom_configs" folder using the native file manager (F1 key).

Step 3: That it you're done! There is no step 3.

# Configuring individual games
Navigate to "pcsx2_custom_configs/games/[your game]" directory and execute the “pcsx2-custom-config” file which will open up pcsx2. Changes in settings made here will not effect other games or the default pcsx2 settings in the system. 

*Testing tip: The easiest way to see if this works is to pick a game drastically change its shader saturation or contrast. the difference in settings from the other games should be obvious pretty much form the PS2 boot screen*

# Uninstalling 
Delete the "pcsx2_custom_configs" directory 

and remove the following lines from the "system/custom.sh" file.

*cd /userdata/pcsx2_custom_configs*

*python start.py*

# known issue
If a game refuses to start and reverts back to the EmulaionStation menu, try deleting its folder in "pcsx2_custom_configs/games/" and start the game again.
