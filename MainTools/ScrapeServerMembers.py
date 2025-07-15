import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

guild_id = input("Enter Guild ID: ")
limit = input("Enter how many members to fetch (max 1000): ")

headers = {"Authorization": token}
url = f"https://discord.com/api/v9/guilds/{guild_id}/members?limit={limit}"

res = requests.get(url, headers=headers)
if res.status_code == 200:
    members = res.json()
    for m in members:
        print(f"{m['user']['username']}#{m['user']['discriminator']} - ID: {m['user']['id']}")
    time.sleep(999)
else:
    print("Failed to scrape members:", res.status_code)
