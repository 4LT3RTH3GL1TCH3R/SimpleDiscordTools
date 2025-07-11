import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

headers = {"Authorization": token}
res = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)
accepted = 0

for user in res.json():
    if user["type"] == 3:  # Incoming request
        uid = user["id"]
        accept = requests.put(f"https://discord.com/api/v9/users/@me/relationships/{uid}", headers=headers)
        print(f"Accepted request from {uid} - {accept.status_code}")
        if accept.status_code == 204:
            accepted += 1

if accepted > 0:
    time.sleep(999)
