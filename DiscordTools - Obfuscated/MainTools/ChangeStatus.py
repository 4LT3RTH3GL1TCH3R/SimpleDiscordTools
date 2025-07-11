import os
import requests
import sys

# Step 1: Load token from one directory above
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_file_path = os.path.join(parent_dir, "token.txt")

if not os.path.exists(token_file_path):
    print("Token file not found.")
    sys.exit()

with open(token_file_path, "r") as file:
    token = file.read().strip()

# Step 2: Ask for new presence status
presence = input("Enter presence (online, idle, dnd, invisible): ").strip().lower()

if presence not in ["online", "idle", "dnd", "invisible"]:
    print("Invalid presence. Must be one of: online, idle, dnd, invisible")
    sys.exit()

# Step 3: Send PATCH request to change presence
url = "https://discord.com/api/v9/users/@me/settings"
headers = {
    "Authorization": token,
    "Content-Type": "application/json",
    "User-Agent": "Discord/129.0.0 (Linux; Python educational bot)",
}
payload = {
    "status": presence
}

response = requests.patch(url, headers=headers, json=payload)

# Step 4: Handle result
if response.status_code == 200:
    print(f"Presence successfully updated to: {presence}")
else:
    print("Failed to update presence.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
