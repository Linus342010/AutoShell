import os
import pyautogui as gui

def open_app(app):
    try:
        os.startfile(app)
    except Exception as e:
        print(f"Error opening {app}: {e}")

def press(*key):
    try:
        if len(key) > 1:

            gui.hotkey(key)
            print(key)
        else:
            
            gui.press(key)
            print(key)
    except Exception as e:
        print(f"Error occured in pyautogui: {e}")
 
