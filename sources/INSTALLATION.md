# Slate for Windows 11 // Guide

After running the CLI utility check the ./downloads/sources folder and follow the guide here in order. If you wish to skip any steps please feel free to do so.

## Step 1 - AME Wizard (System - CORE)

AME Wizard is the primary tool used for stripping down bloat from Windows and running tweaks as bundled as possible. Slate uses Revi OS which requires this application.

Simply run the downloaded executable file that is located in this folder. Proceed to Step 2.

## Step 2 - Revi OS (System - CORE)

Revi OS is a bundled assortment of tweaks, debloating configs and optimizations for Windows 11.

In order to run the bundle or "playbook" you will simply:

1) Drag the respective playbook file to AME Wizard
2) Click next and accept all following licences
3) Select the respective tweaks you wish but ensure to Remove Defender (this can be replaced with a more lightweight anti-virus later if you need it) and Copilot
4) Allow the utility to run. This may take around ~ 5-10 minutes depending on the machine.
5) Let the application restart once completed or restart manually via Ctrl + Alt + Delete.
6) Upon restart open up Revision Tool (this application will be present on your desktop)
7) Select the following tweaks below:

[ Provide Tweaks Screenshot ]

## Step 3a - Optimizer (System - Polish)

Optimizer is an open source utility GUI hosted on GitHub that allows you to run more Windows 11 tweaks and remove specific UWP apps. For this script it is used to cover for anything missed by AME Wizard.

1) Open up Optimizer and select the following tweaks at a minimum.
2) You can also import the Slate pre-configured config file at `./src/config/Optimzier.json`

[ Provide Optimizer Tweaks Screenshot ]

## Step 3b - Win Memory Cleaner (System - Polish)

Win Memory Cleaner is a background utility that will remain running on your system to reduce the amount of processes present on your CPU improving performance. This in combination of disabling background apps is very very effective.

1) Open up the respective application and select "Start-up on Windows"

## Step 3c - Windows On Reins (EXPERT/OPTIONAL)

WOR is a highly effective script that strips the majority of Windows bloat and privacy concerns but at a system breaking level. Only run this is you know what you are doing and want absolute results for optimization that surpasses the provided screenshots for this project. I am talking in terms of as low as 1GB or lower with RAM usage.

1) Open up Powershell as admin and run the respective PS file.

## Step 4 - SecureUXTheme (Shell Themes - CORE)

This utility is used for applying advanced custom msstyle themes. This modifies the shell directly allowing for it to retain per boot without damaging the system. This stage can be optional if you wish to just have the performance gains of Slate however all styling will need this to be run.

1) Open the respective executable and select Install. Afterwards it will prompt you to restart.

2) Download <a href="https://www.deviantart.com/niivu/art/pi11z-for-Windows-11-1084568949">pi11z</a>, unzip the respective ZIP file using either 7z/WinRAR/PeaZIP and paste the contents within the `C:/Windows/Resources/Themes` folder

3) Open up SecureUXTheme's executable and click "Install/Patch". Select the respective theme above then restart when prompted

## Step 5 - UXThemePatcher (Shell Themes - CORE)

This utility covers over any standard patches that are missed by SecureUXTheme. Typically on LTSC systems, Windows needs additional patching.

1) Open the executable and run install. Restart when prompted.

## Step 6 - No!! MeiryoUI // JetBrainsMono Font (Shell Themes - Optional)

This process is purely cosmetic for the Slate look. You can replace the selected font with anything you want.

1) Install MeiryoUI from the respective executable.
2) Install JetBrainsMono for your system.
3) Open up MeiryoUI and replace all fonts with JetBrainsMono.

## Step 7 - 7TSP (Shell Themes - CORE)

This step covers replacing universal system icons across Windows 11 using pi11z icons. 

1) Open the 7TSP folder and run the executable. 
2) Select "Select Icon Pack" and navigate to the pi11z 7TSP icons folder
3) Click on "Patch" and the installer will proceed to merge system files and create a restore point. 

