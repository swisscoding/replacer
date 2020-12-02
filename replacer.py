#!/usr/local/bin/python3

text = input("Import text: ").lower()
print()
wordToReplace = input("Which word do you want to replace?\n").lower()
wordToReplaceWith = input("With which word do you want to replace it?\n").lower()

def replace(text, wTR, wTRW):
    return f"\nModified text: {text.replace(wTR, wTRW)}\n"

print(replace(text, wordToReplace, wordToReplaceWith))
