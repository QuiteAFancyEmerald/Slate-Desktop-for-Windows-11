# Slate-Desktop-for-Windows-11

**Slate Desktop** is a powerful Windows environment and CLI tool focused on **performance**, **productivity enhancements**, **shell modifications**, and a **modern aesthetic** tailored specifically for Windows 11. Unlike other modpacks that revert to outdated styles, Slate Desktop elevates the sleek, modern look of Windows 11 with performance and visual improvements. 

One of the core principles of this project is **full transparency**—it avoids *hidden automation, untrusted applications and the use of untrusted, pre-modded ISOs*. Instead, Slate Desktop employs a seamless, CLI-based process to download assets and automatically import necessary configurations via a `sources.json` file. This ensures that each component of the setup is openly visible and customizable.

Made in Python it runs through `sources.json` which serves as a transparent way of grabbing every asset needed. You can check it out <a href="https://github.com/QuiteAFancyEmerald/Slate-Desktop-for-Windows-11/blob/main/sources.json"></a> to review direct links as well as a list of each project used.

<img width=200px align=right src="https://raw.githubusercontent.com/QuiteAFancyEmerald/Slate-for-Windows-11/main/img/preview.png"></img>

## Table Of Contents

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
- **Layer Two:** Optimizer, winutil (`Polish; tweaks settings automatically`)
- **Layer Three:** WinMemoryCleaner (`Background; optional but useful background utilities`)
- **Optional/Expert:** Windows-On-Reins (`Dangerous/System Breaking; provided for expert power users`)

### Shell Modifications/Styling
