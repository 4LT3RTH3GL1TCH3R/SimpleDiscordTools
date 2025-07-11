import requests, os, time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
token = open(token_path).read().strip()

headers = {
    "Authorization": token,
    "Content-Type": "application/json"
}

statuses = input("Enter statuses separated by commas: ").split(",")
interval = int(input("Interval between status changes in seconds: "))

for status in statuses:
    payload = {
        "custom_status": {"text": status.strip()}
    }
    res = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
    print(f"Changed status to: {status.strip()} - {res.status_code}")
    time.sleep(interval)

time.sleep(999)
