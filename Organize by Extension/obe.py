# Copyright 2017 by Adil Iqbal.
# All rights reserved.

"""Organize by Extension.

Organize directory by file types. For Windows only.
"""

from os import scandir, listdir, rmdir, mkdir, rename
from sys import platform, argv
from pathlib import Path


def main():
    """Run sequence of functions."""
    print("\nRoot directory:", root_dir)
    confirm = input("Re-organize this directory by file-type? (Y/N): ")

    if confirm.lower() == 'n':
        print('Thank you for trying this program.')
        exit()

    elif confirm.lower() == 'y':
        print('\nRemoving branch directories...')
        remove_branches(root_dir)

        print('\nCreating new directories based on file extensions...')
        new_dir_by_ext(root_dir)

        print('\nSorting files into new directories based on file-types...')
        sort_files_by_ext(root_dir)

        print('\nAll files have been sorted. Thank you.\n')
        exit()

    else:
        main()


def remove_branches(this_dir):
    """Remove sub-directories from the root directory."""
    # Iterate over all items in the directory.
    with scandir(this_dir) as cd:
        for entry in cd:
            # Recursively reach from root directory into sub-directories.
            if not entry.name.startswith('.') and entry.is_dir():
                branch_dir = this_dir + "\\" + str(entry.name)
                remove_branches(branch_dir)
            # Temporarily move files from sub-directories to root directory.
            if this_dir != root_dir:
                if entry.is_file():
                    prev_entry_path = entry.path
                    new_entry_path = root_dir + "\\" + entry.name
                    rename(prev_entry_path, new_entry_path)
                    print("Temporarily moved to root directory: ", entry.name)
    # Delete all branch directories once empty.
    if this_dir != root_dir:
        rmdir(this_dir)
        print("Deleted directory: ", this_dir)


def new_dir_by_ext(this_dir):
    """Create new directories based on file types."""
    # Build an array of file names based on the file-types in the directory.
    new_dirs = []
    for entry in listdir(this_dir):
        if Path(this_dir + "\\" + entry).is_file():
            file_ext = Path(entry).suffix[1:].upper()
            for i in range(len(new_dirs)):
                if file_ext == new_dirs[i]:
                    break  # Avoid repeated file names.
            else:
                new_dirs.append(file_ext)
    # Create new branch directories based on file names in the array.
    for extension in new_dirs:
        mkdir(this_dir + "\\" + extension)
        print("Created new directory: " + extension)


def sort_files_by_ext(this_dir):
    """Place all files in respective file-type branch directory."""
    for entry in listdir(this_dir):
        prev_entry_path = this_dir + "\\" + entry
        if Path(prev_entry_path).is_file():
            file_ext = Path(entry).suffix[1:].upper()
            new_entry_path = this_dir + "\\" + file_ext + "\\" + entry
            rename(prev_entry_path, new_entry_path)
            print("Moved this file to \"" + file_ext + "\" folder: " + entry)


# Initialize by defining/validating root directory and invoking script.
if __name__ == '__main__':
    if platform[:3] != 'win':
        print('For Windows only. Unsupported platform: ' + platform)
        exit()
    try:
        root_dir = argv[1]
    except IndexError:
        root_dir = input("What is the chosen root directory: ")
    if not Path(root_dir).exists():
        print('The directory \"' + root_dir + '\" does not exist.", \
            "Please check the directory and try again.')
        exit()
    main()
