from Person import * 
import tkinter as tk

def main():
    window = tk.Tk()
    window.title("MAIN WINDOW")

    label = tk.Label(window,text='hello',padx=20,pady=20)
    label.pack()

    window.mainloop()
    # return 



if __name__ == "__main__":
    main()