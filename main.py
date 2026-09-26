""" 
Name: Note_Taking_App
Author: Jordan Mensah
Purpose: A note-taking app that runs in the terminal that allows users to create, view, and delete notes for all of their classes.
Source Code (References):
    - General Knowledge: Python Crash Course Online Textbook (Chapters 1-7)
    - Getting length of dict: https://www.geeksforgeeks.org/python/get-length-of-dictionary-in-python/
Date: September 14, 2026
"""
dict_of_notes = {}

app_running = True

while app_running:
    print("Python-Based Note Taking App")
    print("1. Create Note")
    print("2. View all Notes")
    print("3. Manage Notes")
    print("4. Close Application")

    user_control = input("Select an Option")

    if user_control == '1':
        note_title: str = input("Enter the title of your note: ")
        note_body: str = input("Enter the body of your note: ")
        dict_of_notes[note_title] = note_body
        
    elif user_control == '2':
        print('Your Notes')
        if len(dict_of_notes) == 0:
            print("You don't have any notes")
        else:
            for title, body in dict_of_notes.items():
                print(f"Title: {title}")
                print(f"Body: {body}")
    elif user_control == '3':
        if len(dict_of_notes) == 0:
            print("You have no notes to manage")
        else:
            note_to_manage = input("Enter the title of the note you want to delete")
            if note_to_manage in dict_of_notes.keys():
                del dict_of_notes[note_to_manage]
                print(f"Your note, {note_to_manage} has been deleted.")
            else:
                print(f"Error, note {note_to_manage} was not found")
    elif user_control == '4':
        print('Goodbye.')
        app_running = False
    else: 
        print('Not a valid option. Please select a number from 1-4.')