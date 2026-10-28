""" 
Name: Note_Taking_App
Author: Jordan Mensah
Purpose: A note-taking app that runs in the terminal that allows users to create, view, and delete notes for all of their classes.
Source Code (References):
    - General Knowledge: Python Crash Course Online Textbook (Chapters 1-7)
    - Getting length of dict: https://www.geeksforgeeks.org/python/get-length-of-dictionary-in-python/
Date: September 14, 2026
"""
from pathlib import Path
import json
from notebook import Notebook

path = Path('notes.json')

def main() -> None:
    """Main fuction that runs the note taking application, including user input, loading existing JSON files, saving to JSON files and loading the UI loop

    Returns:
        None
    """
    # To be refactored
    # if path.exists():
    #     contents: str = path.read_text()
    #     dict_of_notes = json.loads(contents)

    # else:
    #     dict_of_notes: dict[str, str] = {}

    app_notebook = Notebook()
    app_running = True

    while app_running:
        print("Python-Based Note Taking App")
        print("1. Create Note")
        print("2. View all Notes")
        print("3. Manage Notes")
        print("4. Close Application")

        user_control: str = input("Select an Option 1-4: ")

        if user_control == '1':
            note_title: str = input("Enter the title of your note: ")
            note_body: str = input("Enter the body of your note: ")

            app_notebook.create_note(note_title, note_body)
            print(f"Note {note_title} has been created successfully.")

        elif user_control == '2':
            print('Your Notes')
            if len(app_notebook.notes) == 0:
                print(f"You have zero notes.")
            else:
                for title, note_obj in app_notebook.notes.items():
                    print("-----------------")
                    print(f"Title: {title}")
                    print(f"Body: {note_obj.body}")

            input("Press a key to return to the main menu")

        elif user_control == '3':
            if len(app_notebook.notes) == 0:
                print("You have no notes to manage.")
            else:
                print("All Notes")
                for title in app_notebook.notes.keys():
                    print("---------")
                    print(f"{title}")
                note_to_manage: str = input("Enter the title of the note you want to manage: ")

                if note_to_manage in app_notebook.notes.keys():
                    print("Note Options")
                    print("1. Edit Note")
                    print("2. Delete Note")
                    print("3. Return")

                    manage_note: str = input("Select an option 1-3: ")

                    if manage_note == "1":
                        note_rewrite: str = input(f"Enter the new body of {note_to_manage}: ")
                        app_notebook.edit_note(note_to_manage, note_rewrite)
                        print(f"Your note '{note_to_manage}' has successfully been updated.")
                    elif manage_note == "2":
                        app_notebook.delete_note(note_to_manage)
                        print(f"Your note, {note_to_manage} has been deleted.")
                    elif manage_note == "3":
                        print("Returning to menu")
                    else:
                        print(f"Invalid option. Returning to menu")
                else:
                    print(f"Error, note {note_to_manage} was not found")
        elif user_control == '4':
            # To be refactored later
            # contents: str = json.dumps(dict_of_notes)
            # path.write_text(contents)
            print('Goodbye.')
            app_running = False
        else: 
            print('Not a valid option. Please select a number from 1-4.')

main()