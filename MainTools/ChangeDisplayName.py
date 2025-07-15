import os
import requests
import sys

# Step 1: Go up one directory and get token file
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_file_path = os.path.join(parent_dir, "token.txt")

if not os.path.exists(token_file_path):
    print("Token file not found.")
    sys.exit()

with open(token_file_path, "r") as file:
    token = file.read().strip()

# Step 3: Prompt for new display name
new_username = input("Enter your new Discord display name: ").strip()

# Step 4: Send PATCH request to Discord API
url = "https://discord.com/api/v9/users/@me"
headers = {
    "Authorization": token,
    "Content-Type": "application/json",
    "User-Agent": "Discord/129.0.0 (Linux; Python educational bot)",
}
data = {
    "username": new_username
}

response = requests.patch(url, headers=headers, json=data)

# Step 5: Result handling
if response.status_code == 200:
    print(f"Username changed successfully to: {new_username}")
else:
    print("Failed to change username.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
