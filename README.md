# Slate-Desktop-for-Windows-11

**Slate Desktop** is a powerful Windows environment and CLI tool focused on **performance**, **productivity enhancements**, **shell modifications**, and a **modern aesthetic** tailored specifically for Windows 11. Unlike other modpacks that revert to outdated styles, Slate Desktop elevates the sleek, modern look of Windows 11 with performance and visual improvements. 

One of the core principles of this project is **full transparency**—it avoids *hidden automation, untrusted applications and the use of untrusted, pre-modded ISOs*. Instead, Slate Desktop employs a seamless, CLI-based process to download assets and automatically import necessary configurations via a `sources.json` file. This ensures that each component of the setup is openly visible and customizable.

### Considering starring this repository if you support it!

Made in Python it runs through `sources.json` which serves as a transparent way of grabbing every asset needed. You can check it out <a href="https://github.com/QuiteAFancyEmerald/Slate-Desktop-for-Windows-11/blob/main/sources.json"></a> to review direct links as well as a list of each project used.

## Table Of Contents
<img width=250px align=right src="https://raw.githubusercontent.com/QuiteAFancyEmerald/Slate-for-Windows-11/main/img/preview.png"></img>

* [Introduction](#introduction)
* [Installation](#installation)
* [External Assets](#external-assets)
* [Contributing](#contributing)
* [Credits](#credits)


### Supported Windows 11 Versions: 
`Windows 11 21H2`, `Windows 11 22H2`, `Windows 11 23H2`, `Windows 11 24H2` 

(Works with ANY Windows edition however **Windows 11 IoT LTSC** is *highly recommended*)

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

Ensure you verify that you are on Windows 11 and using an [approved](#supported-windows-11-versions) version.

#### Windows ISO Setup
This project highly recommends you use **Windows 11 IoT LTSC 24H2**. You can get an official ISO/release installer from the official <a href="https://www.microsoft.com/en-us/evalcenter/evaluate-windows-11-iot-enterprise-ltsc">Microsoft</a> page or <a href="https://massgrave.dev/genuine-installation-media">Massgrave</a> (Recommended).

For more information on how to upgrade or swap your Windows check this <a href="https://github.com/SysadminWorld/windows11">GitHub</a> repository. You can also just extract the ISO you download with something like WinRAR (or Peazip) if you do not have a USB and install with the setup that way. 

Just note that you will need to **backup ALL your files beforehand and do a clean install.**

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

## Contributing
If you wish to contribute to this repository simply make a pull request! This can include any additional optimization/theming mods you want to be added or refactoring any automatic processes. For greater detail check out `CONTRIBUTING.md`. Additions are made easy via `sources.json`.

## Credits
This project would not be possible without every application used for this project.

| Project | Developer | Description |
| --- | --- | --- |
| [pi11z & icons ](https://www.deviantart.com/niivu/art/pi11z-for-Windows-11-1084568949) | niivu | A clean new theme for your Windows 11 desktop environment. The core theme for this entire project |
| [AME Wizard](https://ameliorated.io/) | Ameliorated LLC | The Ultimate tool for modifying Windows. Used for running registry tweaks and PowerShell scripts in the form of playbooks (ReviOS). |
| [ReviOS Playbook](https://github.com/meetrevision/playbook/) | ReviOS Team | A customized version of Windows designed for performance, privacy, and stability. |
| [Optimizer](https://github.com/hellzerg/optimizer/) | Hellzerg | Used to apply specific system tweaks on fresh installs, layer one of optimization. |
| [WinMemoryCleaner](https://github.com/IgorMundstein/WinMemoryCleaner/) | Igor Mundstein | Utility using native Windows features to optimize memory areas. |
| [Winaero Tweaker](https://winaerotweaker.com/) | Sergey Tkachenko | All-in-one application that comes with dozens of options for fine-grained tuning of various Windows settings and features. |
| [Windows On Reins [EXPERT-OPTIONAL]](https://github.com/gordonbay/Windows-On-Reins) | Gordon Bay | Powershell script for hardcore performance and privacy optimization. |
| [SecureUxTheme](https://github.com/namazso/SecureUxTheme/) | Namazso | Secure boot compatible in-memory UltraUxTheme patcher. |
| [UXThemePatcher](https://uxthemepatcher.com/) | UXThemePatcher Team | Modifies system files to use third-party themes. | 
| [No!! MeiryoUI](https://github.com/Tatsu-syo/noMeiryoUI) | Tatsu-syo | Windows system font setting tool for better customization. |
| [JetBrainsMono Font](https://github.com/ryanoasis/nerd-fonts/) | JetBrains | Font designed specifically for developers. | 
| [VS Cursors 20.0](https://www.deviantart.com/vladsukhetskyi/art/VS-Cursors-20-0-1097245195) | vladsukhetskyi | Core mouse cursor used for this project. Very clean and great display quality. | 
| [7TSP (Optional/Alternative)](https://www.deviantart.com/devillnside/art/7TSP-GUI-2019-Edition-804769422) | Skinpacks | Patches .mun files to allow custom icons. |
| [StartAllBack](https://www.startallback.com/) | StartAllBack | Modifies the start menu and the primary example used for this project. For a free option use ExplorerPatcher below. |
| [Stardock Software](https://www.stardock.com/products/) | Stardock Software | Collection of clean (but paid) Windows modding tools for the Start Menu and workflow. Not needed is optional but nice to have. |
| [ExplorerBlurMica](https://github.com/Maplespe/ExplorerBlurMica/) | Maplespe | Adds background blur effect, Acrylic or Mica effect to Explorer. | 
| [ExplorerBgTool](https://github.com/Maplespe/explorerTool/) | Maplespe | Allows custom background images in Windows Explorer. | 
| [DWMBlurGlass](https://github.com/Maplespe/DWMBlurGlass/) | Maplespe | Adds custom effects to the system title bar and core Windows apps. | 
| [Windhawk](https://github.com/ramensoftware/windhawk/) | Ramen Software | Customization marketplace for Windows programs. | 
| [ExplorerPatcher](https://github.com/valinet/ExplorerPatcher/) | Valinet | Modifies the start menu, a free alternative to StartIsBack. | 
| [RightClickCompress](https://github.com/otdavies/RightClickCompress/) | OT Davies | Adds right-click option to compress images and videos. | 
| [MacType](https://github.com/snowie2000/mactype/) | Snowie2000 | Improves font rendering in Windows. | 
| [Chawye Hsu's MacType Profile](https://github.com/chawyehsu/mactype-profile/) | Chawye Hsu | Custom profile for better font rendering. | 
| [WinSetView](https://github.com/LesFerch/WinSetView/) | LesFerch | Sets Windows File Explorer default folder views easily. | 
| [TranslucentTB](https://github.com/TranslucentTB/TranslucentTB/) | TranslucentTB Team | Makes the Windows taskbar translucent/transparent. | 
| [Rainmeter](https://github.com/rainmeter/rainmeter/) | Rainmeter Team | Displays customizable skins on your desktop. | 
| [Zephyr 2.0](https://www.deviantart.com/smithxtt/art/Zephyr-2-0-891270319) | smithxtt | Very clean rainmeter theme for your desktop. | 
| [Sonder](https://www.deviantart.com/michaelpurses/art/Sonder-Rainmeter-skin-838147223) | michaelpurses | Clean rainmeter skin for clock usage or ultrawide additons. | 
| [MicaForEveryone](https://github.com/MicaForEveryone/MicaForEveryone/) | Mica For Everyone Team | Enables backdrop effects on Win32 apps in Windows 11. |
| [FileOptimizer](https://sourceforge.net/projects/nikkhokkho/files/FileOptimizer/) | Nikkhokkho | Optimizes files to reduce size and improve performance. | 
| [Czkawka](https://github.com/qarmin/czkawka/) | Qarmin | Simple and fast tool for finding duplicate files. |
| [Rose Pine for Ungoogled Chromium/Chrome](https://github.com/rose-pine/google-chrome) | Rose Pine Team | Soho vibes for Google Chrome. |
| [lavender - new tab for Ungoogled Chromium/Chrome](https://chromewebstore.google.com/detail/lavender-new-tab/ffobepdbanoiodmfimpmanafepclokbc) | fvrests | a soft, minimal new tab for your browser. |
| [Simply Darkish for Firefox](https://www.deviantart.com/dpcdpc11/art/Simplify-Darkish-Firefox-Theme-852918492) | dpcdpc11 | Clean Firefox theme with mood |