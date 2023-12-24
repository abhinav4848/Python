import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):
        self.root=tk.Tk()
        self.root.title("My first GUI")
        # Make the menubar with 2 labels. 
        self.menubar = tk.Menu(self.root)
        
        # The first label will have 2 buttons with a separator
        self.filemenu=tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close without Question", command=exit)

        # The second lavel will have 1 button
        self.actionmenu=tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")
        self.root.config(menu=self.menubar)

        # make a textbox with a label
        self.label = tk.Label(self.root, text="Your Message", font=('Arial',18))
        self.label.pack(padx=10,pady=10)

        # textbox has the option to autosubmit if pressed Ctrl+Enter
        self.textbox=tk.Text(self.root, height=5, font=('Arial',16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10,pady=10)

        # make a checkbox to allow a popup to display the text vs show it in console instead
        self.check_state=tk.IntVar()
        self.check=tk.Checkbutton(self.root, text="Show Message Box", font=('Arial',18), variable=self.check_state)
        self.check.pack(padx=10,pady=10)

        # button to submit what is in the textbox
        self.button = tk.Button(self.root, text="Show Message", font=('Arial',18), command=self.show_message)
        self.button.pack(padx=10,pady=10)

        # button to empty the textbox
        self.clearbtn = tk.Button(self.root, text="Clear", font=('Arial', 18), command=self.clear)
        self.clearbtn.pack(padx=10,pady=10)

        # when "X" is pressed to close the window, do something
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() ==0:
            print(self.textbox.get('1.0',tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0',tk.END))

    def shortcut(self, event):
        # print("keysym: "+event.keysym)
        # print("state: "+str(event.state))
        if event.state == 4 and event.keysym =="Return":
            self.show_message()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really wanna quit?"):
            self.root.destroy() # if not done this, then program will not close

    def clear(self):
        self.textbox.delete('1.0',tk.END)

MyGUI()