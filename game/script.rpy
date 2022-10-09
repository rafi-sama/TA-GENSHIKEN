# define characters
define h1 = Character("Asprak Senpai") # h1 = heroine 1 / asprak senpai
define you = Character("You") # you

# character images
image asprak_senpai = "characters/asprak_senpai.png"

# scene images
image lab = "scenes/lab.jpg"

# The game starts here.
label start:

    # scene 1
    scene lab

    show asprak_senpai at right

    h1 "Ara~ ara~ "

    # This ends the game.
    return
