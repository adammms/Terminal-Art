import os
from pyfiglet import Figlet

def print_cool(text):
    #Instance of Figlet with font setting at slant
    cool_text = Figlet(font="slant")
    #clear the terminal window
    os.system("cls")
    #set terminal window to a fixed size
    os.system('mode con: cols=75 lines=30')
    return str(cool_text.renderText(text))

if __name__== "__main__":
    print(print_cool("Python Ini Buatan Adams"))