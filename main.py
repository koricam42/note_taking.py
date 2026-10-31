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
from notebook import Notebook

# path = Path('notes.json') -> To be dealt with later.

class AppInterface:
    def __init__(self):
        self.app_notebook = Notebook()
        self.app_running = True

    # Methods to handle various app functions, to be filled out later...
    def display_note_list(self) -> None:
        """_summary_
        """
        count =  1
        for title, note_obj in self.app_notebook.notes.items():
            print("-----------------")
            print(f"{count}. {title}")
            print(f"Body: {note_obj.body}")
            word_count = len(note_obj.body.split())
            print(f"Word Count: {word_count}")
            count += 1

    def note_creator(self) -> None:
        """_summary_
        """
        # To be finalized later
        note_title: str = input("Enter the title of your note: ")
        note_body: str = input("Enter the body of your note: ")

        self.app_notebook.create_note(note_title, note_body)
        print(f"Note {note_title} has been created successfully.")
        pass
    def note_viewer(self) -> None:
        """_summary_
        """
        # To be finalized later
        print('Your Notes')
        if len(self.app_notebook.notes) == 0:
            print(f"You have zero notes.")
        else:
            self.display_note_list()
        input("Press a key to return to the main menu")
        
        pass
    def note_manager(self) -> None:
        """_summary_
        """
        # Option 3
        if len(self.app_notebook.notes) == 0:
            print("You have no notes to manage.")
            return
    
        print("All Notes")
        self.display_note_list()

        user_input: str = input("Enter the number of the note you want to manage: ")
        
        try:
            user_choice = int(user_input)
            search_counter = 1
            note_to_manage = ""

            for title in self.app_notebook.notes.keys():
                if search_counter == user_choice:
                    note_to_manage = title
                    break
                search_counter += 1

            if note_to_manage != "":
                print(f"Managing {note_to_manage}")
                print("Note Options")
                print("1. Edit Note")
                print("2. Delete Note")
                print("3. Return")

                manage_note: str = input("Select an option 1-3: ")

                if manage_note == "1":
                    note_rewrite: str = input(f"Enter the new body of {note_to_manage}: ")
                    self.app_notebook.edit_note(note_to_manage, note_rewrite)
                    print(f"Your note '{note_to_manage}' has successfully been updated.")
                elif manage_note == "2":
                    self.app_notebook.delete_note(note_to_manage)
                    print(f"Your note, {note_to_manage} has been deleted.")
                elif manage_note == "3":
                    print("Returning to menu")
                else:
                    print(f"Invalid option. Returning to menu")
            else:
                print(f"Error, note {note_to_manage} was not found")

        except ValueError:
            print("Error, please enter a valid number.")
    
        pass

    def main(self) -> None:
        """
        Main fuction that runs the UI loop
        """
        # To be finalized later

        while self.app_running:
            print("Python-Based Note Taking App")
            print("1. Create Note")
            print("2. View all Notes")
            print("3. Manage Notes")
            print("4. Close Application")

            user_control: str = input("Select an Option 1-4: ")

            if user_control == '1':
                self.note_creator()
            elif user_control == '2':
                self.note_viewer()
            elif user_control == '3':
                self.note_manager()
            elif user_control == '4':
                self.app_notebook.save_notes()
                print('Goodbye.')
                self.app_running = False
            else: 
                print('Not a valid option. Please select2 a number from 1-4.')

if __name__ == "__main__":
    ui = AppInterface()
    ui.main()