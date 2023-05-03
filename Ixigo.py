from tkinter import *
import requests

class Ixigo:

    def __init__(self):

        self.root=Tk()

        self.root.minsize(200,300)

        Button(self.root, text="Check PNR Status",
               command=lambda :self.check_pnr()).grid(row=1,column=1)
        Button(self.root, text="Train Running Status",
               command=lambda: self.train_status()).grid(row=2,column=1)

        self.root.mainloop()

    def check_pnr(self):

        self.cancel_window()

        self.pnrInput=Entry(self.root)
        self.pnrInput.grid(row=0,column=0)
        Button(self.root, text="Check PNR Status", command=lambda :self.pnr()).grid(row=0,column=1)

        self.pnrResult=Label(text="", fg="red")
        self.pnrResult.grid(row=2,column=0)

    def pnr(self):

        response=requests.get("""https://api.railwayapi.com/v2/route/train/{}/apikey/x48av3jl89/""".format(self.pnrInput.get()))
        station_names = ""
        for i in response.json()['route']:

            station_names=station_names + i['station']['name'] + "\n"

        self.pnrResult.configure(text=station_names)
        #print(station_names)


    def cancel_window(self):

        for i in self.root.grid_slaves():
            i.destroy()

obj=Ixigo()
