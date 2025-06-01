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

def Story1(win):
    def final(tl: tkinter.Toplevel, name, sports, City, playername, drinkname, snacks):

        text = f'''
            One day me and my friend {name} decided to play a {sports} game in {City}.
            We wanted to watch {playername}.
            We drank {drinkname} and also ate some {snacks} 
            We really enjoyed! We are looking forward to go again and enjoy'''
        tl.geometry('500x550')
        tkinter.Label(tl, text='Story:', wraplength=tl.winfo_width()).place(x=160,y=310)
        tkinter.Label(tl, text=text, wraplength=tl.winfo_width()).place(x=0,y=330)

    NewScreen = tkinter.Toplevel(win, bg='yellow')
    NewScreen.title("A memorable day")
    NewScreen.geometry('500x500')

    tkinter.Label(NewScreen, text='A memorable Day').place(x=100,y=0)
    tkinter.Label(NewScreen, text='Name:').place(x=0,y=35)
    tkinter.Label(NewScreen, text='Enter a game:').place(x=0,y=70)
    tkinter.Label(NewScreen, text='Enter a city:').place(x=0,y=110)
    tkinter.Label(NewScreen, text='Enter the name of a player:').place(x=0,y=150)
    tkinter.Label(NewScreen, text='Enter the name of a drink').place(x=0,y=190)
    tkinter.Label(NewScreen, text='Enter the name of a snack:').place(x=0,y=230)

    Name = tkinter.Entry(NewScreen, width=17)
    Name.place(x=250,y=35)
    game = tkinter.Entry(NewScreen, width=17)
    game.place(x=250,y=70)
    city = tkinter.Entry(NewScreen, width=17)
    city.place(x=250,y=105)
    player = tkinter.Entry(NewScreen, width=17)
    player.place(x=250, y=150)
    drink = tkinter.Entry(NewScreen, width=17)
    drink.place(x=250, y=190)
    snack = tkinter.Entry(NewScreen, width=17)
    snack.place(x=250,y=220)
    SubmitButton = tkinter.Button(NewScreen, text="Submit", background="Blue", font=('Times', 12), command=lambda:final(NewScreen, Name.get(), game.get(), city.get(), player.get(), drink.get(), snack.get()))
    SubmitButton.place(x=150, y=270)

# Buttons
Story1Button = tkinter.Button(Screen, text='A memorable day', font=("Times New Roman", 13),command=lambda: Story1(Screen),bg='Blue')
Story1Button.place(x=140, y=90)

Story2Button = tkinter.Button(Screen, text='Amibtions', font=("Times New Roman", 13),command=lambda: Story1(Screen),bg='Blue')
Story2Button.place(x=150 ,y= 150)

Screen.mainloop()
