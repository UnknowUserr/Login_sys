import json, subprocess, time, win32console
from getpass import getpass
from json import loads
from sys import executable

"""
Date of releases : 19/11/2022
Original creator : https://github.com/XeroxOnTop
"""

requirements = [
    ["animation", "animation"],
    ["pystyle", "pystyle"]
]

for module in requirements:
    try: __import__(module[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {module[1]}", shell=True)
        time.sleep(3)

def CreateL():
    try:
        from pystyle import Colors
        l = input(Colors.white+"[#] -> "+Colors.reset + "Would you like to create an account? (Y/n) : ")
        if l in ('Y', 'y'):
            print("\033c", end="")
            createA = open('config.json', 'w')
            user = input(Colors.white+"[#] -> "+Colors.reset + "Enter your username : ")
            passw = getpass(Colors.white+"[#] -> "+Colors.reset + "Enter your password : ")
            print(Colors.green+"\n[!]"+Colors.reset + " Account created successfully, restart the program to connect\n")
            dikt = {
                "user":{
                    "name":f"{user}",
                    "passw":f"{passw}"
                }
            }
            json_string = json.dumps(dikt)
            createA.write(json_string)
    except KeyboardInterrupt:
        input("Press to close ")
        
def check():
    try:
        import time, os, animation
        from pystyle import Colors
        a = os.getlogin()
        win32console.SetConsoleTitle("Logged to : " + a)
        check = loads(open('config.json', 'r').read())
        l = input(Colors.white+"[#] -> "+Colors.reset + "Would you like to log in ? (Y/n) : ")
        if l in ('Y', 'y'):
            print("\033c", end="")
            user = input(Colors.white+"[#] -> "+Colors.reset + "Enter your username : ")
            passw = getpass(Colors.white+"[#] -> "+Colors.reset + "Enter your password : ")
        else:
            exit()
    except json.decoder.JSONDecodeError:
        win32console.SetConsoleTitle("Error detected")
        print(Colors.red+"[!]"+Colors.reset + " An error has been detected, it is likely that no account has been detected"+Colors.red+"\n\n-->  "+Colors.reset+"Please create a new")
    except KeyboardInterrupt:
        input("Press to close ")
    
    try:
        if user == check['user']["name"] and passw == check['user']["passw"]:
            win32console.SetConsoleTitle("Logged to " + check['user']["name"])
            print("\033c", end="")
            print(Colors.green+"[!]"+Colors.reset + " Successful login")
            time.sleep(1)
            print("\033c", end="")
            @animation.wait('elipses ', color='white' ,text=Colors.green+"[!]"+Colors.reset + " Launching your program")
            def long_running_function():
                time.sleep(4)
            long_running_function()
            if __name__ == '__main__':
                prog()
        elif user != check['user']["name"] and passw != check['user']["passw"]:
            print("\033c", end="")
            print(Colors.red+"[!]"+Colors.reset + " Incorrect username or password")
            win32console.SetConsoleTitle("Incorrect username or password")
            time.sleep(2)
            exit()
    except UnboundLocalError:
        time.sleep(2)
        exit()

def prog():
    print('Put your program here')

if __name__ == '__main__':
    from pystyle import Colors
    print("\033c", end="")
    win32console.SetConsoleTitle("Have an account ?")
    a = input(Colors.white+"[#] -> "+Colors.reset + "Do you already have an account ? (Y/n) : ")
    print("\033c", end="")
    if a in "Nn":
        CreateL()
    if a in "Yy":
        check()
    else:
        input("Press to continue")
