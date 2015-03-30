from colorama import Fore, Style

def warning(text):
    print (Fore.RED + str(text) + Style.RESET_ALL + "\n")

def success(text):
    print (Fore.GREEN + str(text) + Style.RESET_ALL + "\n")

def defaultInput(text, default):
    inputString = input (text + " (" + default +  "): ")
    if inputString == "":
        return str(default)
    else:
        return str(inputString)