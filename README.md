# Keylogger-CyS
Keylogger with Discord Webhook Integration
Utilizes many functions found in [winutils](https://github.com/CernachX/winutils-CyS).

This Python script is a keylogger that captures keyboard input and sends the logged data to a Discord webhook. It also includes functionality to add itself to the Windows Registry for autorun on system startup. The script uses threading to periodically send logged keys to the webhook while continuously monitoring keyboard events. Compatible with pyinstaller, allowing this .py script to be compiled into a .exe file.

Keylogging: Captures every key press using the pynput library. Logs the key press along with the username of the current user and a timestamp.
Discord Webhook Integration: Sends the logged keys to a specified encoded Discord webhook URL every 5 seconds. Combines all logged keys into a single message before sending.
Performance: The script uses threading to ensure smooth operation without blocking the keylogger or webhook sending.
Security Risks: The script modifies the Windows Registry, which may be flagged by antivirus software. Can be disabled but this can impact the persistence ability of the script. 
