import os
from pathlib import Path

def install_requirements():
    root_dir = Path(__file__).resolve().parent.parent
    requirements_path = root_dir / 'requirements.txt'

    if requirements_path.exists():
        print(f"Installing required packages from {requirements_path}...")
        os.system(f"pip install -r {requirements_path}")
    else:
        print("requirements.txt not found in the root directory.")

def run_download_script():
    src_dir = Path(__file__).resolve().parent
    download_script = src_dir / 'sources.py'

    if download_script.exists():
        print("Running sources script to fetch and extract all sources for Slate...")
        os.system(f"python {download_script}")
    else:
        print("sources.py not found in the src directory.")

if __name__ == "__main__":
    install_requirements()
    
    # Clear the terminal after installing requirements
    os.system('cls' if os.name == 'nt' else 'clear')
    
    run_download_script()
