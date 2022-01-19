from Cimpl import *
from simple_Cimpl_filters import grayscale
#Authors:
#-Ramadan Mohamed, 101114234
#-Aditya Wiwekananda, 101147416
#-David Lefebvre, 101143605
#-Talaj Jaber, 101167571

#Red filter
def red_filter(image)-> Image:
        """Returns the image jpg file selected from computer files and creates a
        new image jpg file that removes all blue and green components of the 
        r,g,b in each pixel of the selected image, that new image is saved and 
        displayed afterwards"""
        new_image=copy(image)
        #Checks every pixel in the image and removes the green and blue component
        for pixel in new_image:
                x,y,color=pixel
                r,g,b=color
                red=create_color(r,0,0)
                set_color(new_image,x,y,red) 
        
        return new_image

#Green filter
def green_filter(original_image)-> Image:
        
        """Takes an image and returns it with a green filter applied
        >>>file=load_image(choose_file())
        file=green_filter(file)
        show(file)
        """
        green_image=copy(original_image)
        for pixel in green_image:
                x,y,color=pixel
                r,g,b=color
                green=create_color(0,g,0)
                set_color(green_image,x,y,green)
        return green_image

#Blue filter
def blue_filter(original_image) :
        """Takes an image and returns
        it with a blue filter applied.
        >>>file=load_image(choose_file())
        file=blue_filter(file)
        show(file)
        """
        new_image = copy(original_image)

    #Set each pixel to have only its blue component
        for pixel in original_image:
                x, y, (r, g, b) = pixel
                new_colour = create_color(0, 0, b)
                set_color(new_image, x, y, new_colour)
        return new_image

#Combined filter
def combined_filter(red_image: Image, green_image: Image, blue_image: Image) -> Image:
    #Author: Ramadan Mohamed
        """Takes an image and returns the the red filtered, green filtered, and blue
        filtered images combined
        >>> combined_filter(red_image, green_image, blue_image)
        """

    
        new_image = (copy(red_image))
        get_color
        for x, y, col in red_image:
                r, o, z = get_color(red_image, x, y)
                o, g, z = get_color(green_image, x, y)
                o, z, b = get_color(blue_image, x, y)
                new_colour = create_color(r, g, b)
                set_color(new_image, x, y, new_colour)
        return new_image

#Two tone filter
def two_tone(original_image: Image, color1: str, color2: str) -> Image:
        """ #Author: Aditya Wiwekananda
        Takes an image and two colors represented by strings. 
        Returns an image that looks like a woodcut print
        >>> two_tone(image, "black", "white")
        """
    
        new_image = copy(original_image)

     #Make a list out of the two colors
        colorList = [color1,color2]

    #Converts the color name to its RGB color code equivalent
        for i in range(len(colorList)):
                if colorList[i] == "black":
                        colorList[i] = (0, 0, 0)

                elif colorList[i] == "white":
                        colorList[i] = (255, 255, 255)

                elif colorList[i] == "red":
                        colorList[i] = (255, 0, 0)
                    
                elif colorList[i] == "lime":
                        colorList[i] = (0, 255, 0)

                elif colorList[i] == "blue":
                        colorList[i] = (0, 0, 255)

                elif colorList[i] == "yellow":
                        colorList[i] = (255, 255, 0)

                elif colorList[i] == "cyan":
                        colorList[i] = (0, 255, 255)

                elif colorList[i] == "magenta":
                        colorList[i] = (255, 0, 255)

                elif colorList[i] == "gray":
                        colorList[i] = (128, 128, 128)

    #Set each pixel to have only the color depending on its brightness
        for pixel in original_image:
                x, y, (r, g, b) = pixel

        #Check if the brigtness is between 0 and 127
                if 0 <= ((r+g+b)/3) <= 127:
                        r,g,b = colorList[0]
                        new_colour = create_color(r, g, b)
            
        
                else:
                        r, g, b = colorList[1]
                        new_colour = create_color(r, g, b)

                set_color(new_image, x, y, new_colour)
        return new_image

