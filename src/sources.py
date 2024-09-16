import os
import requests
from pathlib import Path
from colorama import init, Fore, Style
import json
import zipfile
import py7zr
import time
import sys
import platform
import subprocess

init(autoreset=True)

def check_windows_version():
    """Check if the script is running on Windows 11."""
    system_version = platform.version()
    
    if platform.system() == "Windows":
        version_parts = system_version.split('.')
        
        if len(version_parts) >= 3:
            major_version = version_parts[0]
            build_number = int(version_parts[2])
            
            # Check if the version is Windows 11; if not Slate for Windows will not work.
            if major_version == "10" and build_number >= 22000:
                return True
    
    print("This tool is designed for Windows 11 only.")
    print("Press Enter to exit...")
    input()
    sys.exit(1)

def print_slate_text():
    """Print the Slate Desktop ASCII art and information."""
    project_version = "1.0.6"
    author = "Quite A Fancy Emerald"
    github_link = "https://github.com/QuiteAFancyEmerald/Slate-Desktop-for-Windows-11"
    
    blue = Fore.BLUE
    cyan = Fore.CYAN
    grey = Fore.LIGHTBLACK_EX
    green = Fore.GREEN
    yellow = Fore.YELLOW
    reset = Style.RESET_ALL

    art = f'''
    {blue}.o{reset}     {cyan}.o   {blue}.oPYo.{reset} 8          o           ooo.                 8        o                      {blue}.o{reset}     {cyan}.o 
   {blue}.o'{reset}    {cyan}.o'{reset}   8      8          8           8  `8.               8        8                     {blue}.o'{reset}    {cyan}.o'{reset} 
  {blue}.o'{reset}    {cyan}.o'{reset}    `Yooo. 8 {blue}.oPYo.{reset}  o8P {blue}.oPYo.{reset}   8   `8 {blue}.oPYo. {blue}.oPYo.{reset} 8  .o   o8P {blue}.oPYo.{reset} {blue}.oPYo.{reset}     {blue}.o'{reset}    {cyan}.o'{reset}  
 {blue}.o'{reset}    {cyan}.o'{reset}         `8 8 .oooo8   8  8oooo8   8    8 8oooo8 Yb..   8oP'     8  8    8 8    8    {blue}.o'{reset}    {cyan}.o'{reset}   
{blue}.o'{reset}    {cyan}.o'{reset}           8 8 8    8   8  8.       8   .P 8.       'Yb. 8 `b.    8  8    8 8    8   {blue}.o'{reset}    {cyan}.o'{reset}    
o'     o'       `YooP' 8 `YooP8   8  `Yooo'   8ooo'  `Yooo' `YooP' 8  `o.   8  `YooP' 8YooP'   o'     o'     
{grey}..:::::{reset}{blue}..::::::::.....:..:.....:::..::.....:::.....:::.....::.....:..::...::..::.....:8 ....:::..:::::..:::::{reset}
{grey}::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::8 :::::::::::::::::::::{reset}
{grey}::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::..:::::::::::::::::::::{reset}
{blue}╔
{blue}║{reset}                                                             
{blue}║  Welcome to Slate Desktop - {green}Version {project_version}{reset}  
{blue}║  Recommended Windows ISO: {green} Windows 11 IoT LTSC{reset}   
{blue}║  Developed by {green}{author}{reset}                                  
{blue}║  GitHub: {green}{github_link}{reset}                                   
{blue}║  {yellow}Slate Desktop features extensive performance mods,{reset}
{blue}║  {yellow}optimizations, productivity apps, and sleek theming.{reset}
{blue}║{reset}                                                          
{blue}╚
    '''
    print(art)
    time.sleep(2)

def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_rotating_indicator(message):
    """Display a rotating indicator while processing."""
    indicator = ["\\", "|", "/", "-"]
    for _ in range(4):
        for symbol in indicator:
            sys.stdout.write(f"\r{message} {symbol} ")
            sys.stdout.flush()
            time.sleep(0.2)

