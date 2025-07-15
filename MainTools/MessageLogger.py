import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

channel_id = input("Enter channel ID: ")
headers = {"Authorization": token}
seen = set()

print("Logging messages... Press Ctrl+C to stop.")
try:
    while True:
        res = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=10", headers=headers)
        for msg in res.json():
            if msg['id'] not in seen:
                print(f"{msg['author']['username']}: {msg['content']}")
                seen.add(msg['id'])
        time.sleep(5)
except KeyboardInterrupt:
    print("Stopped logging.")
    time.sleep(999)
# If you want to save the logged messages to a file, uncomment the following lines:
# with open("logged_messages.txt", "w") as f:
#     for msg_id in seen:
#         f.write(f"{msg_id}\n")
#     print("Logged messages saved to logged_messages.txt")
# except Exception as e:
#     print(f"An error occurred: {e}")
#     time.sleep(999)
#     sys.exit(1)