## Step 8 - ExplorerBlurMica (Shell Themes - Optional)

This application is primarily used for applying system-wide Mica or Acrylic effects to other applications. Pure cosmetics but great looking.

1) Copy the ExplorerBlurMica folder to C:/Program Files
2) Copy and paste the config file provided at `./config/ExplorerBlurMica.config.ini` to the new location and rename to remove the ExplorerBlurMica prefix at the start of `config.ini`
3) Run `register.cmd` in the folder to apply the shell patches

## Step 9 - ExplorerBGTool (Shell Themes - Optional)

ExplorerBGTool is used for patching explorer (File Explorer) with custom background images. This in combination with ExplorerBlurMica + DWMBlurGlass creates a very clean effect without really impacting performance (due to it being a simple static shell mod).

1) Copy the ExplorerBGM folder to C:/Program Files
2) Copy and paste the config file provided at `./config/ExplorerBGM.config.ini` to the new location and rename to remove the ExplorerBlurMica prefix at the start of `config.ini`
3) Run `register.cmd` in the folder to apply the shell patches

## Step 10 - DWMBlurGlass (Shell Themes - Optional)

This utility takes the attributes of ExplorerBlurMica and applies to globally to the system patching WinUI effecting applications like Task Manager and more.

1) Copy the DWMBlurGlass folder to C:/Program Files
3) Run the respective application (DWMBlurGlass.exe) and click install to apply the shell patches

## Step 11 - Windhawk (Shell Themes - Optional)

Windhawk is used for running pre-packaged utilities that enhance the overall functionality of Windows 11. This arranges from simple icon modifications to taskbar mods.

1) Install Windhawk from the respective installer.
2) Open up Windhawk and follow the default instructions
3) Install the Taskbar Button Click mod and paste the JSON config text from provided at `./config/Windhawk/taskbar-button-click.json` into mod configuration box
4) Install the Taskbar Clock Customization mod and paste the JSON config text from provided at `./config/Windhawk/taskbar-clock-customization.json` into mod configuration box
5) Install the Taskbar Icon Size mod and paste the JSON config text from provided at `./config/Windhawk/taskbar-icon-size.json` into mod configuration box
6) Install the Taskbar Label mod and paste the JSON config text from provided at `./config/Windhawk/taskbar-labels.json` into mod configuration box

## Step 12 - ExplorerPatcher OR StartAllBack (Shell Themes - Optional)

ExplorerPatcher (free) is used for modding the default start menu to create either a more Windows 7 or Windows 10 look. StartAllBack (paid) however is used mostly themed Windows 7 / Windows 11 ish looks with theming capabilities. 

1) Open up ep_setup.exe to install ExplorerPatcher
2) Tweak the respective settings as needed

## Step 13 - RightClickCompress (Shell Themes - Optional)

Simple application that adds a right click menu option to compress image or various media files like videos. Saves some time.

## Step 14 - Mactype + Chawye Hsu's MacType Profile

Mactype is used for replacing the default font rendering method for Windows (Cleartype) with a similar system to Quartz on MacOS. Although this method isn't 100% perfect, font rendering is greatly improved.

## Step 15 - WinSetView

This utility is used for quick tweaks to File Explorer outside of the properties menu.

## Step 16 - TranslucentTB

Simple application that lets you make the Windows taskbar look much better.

## Step 17 - Rainmeter

Rainmeter allows you to utilize custom pre-made skins adding widgets, live players and more. This project currently uses [Zephyr 2.0](https://www.deviantart.com/smithxtt/art/Zephyr-2-0-891270319).  

## Step 18 - MicaForEveryone

A tool to enable backdrop effects on a per application basis.

## Step 19 - File Optimizer

This utility adds a right click menu allowing you to optimize, re-scale and encode files.

## Step 20 - Czkawka

Fast application that allows you to remove duplicate files, etc.

## Step 21 - UniGetUI

Automtically fetches updates using winget. This tool helps ensure all locally installed applications are always up-to-date in a fashion similar to a linux package manager. You can also browser various assets. All with a GUI.



