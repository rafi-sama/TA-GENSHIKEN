﻿# define characters
define h1 = Character ("‎   Asprak Senpai   ‎", color = "#879af2") # h1 = heroine 1 \ asprak senpai
define you = Character("‎      You     ‎") # you
define friend = Character("‎     Friend   ‎")
define ag = Character("‎     Attendance Guy   ‎")
define friend2 = Character("‎     Senpai's Friend   ‎")

# background

image black = "black.png"
image kamar bangun = "scenes/pov_bangun_tidur.jpg"
image kamar bangun_blink = "scenes/pov_bangun_tidur_blink.jpg"
image gerbang1 = "scenes/gerbang1.jpg"
image gerbang2 = "scenes/gerbang2.jpg"
image gerbang3 = "scenes/gerbang3.jpg"
image jalan kosong1 = "scenes/jalan_kosong1.jpg"
image jalan kosong2 = "scenes/jalan_kosong2.jpg"
image jalan mobil1 = "scenes/jalan_mobil1.jpg"
image jalan mobil2 = "scenes/jalan_mobil2.jpg"
image jalan mobil3 = "scenes/jalan_mobil3.jpg"
image jalan mobil4 = "scenes/jalan_mobil4.jpg"
image jalan motor1 = "scenes/jalan_motor1.jpg"
image jalan motor2 = "scenes/jalan_motor2.jpg"
image kantin ramai1 = "scenes/kantin1.jpg"
image kantin ramai2 = "scenes/kantin2.jpg"
image kantin ramai3 = "scenes/kantin3.jpg"
image kantin meja = "scenes/kantin_meja.jpg"
image kos bukapintu = "scenes/kos_bukapintu.jpg"
image kos bukakunci = "scenes/kos_bukakunci.jpg"
image kos lorong1 = "scenes/kos_lorong1.jpg"
image kos lorong2 = "scenes/kos_lorong2.jpg"
image kos lorong3 = "scenes/kos_lorong3.jpg"
image kos meja_kosong = "scenes/kos_meja_kosong.jpg"
image kos meja_laptop = "scenes/kos_meja_laptop.jpg"
image kos sofa_close = "scenes/kos_sofa_close.jpg"
image kos sofa_far = "scenes/kos_sofa_far.jpg"
image kos sofa_duduk = "scenes/kos_sofa_duduk.jpg"
image kos luar = "scenes/kos_luar.jpg"
image lab barometer = "scenes/lab_barometer.jpg"
image lab komputer1 = "scenes/lab_komputer1.jpg"
image lab komputer2 = "scenes/lab_komputer2.jpg"
image lab datang = "scenes/lab_kosong.jpg"
image lab kosong = "scenes/lab_datang.jpg"
image lab pulang = "scenes/lab_pulang.jpg"
image lab loker_buka = "scenes/lab_loker_buka.jpg"
image lab loker_tutup = "scenes/lab_loker_tutup.jpg"
image lab lorong_datang = "scenes/lab_lorong_datang.jpg"
image lab lorong_pulang = "scenes/lab_lorong_pulang.jpg"
image lab meja = "scenes/lab_meja.jpg"
image lab papan1 = "scenes/lab_papan1.jpg"
image lab papan2 = "scenes/lab_papan2.jpg"
image lab pintu_lab = "scenes/lab_pintu.jpg"
image lab ramai1 = "scenes/lab_ramai1.jpg"
image lab ramai2 = "scenes/lab_ramai2.jpg"
image lab timbangan = "scenes/lab_timbangan.jpg"
image lift buka = "scenes/lift_buka.jpg"
image lift tutup = "scenes/lift_tutup.jpg"
image lift pencet = "scenes/lift_pencet.jpg"

# character 
# image asprak_senpai = "characters\asprak_senpai.png"

# non character
image tangan hp = "characters/pegang_hp.png"
image blink = "blink.png"

# sound
define audio.alarm = "sound/sfx/alarm.mp3"

