"""
Name: Notebook
Author: Jordan Mensah
Purpose: Defines Notebook Class & Manages collection of Note objects
Source Code (References): TBA
Date: 10/6/26
"""
from note import Note

class Notebook:
    """
    Manages the collection of Note objects including
    Creating, editing, deleting, persistence
    """
    def __init__(self) -> None:
        self.notes = {}

    def create_note(self, title: str, body: str) -> None:
        """
        Creates a Note and adds it to the notes dictionary
        """
        new_note = Note(title, body)
        self.notes[title] = new_note

    def delete_note(self, title: str) -> None:
        """
        Deletes the selected Note from the note dictionary if it exists
        """
        if title in self.notes:
            del self.notes[title]

        else:
            print(f'Error, note {title} was not found.')

    def edit_note(self, title: str, new_body: str) -> None:
        "Updates the body of a existing note"
        if title in self.notes:
            self.notes[title].body = new_body
        else:
            print(f'Error, note {title} was not found.')