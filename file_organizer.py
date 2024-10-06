import os
from tkinter import Tk, Button, Label, messagebox
from utils import show_message, load_db, edit_db
from file_operations import organize_files, user_prompt

def user_selection_menu() -> None:
    """
    Creates a window that lets the user choose between organizing a folder or editing the JSON file.
    """
    def on_organize():
        extensions_mapping = load_db()
        if not extensions_mapping:
            return # Do nothing if extensions_map.JSON not found
        
        selected_directory = user_prompt()

        # If user clicks "Cancel," selected_directory will be an empty string
        if not selected_directory:
            return # Do nothing if user cancels
         
        #Check for valid directory
        if not os.path.exists(selected_directory):
            show_message('Error', 'INVALID DIRECTORY')
            return # Do nothing if directory doesn't exist
         
        try:
            organize_files(selected_directory, extensions_mapping)
            show_message('Success', 'SUCCESSFULLY SORTED')
        except Exception as e:
            show_message('Error', f"{'SORTING FAILED'}: {str(e)}")

    def on_edit_db():
        edit_db()

    def initialize_gui() -> None:
        root = Tk()
        root.title("File Organizer")
        root.geometry('300x150')

        Label(root, text="Choose an action:", font=("Arial", 14)).pack(pady=10)

        organize_button = Button(root, text="Organize Folder", command=on_organize, width=25)
        organize_button.pack(pady=5)

        edit_button = Button(root, text="Edit JSON File", command=on_edit_db, width=25)
        edit_button.pack(pady=5)

        root.protocol("WM_DELETE_WINDOW", root.quit)  # Close the window properly
        root.mainloop()

    initialize_gui()
