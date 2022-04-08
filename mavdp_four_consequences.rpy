label mavdp_four_c3investigation_patrol_fix:
    stop music fadeout 2.0
    Br brow b "Maverick was guarding last night. But he didn't report anything amiss."
    Sb "Maybe only one night guard isn't enough."
    Br stern b "But we don't have the people to spare, while still investigating anything else."
    play music "mx/judgement.ogg" fadein 2.0
    Sb "So then Reza must have managed to sneak past Maverick."
    jump mavdp_four_c3investigation_patrol_fix_end

label mavdp_four_c3investigation_patrol_fix2:
    Br "Or maybe we're looking at this from the wrong angle. It might not be Reza at all. Plenty of dragons could have managed to sneak up too. It doesn't necessarily have anything to do with Reza or humanity."
    jump mavdp_four_c3investigation_patrol_fix2_end


label mavdp_four_bryce3_cancelled:
    $ renpy.pause (1.0)
    play sound "fx/phonering.ogg"
    scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolveslow
    play sound "fx/phonepickup.ogg"
    c "Uh, hello?"
    Br stern "Hey, [player_name]. It's Bryce."
    c "Hey Bryce. That thing at the beach you told me about is still in another couple hours, right?"
    Br stern "Yeah. About that."
    c "Huh?"
    Br brow "Normally Maverick would be there. After what he did to you, though..."
    c "Forget it, then. I'm not going."
    Br stern "Don't worry about it. Neither am I. Or anyone else. It's cancelled."
    Br "Nobody really wanted to go with everything going on."
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


label mavdp_four_c4meeting:
    label .nowherenear:
        Br stern b "You know you're not supposed to be anywhere near [player_name]."
        Br stern b "We're also quite busy here. What is this about?"
        jump mavdp_four_c4meeting.nowherenear_end

    label .ontheteam:
        play music "mx/intrigue.ogg"
        Br brow b "Maverick? What have you got."
        jump mavdp_four_c4meeting.know_where_reza_is

    label .forgot_badge:
        Br "Hence forgetting your badge. Alright."
        jump mavdp_four_c4meeting.forgot_badge_return

    label .going:
        if mavdp_four_store.maverickstatus == "reported":
            Br "Well, Maverick, I'd like to have you there, but right now you need to get the heck away from [player_name] and back on your 'sick leave'."
            Mv "I understand."
            $ renpy.pause (0.3)
            show maverick normal
            $ renpy.pause (0.3)
            hide maverick with easeoutleft
            $ renpy.pause (0.3)
            play sound "fx/door/doorclose.ogg"
            $ renpy.pause (0.8)
            jump mavdp_four_c4meeting_how_about_player
        else:
            Br "Maverick, you okay with working some off-hours?"
            Mv "Of course."
            jump mavdp_four_c4meeting_how_about_player

    label .after_you:
        if mavdp_four_store.maverickstatus != "reported":
            Br "And Maverick: Good job."
            Mv "Thanks, Chief."

        python:
            if mavdp_four_store.maverickstatus in ["neutral","good"]:
                brycegoodending = True

        show bryce stern b flip
        $ renpy.pause (0.3)
        hide bryce with easeoutright
        show sebastian normal b flip
        $ renpy.pause (0.3)
        hide sebastian with easeoutright
        $ renpy.pause (0.5)
        if mavdp_four_store.maverickstatus != "reported:":
            $ renpy.pause (0.3)
            show maverick normal
            stop music fadeout 2.0
            $ renpy.pause (0.3)
            hide maverick with easeoutleft
            $ renpy.pause (0.3)

        play sound "fx/door/doorclose.ogg"
        jump mavdp_four_c4meeting_after_you_end

label mavdp_four_c4farmhouse:
    label .mayberan:
        Br "Couldn't have. Maverick would have spotted him from the air."
        jump mavdp_four_c4farmhouse.mayberan_return