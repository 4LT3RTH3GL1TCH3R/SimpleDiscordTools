import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

headers = {"Authorization": token, "Content-Type": "application/json"}
names = input("Enter display names separated by commas: ").split(",")
delay = int(input("Delay between changes (in seconds): "))

for name in names:
    name = name.strip()
    res = requests.patch("https://discord.com/api/v9/users/@me", headers=headers, json={"username": name})
    print(f"Changed display name to {name} - {res.status_code}")
    time.sleep(delay)

time.sleep(999)
