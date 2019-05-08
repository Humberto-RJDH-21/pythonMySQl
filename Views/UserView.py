import tkinter as tk 
from Controller.UserController import UserController
from Model.User import User

class UserView:
    def __init__(self):
        self.frame=tk.Tk()
        self.frame.title("Users Management")

        self.lblName=tk.Label(text="Name")
        self.lblName.grid(row="0",column="0")

        self.name=tk.StringVar()
        self.name.grid(row="0",column="1")

        self.btnSave=tk.Button(self.frame,text="Save")
        self.btnSave.grid(row="1",column="1")


    def insert(self):
        user=User()
        user