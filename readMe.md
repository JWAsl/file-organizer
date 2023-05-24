# File Organizer

This file organizer is a Python script that will organize files in a chosen directory based on their file extensions. It will scan the target directory, identify files with specifice extensions and move them to the corresponding folders based on the file type.

## Features

Prompts user to select a directory to organize (No need to input path using text). \
Loads file extension to folder name  mappings from a JSON file. \
Organize files in selected  directory  based on their extension. \
Create destination folders if they don't already exist. \
Move files to their respective folders.

## Usage

1. Ensure you have Python 3.x installed and required dependencies

2. Prepare the JSON file with the file extension to folder name mappings with the following format:

```json
{
    ".ext1: "Folder1",
    ".ext2: "Folder2",
    ".ext3: "Folder3",
    ...
}
```

3. Run the 'organize_files.py' script. You will be prompted to select a directory to organize.

4. After selecting the directory, the script will load the extensions mappings from the JSON file and organize accordingly.
   Note: Make sure you have appropriate permissions as the script will move files into folders within the directory.

## Customization

You can modify the extensions_map.JSON to add or remove entries. I have included some of the more common file types and some folders to put them in already.

# License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.
