from tkinter import *
from tkinter import messagebox

class TipGui:
    def __init__(self,root):
        self.master = root
        self.master.title("Tip Calculator")
        
        #Enter the amount that the services costs here
        self.serviceLabel1 = Label(self.master, text = "Service Cost 1:")
        self.serviceLabel1.grid(row = 0, column=0, sticky=E)

        #Enter the amount that the service costs here
        self.servicePriceEntry1 = Entry(self.master)
        self.servicePriceEntry1.grid(row=0, column=1, sticky=E)

        self.tipOutput1 = Label(self.master, text = "Tip 1:")
        self.tipOutput1.grid(row = 0, column=2, sticky=E)

        self.tipResult1 = Entry(self.master)
        self.tipResult1.config(state="disabled")
        self.tipResult1.grid(row=0, column=3, sticky=E)

        self.serviceLabel2 = Label(self.master, text = "Service Cost 2:")
        self.serviceLabel2.grid(row = 1, column=0, sticky=E)

        self.servicePriceEntry2 = Entry(self.master)
        self.servicePriceEntry2.grid(row=1, column=1, sticky=E)

        self.tipOutput2 = Label(self.master, text = "Tip 2:")
        self.tipOutput2.grid(row = 1, column=2, sticky=E)

        self.tipResult2 = Entry(self.master)
        self.tipResult2.config(state="disabled")
        self.tipResult2.grid(row=1, column=3, sticky=E)

        self.serviceLabel3 = Label(self.master, text = "Service Cost 3:")
        self.serviceLabel3.grid(row = 2, column=0, sticky=E)

        self.servicePriceEntry3 = Entry(self.master)
        self.servicePriceEntry3.grid(row=2, column=1, sticky=E)

        self.tipOutput3 = Label(self.master, text = "Tip 3:")
        self.tipOutput1.grid(row = 2, column=2, sticky=E)

        self.tipResult3 = Entry(self.master)
        self.tipResult3.config(state="disabled")
        self.tipResult3.grid(row=2, column=3, sticky=E)

        self.serviceLabel4 = Label(self.master, text = "Service Cost 4:")
        self.serviceLabel4.grid(row = 3, column=0, sticky=E)

        self.servicePriceEntry4 = Entry(self.master)
        self.servicePriceEntry4.grid(row=3, column=1, sticky=E)

        self.tipOutput4 = Label(self.master, text = "Tip 4:")
        self.tipOutput4.grid(row = 3, column=2, sticky=E)

        self.tipResult4 = Entry(self.master)
        self.tipResult4.config(state="disabled")
        self.tipResult4.grid(row=3, column=3, sticky=E)

        self.serviceLabel5 = Label(self.master, text = "Service Cost 5:")
        self.serviceLabel5.grid(row = 4, column=0, sticky=E)

        self.servicePriceEntry5 = Entry(self.master)
        self.servicePriceEntry5.grid(row=4, column=1, sticky=E)

        self.tipOutput5 = Label(self.master, text = "Tip 2:")
        self.tipOutput5.grid(row = 4, column=2, sticky=E)

        self.tipResult5 = Entry(self.master)
        self.tipResult5.config(state="disabled")
        self.tipResult5.grid(row=4, column=3, sticky=E)

        self.serviceLabel6 = Label(self.master, text = "Service Cost 2:")
        self.serviceLabel6.grid(row = 5, column=0, sticky=E)

        self.servicePriceEntry6 = Entry(self.master)
        self.servicePriceEntry6.grid(row=5, column=1, sticky=E)

        self.tipOutput6 = Label(self.master, text = "Tip 2:")
        self.tipOutput6.grid(row = 5, column=2, sticky=E)

        self.tipResult6 = Entry(self.master)
        self.tipResult6.config(state="disabled")
        self.tipResult6.grid(row=5, column=3, sticky=E)

        self.tipEntry = Entry(self.master)
        self.tipEntry.grid(row=7, column=0, sticky=E)
        
        #Button
        self.calculateButton = Button(self.master, text = "Calculate tip", command = self.calculateTip())


    def calculateTip(self):
        getLabel = {
            1 : self.servicePriceEntry1.get(),
            2 : self.servicePriceEntry2.get(),
            3 : self.servicePriceEntry3.get(),
            4 : self.servicePriceEntry4.get(),
            5 : self.servicePriceEntry5.get(),
            6 : self.servicePriceEntry6.get()
        }

        for i in range(0,6):
            if getLabel[i] != "":
                total += getLabel[i]
        
        if total == 0:
            messagebox.showerror("ERROR", "No services added")
        else:
            