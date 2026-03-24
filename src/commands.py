import os
import pyautogui as gui
import src.log as log
import subprocess

def open_app(app):
    print(f"Opening: {app}")
    try:
        os.startfile(app)
    except Exception as e:
        log.error(f"Error opening {app}: {e}")

def close_app(app):
    try:
        subprocess.run(["taskkill", "/im", app, "/f"], check=True)
    except Exception as e:
        log.error(f"Error closing {app}: {e}")

def press(*key):
    print(f"Pressing: {key}")
    try:
        if len(key) > 1:

            gui.hotkey(*key)
            
        else:
            
            gui.press(key)
            
    except Exception as e:
        log.error(f"Error occured in pyautogui: {e}")