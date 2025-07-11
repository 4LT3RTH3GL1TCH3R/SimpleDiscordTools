import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

headers = {"Authorization": token}
dms = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
success = 0

for dm in dms:
    if dm["type"] == 1:
        res = requests.delete(f"https://discord.com/api/v9/channels/{dm['id']}", headers=headers)
        print(f"Closed DM {dm['id']} - {res.status_code}")
        if res.status_code == 200:
            success += 1

if success > 0:
    time.sleep(999)
