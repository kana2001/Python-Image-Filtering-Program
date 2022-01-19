#Author: Ramadan Mohamed, Aditya Wiwekananda, David Lefebvre, Talal Jaber
from T107_image_filters import *

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
        image = detect_edges(image, 10)

    elif command == 'I':
        image = detect_edges_better(image, 10)

    elif command == 'V':
        image = flip_vertical(image)

    elif command == 'H':
        image = flip_horizontal(image)

    return image

def implementBatch(filename: str) -> None:
    """Takes a filename and applies 
    the filters that are entered in the line
    of the file to the image. After, the image is saved.
    """

    #Open the file
    infile = open(filename)

    for line in infile:
        line = line.split()
        
        filenames = {}
        filterCommands = []

        #Add the first two indices to the filenames dictionary
        #Add the other indices to the filterCommands list
        for i in range(len(line)):
            if i == 0:
                filenames['Input'] = line[0]
            elif i == 1:
                filenames['Output'] = line[1]
            else:
                filterCommands.append(line[i])
        
        #Load the image
        image = load_image(filenames['Input'])
        
        #Apply all the filter commands
        for i in range(len(filterCommands)):
            image = applyFilter(filterCommands[i], image)

        #Save the image as an image with the desired name
        save_as(image, filenames['Output'])
    
    infile.close()


filename = input("Please enter the name of the batch file: ")
implementBatch(filename)