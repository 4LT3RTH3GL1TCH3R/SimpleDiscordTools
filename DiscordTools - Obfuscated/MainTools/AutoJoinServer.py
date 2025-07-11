import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

invite = input("Enter invite code (without discord.gg/): ")
headers = {"Authorization": token}
res = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers)

print(f"Join server response: {res.status_code} {res.text}")
if res.status_code in (200, 201):
    time.sleep(999)
