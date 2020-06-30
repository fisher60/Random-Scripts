import random
import time
from tkinter import Tk, Button, DISABLED


def show_symbol(x,y):
  global first
  global previousX, previousY
  buttons[x,y]['text'] = button_symbols[x,y]
  buttons[x,y].update_idletasks()

  if first:
    previousX = x
    previousY = y
  elif previousX != x or previousY !=y:
    if button[previousX, previousY]['text'] != buttons[x,y]['text']:
        button[previousX, previousY]['text'] = ''
        button[x,y]['text']=''
    else:
        button[previousX, previousY]['command'] = DISABLED
        button[x,y]['command'] = DISABLED
    first = True


root = Tk()
root.title('Matchmaker')
root.resizable(width=False, height=False)

buttons = {}
first = True
previousX = 0
previousY = 0

button_symbols = {}
symbols = [u'\u2702', u'\u2702', u'\u2702', u'\u2702', u'\u2702', u'\u2702', u'\u2702', u'\u2702', u'\u2702', u'\u2702',
           u'\u2702', u'\u2702']
random.shuffle(symbols)

for x in range(3):
  for y in range(4):
    button = Button(command=lambda x=x, y=y: show_symbol(x,y), width=3, height=3)
    button.grid(column=x, row=y)
    buttons[x,y] = button
    button_symbols[x,y] = symbols.pop()

print(buttons)

root.mainloop()