import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

headers = {"Authorization": token}
message = input("Message to send: ")
success = 0

friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
for f in friends:
    if f["type"] == 1:
        dm = requests.post("https://discord.com/api/v9/users/@me/channels", headers=headers, json={"recipient_id": f["id"]})
        if dm.status_code == 200:
            cid = dm.json()["id"]
            res = requests.post(f"https://discord.com/api/v9/channels/{cid}/messages", headers=headers, json={"content": message})
            print(f"Sent to {f['user']['username']}: {res.status_code}")
            success += 1
        else:
            print(f"Failed to DM {f['user']['username']}")
if success > 0:
    time.sleep(999)