def download_file(url, name, description, extract, folder_main, folder_name, headers=None):
    """Download a file from the given URL and extract if necessary."""
    base_path = Path(f"./sources/downloads/{folder_main}")
    base_path.mkdir(parents=True, exist_ok=True)

    subfolder_path = base_path / folder_name
    subfolder_path.mkdir(parents=True, exist_ok=True)
    
    file_name = url.split('/')[-1]
    file_path = subfolder_path / file_name

    print(Fore.GREEN + Style.BRIGHT + f"\nPreparing to download: {name}")
    print(Fore.YELLOW + Style.BRIGHT + f"\n{description}\n")
    display_rotating_indicator("Downloading")

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        with open(file_path, 'wb') as file:
            file.write(response.content)
        
        print(Fore.CYAN + Style.BRIGHT + f"\nDownload complete: {file_name}")

        if extract:
            print(Fore.YELLOW + Style.BRIGHT + f"Preparing to extract: {file_name}")
            display_rotating_indicator("Extracting")
            
            if file_name.endswith('.zip'):
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(subfolder_path)
                print(Fore.CYAN + Style.BRIGHT + f"\nExtraction complete for {file_name}")
            elif file_name.endswith('.7z'):
                with py7zr.SevenZipFile(file_path, 'r') as seven_z_ref:
                    seven_z_ref.extractall(path=subfolder_path)
                print(Fore.CYAN + Style.BRIGHT + f"\nExtraction complete for {file_name}")
    except requests.exceptions.HTTPError as http_err:
        print(Fore.RED + Style.BRIGHT + f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(Fore.RED + Style.BRIGHT + f"Request error occurred: {req_err}")
    except Exception as err:
        print(Fore.RED + Style.BRIGHT + f"An error occurred: {err}")

def execute_command(command):
    """Execute a PowerShell command."""
    try:
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        if result.returncode == 0:
            print(Fore.CYAN + Style.BRIGHT + f"\nCommand executed successfully:\n{result.stdout}")
        else:
            print(Fore.RED + Style.BRIGHT + f"\nCommand execution failed:\n{result.stderr}")
    except Exception as err:
        print(Fore.RED + Style.BRIGHT + f"An error occurred while executing the command: {err}")

def load_sources():
    """Load the sources from sources.json."""
    try:
        root_dir = Path(__file__).parent.parent
        sources_path = root_dir / 'sources.json'

        with open(sources_path, 'r') as file:
            data = json.load(file)
        return data.get('files', [])
    except FileNotFoundError:
        print(Fore.RED + Style.BRIGHT + "sources.json file not found in the root directory.")
        return []
    except json.JSONDecodeError:
        print(Fore.RED + Style.BRIGHT + "Error decoding JSON from sources.json.")
        return []

def main():
    """Main function to run the script."""
    print_slate_text()

    sources = load_sources()
    if not sources:
        print(Fore.RED + Style.BRIGHT + "No files found in sources.json. Exiting...")
        return

    for source in sources:
        path = source.get('path')
        name = source.get('name', 'Unnamed item')
        description = source.get('description', 'No description provided')
        extract = source.get('extract', False)
        folder_main = source.get('folder_main', '01 - Default')
        folder_name = source.get('folder_name', 'Default')
        type_ = source.get('type', 'url') 
        token = source.get('token', None)
        headers = {'Authorization': f'Bearer {token}'} if token else None
        
        if type_ == 'url' and path.strip():
            download_file(path.strip(), name, description, extract, folder_main, folder_name, headers)
        elif type_ == 'cmd' and path.strip():
            execute_command(path.strip())
        else:
            print(Fore.RED + Style.BRIGHT + f"Error: Invalid type or empty path for '{name}'. Skipping...")

if __name__ == "__main__":
    check_windows_version()
    main()
