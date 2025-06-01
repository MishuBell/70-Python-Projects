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
Story1Button.place(x=140, y=90)

Story2Button = tkinter.Button(Screen, text='Amibtions', font=("Times New Roman", 13),command=lambda: Story1(Screen),bg='Blue')
Story2Button.place(x=150 ,y= 150)

Screen.update()
Screen.mainloop()

            # def example(variableName: TypeHint)
def Story1(win):
    def final(tl: Toplevel, name, sports, City, playername, drinkname, snacks):

        text = f'''
            One day me and my friend {name} decided to play a {sports} game in {City}.
            We wanted to watch {playername}.
            We drank {drinkname} and also ate some {snacks} 
            We really enjoyed! We are looking forward to go again and enjoy'''
        tl.geometry(newGeometry='500x550')
        Label(tl, text='Story:', wraplength=tl.winfo_width()).place(x=160,y=310)
        Label(tl, text=text, wraplength=tl.winfo_width()).place(x=0,y=330)

NewSceen = Toplevel(win, bg='yellow')
NewScreen.title("A memorable day")
NewSceen.geometry('500x500')

Label(NewSceen, text='A memorable Day').place(x=100,y=0)
Label(NewSceen, text='Name:').place(x=0,y=35)
Label(NewSceen, text='Enter a game:').place(x=0,y=70)
Label(NewSceen, text='Enter a city:').place(x=0,y=110)
Label(NewSceen, text='Enter the name of a player:').place(x=0,y=150)
Label(NewSceen, text='Enter the name of a drink').place(x=0,y=190)
Label(NewSceen, text='Enter the name of a snack:').place(x=0,y=230)


