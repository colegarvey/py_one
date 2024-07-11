
from __init__ import *
from Person import * 
import tkinter as tk
from sys import argv

'''
python main.py ../bin/users.csv ../bin/data.csv
'''
def main():
    if len(argv) != 3:
        print(" MISSING FILES ARGS ".center(30,'='))
        exit(1)
    
    users,data = argv[1],argv[2]

    userIn = startmenu()
    match userIn:
        case 1:
            login(users)
        case 2:
            register(users)
        case _:
            

    # username = input("Name: ")
    # passw = input("Pass: ")
    # login(users,username,passw)
    # register(users)
    
    
    # window = tk.Tk()
    # window.title("MAIN WINDOW")

    # label = tk.Label(window,text='hello',padx=20,pady=20)
    # label.pack()

    # window.mainloop()
    # return 



if __name__ == "__main__":
    main()