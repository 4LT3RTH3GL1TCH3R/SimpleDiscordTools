import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

headers = {"Authorization": token}
url = "https://discord.com/api/v9/auth/sessions"

res = requests.get(url, headers=headers)
if res.status_code == 200:
    sessions = res.json()
    print("Active Sessions:")
    for session in sessions:
        print(f"- {session.get('client_info', {}).get('os', 'Unknown OS')} at {session.get('location', 'Unknown Location')}")
    time.sleep(999)
else:
    print("Failed to fetch sessions:", res.status_code)
