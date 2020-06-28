import tkinter as tk
from tkinter import ttk
import os
from time import sleep

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.master.geometry('300x150+100+100')

    def create_widgets(self):
        self.Launch = tk.Label(self, text="Launch Runescape")                                  
        self.Launch.grid(row=1, column=1, pady=20, sticky="n")                         
        self.EnLaunch = tk.Entry(self)                                                 
        self.EnLaunch.grid(row=1, column=2, pady=20, ipadx=20, sticky="w")           
        
        def sleepy_time():
            sleep(self.slider.get())

        def Runescape():
            amount = self.EnLaunch.get()
            try:
                amount = int(amount)
            except ValueError:
                print(f"Please input a number not {str(amount)}")
            else:
                print(f'Launching {amount} Runescape clients')
                for client in range(int(amount)):
                    os.startfile("rs-launch://www.runescape.com/k=5/l=$(Language:0)/jav_config.ws")
                    sleepy_time()

        self.slider = tk.Scale(self, orient="horizontal", from_=0, to=60) 
        self.slider.grid(row=2, column=1)

        self.launch = tk.Button(self, text="Launch", command=Runescape)
        self.launch.grid(row=2, column=2, pady=10, ipadx=20, sticky="n")
        
        self.quit = tk.Button(self, text="Cancel", command=self.master.destroy)
        self.quit.grid(row=3, column=2, pady=10, ipadx=20, sticky="n")
        
root = tk.Tk()
root.title("Runescape Launcher")
app = Application(master=root)
app.mainloop()
