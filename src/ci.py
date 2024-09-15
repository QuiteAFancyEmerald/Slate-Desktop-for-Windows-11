import json
import requests
import sys
import os

def check_url_status(url):
    """Check HTTP status of a URL."""
    try:
        response = requests.get(url)
        return response.status_code
    except requests.RequestException as e:
        print(f"Error accessing URL '{url}': {e}")
        return None

def main():
    json_file_path = os.path.join(os.path.dirname(__file__), '../sources.json')

    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: {json_file_path} not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Failed to parse sources.json.")
        sys.exit(1)

    files = data.get('files', [])
    if not files:
        print("Error: No files found in sources.json.")
        sys.exit(1)

    # Check URLs
    all_urls_successful = True
    for file in files:
        url = file.get('url')
        if url:
            status_code = check_url_status(url)
            if status_code != 200:
                print(f"Error: URL '{url}' returned status code {status_code}.")
                all_urls_successful = False

    if all_urls_successful:
        print("All URLs returned a successful status.")
        sys.exit(0) 
    else:
        sys.exit(1) 

if __name__ == "__main__":
    main()
