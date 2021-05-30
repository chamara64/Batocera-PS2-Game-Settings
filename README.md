Batocera PS2 Game Settings mod 1.2 (updated for Batocera 27) (!!! THIS WILL NOT WORK FOR BATOCERA 30 !!!)

# Batocera PS2 Game settings (formerly PCSX2 custom-configs)
This add-on will enable Batocera to keep separate sets of settings (speed hacks, plugin configs etc) for individual games for the PCSX2 emulator. The roms will play (via the EmulationStation frontend) with these per-game settings automatically loaded, effectively putting an END to the pain of opening up PCSX2 settings and tweaking around every time you want to switch to a different game that requires its own set of unique PCSX2 configs to run best (Oh you know what I'm talking about). 


# Installation
Step 1: Extract the "ps2_game_settings.tar" and copy the "ps2_game_settings" directory to the root of the Batocera "SHARE" partition (along side the bios, roms, themes etc. directories). 

VERY IMPORTANT!: Make sure "ps2_game_settings/files/pcsx2-custom-config" and "ps2_game_settings/install.py" script files have permission to excecute as programs. (right-click > Properties). And if you haven't properly configured the PCSX2 settings at least once on your Batocera installation already (File manager -> Applications-> Pcsx2), (specially the controller mapping) do that before continuing on to step 2. 

Step 2: Start Batocera. Open the native file manager (F1 key on the keyboard) navigate to the "ps2_game_settings" directory and execute the "install.py" script by double-clicking on it.

Step 3: That it you're done! There is no step 3.


# Configuring individual games
1: Navigate to "ps2_game_settings/games/[your game]" directory (via the native file manager F1 key).

2: Double click on the “pcsx2-custom-config” the script file to execute it, which will launch pcsx2. 

3: Tweak the settings for the game as you wish. Any changes to the settings made here will only effect this [game] and not others nor the default pcsx2 settings on Batocera. 

*Testing tip: The easiest way to see if this works is to pick a game and drastically change its shader saturation or contrast. The difference in settings from the other games should be obvious pretty much form the PS2 boot screen*


# Uninstalling 
Delete the "ps2_game_settings" directory and remove the following two lines from the "system/custom.sh" file.

*cd /userdata/ps2_game_settings*
*python start.py*


# known issue
If a game refuses to start and reverts back to the EmulaionStation menu, try deleting its folder in "pcsx2_custom_configs/games/" and start the game again.
