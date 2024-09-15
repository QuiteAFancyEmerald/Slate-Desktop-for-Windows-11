import json
import os
import requests
import sys

def check_http_status(url):
    try:
        response = requests.get(url)
        return response.status_code in [200, 201, 202, 204]
    except requests.RequestException as e:
        print(f"Request failed for URL {url}: {e}")
        return False

def main():
    sources_file = './sources.json'
    
    if not os.path.exists(sources_file):
        print(f"Error: {sources_file} not found.")
        sys.exit(1)
    
    with open(sources_file, 'r') as f:
        data = json.load(f)
    
    all_successful = True
    for file_entry in data.get('files', []):
        url = file_entry.get('url')
        
        if url:
            if not check_http_status(url):
                print(f"URL check failed for: {url}")
                all_successful = False
        else:
            print("Error: Empty URL found in sources.json.")
            all_successful = False
    
    if all_successful:
        print("All URLs checked successfully.")
        sys.exit(0)
    else:
        print("Some URLs failed to check.")
        sys.exit(1)

if __name__ == "__main__":
    main()
