"""
Name: Note
Author: Jordan Mensah
Purpose: Note class that represents an individual note.
Source Code (References): Acknowledgements
Date: 10/6/26
"""

class Note:
    """Class that defines a single note with a title and body."""

    def __init__(self, title: str, body: str) -> None:
        """Intializes the note with a title and body"""
        self.title = title
        self.body = body

    def get_word_count(self):
        """Returns the number of words in the note's body."""
        return len(self.body.split())