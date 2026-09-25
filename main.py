""" 
Name: Note_Taking_App
Author: Jordan Mensah
Purpose: A note-taking app that runs in the terminal that allows users to create, view, and delete notes for all of their classes.
Resources: Python Crash Course Online Textbook (Chapters 1-7)
Date: September 14, 2026
"""
# List to contain notes to maintain order of note creation
dict_of_notes = {}
# Boolean to maintain app state for the primary while loop
app_running = True

while app_running:
    print("Python-Based Note Taking App")
    print("1. Create Note")
    print("2. View all Notes")
    print("3. Close Application")

    user_control = input("Select an Option")

    if user_control == '1':
        note_title: str = input("Enter the title of your note: ")
        note_body: str = input("Enter the body of your note: ")
        dict_of_notes[note_title] = note_body
        
    elif user_control == '2':
        print('To Be Added')
    elif user_control == '3':
        print('Goodbye.')
        app_running = False
    else: 
        print('Not a valid option. Please select a number from 1-3.')