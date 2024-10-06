# Slate-Desktop-for-Windows-11

**Slate Desktop** is a powerful Windows environment and CLI tool focused on **performance**, **productivity enhancements**, **shell modifications**, and a **modern aesthetic** tailored specifically for Windows 11. Unlike other modpacks that revert to outdated styles, Slate Desktop elevates the sleek, modern look of Windows 11 with performance and visual improvements. 

One of the core principles of this project is **full transparency**—it avoids *hidden automation, untrusted applications and the use of untrusted, pre-modded ISOs*. Instead, Slate Desktop employs a seamless, CLI-based process to download assets and automatically import necessary configurations via a `sources.json` file. This ensures that each component of the setup is openly visible and customizable.

### Considering starring this repository if you support it!

Made in Python it runs through `sources.json` which serves as a transparent way of grabbing every asset needed. You can check it out <a href="https://github.com/QuiteAFancyEmerald/Slate-Desktop-for-Windows-11/blob/main/sources.json"></a> to review direct links as well as a list of each project used.

### Requires Python to be downloaded: https://www.python.org/downloads/

## Table Of Contents
<img width=250px align=right src="https://raw.githubusercontent.com/QuiteAFancyEmerald/Slate-for-Windows-11/main/img/preview.png"></img>

* [Introduction](#introduction)
* [Installation](#installation)
* [External Assets](#external-assets)
* [Contributing](#contributing)
* [Credits](#credits)


### Supported Windows 11 Versions: 
`Windows 11 21H2`, `Windows 11 22H2`, `Windows 11 23H2`, `Windows 11 24H2` (Works with ANY Windows edition however **Windows 11 IoT LTSC** is *highly recommended*)

> [!CAUTION]
> You are responsible for running this script. Make sure you have backups prior to utilizing Slate and ensure you are on **Windows 11 22H2/Windows 11 23H2/Windows 11 IoT LTSC**. This project will not work on **Windows 10** and will damage it!!!

> [!TIP]
> For the best results use a fresh (legal) copy of **Windows 11 IoT LTSC**. You can get this from the official Microsoft website. LTSC is the best version of Windows 11 to utilize these scripts on as versus standard Windows 11 Home it has no bloatware or useless Windows apps pre-installed. Have a peace of mind and consider "massgravel" for those who live within the seas brrr

> [!NOTE]
> After installation simply check the `/sources` folder for each step. Some configuration files will need to be moved manually but detailed instructions are provided. More information is provided within the **Installation** section. 


<img src="https://raw.githubusercontent.com/QuiteAFancyEmerald/Slate-for-Windows-11/main/img/preview.png"></img>

<table>
  <tr>
    <td>
      <img src="https://raw.githubusercontent.com/QuiteAFancyEmerald/Slate-for-Windows-11/main/img/style-example.png" alt="Explorer Style Example" />
    </td>
    <td>
      <img src="https://raw.githubusercontent.com/QuiteAFancyEmerald/Slate-for-Windows-11/main/img/task-manager.png" alt="Task Manager Example" />
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://raw.githubusercontent.com/QuiteAFancyEmerald/Slate-Desktop-for-Windows-11/refs/heads/main/img/powertoys.png" alt="Search Powertoys Example" />
    </td>
    <td>
      <img src="https://raw.githubusercontent.com/QuiteAFancyEmerald/Slate-Desktop-for-Windows-11/main/img/rightclick.png" alt="Right Click Example" />
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://raw.githubusercontent.com/QuiteAFancyEmerald/Slate-Desktop-for-Windows-11/refs/heads/main/img/clipreview.png" alt="Search Powertoys Example" />
    </td>
  </tr>
</table>

## Introduction
**Slate for Windows** is designed with a layered approach to enhance performance and customization while maintaining system stability. The installation script automatically handles the download and setup process for each stage, allowing users to customize their setup by skipping or adding applications and modifications as desired. **Contributing has never been easier!**

Each source is not installed automatically but is instead downloaded and organized in `./sources/downloads`. This approach allows the user to select between **core** and **optional** mods while verifying their integrity, rather than having the process be entirely automatic. You could use this entire project solely for optimizations and productivity without applying the theming if preferred!

#### sources.json Example:
```json
{
  "path": "https://github.com/Ameliorated-LLC/trusted-uninstaller-cli/releases/download/0.7.6/AME-Wizard-Beta.exe",
  "name": "AME Wizard",
  "description": "The Ultimate tool for modifying Windows. This is used for essentially running registry tweaks and powershell scripts in the form of playbooks (ReviOS). Much safer than using unknown distributed ISO mods.",
  "extract": true,
  "folder_main": "01 - Optimization", // ./sources/downloads/01 - Optimization
  "folder_name": "Step 1 - AME Wizard",
  "type": "url" // @type = url, cmd
},
```

### Performance
The performance enhancements in Slate are applied through multiple layers, each providing optimizations that do not compromise *core* Windows functionality or user experience. At the core, Slate utilizes AME Wizard as the primary optimization layer, allowing users to switch between different "playbooks" — collections of PowerShell scripts and registry tweaks — that enhance system performance without requiring untrusted or modified ISOs. For this project ReviOS is integrated for its flexibility, open-source nature, and ability to configure optimizations via a GUI settings menu after being installed, offering performance improvements while preserving essential Windows features.

- **Layer One:** AME Wizard, ReviOS (`Core; essential mods that must be used`)
- **Layer Two:** Optimizer, winutil (`Polishing; tweaks settings automatically`)
- **Layer Three:** WinMemoryCleaner (`Background; optional but useful background utilities; recommended`)
- **Optional/Expert:** Windows-On-Reins (`Dangerous/System Breaking; provided for expert power users`)

### Shell Modifications/Styling
Core windows theming is done through SecureUXTheme (Allows for patching msstyles themes), UXThemePatcher and Winaero Theme Switcher. SecureUXTheme directly interacts with the Windows/Resources folder ensuring unsigned themes can be loaded (third party). UXThemePatcher is an additional resource patcher for LTSC or other W11 versions that don't work with SecureUXTheme alone. Lastly for LTSC alone Winaero Theme Switcher is added for getting around a bug when applying a theme (you would run all three at once). 

- **Layer One:** SecureUXTheme, UXThemePatcher, Winaero Theme Switcher (`Core; essential mods that must be used`)

### Primary Themes
Primary theming are the msstyles, icons and configuration files for Rainmeter within this project. Core windows theming steps must be done first in order to patch the required files for this to work.

- **Layer One:** <a href="https://www.deviantart.com/niivu/art/pi11z-for-Windows-11-1084568949">pi11z</a> (`Core; Primary mssstyle/theme mod made by niivu. Download from DeviantArt`)
- **Layer Two:** <a href="https://www.deviantart.com/niivu/art/pi11z-for-Windows-11-1084568949">pi11z Icons</a> (`Core; Primary icon theme set via 7tsp or Windhawk made by niivu. Download from DeviantArt`)
- **Layer Three:** <a href="https://github.com/Tatsu-syo/noMeiryoUI/releases/download/TAG-3.3.1/noMeiryoUI3.3.1.zip">MeiryoUI</a> (`Core; Primary mssstyle/theme mod made by niivu. Download from DeviantArt`)
- **Layer Four:** <a href="https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/JetBrainsMono.zip">JetBrainsMono</a> (`Core; Primary mssstyle/theme mod made by niivu. Download from DeviantArt`)

### Explorer Mods/Additional Theming
Explorer mods include any changes to add the mica/acrylic effect to DWM (all native windows such as File Explorer, etc.), polishing menus and lastly background styles. This entire stage is a technically optional as some users do not enjoy transparency within their applications however you can still use each tool since a config exists where you can set the alpha to 255 (essentially zero transparency) but still get the clean mica effect. The optional parts include optimized font-rendering for Windows (ClearType often results in jagged, not decent font rendering so MacType solves that but allowing the modifications of default font rendering) and lastly features to be added to the right click menu such as File Converter and Compress File. 

The last stage of this process is of course taskbar and start menu modifications using either ExplorerPatcher (free) or StartAllBack (paid but you can use the seven seas brrr). For the taskbar itself Windhawk is used with various configuration files (provided in `/config`) for a clean, sleek look retaining Windows 11's fancy animations.

- **Layer One:** Windhawk, ExplorerPatcher, StartAllBack (`Core; essential mods that must be used`)
- **Layer Two:** ExplorerBlurMica, ExplorerBgTool, DWMBlurGlass, TranslucentTB, Rainmeter, Mica For Everyone (`Styling; tweaks settings automatically`)
- **Layer Three:** Right Click Compress, Right Click File Converter, WinSetView, FileOptimizer, Czkawka (`Tools; useful background utilities; recommended`)
- **Layer Four:** Mactype, Chawyehsu Mactype Profile, Wallpaper Engine (`Background; optional but useful background utilities; recommended`)

## Installation

### Dependencies
Requires **Python** to be downloaded in order to run. Download from below.

**Python (Latest):** https://www.python.org/downloads/

### Download Release
1. Download the latest release from the <a href="https://github.com/QuiteAFancyEmerald/Slate-Desktop-for-Windows-11/releases">Releases</a> page or the source code button
2. Unzip it to a location such as `C:\Users\[USER]\Documents`.
3. Run "`install.bat`" as administrator.
4. Within the Powershell/Command Prompt window that opens follow the CLI process by pressing Enter
5. Navigate to `[Location Path]\Slate-Desktop-for-Windows-11\sources` and read over the `Installation.md` file to step by step information on running all of the assets in `.\sources\downloads` (it is also numbered in the downloads folder)
6. Follow each step within the `Installation.md` file by the numbers running each application in the `.\sources\downloads` folder and pasting configs from the correct folder `.\config`

### Uninstall
**Note:** This project **CANNOT** be uninstalled fully. The tweaks are safe for updating windows however just be sure to check this repository for updates or detailed information on supported versions

## External Assets
Some themes and tools CANNOT be downloaded via the CLI and have to be downloaded from the official site due to licencing. Below is a list of all external assets but are also provided in `./sources/INSTALLATION.md` step by step. Special thanks to each creator/project for their amazing work.

- **pi11z & pi11z Icons:** https://www.deviantart.com/niivu/art/pi11z-for-Windows-11-1084568949
- **Winaero Tweaker:** https://winaerotweaker.com/
- **StartAllBack:** https://www.startallback.com/
- **VS Cursors 20.0:** https://www.deviantart.com/vladsukhetskyi/art/VS-Cursors-20-0-1097245195
- **Zephyr 2.0:** https://www.deviantart.com/smithxtt/art/Zephyr-2-0-891270319
- **Sonder:** https://www.deviantart.com/michaelpurses/art/Sonder-Rainmeter-skin-838147223
- **Simply Darkish For Firefox:** https://www.deviantart.com/dpcdpc11/art/Simplify-Darkish-Firefox-Theme-852918492
- **Rose Pine For Ungoogled Chromium/Chrome:** https://github.com/rose-pine/google-chrome
- **Lavender | New Tab for Ungoogled Chromium/Chrome:** https://chromewebstore.google.com/detail/lavender-new-tab/ffobepdbanoiodmfimpmanafepclokbc
- **7TSP GUI 2019:** https://www.deviantart.com/devillnside/art/7TSP-GUI-2019-Edition-804769422
- **Cider 2 (Music Client):** https://cider.sh/
- **Rain Day (Wallpaper Engine Wallpaper):** https://steamcommunity.com/sharedfiles/filedetails/?id=2474749882
- **Rainy Street (Wallpaper Engine Wallpaper):** https://steamcommunity.com/sharedfiles/filedetails/?id=3019553019
