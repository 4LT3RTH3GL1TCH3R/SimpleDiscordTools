import os
import requests
import sys

# Load credentials from parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_path = os.path.join(parent_dir, "token.txt")
password_path = os.path.join(parent_dir, "password.txt")

# Check for token file
if not os.path.exists(token_path):
    print("token.txt not found.")
    sys.exit()

# Check for password file
if not os.path.exists(password_path):
    print("password.txt not found.")
    sys.exit()

# Read token and password
with open(token_path, "r") as f:
    token = f.read().strip()

with open(password_path, "r") as f:
    password = f.read().strip()

# Prompt for new username
new_username = input("Enter new Discord username: ").strip()
if not new_username:
    print("Username cannot be empty.")
    sys.exit()

# Send PATCH request to change username
url = "https://discord.com/api/v9/users/@me"
headers = {
    "Authorization": token,
    "Content-Type": "application/json",
    "User-Agent": "Discord/129.0.0 (Linux; Python educational bot)",
}
payload = {
    "username": new_username,
    "password": password
}

response = requests.patch(url, headers=headers, json=payload)

# Output result
if response.status_code == 200:
    print(f"Username successfully changed to: {new_username}")
else:
    print("Failed to change username.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
