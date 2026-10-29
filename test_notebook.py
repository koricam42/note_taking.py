"""
Name: Notebook Test
Author: Jordan Mensah
Purpose: Contains automated tests for Note and Notebook classes via pytest
Source Code: TBA
Date: 10/6/26
"""
from notebook import Notebook

def test_create_note():
    """TBA
    """
    test_note = Notebook()

    test_note.create_note("Test Title", "Test Body")

    assert "Test Title" in test_note.notes

    assert test_note.notes["Test Title"].body == "Test Body"

