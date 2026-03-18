import os
import pyautogui as gui
import src.log as log
import subprocess

def open_app(app):
    try:
        subprocess.run(app)
    except Exception as e:
        log.error(f"Error opening {app}: {e}")

def press(*key):
    try:
        if len(key) > 1:

            gui.hotkey(*key)
            
        else:
            
            gui.press(key)
            
    except Exception as e:
        log.error(f"Error occured in pyautogui: {e}")
 
def mouse_click(*number):
    gui.click(*number)