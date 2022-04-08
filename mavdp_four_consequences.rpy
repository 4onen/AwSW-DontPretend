label mavdp_four_bryce3_cancelled:
    $ renpy.pause (1.0)
    scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed
    play sound "fx/phonepickup.ogg"
    c "Uh, hello?"
    Br stern "Hey, [player_name]. It's Bryce."
    c "Hey Bryce. That thing at the beach you told me about is still in another couple hours, right?"
    Br stern "Yeah. About that."
    c "Huh?"
    Br brow "Normally Maverick would be there. After what he did to you, though..."
    c "Forget it, then. I'm not going."
    Br stern "Don't worry about it. Neither am I. It's cancelled."
    c "Oh."
    Br stern "Anyway. Since I have the evening back, I'm going to focus on getting through paperwork."
    Br "We'll have to catch up another time."
    c "Ah. Thanks for letting me know."
    Br "Yeah. I'll see you around."
    play sound "fx/phonesetdown.ogg"
    python: 
        brycestatus = "neutral"
        brycescenesfinished = 3
        renpy.pause(1.0)
    jump _mod_fixjmp

label mavdp_four_bryce3_report:
    # c "I-I can't. I--"
    $ renpy.pause (1.0)
    Br brow "Really?"
    Br stern "[player_name], I'm just asking you to be civil."
    Br brow "Is everything okay?"
    c "I-I can't be around him."
    Br stern "What's going on?"
    menu:
        "Tell him.":
            stop music fadeout 2.0
            python:
                mavdp_four_store.maverickstatus = "reported"
                brycestatus = "neutral"
                brycescenesfinished = 3
                renpy.pause(0.5)
            c "Maverick attacked me in the woods, tried to make me confess to colluding with Reza."
            c "He dangled me from a tree and told me he'd kill me."
            $ renpy.pause (0.8)
            Br "..."
            $ renpy.pause (0.5)
            Br "I see."
            c "I'm sorry. I- I thought if I just avoided him..."
            Br brow "No, that's not the right answer here. You should have come to me with this sooner."
            Br stern "Go home for tonight. I'll sort this out."
            c "..."
            $ renpy.pause (0.5)
            scene black with dissolveslow
            $ renpy.pause (0.5)
        "Leave.":
            Br stern "[player_name]?"
            stop music fadeout 2.0
            scene black with dissolve
            python:
                renpy.pause(0.5)
                brycestatus = "bad"
                brycescenesfinished = 3
            m "Without another word, I turned and left."
    jump _mod_fixjmp

