''' Python 2.7 Tk example app. '''
import Tkinter as tk
import sys

def onQuit(): sys.exit(0)

win = tk.Frame(width=400,height=100)
win.master.title("Python 2.7 Example Application")
win.master.lift()
win.master.minsize(400,100)
win.master.attributes('-topmost',True)
win.master.after_idle(win.master.attributes,'-topmost',False)
btn = tk.Button(win,text=u"Quit",command=onQuit)
btn.grid(row=0,column=0)
win.grid()
tk.mainloop()