#Three tone filter
def three_tone(original_image: Image, color1: str, color2: str, color3: str) -> Image:
        """ #Author: Aditya Wiwekananda
        Takes an image and three colors represented by strings. 
        Returns an image that looks like a woodcut print
        >>> three_tone(image, "black", "white", "cyan")
        """

        new_image = copy(original_image)

        #Make a list out of the three colors
        colorList = [color1, color2, color3]

        #Converts the color name to its RGB color code equivalent
        for i in range(len(colorList)):
                if colorList[i] == "black":
                        colorList[i] = (0, 0, 0)

                elif colorList[i] == "white":
                        colorList[i] = (255, 255, 255)

                elif colorList[i] == "red":
                        colorList[i] = (255, 0, 0)

                elif colorList[i] == "lime":
                        colorList[i] = (0, 255, 0)

                elif colorList[i] == "blue":
                        colorList[i] = (0, 0, 255)

                elif colorList[i] == "yellow":
                        colorList[i] = (255, 255, 0)

                elif colorList[i] == "cyan":
                        colorList[i] = (0, 255, 255)

                elif colorList[i] == "magenta":
                        colorList[i] = (255, 0, 255)

                elif colorList[i] == "gray":
                        colorList[i] = (128, 128, 128)

                MIDDLE_BOUND = 84
                UPPER_BOUND = 170
    
    #Set each pixel to have only the color depending on its brightness
        for pixel in original_image: 
                x, y, (r, g, b) = pixel
                brightness = ((r+g+b)/3)
        
       #Check if the brightness is between 0 and 84
                if 0 <= brightness <= MIDDLE_BOUND:
                        r, g, b = colorList[0]
                        new_colour = create_color(r, g, b)

        #Check if the brightness is between 85 and 170
                elif MIDDLE_BOUND+1 <= brightness <= UPPER_BOUND:
                        r, g, b = colorList[1]
                        new_colour = create_color(r, g, b)

                else:
                        r, g, b = colorList[2]

                        new_colour = create_color(r, g, b)

                set_color(new_image, x, y, new_colour)

        return new_image

#Extreme contrast filter
def extreme_contrast(original_image: Image) -> Image:
        """Return a copy of the original image where each pixel is either
        maximized or minimized in terms of their values; the adjustment of the
        contrast of the image is gonna be transformed and shown

        >>> extreme_contrast(original_image)
        """ 
        contrast_image = copy(original_image)
        LOWER_BOUND = 127
        UPPER_BOUND = 255
        for pixel in contrast_image:
                x, y, (r, g, b) = pixel

        #Check Red component
                if 0<=r<=LOWER_BOUND:
                        r = 0
                elif LOWER_BOUND<r<=UPPER_BOUND:
                        r = 255
        
        #Check Green component
                if 0<=g<=LOWER_BOUND:
                        g = 0
                elif LOWER_BOUND<g<=UPPER_BOUND:
                        g = 255
        
        #Check Blue component
                if 0<=b<=LOWER_BOUND:
                        b = 0
                elif LOWER_BOUND<b<=UPPER_BOUND:
                        b = 255      

                contrast = create_color(r, g, b)
                set_color(contrast_image, x, y, contrast)
        return contrast_image

#Sepia filter
def sepia(image:Image)->Image:
        
        """Returns an image with a sepia tint to it by applying the grey filter 
        first, and then for each pixel we slightly increasing the red and slightly
        decreasing the blue depending on its darkness in order to 
        give it a small yellowish tint that is sepia tinting
        """
        gray = grayscale(image)
        tinting=copy(gray)
        for x, y, (r, g, b) in gray:
                color = (r+g+b)//3
                if color < 63:
                        dark=create_color(round(r*1.1), g, round(b*0.9))
                        set_color(tinting, x, y, dark)
                elif color <= 191:
                        medium=create_color(round(r*1.15), g, round(b*0.85))
                        set_color(tinting, x, y, medium)
                elif color > 191:
                        light=create_color(round(r*1.08), g, round(b*0.93))
                        set_color(tinting, x, y, light)
        return tinting

#Posterizing filter
def _adjust_component(rgb:int)->int:
        """Will set the intensity of a rgb value to one of the midpoints of 4 quadrants
        depending on its range from 0 to 255
        >>>_adjust_component(120)
        95
        >>>_adjust_component(45)
        31
        """
        QUADRANT1=31
        QUADRANT2=95
        QUADRANT3=159
        QUADRANT4=223   
    
        if rgb <=63:
                return QUADRANT1
        elif rgb <=127:
                return QUADRANT2
        elif rgb <=191:
                return QUADRANT3
        else:
                return QUADRANT4

def posterize(original_image:Image)->Image:
        """Returns the image with only 4 color intensities for all rgb values that
        end up making the image have a smaller amount of colors
        >>> original = load_image(choose_file()) 
        >>> new_image = posterize(original)
        >>> show(new_image)
        """
        new_image=copy(original_image)
        for pixel in new_image:
                x, y, (r, g, b) = pixel
                R_component = _adjust_component(r)
                G_component = _adjust_component(g)
                B_component = _adjust_component(b)
                new_colour = create_color(R_component,G_component,B_component)
                set_color(new_image, x, y, new_colour)

        return new_image

