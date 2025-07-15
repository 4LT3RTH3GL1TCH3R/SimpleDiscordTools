import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

user_id = input("Enter user ID to check mutual servers: ")
headers = {"Authorization": token}
res = requests.get(f"https://discord.com/api/v9/users/{user_id}/profile", headers=headers)

if res.status_code == 200:
    mutuals = res.json().get("mutual_guilds", [])
    print(f"Mutual servers with {user_id}:")
    for g in mutuals:
        print(f"- ID: {g['id']}")
    time.sleep(999)
else:
    print("Failed to fetch profile:", res.status_code)
