import requests, json, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

headers = {"Authorization": token, "Content-Type": "application/json"}

with open("backup.json", "r") as f:
    data = json.load(f)

payload = {
    "username": data.get("username"),
    "bio": data.get("bio", "")
}

res = requests.patch("https://discord.com/api/v9/users/@me", headers=headers, json=payload)
print("Restore result:", res.status_code, res.text)
if res.status_code == 200:
    time.sleep(999)
