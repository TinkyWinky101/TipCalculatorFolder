from tkinter import *

#class MathMaker:

class TipGui:
    def __init__(self,root):
        self.master = root
        self.master.title("Tip Calculator")

        self.serviceLabel = Label(self.master, text = "Service Cost:")
        self.serviceLabel.grid(row = 0, column=0, sticky=E)

        self.servicePriceEntry = Entry(self.master)
        self.servicePriceEntry.config(state="disabled")
        self.servicePriceEntry.grid(row=0, column=1, sticky=E)