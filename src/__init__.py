
def startmenu() -> int:
    print("1_Login\n2_Register")
    return input()


def register(filename: str) -> None:
    try:
        username = input("Name: ")
        key = input("password: ")
    except:
        print("Unable to open file")
    else:
        # 'with' will close file after execution finishes
        with open(filename,'a') as file:
            file.write("{0},{1}\n".format(username,key))
        
    return


def login(filename: str) -> bool:
    try:
        username = input("Name: ")
        key = input("password: ")
    except:
        print("Credentials could not be checked")
        return False
    else:
        found = False
        with open(filename,'r') as file:
            print(file.read())

        return found
