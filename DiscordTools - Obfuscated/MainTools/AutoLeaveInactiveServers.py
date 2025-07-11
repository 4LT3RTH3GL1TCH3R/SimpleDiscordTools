import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

headers = {"Authorization": token}
guilds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
left = 0

for g in guilds:
    if not g.get("owner", False) and g.get("permissions", 0) == 0:
        res = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{g['id']}", headers=headers)
        print(f"Left inactive server {g['name']} - {res.status_code}")
        if res.status_code == 204:
            left += 1

if left > 0:
    time.sleep(999)
