import csv
from random import randint
import Person

def startmenu():
    print("\n(1) Login",
          "(2) Register",
          "(Q) Exit")
    
    user_in = input("> ")[0] # take only the first character
    if user_in in "12":
        return user_in
    elif user_in in "Qq":
        return None
    else:
        return "input_err"


def register(filename: str) -> bool:
    try:
        append_file = open(filename,'a')
    except:
        print("Unable to open file")
        return False
    else:
        # 'with' will close file after execution finishes
        username = input("Name: ")
        key = input("Password: ")
        with append_file as file:
            file.write("{0},{1},{2}\n".format(username,key,randint(1,999)))
        print(" ACCOUNT CREATED ".center(25,'='))
        return True


def login(filename: str) -> bool:
    try:
        read_file = open(filename,'r')
    except:
        print("Credentials could not be checked")
        return (False,-1)
    else:
        username = input("Name: ")
        key = input("Password: ")
        with read_file as file:
            data = csv.reader(file,delimiter=',')
            for line in data:
                if line[0] == username and line[1] == key:
                    return (True,line[2])
        return (False,-1)


def getData(filename,user_id: str):
    try:
        read_file = open(filename,'r')
    except:
        print("ERR ACCESSING DATA")
    else:
        with read_file as file:
            data = csv.reader(file,delimiter=',')
            for line in data:
                if line[0] != user_id:
                    continue
                else:
                    user_data = line
        if user_data:
            # ignore user id, turn weight values to float and return list of values
            return list(map(float,user_data[1:]))
        else:
            return None
        