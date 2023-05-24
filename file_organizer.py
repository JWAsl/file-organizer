# Allows program to interact with OS.
import os
# Shell utilities, allows program to perform common file operations such as copying or moving.
import shutil
import json
from typing import Dict
# Able to create and manipulate GUI widgets
from tkinter import Tk, messagebox
# Convenient way to prompt user to select a directory using a dialog box
from tkinter.filedialog import askdirectory


def show_error_message(title: str, message: str) -> None:
    root = Tk()
    root.withdraw()
    messagebox.showerror(title, message)


def show_success_message(title: str, message: str) -> None:
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title, message)


def load_db() -> Dict[str, str]:
    """

    Loads extensions_map.JSON in directory file_organizer.py is run in.
    Returns:
        Dict[str, str]: Dictionary mapping file extensions to folder names.

    """

    file_path = os.path.join(os.curdir, 'extensions_map.JSON')
    try:
        with open(file_path) as file:
            extensions_map = json.load(file)
        return extensions_map
    except FileNotFoundError:
        show_error_message('Error', 'extensions_map.JSON not found')
        return {}


def user_prompt() -> str:
    """

    Prompt user to select a directory to organize
    Returns:
        str: Selected path

    """
    root = Tk()
    root.withdraw()
    return askdirectory(title="Select a folder")


def organize_files(working_directory: str, extension_to_folder: Dict[str, str]) -> None:
    """

    Organizes files in a given directory based on the file extension.

    Parameters:
        working_directory (str) : Target directory where files are located.
        extension_to_folder (dict) : Dictionary mapping file extensions to folder names.

    """
    for filename in os.listdir(working_directory):
        if os.path.isfile(os.path.join(working_directory, filename)):
            file_extension = os.path.splitext(filename)[1]
            if file_extension in extension_to_folder:
                folder_name = extension_to_folder[file_extension]
                folder_path = os.path.join(working_directory, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                shutil.move(os.path.join(working_directory, filename),
                            os.path.join(folder_path, filename))


extensions_mapping = load_db()

if extensions_mapping:
    selected_directory = user_prompt()
    if selected_directory != '' and os.path.exists(selected_directory):
        try:
            organize_files(selected_directory, extensions_mapping)
            show_success_message('Success', 'Folder is now sorted')
        except Exception as e:
            show_error_message('Error', str(e))
    else:
        show_error_message('Error', 'Either no directory or an invalid one was selected')


