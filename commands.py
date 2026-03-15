import os

def open_app(app):
    try:
        os.startfile(app)
    except Exception as e:
        print(f"Error opening {app}: {e}")

