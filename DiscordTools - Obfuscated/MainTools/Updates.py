import requests
import time

# Replace this with your raw Pastebin URL
pastebin_raw_url = "https://pastebin.com/raw/G82HY6kx"

try:
    response = requests.get(pastebin_raw_url)
    response.raise_for_status()  # Raises error for 4xx or 5xx status codes
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Failed to fetch Pastebin content:\n{e}")
time.sleep(999)  # Keep the console open for viewing