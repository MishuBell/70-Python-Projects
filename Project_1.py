import tkinter

# Madlibs Generator by PythonGeeks
# https://pythongeeks.org/python-mad-libs-generator-project/


# "Mad Libs is a word game created by Leonard Stern and Roger Price. It consists of one player prompting
# others for a list of words to substitute for blanks in a story before reading aloud."
# https://en.wikipedia.org/wiki/Mad_Libs

# "Frankenstein; Or, The Modern Prometheus" by Mary Wollstonecraft Shelley is a novel
# written in the early 19th century.
# https://www.gutenberg.org/ebooks/84
 
# Needs:
# Adjective, Adverb, Noun, Verb, Tense, Place,
# Exclamation, Silly Word, Number, Color, Animal, Part of the Body, Plurals

Screen = tkinter.Tk()
Screen.title("PythonGeeks Mad Libs Generator")
Screen.geometry('400x400')
Screen.config(bg="pink")
tkinter.Label(Screen, text='PythonGeeks Mad Libs Generator').place(x=100, y=20)

# Buttons
Story1Button = tkinter.Button(Screen, text='A memorable day', font=("Times New Roman", 13),command=lambda: Story1(Screen),bg='Blue')

Story1Button.place(x=125, y=50)


Screen.update()
Screen.mainloop()

