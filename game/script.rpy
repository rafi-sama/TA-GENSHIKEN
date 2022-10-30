# define characters
define h1 = Character("Asprak Senpai", color = "#879af2") # h1 = heroine 1 / asprak senpai
define you = Character("You") # you
define friend = Character("Friend 1")

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
    friend "Where have you been? We were looking for you."
    you "Sorry guys, I was-"
    show asprak_senpai at left
    h1 "*clears throat"

    scene papan_tulis

    show asprak_senpai at right
    h1 "I'll start the briefing, now that your group is complete."
    h1 "Please note, I'm giving you *looking at MC some leniency just because this is your first session."
    h1 "Your next assistant might not be so forgiving."
    h1 "Gather all of your preliminary assignments on the desk before we start the test."
    h1 "Done? Good. Get your pen and papers, here's your test."
    h1 "*flips the whiteboard"

    scene meja_lab

    you "\[What the hell am I looking at?\]"
    you "\[What in the actual fuck is regression analysis\]"
    h1 "Five minutes remaining."
    you "Bro, could you help me out on that regression thing?"
    friend "(MC's name), you passed 8th grade, right?"
    friend "You literally only have to find the slope of that equation. The. Slope. Of. The. Equation."
    you "How?"
    friend "It's literally written on the damn equation."

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

    scene dapur_kulkas

    you "*walks to the lounge, opens the fridge, and finds a masterless oreo"
    you "\[They didn't call me a corsair back at high school for nothing.\]"

    you "*while reaching said oreo, he finds a bag of chips in one of the drawers"
    you "[What kind of psychopath chills their chips?]"

    "*sound of a book dropped onto the floor"
    you "\[Huh?\]"

    # This ends the game.

    scene ruang_tamu

    "*MC looks around to find the source, only to see FL1 laying on a sofa. "
    "She wears (insert clothes, don't wanna be held liable for the details), one hand inside a bag of chips, another hand just hanging out from the sofa."
    "Apparently, she fell asleep while reading a manga and got startled by it being dropped."
    "Reaching down to get the fallen manga, she sees MC by the fridge looking at her, dumbfounded."

    you "Uhh, hi?"

    h1 "*squeals"
    h1"YOU DIDN'T SEE ANYTHING!"
    h1"*FL1 grabs her stuff and sprints to her room"

    you "\[...\]"
    you "\[The fuck just happened?\]"
    you "\[...\]"
    you "\[You know what? I'm not hungry.\]"
    you "*returns the oreo and heads back to his room"
    
    scene kamar

    "*time skip to the next day"
    "*alarms blaring, MC wakes up, still can't wrap his head around yesterday's incident"

    you "\[Did yesterday really happen? Was that really her?\]"
    you "*reminisces once more, fuckin simp"
    you "\[Why can't I stop thinking about her?\]"

    scene kosan lorong

    you "*MC gets up and prepares for his day. Opening his door, our clumsy MC bumps into another person"
    you "Ah, sorry. Didn't see you th-"
    "*Of course, it's FL1. They stare each other for quite some time before the silence got broken by MC's alarm. He reaches into his pocket and looks at his phone"
    you "\[Oh shit, only half an hour remaining before class. Better get going now.\]"
    "*MC peers up and looks at the exit to find FL1 already closing the dorm's gate."

    scene depan kosan

    you "\[Gotta take a shot.\]"
    you "*MC pockets his phone and runs up to her"
    you "Uhh, hey! Hey! How are you this morning?" 

    # *he asked as he caught up to her while walking backwards

    scene pinggir jalan

    h1 "*doesn't answer, eyes straight ahead"

    you "Uhh, you remember me, right? It's (insert MC's name), from the lab yesterda-"

    h1 "*pulls MC closer to the side of the road since there's a car heading their way"
    h1 "*spins MC around and tells him to walk correctly"
    h1 "“Dummy, look where you're going when you walk."

    you "Oh shit." # *looks at the car that just passed
    you "Thanks."

    "*The campus is just a couple hundred meters ahead"

    you "So uhh, you're having a morning class, too?"
    "*FL1 doesn't answer"

    you "By the way, I really didn't expect us to live in the same dorm."
    "FL1 gets flustered"

    scene kantin general_area

    you "*reminisces about FL1 back at the lab"
    you "*reminisces about the incident yesterday"
    you "\[She's damn cute, I get that. But I didn't expect that big of a gap moe.\]"
    you "*reminiscing how flustered she got when they walk together"
    "*suddenly, people around him are shuffling around and lecturer is picking up their stuff"

    you "\[Hold up, the class is finished?\]"
    you "\[But I haven't understood shit.\]"
    you "\[Welp, that's two extra hours of “independent learning”.\]"
    you "*stomach rumbles"
    you "\[Oh yeah, I haven't had breakfast.\]"

    you "*MC got up and went to cafetaria and orders his lunch"

    you "*bumps into his friend"
    you "Oh hey, getting some chow, too?"

    friend "Hey! Yeah. Didn't understand anything at class, my brain was too busy asking whether I should buy ayam geprek or ayam penyet for lunch."

    you "Damn, same. By the way, got any seats yet?"
    you "*MC eyes around to find an empty seat and instantly saw FL1 sitting alone at the far end of the cafetaria"

    friend "Nah, I'm taking it away, gonna have a group work right after this."

    friend "*looks at MC, looks at where he's looking"
    friend "But I guess you have a seat in mind already."

    you "W-What? Oh, no, I guess you're misinterpreting something."

    friend "Yeah, sure, sure. You've been eyeing our lab assistant since she scolded youabout the caliper."

    you "What? No! It's just that we happen to live in the same dorm."

    friend "Real shit? Well you're in luck, my friend."
    "*both of their orders are finished"
    friend "Welp, gotta get going. See you around, (MC)!"
    "*leans to MC and whispers"
    friend "And good luck."

    you "Hey, come back here! I'm not done yet!"

    you "See ya later!"

    scene kantin meja

    you "\[That fucker better not leak it to everybody.\]"
    you "*glances at FL1"
    you "\[But coming to it again, why did I notice her that quickly in the first place?\]"
    you "*breathes in"
    you "\[Here we go.\]"

    you "*MC approaches the table"

    you "Hey! Is this seat taken?"

    h1 "shocked pikachu face, shakes her head"

    you "Mind if I sit here?"

    h1 "*shakes her head, getting a bit tense"

    you "*sits and starts to eat his meal"
    "*they both eat in silence, not daring to break the ice"
    you "\[Do I make her uncomfortable?\]"
    "*looks around for a vacant seat, but there isn't any"
    you "\[Better eat this quickly.\]"
    you "*finishing his lunch, he looks up to see FL1 staring at him"
    you "I-I think I ought to change tables."

    h1 "No, don't." #*holding the hem of his sleeve

    you "*sits back down"
    you "“Okay?"

    "*MC continues to eat his lunch in silence"

    h1 "Why do you keep approaching me?"

    you "I beg your pardon?" #*a bit shocked

    h1 "You heard me. But don't get it wrong, though. I just wanna know why."

    you "Well, for starters, I just want to be friends with you." 
    you "I mean, we live in the same dorm, we will bump into each other every day. Might as well get to know you better."
    you "\[And for the last part, I really want to know you better.\]"

    h1 "Oh, well that's nice."

    you "And we will meet each other every other week at the lab, so-"

    h1 "*stares daggers at MC"
    h1 "Thank you for bringing it up, but I much prefer that we stop talking about the lab."

    you "R-Right."
    you "[Nearly stepped on a landmine back there.]"

    h1 "If that's the case." 
    h1 "*she stands up and packs her stuff"
    h1 "I'll be in your care, (MC). I hope we can get to know each other better."

    you "Y-yeah. Me, too."

    h1 "Well, I have to tutor a freshman calculus class in half an hour. It's good to see (MC), take care." 
    h1 "*leaves MC"

    scene kantin general_area

    you "*looks at FL1 as she walks away"
    you "\[What a nice start.\]"

    "*his phone vibrates rapidly, mafiki class' group chat is in chaos"
    you "\[A fucking physics pop quiz in 30 minutes? Oh fuck.\]"

    you "*books out to class to get some crash course"

    "*time skip to the red highlighted part"

    scene ?

    you "*wakes up startled"
    you "\[How come has the alarm not gone berserk yet? My sleep quality is getting a bit too suspicious.\]"

    #Hey, you. You're finally awake. *some 4th wall skyrim shit ?

    you "\[Who the fuck is that?\]"

    you "*looks at phone for time"
    you "\[There's no fucking way it's still 5 am. That was the best sleep I had in weeks. It must be 5 pm.\]"

    you "*looks out his windows. The sky is still dark"
    you "\[Well I'll be damned.\]"

    you "*turns off alarms"
    you "*reminisces on yesterday's encounter with FL1"
    you "\[Welp, better get ready and find her again.\]"

    "*time skip to lunch"

    scene kantin

    you "*orders his food and looks around the cafeteria"
    you "\[Where is she?\]"

    friend "Yo, MC! Wanna join us?"
    you "\[Meh, I'll look for her at the lab after class.\]"

    you "Sure thing!"

    scene luar lab

    "*time skip to the afternoon, he went straight to the physics lab building and wait outside"

    you "\[Guess she's not here. Well, nice try, I guess.\]"

    scene kamar
    you "MC heads back to his dorm and got to his room"
    you "*stomach rumbles"
    you "\[I literally just ate four hours ago.\]"
    you "*rumbles some more"
    you "\[Now, should I order a balanced meal like a responsible college student should or should I order diabetes incarnate?\]"
    you "*spoiler alert, his intrusive thought wins"
    you "\[A wise person once said an apple a day keeps the doctor away. Unfortunately, I’m not a wise guy.\]"
    you "*orders a martabak manis/terang bulan/hok lo pan/kue bandung/apam balik/whatever the fuck you call it"    

    scene ruang_tamu
    you "*his order arrives. He takes it and went to the lounge"
    you "*sees FL1 on her phone"
    you "\[Time to shoot my shot\]"
    you "Fancy seeing you here."

    h1 "*kinda startled"
    h1 "Hey, didn’t see you there."
    
    you "*sits down"
    you "Do you mind?" #point to the sofa

    h1 "*pats the cushion"
    h1 "C'mere."

    you "Nice."
    you "*open the martabak"
    you "Here, take some."

    h1 "Ah, thank you."

    you "*turns the tv on"



    return
