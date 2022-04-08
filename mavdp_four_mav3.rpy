init:
    default mavdp_four_store.mav3mood = 0

label mavdp_four_mav3:
    scene black with fade
    $ renpy.pause (1.0)
    scene cafe with dissolveslow

    nvl clear
    window show
    n "When I reached out to Maverick, to ask for any way I could help with the investigation, he directed me to meet him at the cafe."
    n "Though I wasn't sure what kinds of investigation we'd be able to perform there, any way I could help him find Reza was important."
    show maverick normal flip with dissolve
    n "He stood near the door, waiting for me."
    window hide
    nvl clear

    play music "mx/jazzy.ogg" fadein 3.0

    c "Hey, Maverick."
    Mv nice flip "[player_name]."

    $ renpy.pause (0.5)
    show maverick normal with dissolve
    $ renpy.pause (0.3)
    show maverick normal at Position(xpos=0.45) with ease
    play sound "fx/chair.wav"
    $ renpy.pause (0.3)
    show maverick normal flip with dissolve
    m "Maverick led us to the table where Reza and I had sat, many days ago. He squeezed in on Reza's side."
    play sound "fx/chair.wav"
    m "I joined him on the other side."

    $ renpy.pause (0.5)

    c "So, how can I help?"
    Mv "When you and Reza sat here, I wasn't able to overhear many parts of your conversation."
    Mv "I was hoping you'd be able to recall exactly what he said. Perhaps there's something we can make a connection with now that you couldn't before."
    menu:
        "Sure, I can try.":
            $ renpy.pause (0.5)
            $ mavdp_four_store.mav3mood += 1
            show maverick nice flip with dissolve
        "Are you sure you don't just want time with me?":
            $ renpy.pause (0.5)
            $ mavdp_four_store.mav3mood -= 2
            show maverick angry flip with dissolve
            Mv "Don't make light of this investigation."
            c "Alright, alright, sorry."
        "My memory isn't magical.":
            $ renpy.pause (0.5)
            $ mavdp_four_store.mav3mood -= 1
            show maverick annoyed flip with dissolve
            Mv "I'm only asking you to try."

    $ renpy.pause (0.3)

    show adine normal b flip at left with easeinleft
    if adinestatus == "bad":
        Ad annoyed b flip "Oh. You."
    else:
        Ad normal b flip "Hello, [player_name]!"

    m "Noticing Maverick, her face fell."
    Ad think b flip "Is this some kind of police business?"

    c "Yes and no."
    Mv "Order what you ordered when you were here."
    c "Ah..."

    $ renpy.error("TODO: Remainder of scnee.")