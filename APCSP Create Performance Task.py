# APCSP Create Performance Task
# importing methods
import turtle
import random
import keyboard


# initialize screen
wn = turtle.Screen()
wn.title("Flowory")
wn.setup(width = 1920, height = 1080)


# initialize turtle
turtle.bgcolor("lightpink1")
turtle.hideturtle()
turtle.register_shape("sunflower.gif")
turtle.register_shape("daisy.gif")
turtle.register_shape("iris.gif")
turtle.register_shape("daffodil.gif")
turtle.register_shape("lavender.gif")
turtle.register_shape("rose.gif")
turtle.register_shape("tulip.gif")
turtle.register_shape("peony.gif")
turtle.register_shape("lily.gif")
turtle.register_shape("snapdragon.gif")

# functions
#   begins the game
def start():
    print("When you are ready to begin, press B.")
    while True:
        if keyboard.is_pressed('b'):
            turtle.clear()
            break

def input_order():
    #   empty list where the player's inputs will be stored
    player_order = []
    #   prompting player to input the order of shuffled images
    for i in range(len(flower_images)):
        player_input = wn.textinput("Enter Image Order", f"Enter name of flower {i + 1}:")
        player_order.append(player_input)
    # checking if player input matches order of shuffled images
    if (player_order == original_order):
        print("Congratulations! You got it right!")
    else:
        print("Oops! That's not the correct order.")

#   main game engine
while True:
    while True:
        #   introducing the game to player
        instructions = input("Hi! Do you know how to play the game? Y/N\n").lower()
        if (instructions == "y"):
             print("Awesome!")
        if (instructions == "n"):
            print("How to Play: Images of flowers will appear on your screen in a randomly generated order. You must remember and input the order in which the flowers appeared. The higher the difficulty, the more flowers you need to remember.")
        #   asking player to input difficulty
        difficulty = input("What difficulty would you like to play? Easy/Medium/Hard\n").lower()
        #   setting the list of flowers that will appear in random order depending on difficulty
        if (difficulty == "easy"):
            flower_images = ["sunflower.gif", "daisy.gif", "iris.gif", "daffodil.gif"]
            break
        elif (difficulty == "medium"):
            flower_images = ["sunflower.gif", "daisy.gif", "iris.gif", "daffodil.gif", "lavender.gif", "rose.gif","tulip.gif"]
            break
        elif (difficulty == "hard"):
            flower_images = ["sunflower.gif", "daisy.gif", "iris.gif", "daffodil.gif", "lavender.gif", "rose.gif","tulip.gif", "peony.gif", "lily.gif", "snapdragon.gif"]
            break
        else:
            print("Please try again.")
    #   prompting player to start game
    start()
    #   shuffling images
    original = random.shuffle(flower_images)
    original_order = []
    original_order.append(original)
    #   display images
    turtle.goto(0,0)
    for image in flower_images:
        turtle.shape(image)
        turtle.stamp()
        turtle.delay(100)
    turtle.delay(100)
    #   player input
    input_order()
    #   prompting player to play again
    play_again = input("Would you like to play again? Y/N\n")
    if (play_again == "y"):
        turtle.clear()
    elif (play_again == "n"):
        turtle.clear()
        break
    else:
        print("Please try again.")

#   ending game screen
turtle.write("Thanks for playing!", align="center", font=("Arial", 24, "normal"))

#   keep screen open until player closes
wn.mainloop()
