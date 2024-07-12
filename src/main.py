
from __init__ import *
from Person import * 
import tkinter as tk
from sys import argv

'''
python main.py ../bin/users.csv ../bin/data.csv
'''
def main() -> None:
    if len(argv) != 3:
        print(" MISSING FILES ARGS ".center(30,'='))
        exit(1)
    
    users,data = argv[1],argv[2]

    userIn = startmenu()
    match userIn:
        case 0:
            print("Too many invalid entries..exiting")
            exit(0)
        case '1':
            # login(users)
            print("LOGIN")
        case '2':
            register(users)
            print("REGISTER")
        case _:
            print("EXIT")
            # exit(0)

    
    # exit(0)
    # window = tk.Tk()
    # window.title("MAIN WINDOW")

    # label = tk.Label(window,text='hello',padx=20,pady=20)
    # label.pack()

    # window.mainloop()
    # return 



if __name__ == "__main__":
    main()