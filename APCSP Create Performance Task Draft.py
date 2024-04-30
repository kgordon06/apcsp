# APCSP Create Performance Task
# importing methods
import turtle
import random
import keyboard


# initialize screen
wn = turtle.Screen()
wn.title("Five Nights of Memory")
wn.setup(width=600, height=800)


# initialize turtle
turtle.hideturtle()
turtle.bgcolor("light pink")
turtle.register_shape("freddy.gif")
turtle.register_shape("foxy.gif")
turtle.register_shape("chica.gif")
turtle.register_shape("bonnie.gif")
turtle.register_shape("baby.gif")
turtle.register_shape("mangle.gif")
turtle.register_shape("springtrap.gif")


# functions
def start_on_keypress():
    turtle.clear()
    turtle.write("When you are ready to\n begin, press S.", align="center", font=("Arial", 24, "normal"))
    while True:
        if keyboard.is_pressed('s'):
            turtle.clear()
            break
'''
def shuffle_images():
    shuffled_images = image_files[:]
    random.shuffle(shuffled_images)
    return shuffled_images
'''


def display_images(images):
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 0)
    for image in image_files:
        shuffled_images = image_files[:]
        random.shuffle(shuffled_images)
        turtle.stamp(image)


def player_order():
    # empty list where player inputs will be stored
    player_order = []
    # prompting player to input the order of images
    for i in range(len(image_files)):
        player_input = wn.textinput("Enter Image Order", f"Enter name of character {i + 1}:")
        player_order.append(player_input)


def check_order():
    if (player_order == display_images):
        print("Congratulations! You win!")
    else:
        print("Sorry, wrong order. Better luck next time!")


# main game engine
while True:
    while True:
        # asking player to input difficulty
        difficulty = input("What difficulty would you like to play? easy/medium/hard\n").lower()
        # setting list of images and their names based on chosen difficulty
        if (difficulty == "easy"):
            image_files = ["freddy.gif", "foxy.gif", "chica.gif", "bonnie.gif"]
            break
        elif (difficulty == "medium"):
            image_files = ["freddy.gif", "foxy.gif", "chica.gif", "bonnie.gif","baby.gif","mangle.gif"]
            break
        elif (difficulty == "hard"):
            image_files = ["freddy.gif", "foxy.gif", "chica.gif", "bonnie.gif","baby.gif","mangle.gif","springtrap.gif"]
            break
        else:
            print("Please try again.")
    #   prompting player to start game
    start_on_keypress()
    #   shuffling images
    'shuffle_images()'
    display_images(image_files)
    #   players input the order
    player_order()
    #   checking if player input matches shuffled image
    check_order()
    #   prompting play to play again
    play_again = input("Would you like to play again? y/n\n")
    if(play_again == "y"):
        turtle.clear()
        wn.bgcolor("light pink")
    elif(play_again == "n"):
        turtle.clear()
        break
    else:
        print("Please try again.")


# ending game screen
turtle.write("Thanks for playing!", align="center", font=("Arial", 24, "normal"))


# keep screen open until player closes
wn.mainloop()


'''
# APCSP Create Performance Task
# importing methods
import turtle
import random
import keyboard
from PIL import Image


# initialize screen
wn = turtle.Screen()
wn.title("Five Nights of Memory")
wn.setup(width=600, height=800)
start_x = -100
start_y = 100


# initialize turtle
turtle.hideturtle()
turtle.bgcolor("light pink")
turtle.register_shape("freddy.gif")
turtle.register_shape("foxy.gif")
turtle.register_shape("chica.gif")
turtle.register_shape("bonnie.gif")
turtle.register_shape("baby.gif")
turtle.register_shape("mangle.gif")
turtle.register_shape("springtrap.gif")


# functions
def start_on_keypress():
    turtle.clear()
    turtle.write("When you are ready to\n begin, press S.", align="center", font=("Arial", 24, "normal"))
    while True:
        if keyboard.is_pressed('s'):
            turtle.clear()
            break


def player_order():
    # empty list where player inputs will be stored
    player_order = []
    # prompting player to input the order of images
    for i in range(len(image_files)):
        player_input = wn.textinput("Enter Image Order", f"Enter name of character {i + 1}:")
        player_order.append(player_input)


def display_image(filename, x, y):
    # load the image
    img = Image.open(filename)
    # resize the image
    img.thumbnail((200, 200))
    # create a Turtle to display the image
    t = turtle.Turtle()
    t.hideturtle()
    # set the position for the Turtle
    t.penup()
    t.goto(x, y)
    t.pendown()
    # display the image
    wn.addshape(filename)
    t.shape(filename)


def display_timer():
    for i, filename in enumerate(image_files):
        x = start_x
        y = start_y
        # clear the previous image
        turtle.clear()
        # display the current image
        display_image(image_files, x, y)
        # pause for a short duration before displaying the next image
        turtle.delay(75)
        # hide the turtle to avoid seeing it moving
        turtle.hideturtle()


# main game engine
while True:
    while True:
        # asking player to input difficulty
        difficulty = input("What difficulty would you like to play? easy/medium/hard\n").lower()
        # setting list of images and their names based on chosen difficulty
        if (difficulty == "easy"):
            image_files = ["freddy.gif", "foxy.gif", "chica.gif", "bonnie.gif"]
            image_names = ["Freddy","Foxy","Chica","Bonnie"]
            break
        elif (difficulty == "medium"):
            image_files = ["freddy.gif", "foxy.gif", "chica.gif", "bonnie.gif","baby.gif","mangle.gif"]
            image_names = ["Freddy","Foxy","Chica","Bonnie","Baby","Mangle"]
            break
        elif (difficulty == "hard"):
            image_files = ["freddy.gif", "foxy.gif", "chica.gif", "bonnie.gif","baby.gif","mangle.gif","springtrap.gif"]
            image_names = ["Freddy","Foxy","Chica","Bonnie","Baby","Mangle","Springtrap"]
            break
        else:
            print("Please try again.")
    #   prompting player to start game
    start_on_keypress()
    #   shuffling images
    original_order = []
    original = random.shuffle(image_files)
    original_order.append(original)
    #   displaying images
    display_timer()
    #   players input the order
    player_order()
    #   checking if player order equals original order
    if (player_order == original_order):
        print("Congratulations! You win!")
    else:
        print("Sorry, that is not the correct order.")
    #   prompting play to play again
    play_again = input("Would you like to play again? y/n\n")
    if(play_again == "y"):
        turtle.clear()
        wn.bgcolor("light pink")
    elif(play_again == "n"):
        turtle.clear()
        break
    else:
        print("Please try again.")


# ending game screen
turtle.write("Thanks for playing!", align="center", font=("Arial", 24, "normal"))


# keep screen open until player closes
wn.mainloop()
'''
