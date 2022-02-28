label mavdp_four_mav2:
    m "I picked up the phone, pulling out the scrap of paper on which I'd written down Maverick's number."
    c "(I might as well try, right?)"
    # TODO: Dialing noises or something. This silence sucks.
    $ renpy.pause(0.5)
    m "Before I could say anything, Maverick spoke."
    Mv normal b "The forest behind your home. Just after sunset."
    m "Then he hung up."
    c "(Nothing to do but wait, then.)"
    $ renpy.pause(1.0)
    # TODO: Describe waiting activities.
    scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolveslow
    stop music fadeout 3.0
    $ renpy.pause(1.0)
    c "(Time to go.)"
    # TODO: Put away waiting activity.
    scene black with dissolvemed
    play music "mx/amb/night.ogg" fadein 5.0
    play sound "fx/steps/rough_gravel.wav"
    scene forestx at Pan((0, 360), (0, 0), 10.0) with dissolveslow
    m "I wasn't clear on exactly how far into the forest to walk, nor what would await me when I got there."
    show maverick normal dk with dissolvemed
    m "Well into the woods, I spotted Maverick, his monochrome grey hues blending well with the darkness of the moonlit forest."
    Mv "..."
    Mv "You came."
    m "He seemed more defeated by my presence, than excited that I was trying to answer his questions."
    menu:
        "You asked me to.":
            $ renpy.pause(0.5)
            Mv "I did. And I knew what the result would be."
        "[[Say nothing.]":
            $ renpy.pause(0.8)
    Mv "Will you at least tell me your end-game?"
    Mv "What was important enough about your information to you, that you would turn on us and steal the generators you wanted, rather than accept the deal we had?"
    $ renpy.error("TODO: Remainder of the scene.")