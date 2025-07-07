#regionstart (Imports)
import time
import os
import sys
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
#regionend (README)

#regionstart (Info)
print("Free Tools For Discord")
print("Made by: ! No0neX")
print("Version: 1.0.0")
time.sleep(5)
os.system("cls")
#regionend (Info)

#regionstart (Get Token)
print("Please input your Discord token: (You can get your token by following the instructions in the README)")
token = input("Token: ")
with open("token.txt", "w") as file:
    file.write(token)
print("Token saved to token.txt")
time.sleep(2)
os.system("cls")
#regionend (Get Token)

#regionstart (Get Password)
print("Please input your Discord password: (This is needed for some tools to function properly)")
password = input("Password: ")
with open("password.txt", "w") as file:
    file.write(password)
print("Password saved to password.txt")
time.sleep(2)
os.system("cls")
#regionend (Get Password)

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
print("12. Exit")
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
    print("Exiting the tool. Thank you for using Free Tools For Discord!")
    time.sleep(2)
    sys.exit()