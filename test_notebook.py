"""
Name: Notebook Test
Author: Jordan Mensah
Purpose: Contains automated tests for Note and Notebook classes via pytest
Source Code: TBA
Date: 10/6/26
"""
from pathlib import Path
import pytest

from notebook import Notebook

@pytest.fixture
def sample_notebook(tmp_path: Path) -> Notebook:
    """Makes seperate notebook instance with temp JSON file"""
    test_file = tmp_path / 'test_note.json'
    notebook = Notebook(storage_path=test_file)
    notebook.create_note("CSCI 2467",  "Java Programming")
    return notebook

def test_create_note(sample_notebook: Notebook) -> None:
    """Verify that creating a note properly stores the title and body"""
    sample_notebook.create_note("Test Title", "Test Body")
    assert "Test Title" in sample_notebook.notes
    assert sample_notebook.notes["Test Title"].body == "Test Body"

def test_note_word_count(sample_notebook: Notebook) -> None:
    """Verifies that Note.get_word_count returns the exact number of words"""
    note = sample_notebook.notes["CSCI 2467"]
    assert note.get_word_count() == 2
