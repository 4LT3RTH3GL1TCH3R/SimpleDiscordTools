import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

headers = {"Authorization": token}
friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()

for f in friends:
    if f["type"] == 1:
        user = f["user"]
        print(f"{user['username']}#{user['discriminator']} | ID: {user['id']}")

time.sleep(999)
