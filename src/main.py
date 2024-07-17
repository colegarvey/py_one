
from __init__ import *
from Person import * 
import tkinter as tk
from sys import argv
from time import sleep
'''
python src/main.py bin/users.csv bin/data.csv
'''
def main() -> None:
    if len(argv) != 3:
        print(" MISSING CMD ARGS ".center(30,'='))
        exit(1)
    
    users,data = argv[1],argv[2]
    authenticated = False
    user_id = -1

    while (authenticated == False) and (user_id == -1): # stop when user is authenticated and have id number
        userIn = startmenu()
        match userIn:
            case '1':
                authenticated,user_id = login(users)
            case '2':
                register(users)
            case 'input_err':
                print("input err")
            case _:
                sleep(1)
                exit(0)
        sleep(1)
    
    # if authenticated:
    #     print("User is authed")

    print(user_id)
    getData(argv[2],user_id)


    # window = tk.Tk()
    # window.title("MAIN WINDOW")

    # label = tk.Label(window,text='hello',padx=20,pady=20)
    # label.pack()

    # window.mainloop()
    # return 



if __name__ == "__main__":
    main()