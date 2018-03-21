# Smart Folder (Desktop Organizer 2.0)

This is a simple application for organizing desktop space by sorting files based on their extensions into corresponding folders

Folders with [!smart!] included in the name will be recognized as smart folders by the application. A corresponding extbank.fc file is generated in each smart folder holding a list of file extension types of the files exist inside the folder. Files with the same extensions on the desktop as those that already exist inside the smart folder will be pulled inside the folder every time the program is run.

To create a smart folder, simply add [!smart!] as part of the folder name then run the program or through the program following the prompt.

Known issues:

- Smart Folder cannot move files that are currently open or being used.
- When two or more folders contain the same extension type, the files will be automatically moved into the first folder based on alphabetical order
