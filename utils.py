# utils.py

import json
from tkinter import Tk, messagebox
from pathlib import Path
import sys
import subprocess

def show_message(title: str, message: str) -> None:
    root = Tk()
    root.withdraw()
    if title == "Error":
        messagebox.showerror(title, message)
    elif title == "Success":
        messagebox.showinfo(title, message)
    root.destroy()

def open_editor(file_path: str) -> None:
    """
    Loads extensions_map.JSON in notepad for windows and default editor for other OS'
    """
    if sys.platform.startswith('win'): # If windows
        subprocess.run(['notepad', str(file_path)]) # Open with notepad
    elif sys.platform.startswith('darwin'): # If mac
        subprocess.run(['open', str(file_path)])  # Open with default editor
    else: # If not windows or mac, assume linux/uniux
        subprocess.run(['xdg-open', str(file_path)]) # Open with default editor

def load_db() -> dict:
    """
    Loads extensions_map.JSON in the directory main.py is run in.
    Returns:
        dict: Dictionary mapping file extensions to folder names.
    """
    file_path = Path('extensions_map.JSON')

    try:
        with file_path.open('r') as file:
            return json.load(file)
    except FileNotFoundError:
        show_message('Error', 'extensions_map.JSON not found')
        return {}
    
def edit_db() -> None:
    """
    Opens the extensions_map.JSON file located in the program's directory for editing.
    """
    file_path = Path('extensions_map.JSON')
    
    if file_path.exists():
        open_editor(file_path)
    else:
        show_message('Error', 'extensions_map.JSON not found in the current directory')