# The game starts here.
label start:
    play sound alarm loop

    scene black with Dissolve(4)

    # play music "sound/Bar_at_the_port.mp3" loop 
    # play sound "sound/sfx/yawn.mp3" loop

    scene kamar bangun_blink with Dissolve(3)

    stop sound

    you "*wakes up at 06.30 AM on a Monday"
    
    scene kamar bangun with Dissolve(2)
    
    show tangan hp with moveinbottom

    you "*Checks his phone for time"
    you "\[Why did I wake up this early? I have no class on Mondays.\]"

    hide tangan with moveoutbottom

    scene kamar bangun_blink with Dissolve(1.5)
    you "*proceeds to close  his eyes, then remembers something"

    scene kamar bangun with Dissolve(1.5)
    you "\[I have a fucking physics practice session this morning.\]"

    scene beres2in_barang

    you "*MC prepares his stuffs and double-timed his way to ITB"

    scene gerbang3

    you "*MC looks at his watch as he passed through the gate, 07.00 AM"

    scene lab pintu_lab

    you "\[Fuck, I'm gonna be late\]"

    scene lab ramai1

    you "Excuse me!" #*as he pushed his way to the lab

    you "*MC somehow managed to enter the lab just as his group got called by the assistant for briefing"
    
    scene lab komputer1

    friend "Where have you been? We were looking for you."
    you "Sorry guys, I was-"

    scene lab papan2

    show asprak_senpai at left

    h1 "*clears throat"

    show asprak_senpai at right

    h1 "I'll start the briefing, now that your group is complete."
    h1 "Please note, I'm giving you *looking at MC some leniency just because this is your first session."
    h1 "Your next assistant might not be so forgiving."
    h1 "Gather all of your preliminary assignments on the desk before we start the test."
    h1 "Done? Good. Get your pen and papers, here's your test."
    h1 "*flips the whiteboard"

    scene lab papan3

    you "\[What the hell am I looking at?\]"
    you "\[What in the actual fuck is regression analysis\]"

    scene lab meja

    h1 "Five minutes remaining."
    you "Bro, could you help me out on that regression thing?"
    friend "Bro.. you passed 8th grade, right?"
    friend "You literally only have to find the slope of that equation. The. Slope. Of. The. Equation."
    you "How?"
    friend "It's literally written on the damn equation."

    scene lab papan2

    h1 "Alright, time's up, hand them in."
    h1 "*looks at MC's paper"
    h1 "*under her breath"
    h1 "\[What is wrong with this kid.\]"
    h1 "Kay, I'm (insert name), registration number (insert NIM), and I'm going to be your practice assistant for today."
    h1 "If you need any help for today's session, feel free to reach out."
    h1 "Your module for today will be Measurement and Physical Data Processing."
    h1 "I want you guys to split into three groups to make things faster. "

    h1 "First group, follow me to the barometer …"

    scene lab barometer 

    you "\[I don't know how to read this thing..\]"

    scene lab meja

    "*time skip, MC's group is tasked with this bad boy"
    "Insert gambar regresi linier"
    "*big F to him"
    h1 "*approaches MC, who is trying to figure out how to use a vernier caliper"
    h1 "You got the length of the first block, already?"
    you "Uhh, yeah? It's *looking at the caliper around 9.255 cm."
    h1 "What? How on earth did you get that number? Let me check."
    you "*measures"
    h1 "It says 9.55 cm."
    you "But-"
    h1 "You learned this back in middle school, dummy. You're supposed to understand this thing from the preliminaries."
    h1 "Now go weigh them at the scale."
    you "Ah, okay. I'm, uhh, gonna weigh them now."

    scene lab timbangan

    you "\[This should be easy enough\]"

    scene lab papan2

    h1 "Alright, the time for measurement is up. Get your journals, we're writing the Report."
    h1 "Before we start, I want to stress that the bulk of the score is at the observation and discussion part of your report, so make them well."
    h1 "Also, for Group 4, you can take out your calculators to get the regression equation."
    you "Oh, no."

    scene lab loker_buka

    you "*fumbles around his bag and lab coat"
    h1 "Is something matter?"

    scene lab loker_tutup

    you "Uhh, yeah. I think I left my calculator back at my dorm."
    h1 "And I thought you couldn't mess up more. Go pair up with a friend."
    "*time skips, reports are submitted"

    scene lab papan2

    h1 "Aaand, we're done. Thank you for coming to today's session."
    h1 "(MC), a word?"
    you "Am I in trouble?"
    h1 "For now, no. But you have taken quite the attention of other assistants."
    h1 "The assistants and practice chief have agreed to not go too rough on minor infractions, but looking at how your practice went, I think I have to warn you."
    h1 "Just make sure to come on time and come prepared. Capiche?"
    you "Understood."
    h1 "Good. Have a nice day, take care."
    you "*pack his things and left the lab"

    scene lab lorong_pulang

    you "\[Well that went fantastic. Getting myself in the assistant's sight. What a wonderful way to start my week.\]"
    you "*still walking, reminisces on his senpai"
    you "\[But she's a lowkey cutie, though.\]"

    "*time skip to the afternoon, MC has finished his class for the day and just arrived at his mix-gender dorm"

    scene kos bukakunci with Pause(1.5)

    scene kos tiduran

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
    you "\[What kind of psychopath chills their chips?\]"

    "*sound of a book dropped onto the floor"
    you "\[Huh?\]"

    scene kos sofa_far

    "*MC looks around to find the source, only to see FL1 laying on a sofa. "
    "She wears (insert clothes, don't wanna be held liable for the details), one hand inside a bag of chips, another hand just hanging out from the sofa."
    "Apparently, she fell asleep while reading a manga and got startled by it being dropped."
    "Reaching down to get the fallen manga, she sees MC by the fridge looking at her, dumbfounded."

    scene kos sofa_close

    you "Uhh, hi?"

    h1 "*squeals"
    h1"YOU DIDN'T SEE ANYTHING!"
    h1"*FL1 grabs her stuff and sprints to her room"

    scene kos lorong2

    you "\[...\]"
    you "\[The fuck just happened?\]"
    you "\[...\]"
    you "\[You know what? I'm not hungry.\]"

    scene dapur_kulkas ###########

    you "*returns the oreo and heads back to his room"
    
    scene pov_bangun_tidur

    "*time skip to the next day"
    "*alarms blaring, MC wakes up, still can't wrap his head around yesterday's incident"

    you "\[Did yesterday really happen? Was that really her?\]"
    you "*reminisces once more, fuckin simp"
    you "\[Why can't I stop thinking about her?\]"

    "*MC gets up and prepares for his day. Opening his door, our clumsy MC bumps into another person"
    
    scene kos bukapintu

    you "Ah, sorry. Didn't see you th-"
    "*Of course, it's FL1. They stare each other for quite some time before the silence got broken by MC's alarm. He reaches into his pocket and looks at his phone"
    you "\[Oh shit, only half an hour remaining before class. Better get going now.\]"

    scene kos gerbang

    "*MC peers up and looks at the exit to find FL1 already closing the dorm's gate."

    scene kos luar

    you "\[Gotta take a shot.\]"
    you "*MC pockets his phone and runs up to her"


    # *he asked as he caught up to her while walking backwards

    scene jalan motor2

    you "Uhh, hey! Hey! How are you this morning?" 
    h1 "*doesn't answer, eyes straight ahead"

    you "Uhh, you remember me, right? It's (insert MC's name), from the lab yesterda-"

    scene jalan mobil1

    h1 "*pulls MC closer to the side of the road since there's a car heading their way"

    scene jalan kosong1

    h1 "*spins MC around and tells him to walk correctly"

    scene jalan motor2

    h1 "Dummy, look where you're going when you walk."

    you "Oh shit." # *looks at the car that just passed
    you "Thanks."

    "*The campus is just a couple hundred meters ahead"

    you "So uhh, you're having a morning class, too?"
    "*FL1 doesn't answer"

    you "By the way, I really didn't expect us to live in the same dorm."
    "*FL1 gets flustered"

    scene kelas1

    you "*reminisces about FL1 back at the lab"
    you "*reminisces about the incident yesterday"
    you "\[She's damn cute, I get that. But I didn't expect that big of a gap moe.\]"
    you "*reminiscing how flustered she got when they walk together"
    "*suddenly, people around him are shuffling around and lecturer is picking up their stuff"

    you "\[Hold up, the class is finished?\]"
    you "\[But I haven't understood shit.\]"
    you "\[Welp, that's two extra hours of independent learning.\]"
    you "*stomach rumbles"
    you "\[Oh yeah, I haven't had breakfast.\]"

    you "*MC got up and went to cafetaria and orders his lunch"

    scene kantin ramai3

    you "*bumps into his friend"
    you "Oh hey, getting some chow, too?"

    friend "Hey! Yeah. Didn't understand anything at class, my brain was too busy asking whether I should buy ayam geprek or ayam penyet for lunch."

    you "Damn, same. By the way, got any seats yet?"
    you "*MC eyes around to find an empty seat and instantly saw FL1 sitting alone at the far end of the cafetaria"

    friend "Nah, I'm taking it away, gonna have a group work right after this."

    friend "*looks at MC, looks at where he's looking"
    friend "But I guess you have a seat in mind already."

    you "W-What? Oh, no, I guess you're misinterpreting something."

    friend "Yeah, sure, sure. You've been eyeing our lab assistant since she scolded you about the caliper."

    you "What? No! It's just that we happen to live in the same dorm."

    friend "Real shit? Well you're in luck, my friend."
    "*both of their orders are finished"
    friend "Welp, gotta get going. See you around!"
    friend "*leans to MC and whispers"
    friend "And good luck."

    you "Hey, come back here! I'm not done yet!"

    you "See ya later!"

    scene kantin meja

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
    you "Okay?"

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
    you "\[Nearly stepped on a landmine back there.\]"

    h1 "If that's the case." 
    h1 "*she stands up and packs her stuff"
    h1 "I'll be in your care. I hope we can get to know each other better."

    you "Y-yeah. Me, too."

    h1 "Well, I have to tutor a freshman calculus class in half an hour. It's good to see you, take care." 
    h1 "*leaves"

    scene kantin ramai2

    you "*looks at FL1 as she walks away"
    you "\[What a nice start.\]"

    # "*his phone vibrates rapidly, mafiki class' group chat is in chaos"
    # you "\[A fucking physics pop quiz in 30 minutes? Oh fuck.\]"

    # you "*books out to class to get some crash course"

    "*time skips to the next day"

    scene pov_bangun_tidur

    you "*wakes up startled"
    you "\[How come has the alarm not gone berserk yet? My sleep quality is getting a bit too suspicious.\]"

    #Hey, you. You're finally awake. *some 4th wall skyrim shit ?

    # you "\[Who the fuck is that?\]"

    you "*looks at phone for time"
    you "\[There's no way it's still 5 am. That was the best sleep I had in weeks. It must be 5 pm.\]"

    you "*looks out his windows. The sky is still dark"
    you "\[Well I'll be damned.\]"

    you "*turns off alarms"
    you "*reminisces on yesterday's encounter with senpai"
    you "\[Welp, better get ready and find her again.\]"

    "*time skip to lunch"

    scene kantin ramai3

    you "*orders his food and looks around the cafeteria"
    you "\[Where is she?\]"

    friend "Yo! Wanna join us?"
    you "\[Meh, I'll look for her at the lab after class.\]"

    you "Sure thing!"

    "*time skip to the afternoon, he went straight to the physics lab building and wait outside"

    scene lab datang
    
    you "\[Guess she's not here. Well, nice try, I guess.\]"

    scene lab pulang

    you "*heads back to his dorm"

    ##########################################################################################################################################

    scene kamar 

    you "*stomach rumbles"
    you "\[I literally just ate four hours ago.\]"
    you "*rumbles some more"
    you"\[Now, should I order a balanced meal like a responsible college student should or should I order diabetes incarnate?\]"
    "*spoiler alert, his intrusive thought wins"
    you "\[A wise person once said an apple a day keeps the doctor away. Unfortunately, I'm not a wise guy.\]"

    you "*orders a martabak manis"

    scene gofood alert
        
    "*his order arrives. He takes it and went to the lounge"

    scene sofa pov

    you "*sees FL1 on her phone"
    you "\[Time to shoot my shot\]"
    you "Fancy seeing you here."

    h1 "*kinda startled"
    h1 "Hey, didn't see you there."

    you "*sits down"
    you "Do you mind?" #*point to the sofa

    h1 "*pats the cushion"
    h1 "C'mere."

    you "Nice."
    you "*opens the martabak"
    you "Here, take some."

    h1 "Ah, thank you."

    you "*turns the TV on"

    "*they both sat and enjoy the sweet delicacy in silence"

    you "\[Gotta break the ice.\]"
    you "So, uhhh, what're you doing?"

    h1 "Oh, nothing. Just chilling and hunting for new mangas."

    you "\[Oh yeah, she's a closet weeb.\]"

    "Oh really? You really didn't look like someone who would indulge herself in reading man-"

    h1 "*throws a pillow at MC"
    h1 "Shut."

    you "Ow."

    h1 "Anyway, got any recommendations?"

    you "Meh, I don't know. Do you have any genre preferences in mind?"

    h1 "Anything with a lot of actions, especially the ones with some fantasy or magic or whatever you call it."

    you "Are isekais okay?"

    h1 "Preferably not, too cliche."

    you "Well shit. Fate?"

    h1 "I have watched, played, and read the franchise to oblivion."

    you "*kinda shocked pikachu face"
    you "\[H-hol up. Played? S-she couldn't have played the OG VN right?\]"

    h1 "Hey, are you okay? You look pretty shocked knowing I watch Fate."

    you "N-nothing. It's just that I rarely find someone that watches fate, too. By the way, which one is your favorite?"

    h1 "Surprisingly, Today's Menu for the Emiya Family. I think I got sick of all the misery sometime in the middle of reading Strange Fake."

    you "Very understandable."
    you "Have you tried Garden of Sinners?"

    h1 "Huh, didn't think of that. I've watched the anime, but I haven't really thought of reading the light novels. You know where to get them?"

    you "Uhh, maybe try the book store? I'd find a couple hidden gems here and there sometimes."

    h1 "*smiles"
    h1 "I'll try."

    you "Though if I were you, I'd just sail the high seas."

    h1 "Ah, a fellow corsair."

    you "*laughs"
    you "By the way, do you really love Fate that much?"

    h1 "Well, yes, at least when it comes to franchises. Shit slaps."
    h1 "I mean, where else can you find King Arthur portrayed as women. Mind the plural form."

    you "Shiiiiieeet. Coming to it, I'm quite surprised that FGO or Type-Moon has yet to make a Monty Python reference."

    h1 "Yeah, I really expected Artoria to ask something about swallows at least once."

    you "By the way, have you tried Tsukihime?"

    h1 "I have. As a matter of fact, I just finished the new one last week. Both routes."

    you "Damn."

    h1 "You got any anime or manga of your liking?"

    you "Do you know Ghost in the Shell?"

    h1 "The anime, right? Not the live action."

    you "Of fucking course, making a live action version of Ghost in the Shell was a
    mistake."

    h1 "I think that applies to a lot of anime."

    you "Anyway, there was this pretty old series called the Stand Alone Complex, made
    in the early 2000's or something. The first season was okay, but the second season
    was out of this world."

    h1 "Oh, does it have a great plot or something?"

    you "Nah, the overall plot is good, but not that remarkable. However, the mix
    between the subplots, soundtracks, and actions was something else. I haven't
    seen another anime that comes close."

    h1 "Action, you said?"

    you "Well, yeah. It's literally a cyberpunk police anime."

    h1 "I think I should give it a chance. I've watched the new one in Netflix, it was okay, I think?"

    h1  "But if it's about my actual favorite it's got to be those tearjerkers. You know, like Grave of the Firef-"

    you "Please don't elaborate further, I don't want to get PTSD at the moment."

    return