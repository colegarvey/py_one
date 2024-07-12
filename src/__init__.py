from time import sleep


def startmenu() -> int:
    print("\n(1) Login",
          "(2) Register")

    for i in range(0,4):
        try:
            num = input("> ")
            int_error = None
        except Exception as err:
            int_error = int(err)
        
        if int_error:
            sleep(2)
        else:
            break

    return num


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
