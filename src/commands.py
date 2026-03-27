import os
import pyautogui as gui
import src.log as log
import subprocess
import webbrowser

def open_app(app):
    log.info(f"Opening: {app}")
    try:
        os.startfile(app)
        log.success(f"Successfully opened: {app}")
    except Exception as e:
        log.error(f"Error opening {app}: {e}")

def close_app(app):
    log.info(f"Closing: {app}")
    try:
        subprocess.run(["taskkill", "/im", app, "/f"], check=True)
        log.success(f"Successfully closed: {app}")
    except Exception as e:
        log.error(f"Error closing {app}: {e}")


def press(*key):
    log.info(f"Pressing: {key}")
    try:
        if len(key) > 1:

            gui.hotkey(*key)
            
        else:
            
            gui.press(key)
        
        log.success(f"Successfully pressed: {key}")
            
    except Exception as e:
        log.error(f"Error occured in pyautogui: {e}")

def open_url(url):
    log.info(f"Opening URL: {url}")
    try:
        webbrowser.open(url)
        log.success(f"Successfully opened URL: {url}")
    except Exception as e:
        log.error(f"Error opening URL: {e}")

def open_file(file):
    log.info(f"Opening file: {file}")
    try:
        os.startfile(file)
        log.success(f"Successfully opened file: {file}")
    except Exception as e:
        log.error(f"Error opening file: {e}")

def show_in_explorer(path):
    log.info(f"Showing in explorer: {path}")
    try:
        subprocess.Popen(['explorer', '/select,', path])
        log.success(f"Successfully showed in explorer: {path}")
    except Exception as e:
        log.error(f"Error opening in explorer: {e}")

def open_file(path):
    log.info(f"Opening file: {path}")
    try:
        subprocess.Popen(['explorer', path])
        log.success(f"Successfully opened in explorer: {path}")
    except Exception as e:
        log.error(f"Error opening in explorer: {e}")