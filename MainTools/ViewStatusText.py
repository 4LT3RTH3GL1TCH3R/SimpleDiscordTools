import os
import requests
import sys
import time

def load_token():
    parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    token_file = os.path.join(parent, "token.txt")
    if not os.path.exists(token_file):
        print("Token file not found."); sys.exit()
    with open(token_file, "r") as f: token = f.read().strip()
    return token

def main():
    token = load_token()
    url = "https://discord.com/api/v9/users/@me/settings"
    headers = {"Authorization": token, "User-Agent": "DiscordViewer/1.0"}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        cs = res.json().get("custom_status")
        if cs:
            emoji = cs.get("emoji_name", "")
            text = cs.get("text", "")
            print(f"Custom Status: {emoji} {text}".strip())
        else:
            print("Custom Status: (none set)")
    else:
        print(f"Failed to fetch custom text status: {res.status_code}")

if __name__ == "__main__":
    main()
time.sleep(999)  # Keep the script running so the user can see the output