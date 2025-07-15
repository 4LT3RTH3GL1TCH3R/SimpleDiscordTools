import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

channel_id = input("Enter Channel ID: ")
headers = {"Authorization": token}

res = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=50", headers=headers)
if res.status_code == 200:
    for m in res.json():
        print(f"{m['author']['username']}: {m['content']}")
    time.sleep(999)
else:
    print("Failed to get message history:", res.status_code)
