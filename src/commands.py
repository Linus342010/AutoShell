import os
import pyautogui as gui
import src.log as log

def open_app(app):
    print(f"Opening: {app}")
    try:
        os.startfile(app)
    except Exception as e:
        log.error(f"Error opening {app}: {e}")

def press(*key):
    print(f"Pressing: {key}")
    try:
        if len(key) > 1:

            gui.hotkey(*key)
            
        else:
            
            gui.press(key)
            
    except Exception as e:
        log.error(f"Error occured in pyautogui: {e}")
 
class Logic:
    def __init__(self):
        pass

    def equal(self, a, b):
        if a == b:
            return True
        else:
            return False
    def bigger(self, a, b):
        if a > b:
            return True
        else:
            return False
    def smaller(self, a, b):
        if a < b:
            return True
        else:
            return False
    def not_equal(self, a, b):
        if a != b:
            return True
        else:
            return False