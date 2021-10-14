import subprocess
import re  

command_out = subprocess.run(['netsh', 'wlan', 'show', 'profile', 'tumoGuest'], capture_output=True).stdout.decode()

print(command_out)