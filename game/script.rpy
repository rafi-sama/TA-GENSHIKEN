# define characters
define h1 = Character("Heroine") # h1 = heroine 1 / asprak senpai
define you = Character("You") # you

# character images
image asprak_senpai = "characters/asprak_senpai.png"

# scene images
image lab = "scenes/lab.jpg"

# The game starts here.
label start:

    # scene 1
    scene background

    show heroine at right

    h1 "Ohayou"
    h1 "Ohayou1"
    h1 "Ohayou2"


    # This ends the game.
    return
