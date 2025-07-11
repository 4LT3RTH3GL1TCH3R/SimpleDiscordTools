import os
import requests
import sys
import time

# Load token from parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_file_path = os.path.join(parent_dir, "token.txt")

if not os.path.exists(token_file_path):
    print("Token file not found.")
    sys.exit()

with open(token_file_path, "r") as file:
    token = file.read().strip()

# Prompt for new About Me text
about_me = input("Enter your new About Me (bio): ").strip()

# Send PATCH request to update About Me
url = "https://discord.com/api/v9/users/@me/profile"
headers = {
    "Authorization": token,
    "Content-Type": "application/json",
    "User-Agent": "Discord/129.0.0 (Linux; Python educational bot)",
}

payload = {
    "bio": about_me
}

response = requests.patch(url, headers=headers, json=payload)

if response.status_code == 200:
    print("About Me updated successfully.")
else:
    print("Failed to update About Me.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)