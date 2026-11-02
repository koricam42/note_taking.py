"""
Name: Notebook Test
Author: Jordan Mensah
Purpose: Contains automated tests for Note and Notebook classes via pytest
Source Code: Acknowledgements
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

def test_edit_note(sample_notebook: Notebook) -> None:
    """Verifies editing an existing note updates its body, and missing notes return False"""
    assert sample_notebook.edit_note("CSCI 2467", "Updated Body Text") is True
    assert sample_notebook.notes["CSCI 2467"].body == "Updated Body Text"
    assert sample_notebook.edit_note("Note which does not exist", "New Text") is False

def test_delete_note(sample_notebook: Notebook) -> None:
    """Verifies deleting an existing note removes it, and missing notes return False"""
    assert sample_notebook.delete_note("CSCI 2467") is True
    assert "CSCI 2467" not in sample_notebook.notes
    assert sample_notebook.delete_note("CSCI 2467") is False


def test_note_persistence(tmp_path: Path) -> None:
    """Tests saved notes save to JSON and load into a new Notebook instance"""
    test_file = tmp_path / "persistence_test.json"
    first_notebook = Notebook(storage_path=test_file)
    first_notebook.create_note("Stat 1400", "Standard Deviation and Mean")
    first_notebook.save_notes()

    reloaded_notebook = Notebook(storage_path=test_file)
    assert "Stat 1400" in reloaded_notebook.notes
    assert reloaded_notebook.notes["Stat 1400"].body == "Standard Deviation and Mean"

