"""
Name: 
Author: Jordan Mensah
Purpose: Note class that represents an individual note.
Source Code (References): TBA
Date: 10/6/26
"""

class Note:
    """
    Class that defines a single note with a title and body.
    """

    def __init__(self, title: str, body: str) -> None:
        """Intializes the note with a title and body

        Args:
            title (str): The name of the note
            body (str): The contents of the note
        """
        self.title = title
        self.body = body