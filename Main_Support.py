__author__ = 'Gal Reshef S'

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


def set_Tk_var():
    global radioVar
    radioVar = tk.StringVar()


def init(top, gui):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def Credits():
    return """
       Rock
     ___                            
    |   |
 /------------------                    Created by 
/            \     |                             Gal
|       ------------                              Reshef S
|       ------------
|            \     |
|       ------------
|       ------------
|            \     |      
|       ------------                            Scissors
\       ------------                 _____  ___________________________ 
 \           \     /                |     \                           |
  \---------------/                 |  \    \_________________________/
                                    |   \    \    \   
          Paper                     |    \____\    \ ________________
  ___  ___  ___  ___                |                                |
 |   ||   ||   ||   | ___           |               _________________/
 |   ||   ||   ||   ||   |          |______________|
 |   ||   ||   ||   ||   |          |______________|
 |   ||   ||   ||   ||   |       
 |   ||   ||   ||   ||   |       
 \                       /
  \                     /
   \                   /
    \                 /
     \_______________/"""


if __name__ == '__main__':
    import unknown

    unknown.vp_start_gui()
