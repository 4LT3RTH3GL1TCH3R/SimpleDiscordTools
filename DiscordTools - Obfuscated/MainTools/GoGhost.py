import os
import requests
import time

# Load token from parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()
headers = {
    "Authorization": token,
    "Content-Type": "application/json"
}

def clear_profile():
    print("[*] Clearing profile info...")
    payload = {
        "bio": "",
        "username": input("Enter a new username (required to reset): "),
        "avatar": None,
        "banner": None
    }
    r = requests.patch("https://discord.com/api/v9/users/@me", headers=headers, json=payload)
    print(f"Cleared profile info - {r.status_code} {r.text}")

    # Clear status
    payload = {
        "custom_status": None
    }
    s = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
    print(f"Cleared status - {s.status_code} {s.text}")

def leave_all_servers():
    print("[*] Leaving all servers...")
    guilds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
    for g in guilds:
        res = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{g['id']}", headers=headers)
        print(f"Left {g.get('name', 'Unknown')} - {res.status_code}")
        time.sleep(0.5)

def delete_owned_servers():
    print("[*] Deleting owned servers...")
    guilds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
    for g in guilds:
        if g.get("owner", False):
            res = requests.delete(f"https://discord.com/api/v9/guilds/{g['id']}", headers=headers)
            print(f"Deleted owned server {g['name']} - {res.status_code}")
            time.sleep(0.5)

def clear_friends():
    print("[*] Removing all friends...")
    friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
    for f in friends:
        if f["type"] == 1:
            res = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{f['id']}", headers=headers)
            print(f"Removed friend {f['user']['username']} - {res.status_code}")
            time.sleep(0.5)

def close_dms():
    print("[*] Closing DMs...")
    dms = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
    for dm in dms:
        if dm["type"] == 1:
            res = requests.delete(f"https://discord.com/api/v9/channels/{dm['id']}", headers=headers)
            print(f"Closed DM with ID {dm['id']} - {res.status_code}")
            time.sleep(0.5)

# Execute everything
clear_profile()
delete_owned_servers()
leave_all_servers()
clear_friends()
close_dms()

print("\n[*] Account ghosted successfully.")
time.sleep(999)
