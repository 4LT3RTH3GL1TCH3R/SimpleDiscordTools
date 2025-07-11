import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

channel_id = input("Enter Channel ID to fake typing: ")
headers = {"Authorization": token}

print("Sending typing indicator for 30 seconds...")
for _ in range(6):
    res = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/typing", headers=headers)
    print("Typing...")
    time.sleep(5)

time.sleep(999)
