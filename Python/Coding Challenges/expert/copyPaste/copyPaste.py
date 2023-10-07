"""
Project

    Given a sentence containing few instances of "Ctrl + C" and "Ctrl + V", return the sentence after those keyboard shortcuts have been applied! Note that:

    "Ctrl + C" will copy all text before it.
    "Ctrl + V" will do nothing if there is no "Ctrl + C" before it.
    A "Ctrl + C" which follows another "Ctrl + C" will overwrite what it copies.

Examples

    keyboard_shortcut("the egg and Ctrl + C Ctrl + V the spoon") ➞ "the egg and the egg and the spoon"

    keyboard_shortcut("WARNING Ctrl + V Ctrl + C Ctrl + V") ➞ "WARNING WARNING"

    keyboard_shortcut("The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V") ➞ "The The Town The The Town"

Notes

    - Keyboard shortcut commands will appear like normal words in a sentence but shouldn't be copied themselves (see example #2).
    - Pasting should add a space between words.

    link: https://edabit.com/challenge/6Ran7nuFijxkXD95o

Thoughts

    - maybe match exactly "Ctrl + C" or paste, and execute their command, then delete from string.

"""

def keyboard_shortcut(txt):
    copyIndex = txt.find("Ctrl + C")
    pasteIndex = txt.find("Ctrl + V")
    clipboard = ""

    while(copyIndex > -1 or pasteIndex > -1):
        if(copyIndex == 0 or pasteIndex == 0): # edge case: if the given string starts with a command. Nothing to be done, just delete the command and move on.
            txt = txt[9:]
        elif(copyIndex < pasteIndex and copyIndex > -1 or pasteIndex == -1): # if a valid copy command occurs first, in current string
            clipboard = txt[:copyIndex - 1] + " "
            txt = txt[:copyIndex] + txt[(copyIndex + 9):]
        elif(pasteIndex < copyIndex and pasteIndex > -1 or copyIndex == -1): # if a valid paste command occurs first, in current string
            txt = txt[:pasteIndex] + clipboard + txt[(pasteIndex + 9):] # effectively replaces "Ctrl + V" with whatever is on the clipboard. Clipboard can be empty
        copyIndex = txt.find("Ctrl + C")
        pasteIndex = txt.find("Ctrl + V")

    # if a string ends with a paste command, an extra space will be present. Remove that space if present.
    if(txt[len(txt) - 1] == " "):
        txt = txt[:len(txt) - 1]
    return(txt)
        

    # txt = txt[0:txt.find("Ctrl + C")] + txt[txt.find("Ctrl + C") + 9:len(txt)]


# keyboard_shortcut("Ctrl + C The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V")

# txt = "Ctrl + C The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V"

# txt = txt[9:]
# print(txt)

# print(txt.find("Ctrl + C"))
# clipboard = txt[:4 - 1]
# print(clipboard)
# txt = txt[:4] + txt[4+9:]
# print(txt)

# pasteIndex = txt.find("Ctrl + V")
# print("Paste", pasteIndex)
# txt = txt[:pasteIndex] + clipboard + " " + txt[(pasteIndex + 9):]
# print(txt)




# Complete and tested Aug. 16, 2023.