# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Suomi Placeholder")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    "suatu hari..."

    scene bg tracen

    "ada peneliti uma gila memampiriku"
    
    show agnes default:
        zoom 1.5
        xalign 0.5
        yalign 0.2

    # These display lines of dialogue.

    e "ahahahaha!"

    e "iwak koyok asu!"

    hide agnes default with dissolve

    scene black with dissolve

    "udah gitu aja:v"

    # This ends the game.

    return
