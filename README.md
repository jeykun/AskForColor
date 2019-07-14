# AskForColor
Based on Tkinter, this class called "AskForColor" opens a window for the user to set a color in RGB system. To get the value in format "#RRGGBB" (used on Tkinter as a pattern), just use the "get( )" method. A default color is needed. See the next example:


from ask_for_color import AskForColor 

ask = AskForColor("#1a2b3c")

color = ask.get()
