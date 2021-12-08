# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define e = Character("Eileen")

define po = Character("Professor Oak")
define toto = Character("Totodile")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg cave

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show po happy :
        xalign 0.75
        yalign 1

    # These display lines of dialogue.

    po "welcome brave traveler, to the world of pokemon."
    po "this here is a pokemon"
    show po happy at right:
        yalign 1

    show totodile
    po "in this world, people and pokemon live side by side as friends"

    toto "toto"

    # This ends the game.

    return
