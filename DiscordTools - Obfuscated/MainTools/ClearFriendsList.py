import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

headers = {"Authorization": token}
friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
success = 0

for f in friends:
    if f["type"] == 1:
        res = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{f['id']}", headers=headers)
        print(f"Removed friend {f['user']['username']} - {res.status_code}")
        if res.status_code == 204:
            success += 1

if success > 0:
    time.sleep(999)
