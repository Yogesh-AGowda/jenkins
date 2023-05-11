import os
import urllib.request

# Get the AnyDesk download URL
url = "https://download.anydesk.com/AnyDesk.exe"

# Check if the AnyDesk app is already installed
if os.path.exists("AnyDesk.exe"):
  print("AnyDesk is already installed.")
else:
  # Download the AnyDesk app
  print("Downloading AnyDesk...")
  with urllib.request.urlopen(url) as response:
    with open("AnyDesk.exe", "wb") as f:
      f.write(response.read())

  # Install the AnyDesk app
  print("Installing AnyDesk...")
  os.system("AnyDesk.exe /install")

  # Start the AnyDesk app
  print("Starting AnyDesk...")
  os.system("AnyDesk")
