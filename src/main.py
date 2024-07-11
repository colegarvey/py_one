from Person import * 
import tkinter as tk
from sys import argv,exit

'''
python main.py users.csv data.csv
'''
def main():
    if len(argv) != 3:
        print(" MISSING FILES ARGS ".center(30,'='))
        exit(1)
    
    users,data = argv[1],argv[2]

    
    
    
    # window = tk.Tk()
    # window.title("MAIN WINDOW")

    # label = tk.Label(window,text='hello',padx=20,pady=20)
    # label.pack()

    # window.mainloop()
    # return 



if __name__ == "__main__":
    main()