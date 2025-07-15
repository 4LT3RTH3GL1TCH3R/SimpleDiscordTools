import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

headers = {"Authorization": token}
dms = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
success = 0

for dm in dms:
    if dm["type"] == 1:
        cid = dm["id"]
        messages = requests.get(f"https://discord.com/api/v9/channels/{cid}/messages?limit=50", headers=headers).json()
        for msg in messages:
            if msg["author"]["id"] == requests.get("https://discord.com/api/v9/users/@me", headers=headers).json()["id"]:
                res = requests.delete(f"https://discord.com/api/v9/channels/{cid}/messages/{msg['id']}", headers=headers)
                print(f"Deleted message {msg['id']} in {cid} - {res.status_code}")
                if res.status_code == 204:
                    success += 1

if success > 0:
    time.sleep(999)
