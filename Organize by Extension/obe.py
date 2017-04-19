# Organize by Extension
# by Adil Iqbal

from os import scandir, listdir, rmdir, mkdir, rename
from sys import argv
from pathlib import Path


def main():
    print("\nRoot directory:", rootDirectory)
    confirm = input("Re-organize this directory by file-type? (Y/N): ")

    if confirm.lower() == 'n':
        print('Thank you for trying this program.')
        exit()

    elif confirm.lower() == 'y':
        print('\nRemoving branch directories...')
        removeBranches(rootDirectory)

        print('\nCreating new directories based on file extensions...')
        newDirectoriesByExtension(rootDirectory)

        print('\nSorting files into new directories based on file-types...')
        sortByExtension(rootDirectory)

        print('\nAll files have been sorted. Thank you.\n')
        exit()

    else:
        main()


def removeBranches(thisDirectory):

    # Iterate over all items in the directory.
    with scandir(thisDirectory) as cd:
        for entry in cd:

            # Recursively reach from the root directory into all branch directories.
            if not entry.name.startswith('.') and entry.is_dir():
                branchDirectory = thisDirectory + "\\" + str(entry.name)
                removeBranches(branchDirectory)

            # Temporarily move all files in branch directories to the root directory.
            if thisDirectory != rootDirectory:
                if entry.is_file():
                    previousEntryPath = entry.path
                    newEntryPath = rootDirectory + "\\" + entry.name
                    rename(previousEntryPath, newEntryPath)
                    print("Temporarily moved to root directory: ", entry.name)

    # Delete all branch directories once empty.
    if thisDirectory != rootDirectory:
        rmdir(thisDirectory)
        print("Deleted directory: ", thisDirectory)


# Create new branch directories based on file types in the directory.
def newDirectoriesByExtension(thisDirectory):

    # Build an array of file names based on the file-types in the directory.
    newDirectories = []
    for entry in listdir(thisDirectory):
        if Path(thisDirectory + "\\" + entry).is_file():
            fileExtension = Path(entry).suffix[1:].upper()
            for i in range(len(newDirectories)):
                if fileExtension == newDirectories[i]:
                    break # Avoid repeated file names.
            else:
                newDirectories.append(fileExtension)

    # Create new branch directories based on file names in the array.
    for extension in newDirectories:
        mkdir(thisDirectory + "\\" + extension)
        print("Created new directory: " + extension)


# Place all files in respective file-type branch directory.
def sortByExtension(thisDirectory):
    for entry in listdir(thisDirectory):
        previousEntryPath = thisDirectory + "\\" + entry
        if Path(previousEntryPath).is_file():
            fileExtension = Path(entry).suffix[1:].upper()
            newEntryPath = thisDirectory + "\\" + fileExtension + "\\" + entry
            rename(previousEntryPath, newEntryPath)
            print("Moved following file to \"" + fileExtension + "\" folder: " + entry)


# Initialize by defining/validating root directory and invoking script.
if __name__ == '__main__':
    try:
        rootDirectory = argv[1]
    except:
        rootDirectory = input("What is the chosen root directory: ")
    if not Path(rootDirectory).exists():
        print('The directory \"' + rootDirectory + '\" does not exist. Please check the directory and try again.')
        exit()
    main()