#Edge detection filter
def detect_edges(original_image: Image, threshold: float) -> Image:
        """ Takes an image and a float, threshold. 
        Returns an image that looks like a pencil sketch

        >>> detect_edges(image, 50)
        """
        new_image = copy(original_image)

    
        for y in range(get_height(original_image)):
                for x in range(get_width(original_image)):
            
            #Set pixels of bottom row to white
                        if y == get_height(original_image)-1:
                                set_color(new_image, x, y, create_color(255, 255, 255))

            #This segment will run for every other row
                        else:

                                brightnessTop = sum(get_color(original_image, x, y)) / \
                                        len(get_color(new_image, x, y))
                                brightnessBottom = sum(get_color(original_image, x, y+1)) / \
                                        len(get_color(new_image, x, y+1))
                
                #If the absolute value of this difference is greater than the threshold
                #The contrast between the two pixels is high, so change top pixel to black
                                if abs(brightnessTop-brightnessBottom) > threshold:
                                        set_color(new_image, x, y, create_color(0, 0, 0))

                #Changes top pixel to white if there is low contrast 
                                else:
                                        set_color(new_image, x, y, create_color(255, 255, 255))
        return new_image

#Improved edge detection filter
def detect_edges_better(original_image: Image, threshold: float) -> Image:
        """
        Takes an image and an inserted threshold to filter it into a black and white 
        image that will have black along the edges depending on the contrast 
        between the pixel to the bottom and to the right of each pixel.

        >>> detect_edges_better(image, 40)
        """
        new_image = copy(original_image)

    
        for y in range(get_height(original_image)):
                for x in range(get_width(original_image)):
            
            #Set pixels of bottom row to white to start
                        if y == get_height(original_image)-1:
                                set_color(new_image, x, y, create_color(255, 255, 255))

            #Set pixels of most right column to white
                        elif x == get_width(original_image)-1:
                                set_color(new_image, x, y, create_color(255, 255, 255))

            #This segment will run for every other row
                        else:
                #Brightness of the main pixel
                                brightnessTop = sum(get_color(original_image, x, y)) / \
                                        len(get_color(new_image, x, y))
                #Brightness of the bottom pixel
                                brightnessBottom = sum(get_color(original_image, x, y+1)) / \
                                        len(get_color(new_image, x, y+1))
                #Brightness of the right pixel
                                brightnessRight = sum(get_color(original_image, x+1, y))/ \
                                        len(get_color(new_image, x+1, y))
                
                #If the absolute value of this difference is greater than the threshold
                #The contrast between the two pixels is high, so change top pixel to black
                                if abs(brightnessTop-brightnessBottom) > threshold or abs(brightnessTop-brightnessRight) > threshold:
                                        set_color(new_image, x, y, create_color(0, 0, 0))

                #Changes top pixel to white if there is low contrast 
                                else:
                                        set_color(new_image, x, y, create_color(255, 255, 255))
        return new_image

#Vertical flip filter
def flip_vertical(original_image: Image) -> Image:
        """Takes an image and returns an image that is 
        vertically flipped (flipped over a vertical line) from the original

        >>> flip_vertical(original_image)
        """
        new_image = copy(original_image)
        width = get_width(new_image)
        height = get_height(new_image)
        for y in range(height):
                for x in range(width // 2):
                        left = get_color(new_image, x, y)
                        right = get_color(new_image, width - 1 - x, y)
                        set_color(new_image, width - 1 - x, y, left)
                        set_color(new_image, x, y, right)
        return new_image

#Horizontal flip filter
def flip_horizontal(original_image: Image) -> Image:
        """Return a copy of the original Image where the copy is transformed 
        into a new image that is horizontal flipped from the original
        >>> original_image = load_image(choose_file())
        >>> image = flip_horizontal(original_image)
        >>> show(image)
        """
        new_image = copy(original_image)
        width = get_width(new_image)
        height = get_height(new_image)
        for y in range(height // 2):
                for x in range(width):
                        left = get_color(new_image, x, y)
                        right = get_color(new_image, x, height - 1 - y)
                        newleft = set_color(new_image, x, height - 1 - y, left)
                        newright = set_color(new_image, x, y, right)
        return new_image

if __name__ == "__main__":
        original = load_image(choose_file())
        red_image = red_filter(original)
        show(red_image)
        green_image = green_filter(original)
        show(green_image)
        blue_image = blue_filter(original)
        show(blue_image)
        combined = combined_filter(red_image, green_image, blue_image)
        show(combined)
        two_tone = two_tone(original, 'gray', 'white')
        show(two_tone)
        three_tone = three_tone(original, 'cyan', 'black', 'red')
        show(three_tone)
        contrast = extreme_contrast(original)
        show(contrast)
        sepia = sepia(original)
        show(sepia)
        posterize = posterize(original)
        show(posterize)
        edge = detect_edges(original,50)
        show(edge)
        better_edge = detect_edges_better(original,50)
        show(better_edge)
        vertical = flip_vertical(original)
        show(vertical)
        horizontal = flip_horizontal(original)
        show(horizontal)
