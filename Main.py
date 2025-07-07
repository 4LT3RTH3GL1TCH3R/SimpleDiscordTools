#regionstart (Imports)
import time
import os
import sys
import requests
#regionend (Imports)

#regionstart (README)
      # Free Tools For Discord is a collection of tools for Discord users.
      # This tool requires a Discord token to function.
      # You can get your token by following these steps:
      # 1. Open Discord in your browser or desktop app.
      # 2. Open the Developer Tools (F12 or Ctrl+Shift+I).
      # 3. Go to the Application tab.
      # 4. Look for the "Local Storage" section.
      # 5. Find the key "token" and copy its value.
      # 6. Paste it below when prompted.
      # Note: Do not share your token with anyone. It is your personal key to access your account.
      # This tool is for educational purposes only and should not be used for malicious activities.
      # Use at your own risk.
      # This tool is not affiliated with Discord in any way.
      # We are not responsible for any actions taken using this tool.
      # Please use it responsibly.
      # If you have any questions or issues, please contact the developer.
      # Please note that when we prompt for your token, it is stored in a file called "token.txt" in the same directory as this script, it is NOT sent anywhere, or used for any malicious purposes.
      # ! No0neX is not responsible for any misuse of this tool.
      # DO NOT USE ANOTHER PERSON'S TOKEN, IT IS AGAINST DISCORD'S TERMS OF SERVICE AND CAN RESULT IN A BAN.
      # If you have any suggestions for new features, please let the developer know (Discord: d3c0mp0s1ngc0rps3)
      # This tool is open source, you can find the source code on GitHub:https://github.com/4LT3RTH3GL1TCH3R/SimpleDiscordTools
      # If you want to contribute to the project, feel free to fork the repository and submit a pull request.
      # Please note that this tool is still in development and may have bugs.
      # If you encounter any issues, please report them on the GitHub repository.
      # Thank you for using Free Tools For Discord!
      # Any sort
#regionend (README)

#regionstart (Strings)
CurrentVersion = "1.0.0"
pastebin_newest_version = "https://pastebin.com/raw/6aqEeTg8"
#regionend (Strings)

#regionstart (Backend Code)
try:
    response = requests.get(pastebin_newest_version)
    response.raise_for_status()  # Raises error for 4xx or 5xx status codes
    newest_version = response.text.strip()
    if newest_version != CurrentVersion:
        print(f"A new version of Free Tools For Discord is available: {newest_version}")
        print("Please update to the latest version for the best experience.")
        time.sleep(5)
        sys.exit()
except requests.exceptions.RequestException as e:
    print(f"Failed to fetch Pastebin content:\n{e}")
#regionend (Backend Code)

#regionstart (Info)
print("Free Tools For Discord")
print("Made by: ! No0neX")
print("Current Version: " + CurrentVersion)
print("Contact: d3c0mp0s1ngc0rps3")
print("There are more updates to come, please be patient.")
time.sleep(5)
os.system("cls")
#regionend (Info)

#regionstart (Token Sequence)
choice = input("Do you want to input your token? (yes if you don't already have a valid token in token.txt or to change token to use/skip if you already have a valid token in token.txt): ").strip().lower()
if choice == "yes":
    print("Please input your Discord token: (This is needed for some tools to function properly)")
    token = input("Token: ")
    with open("token.txt", "w") as file:
        file.write(token)
elif choice == "skip":
    print("Skipping token input. If you have a valid token in token.txt, it will be used.")
time.sleep(2)
os.system("cls")
#regionend (Token Sequence)

#regionstart (Password Sequence)
choice = input("Do you want to input your password? (PASSWORD MUST BELONG TO THE ACCOUNT THAT THE TOKEN YOU PUT BELONGS TO) (yes if you don't already have a valid password in password.txt or to change password to use/skip if you already have a valid password in password.txt): ").strip().lower()
if choice == "yes":
    print("Please input your Discord password: (This is needed for some tools to function properly)")
    password = input("password: ")
    with open("password.txt", "w") as file:
        file.write(password)
elif choice == "skip":
    print("Skipping password input. If you have a valid password in password.txt, it will be used.")
time.sleep(2)
os.system("cls")
#regionend (Password Sequence)

#regionstart (Free Tools For Discord)
#regionstart (Change Profile Options)
print("1. Change Display Name")
print("2. Change Profile Picture (link to the image you want)")
print("3. Change Status Text")
print("4. Change Status (Online/Idle/DND)")
print("5. Change Username")
print("6. Change About Me")
#regionend (Change Profile Options)

#regionstart (View Profile Options)
print("7. View Display Name")
print("8. View Status Text")
print("9. View Status (Online/Offline/Idle/DND)")
print("10. View Username")
print("11. View About Me")
#regionend (View Profile Options)
#regionend (Free Tools For Discord)

#regionstart (Other)
print("12. Updates")
print("13. Exit")
#regionend (Other)

#regionstart (Choice Inputs)
choice = input("Please choose a tool by their designated number. ")
if choice == "1":
    os.system("cls")
    print("You have chosen to change your display name.")
    os.system("python MainTools/ChangeDisplayName.py")
if choice == "2":
    os.system("cls")
    print("You have chosen to change your status text.")
    os.system("python MainTools/ChangeStatusText.py")
if choice == "3":
    os.system("cls")
    print("You have chosen to change your status (Online/Idle/DND).")
    os.system("python MainTools/ChangeStatus.py")
if choice == "4":
    os.system("cls")
    print("You have chosen to change your username.")
    os.system("python MainTools/ChangeUsername.py")
if choice == "5":
    os.system("cls")
    print("You have chosen to change your About Me.")
    os.system("python MainTools/ChangeAboutMe.py")
if choice == "6":
    os.system("cls")
    print("You have chosen to view your display name.")
    os.system("python MainTools/ViewDisplayName.py")
if choice == "7":
    os.system("cls")
    print("You have chosen to view your profile picture.")
    os.system("python MainTools/ViewProfilePicture.py")
if choice == "8":
    os.system("cls")
    print("You have chosen to view your status text.")
    os.system("python MainTools/ViewStatusText.py")
if choice == "9":
    os.system("cls")
    print("You have chosen to view your status (Online/Offline/Idle/DND).")
    os.system("python MainTools/ViewStatus.py")
if choice == "10":
    os.system("cls")
    print("You have chosen to view your username.")
    os.system("python MainTools/ViewUsername.py")
if choice == "11":
    os.system("cls")
    print("You have chosen to view your About Me.")
    os.system("python MainTools/ViewAboutMe.py")
if choice == "12":
    os.system("cls")
    print("You have chosen to view updates.")
    os.system("python MainTools/Updates.py")
if choice == "13":
    os.system("cls")
    print("You have chosen to exit.")
    print("Thank you for using Free Tools For Discord!")
    time.sleep(2)
    sys.exit()