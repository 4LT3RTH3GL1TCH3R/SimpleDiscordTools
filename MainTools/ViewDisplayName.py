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
    url = "https://discord.com/api/v9/users/@me"
    headers = {"Authorization": token, "User-Agent": "DiscordViewer/1.0"}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = res.json()
        display_name = data.get("global_name") or f"{data['username']}#{data['discriminator']}"
        print(f"Display Name: {display_name}")
    else:
        print(f"Failed to fetch display name: {res.status_code} | {res.text}")

if __name__ == "__main__":
    main()

time.sleep(999)  # Keep the script running so the user can see the output
