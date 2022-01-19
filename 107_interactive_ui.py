#Author: Ramadan Mohamed, Aditya Wiwekananda, David Lefebvre, Talal Jaber
from T107_image_filters import *

def showMenu() -> None:
    """Displays the menu of 
    commands

    >>> showMenu()
    """ 
    print("L)oad image  S)ave-as")
    print("2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize")
    print("E)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip")
    print("Q)uit\n")

def enterCommand() -> str:
    """Displays the menu of
    commands and prompts the
    user to enter an input.
    Returns the string input

    >>> enterCommand()
    """
    showMenu()
    return input(": ").upper()

def checkValid(command: str) -> None:
    """Takes a command and displays
    whether they have inputed an
    invalid command or if they
    did not load an image
    
    >>> checkValid('xyz')
    """
    if command in ['S', '2', '3', 'X', 'T', 'P', 'E', 'I', 'V', 'H']:
            print("No image loaded\n")
    else:
        print("No such command\n")

def applyFilter(command: str, image: Image) -> Image:
    """Takes a command and an image
    and applys the corresponding 
    filter to the image"""

    if command == '2':
        image = two_tone(image, 'yellow', 'cyan')

    elif command == '3':
        image = three_tone(image, 'yellow', 'magenta', 'cyan')

    elif command == 'X':
        image = extreme_contrast(image)

    elif command == 'T':
        image = sepia(image)

    elif command == 'P':
        image = posterize(image)

    elif command == 'E':
        image = detect_edges(image, float(input("Threshold?: ")))

    elif command == 'I':
        image = detect_edges_better(image, float(input("Threshold?: ")))

    elif command == 'V':
        image = flip_vertical(image)

    elif command == 'H':
        image = flip_horizontal(image)

    return image

command = True
loaded = False
validCommands = ['L', 'Q', 'S', '2', '3', 'X', 'T', 'P', 'E', 'I', 'V', 'H']

while command != 'Q':

    command = enterCommand()

    if command in validCommands:

        if command == 'L':
            image = load_image(choose_file())
            show(image)
            loaded = True

        elif command == 'Q':
            #The while loop ends
            pass

        elif loaded == False:
            print("No image loaded\n")

        elif command == 'S':
            save_as(image)
        
        else:
            image = applyFilter(command, image)
            show(image)

    else: 
        print("No such command\n")
