# define characters
define h1 = Character("Asprak Senpai", color = "#879af2") # h1 = heroine 1 / asprak senpai
define you = Character("You") # you
define f1 = Character("Friend 1")

# character images
# image asprak_senpai = "characters/asprak_senpai.png"

# scene images
image kamar bangun = "scenes/pov_bangun_tidur.jpg"
image tangan hp = "characters/pegang_hp.png"

# The game starts here.
label start:

    # scene 1

    # play music "sound/Bar_at_the_port.mp3" loop

    scene kamar bangun

    you "*wakes up at 06.30 AM on a Monday"
    show tangan hp with moveinbottom
    you "*Checks his phone for time"
    you "\[Why did I wake up this early? I have no class on Mondays.\]"
    hide tangan with moveoutbottom
    you "*proceeds to close his eyes, then remembers something"
    you "\[I have a fucking physics practice session this morning.\]"

    scene beres2in_barang

    you "*MC prepares his stuffs and double-timed his way to ITB"

    scene gerbang_itb

    you "*MC looks at his watch as he passed through the gate, 07.00 AM"
    you "\[Fuck, I'm gonna be late\]"

    scene pintu_lab

    you "Excuse me!” *as he pushed his way to the lab"

    scene meja_lab

    you "*MC somehow managed to enter the lab just as his group got called by the assistant for briefing"
    f1 "Where have you been? We were looking for you."
    you "Sorry guys, I was-"
    show asprak_senpai at left
    h1 "*clears throat"

    scene papan_tulis

    show asprak_senpai at right
    h1 "I’ll start the briefing, now that your group is complete."
    h1 "Please note, I’m giving you *looking at MC some leniency just because this is your first session."
    h1 "Your next assistant might not be so forgiving."
    h1 "Gather all of your preliminary assignments on the desk before we start the test."
    h1 "Done? Good. Get your pen and papers, here's your test."
    h1 "*flips the whiteboard"

    scene meja_lab

    you "\[What the hell am I looking at?\]"
    you "\[What in the actual fuck is regression analysis\]"
    h1 "Five minutes remaining."
    you "Bro, could you help me out on that regression thing?"
    f1 "(MC's name), you passed 8th grade, right?"
    f1 "You literally only have to find the slope of that equation. The. Slope. Of. The. Equation."
    you "How?"
    f1 "It's literally written on the damn equation."

    scene papan_tulis

    h1 "Alright, time's up, hand them in."
    h1 "*looks at MC's paper"
    h1 "*under her breath"
    h1 "\[What is wrong with this kid.\]"
    h1 "Kay, I'm (insert name), registration number (insert NIM), and I'm going to be your practice assistant for today."
    h1 "If you need any help for today's session, feel free to reach out."
    h1 "Your module for today will be Measurement and Physical Data Processing."
    h1 "I want you guys to split into three groups to make things faster. "
    h1 "First group, follow me to the barometer …"

    scene meja_lab

    "*time skip, MC's group is tasked with this bad boy"
    "Insert gambar regresi linier"
    "*big F to him"
    h1 "*approaches MC, who is trying to figure out how to use a vernier caliper"
    h1 "“You got the length of the first block, already?"
    you "Uhh, yeah? It's *looking at the caliper around 9.255 cm."
    h1 "“What? How on earth did you get that number? Let me check."
    you "*measures"
    h1 "It says 9.55 cm."
    you "But-"
    h1 "“You learned this back in middle school, dummy. You're supposed to understand this thing from the preliminaries."
    h1 "Now go weigh them at the scale."
    you "Ah, okay. I'm, uhh, gonna weigh them now."
    you "\[Fuck, I'm getting scolded\]"
    h1 "Alright, the time for measurement is up. Get your journals, we're writing the Report."
    h1 "Before we start, I want to stress that the bulk of the score is at the observation and discussion part of your report, so make them well."
    h1 "Also, for Group 4, you can take out your calculators to get the regression equation."
    you "Oh, no."
    you "*fumbles around his bag and lab coat"
    h1 "Is something the matter, (MC)?"
    you "Uhh, yeah. I think I left my calculator back at my dorm."
    h1 "And I thought you couldn't mess up more. Go pair up with a friend."
    "*time skips, reports are submitted"

    scene papan_tulis

    h1 "Aaand, we're done. Thank you for coming to today's session."
    h1 "(MC), a word?"
    you "Am I in trouble?"
    h1 "For now, no. But you have taken quite the attention of other assistants."
    h1 "The assistants and practice chief have agreed to not go too rough on minor infractions, but looking at how your practice went, I think I have to warn you."
    h1 "Just make sure to come on time and come prepared. Capiche?"
    you "Understood."
    h1 "Good. Have a nice day, take care."
    you "*pack his things and left the lab"

    scene lorong_lab

    you "\[Well that went fantastic. Getting myself in the assistant's sight. What a wonderful way to start my week.\]"
    you "*still walking, reminisces on FL1"
    you "\[But she's a lowkey cutie, though.\]"

    scene kamar

    "*time skip to the afternoon, MC has finished his class for the day and just arrived at his mix-gender dorm"
    you "*laying down on his bed"
    you "\[Man, do I not love studying in ITB.\]"
    you "*reminisces on FL1 again"
    you "\[Stop thinking about her, you simp.\]"
    you "*stomach rumbles"
    you "\[Welp, I guess it's raid-the-fridge o'clock.\]"

    # This ends the game.
    return
