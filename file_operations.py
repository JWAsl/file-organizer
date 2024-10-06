import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory
from pathlib import Path

def user_prompt() -> str:
    """
    Prompt user to select a directory to organize
    Returns:
        str: Selected path
    """
    root = Tk()
    root.withdraw()
    return askdirectory(title="Select a folder")

def organize_files(working_directory: str, extension_to_folder: dict) -> None:
    """
    Organizes files in a given directory based on the file extension.
    
    Parameters:
        working_directory (str): Target directory where files are located.
        extension_to_folder (dict): Dictionary mapping file extensions to folder names.
    """

    working_path = Path(working_directory)

    for file_path in working_path.iterdir():
        if file_path.is_file():
            file_extension = file_path.suffix
            if file_extension in extension_to_folder:
                folder_name = extension_to_folder[file_extension]
                folder_path = working_path / folder_name
                # Create folder if it doesn't exist
                folder_path.mkdir(exist_ok=True)
                # Move the file
                shutil.move(str(file_path), str(folder_path / file_path.name))

