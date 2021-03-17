#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg

# decoration
print(stylize("\n---- | Replacer using Python3 | ----\n", fg("red")))

# user interaction
text = input("Import text: ").lower()
wordToReplace = input("\nWord to replace: ").lower()
wordToReplaceWith = input("Word to replace with: ").lower()

# function
def do_replace(text, wTR, wTRW):
    return f"\nModified text: {text.replace(wTR, wTRW)}\n"

# output
print(do_replace(text, wordToReplace, wordToReplaceWith))
