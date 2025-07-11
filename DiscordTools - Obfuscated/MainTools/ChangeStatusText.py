import os
import requests
import sys

# Step 1: Load token from ../discord_token.txt
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
token_file_path = os.path.join(parent_dir, "token.txt")

if not os.path.exists(token_file_path):
    print("Token file not found.")
    sys.exit()

with open(token_file_path, "r") as file:
    token = file.read().strip()

# Step 2: Prompt for custom status and emoji
custom_text = input("Enter your custom status message: ").strip()
custom_emoji = input("Enter emoji (leave blank for none): ").strip()

# Step 3: Send PATCH request to set custom status
url = "https://discord.com/api/v9/users/@me/settings"
headers = {
    "Authorization": token,
    "Content-Type": "application/json",
    "User-Agent": "Discord/129.0.0 (Linux; Python educational bot)",
}

# Compose payload
payload = {
    "custom_status": {
        "text": custom_text
    }
}

if custom_emoji:
    payload["custom_status"]["emoji_name"] = custom_emoji

response = requests.patch(url, headers=headers, json=payload)

# Step 4: Result
if response.status_code == 200:
    print("Custom status updated successfully.")
else:
    print("Failed to update status.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
