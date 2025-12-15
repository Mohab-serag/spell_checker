# spell_checker
This project is a simple spell-checker application that loads a dictionary of valid English words from a text file and checks whether a user-entered word is spelled correctly. If the word exists in the dictionary, the program confirms that it is correct; if not, it compares the user’s input with all words in the dictionary using a similarity score (based on Levenshtein distance) to find the closest matches, then displays a list of suggested correct words. In short, the project validates user input and provides intelligent spelling suggestions when the input is incorrect.

                               Requirements :

Python 3.x

words.txt file

How to Run

Place code.py and words.txt in the same folder.

Run the program using:

python code.py

How to Use

Enter a word to check its spelling.

If the word is incorrect, suggestions will be shown.

Type exit to stop the program.
