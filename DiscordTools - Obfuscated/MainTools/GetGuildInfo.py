import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

guild_id = input("Enter Guild ID: ")
headers = {"Authorization": token}

res = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}", headers=headers)
if res.status_code == 200:
    g = res.json()
    print(f"Name: {g['name']}\nID: {g['id']}\nOwner: {g['owner_id']}\nMembers: {g['approximate_member_count'] if 'approximate_member_count' in g else 'N/A'}")
    time.sleep(999)
else:
    print("Failed to get guild info:", res.status_code)
