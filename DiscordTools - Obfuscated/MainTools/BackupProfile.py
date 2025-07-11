import requests, json, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

headers = {"Authorization": token}
url = "https://discord.com/api/v9/users/@me"

res = requests.get(url, headers=headers)
if res.status_code == 200:
    with open("backup.json", "w") as f:
        json.dump(res.json(), f, indent=4)
    print("Backup saved to backup.json")
    time.sleep(999)
else:
    print("Failed to get profile:", res.status_code)
