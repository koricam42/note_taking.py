"""
Name: Notebook
Author: Jordan Mensah
Purpose: Defines Notebook Class & Manages collection of Note objects
Source Code (References): TBA
Date: 10/6/26
"""
import json
from pathlib import Path

from note import Note


class Notebook:
    """Manages the creation, editing, deleting, and persistence of Note objects"""

    def __init__(self, storage_path: Path = Path("notes.json")) -> None:
        """Initalizes the notebook dictionary and loads existing notes from storage"""
        self.storage_path = storage_path
        self.notes = dict[str, Note] = {}
        self.load_notes()

    def create_note(self, title: str, body: str) -> None:
        """ Creates a Note and stores it in the notes dictionary"""
        self.notes[title] = Note(title, body)

    def delete_note(self, title: str) -> bool:
        """Deletes a Note by title if it exists if it exists and return True, otherwise return False"""
        if title in self.notes:
            del self.notes[title]
            return True
        return False

    def edit_note(self, title: str, new_body: str) -> bool:
        "Updates the body of a existing note and returns True, returns False if no note was found"
        if title in self.notes:
            self.notes[title].body = new_body
        else:
            print(f'Error, note {title} was not found.')

    def save_notes(self) -> None:
        """Convert all notes to JSON string and write them to a file"""
        save_data = {}
        for title, note_obj in self.notes.items():
            save_data[title] = note_obj.body

        contents = json.dumps(save_data, indent=4)
        self.storage_path.write_text(contents, encoding="utf-8")

    def load_notes(self) -> None:   
        """Read JSON file and loads the data back into the dictionary object"""
        try:
            contents = self.storage_path.read_text(encoding="utf-8")    
        except FileNotFoundError:
            pass
        else:
            loaded_notes = json.loads(contents)
            for title, body in loaded_notes.items():
                self.create_note(title, body)
            