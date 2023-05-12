from django.shortcuts import render
import random

letters = ["A", "B", "C", "D", "E"]

# Define a list of letters
letters = ["A", "B", "C", "D", "E"]

# Open the dictionary file
with open("dictionary.txt") as f:
    # Read all the words from the file
    words = f.readlines()

    # Choose a random word from the list
    word = random.choice(words)

    # Remove the newline character from the word
    word = word.strip()

# Define the right letter and the position to check
right_letter = word[0]
position = 0

def letter_view(request):
    # Get the letter entered by the user
    user_letter = request.GET.get("letter")

    # Check if the letter entered is the right letter
    if user_letter == right_letter:
        # Do something if the letter is correct
        message = "You got it right!"
    else:
        # Do something else if the letter is wrong
        message = "Sorry, try again."

    # Check if the letter entered is in the right position
    # Get the letter at the position in the word
    word_letter = word[position]

    # Compare the user letter and the word letter
    if user_letter == word_letter:
        # Do something if the letter is in the right position
        position_message = "You got the position right!"
    else:
        # Do something else if the letter is in the wrong position
        position_message = "Sorry, wrong position."

    # Get all the letters from the list
    letters = letters

    # Return a template with some context variables
    return render(request, "myapp/letter.html", {
        "letters": letters,
        "message": message,
        "position_message": position_message,
    })