import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

user_id = input("User ID: ")
message = input("Message: ")

headers = {"Authorization": token, "Content-Type": "application/json"}

dm = requests.post("https://discord.com/api/v9/users/@me/channels", headers=headers, json={"recipient_id": user_id})
if dm.status_code == 200:
    cid = dm.json()["id"]
    res = requests.post(f"https://discord.com/api/v9/channels/{cid}/messages", headers=headers, json={"content": message})
    print("Message sent:", res.status_code)
    if res.status_code == 200:
        time.sleep(999)
else:
    print("Failed to create DM channel.")
