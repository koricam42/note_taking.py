""" 
Name: Note_Taking_App
Author: Jordan Mensah
Purpose: A note-taking app that runs in the terminal that allows users to create, view, and delete notes for all of their classes.
Source Code (References):
    - General Knowledge: Python Crash Course Online Textbook (Chapters 1-7)
    - Getting length of dict: https://www.geeksforgeeks.org/python/get-length-of-dictionary-in-python/
Date: September 14, 2026
"""
from notebook import Notebook

class AppInterface:
    """Handles the terminal-based interface for the application"""

    def __init__(self):
        """Initalize notebook backend, flag for application state, and note state"""
        self.app_notebook = Notebook()
        self.app_running = True
        self.note_to_manage = ""

    def display_note_list(self) -> None:
        """Method to handle the displaying of all stored notes with numbers, bodies, and word count"""
        count =  1
        for title, note_obj in self.app_notebook.notes.items():
            print("-----------------")
            print(f"{count}. {title}")
            print(f"Body: {note_obj.body}")
            print(f"Word Count: {note_obj.get_word_count()}")
            count += 1

    def note_creator(self) -> None:
        """Prompts user for a title and body to create a new note"""
        note_title: str = input("Enter the title of your note: ")
        note_body: str = input("Enter the body of your note: ")

        self.app_notebook.create_note(note_title, note_body)
        print(f"Note {note_title} has been created successfully.")

    def note_viewer(self) -> None:
        """Display all existing notes or notify user if the notebook is empty"""
        print('Your Notes')
        if not self.app_notebook.notes:
            print(f"You have zero notes.")
        else:
            self.display_note_list()
        input("\nPress a key to return to the main menu")

    def note_manager_editor(self) -> None:
        """Prompts user for a new body and updates the currently active note"""
        note_rewrite: str = input(f"Enter the new body of {self.note_to_manage}: ")
        if self.app_notebook.edit_note(self.note_to_manage, note_rewrite):
            print(f"Your note '{self.note_to_manage}' has successfully been updated.")
        else:
            print(f"Error, note {self.note_to_manage} was not found.")

    def note_manager_removal(self) -> None:
        """Deletes currently selected note from the notebook"""
        if self.app_notebook.delete_note(self.note_to_manage):
            print(f"Your note, {self.note_to_manage} has been deleted.")
        else:
            print(f"Error, note {self.note_to_manage} was not found.")

    def note_manager_dismissal(self) -> None:
        """Cancel note management and return to main menu"""
        print("Returning to menu")
        
    def note_manager_main(self) -> None:
        """Display notes, prompts user to select note by number and routes input to management actions"""
        if not self.app_notebook.notes:
            print("You have no notes to manage.")
            return
    
        print("\nAll Notes")
        self.display_note_list()

        user_input: str = input("Enter the number of the note you want to manage: ")
        
        try:
            user_choice = int(user_input)
        except ValueError:
            print("Error, please enter a valid number.")
        else:
            search_counter = 1
            self.note_to_manage = ""

            for title in self.app_notebook.notes.keys():
                if search_counter == user_choice:
                    self.note_to_manage = title
                    break
                search_counter += 1

            if self.note_to_manage != "":
                print(f"\nManaging {self.note_to_manage}")
                print("Note Options")
                print("1. Edit Note")
                print("2. Delete Note")
                print("3. Return")

                manage_note: str = input("Select an option 1-3: ")

                manager_actions = {
                    "1": self.note_manager_editor,
                    "2": self.note_manager_removal,
                    "3": self.note_manager_dismissal
               }

                action = manager_actions.get(manage_note)

                if action:
                    action()
                else:
                    print(f"Invalid option. Returning to menu")
            else:
                print(f"Error, note number {user_choice} was not found.")        

    def note_shutdown(self):
        """Saves all notes to JSON storage and ends main application loop"""
        self.app_notebook.save_notes()
        print("Goodbye.")
        self.app_running = False

    def main(self) -> None:
        """Main fuction that runs the UI loop via dictionary dispatch"""
        menu_options = {
            "1": self.note_creator,
            "2": self.note_viewer,
            "3": self.note_manager_main,
            "4": self.note_shutdown
        }

        while self.app_running:
            print("\nPython-Based Note Taking App")
            print("1. Create Note")
            print("2. View all Notes")
            print("3. Manage Notes")
            print("4. Close Application")

            user_control: str = input("Select an Option 1-4: ")

            option = menu_options.get(user_control)
                
            if option:
                option()
            else:
                print("Not a valid option. Please select a number from 1-4.")

if __name__ == "__main__":
    ui = AppInterface()
    ui.main()