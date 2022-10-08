# define characters

define h1 = Character("Asprak Senpai") # h1 = heroine 1
define you = Character("You") # you

# define character images
image asprak_senpai = "characters/asprak_senpai.png"

# define scene images
image lab = "scenes/lab.jpg"

# The game starts here.
label start:

    # scene 1
    scene lab

    show asprak_senpai at right

    h1 "Ohayou onii-chan!"

    # This ends the game.
    return
