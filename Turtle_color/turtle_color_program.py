#Robert Marsh
#July 24, 2020
#Program uses turtle to draw and fill in circles with colors

##The program must use at least one function.If the program does not use
##any user-defined functions, no grade will be given.

##The file must be opened using error handling (try/except)

##Program utilizes a file containing ten hexadecimal colors. You create this
##text file. Be sure to submit that, too.

##The program creates a Turtle window

##There is a loop that executes ten times

##Each time through the loop, the program draws a circle on the screen, and
##fills it with the next color from the file

##Pause the program with a timer so the circle doesn’t disappear immediately

##It must work with any text file that has hexadecimal colors

##Extra credit: Give the user a choice of whether to use RGB colors or 
##hexadecimalcolors. You will need an additional text file of RGB colors for this.

##def draw_circle_rgb(file_name, mode): #test function
##    file = open(file_name, mode)
##    colors = file.readlines()
##    for i in colors:
##        t = turtle.Turtle()
##        t.shape("turtle")
##        t.fillcolor("#" + i[:6])
##        t.fillcolor(i[:7])
##        t.begin_fill()
##        t.up()
##        t.goto(0, -50)
##        t.down()
##        t.circle(100)
##        t.end_fill()
##        t.up()
##        time.sleep(1)
##        t.clear()
##    file.close()


import time
import sys
import turtle



#functions

def open_file(file_name, mode): #checks file name
    """Opens and file and error checks"""
    try:
        file = open(file_name, mode)
    except IOError as e:
        print("Unable to open file", file_name, ". Ending program.\n", e)
        input("Press the enter key to exit.")
        sys.exit()
    else:
        return file

def start_program(): #welcomes user and gives instructions and gets input
    """Tells user instructions and asks for input"""
    print("Welcome, were gonna draw some circles!\n")
    print("""The text file you use must be formated like the examples below.

Hexadecimal file must have a "#" before the number and no empty lines after entries:
#123456
#FFFFFF
#000000

RGB file must have each individual number on it's own line with no empty lines after each entry:
255
54
125
234
57
234
""")
    answer = input("""Would you like to use a hexadecimal color file or RGB color file? 
Please enter \"H\" for hexadecimal or \"R\" for RGB: """).lower()
    
    while answer not in ("h", "r"):
        answer = input("""\nWould you like to use a hexadecimal color file or RGB color file? 
Please enter \"H\" for hexadecimal or \"R\" for RGB: """).lower()
    print()
    if answer == "h":
        open_file("colorshex.txt", "r")
        window = turtle.Screen()
        window.title("Drawing Circles")
        window.bgcolor("grey")
        circle_hex("colorshex.txt", "r")
        
    if answer == "r":
        open_file("colorsrgb.txt", "r")
        window = turtle.Screen()
        window.title("Drawing Circles")
        window.bgcolor("grey")
        draw_circle_rgb("colorsrgb.txt", "r")


def draw_circle_rgb(file_name, mode): #one way of drawing and filling circles
    """Draws and fills circles with RGB colors from txt file"""
    file = open(file_name, mode)
    #colors = file.readlines()
    whole_thing = file.readlines()
    #print(whole_thing)
    x = 0
    y = 1
    z = 2
    #print(len(whole_thing)//3)
    for i in range(len(whole_thing)//3):
        r = int(whole_thing[x][:-1])
        g = int(whole_thing[y][:-1])
        b = int(whole_thing[z][:-1])
        print("The color is:", r, g, b)
        turtle.colormode(255)
        t = turtle.Turtle()
        t.shape("turtle")
        t.fillcolor(r, g, b)
        t.begin_fill()
        t.up()
        t.goto(0, -50)
        t.down()
        t.circle(100)
        t.end_fill()
        t.up()
        t.hideturtle()
        time.sleep(1)
        t.clear()
        x += 3
        y += 3
        z += 3
    file.close()
def rgb_test(file_name, mode):
    file = open_file(file_name, mode)
    color = file.readline()
    while color:
        count = 0
        r = ""
        g = ""
        b = ""
        for i in color:
            if i == ",":
                #color.remove(i)
                count += 1
            if count == 0 and i != "," and i != " ":
                r += i
                #color.remove(i)
            if count == 1 and i != "," and i != " ":
                g += i
                #color.remove(i)
            if count == 2 and i != "," and i != " ":
                b += i
                #color.remove(i)
##        print(r, g, b)
##        color = file.readline()
##    whole_thing = file.readlines()
        print("The color is:", r, g, b)
        turtle.colormode(255)
        t = turtle.Turtle()
        t.shape("turtle")
        t.fillcolor(int(r), int(g), int(b))
        t.begin_fill()
        t.up()
        t.goto(0, -50)
        t.down()
        t.circle(100)
        t.end_fill()
        t.up()
        t.hideturtle()
        time.sleep(1)
        t.clear()
        color = file.readline()
    file.close()
        
def circle_hex(file_name, mode): #another way of drawing and filling circles
    """Draws and fills circle with hex colors from txt file"""
    file = open_file(file_name, mode)
    color = file.readline()
    #print(color)
    while color:
        print("The color is:", color)
        t = turtle.Turtle()
        t.shape("turtle")
        t.fillcolor(color[:7])
        t.begin_fill()
        t.up()
        t.goto(0, -50)
        t.down()
        t.circle(100)
        t.end_fill()
        t.up()
        t.hideturtle()
        time.sleep(1)
        t.clear()
        color = file.readline()
    file.close()

def have_a_nice_day(): #goof around function
    """Draws smiley face and message"""
    t = turtle.Turtle()
    t.shape("turtle")
    t.fillcolor("yellow")
    t.begin_fill()
    t.up()
    t.goto(0, -50)
    t.down()
    t.circle(100)
    t.end_fill()
    t.up()
    t.goto(-35, 80)
    t.down()
    t.dot(25)
    t.up()
    t.goto(35, 80)
    t.down()
    t.dot(25)
    t.up()
    t.goto(-40, 15)
    t.right(90)
    t.pensize(10)
    t.down()
    t.circle(40, 180)
    t.up()
    t.hideturtle()
    t.goto(0, -150)
    t.down()
    t.write("Have A Nice Day!", align = "center", font = ("Comic Sans MS", 50, "normal"))
    time.sleep(3)
    t.clear()

#Main program

start_program()

have_a_nice_day()

rgb_test("testrgb.txt", "r")




