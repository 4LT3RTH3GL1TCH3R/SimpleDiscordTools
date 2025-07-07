import os
import requests
import sys
import time

def load_token():
    parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    token_path = os.path.join(parent, "token.txt")
    if not os.path.exists(token_path):
        print("Token file not found."); sys.exit()
    with open(token_path, "r") as f: token = f.read().strip()
    return token

def main():
    token = load_token()
    url = "https://discord.com/api/v9/users/@me"
    headers = {"Authorization": token, "User-Agent": "DiscordViewer/1.0"}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        bio = res.json().get("bio") or "(No bio set)"
        print(f"About Me (Bio): {bio}")
    else:
        print(f"Failed to fetch bio: {res.status_code} | {res.text}")

if __name__ == "__main__":
    main()

time.sleep(999)
