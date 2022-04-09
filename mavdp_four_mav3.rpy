init:
    default mavdp_four_store.mav3mood = 0

    default mavdp_four_store.newfood = None

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
            show maverick normal flip with dissolve
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
    if food == "coffee":
        c "Coffee for me. Reza ordered one too."
        Ad think b flip "So that will be two coffees?"
        Mv "Yes. Was that everything?"
        c "Yeah."
        show adine normal b with dissolve
    elif food == "eggs":
        c "Scrambled eggs and bacon. Reza ordered one too."
        Ad think b flip "So that will be two orders of scrambled eggs with bacon?"
        Mv "Yes. Was that everything?"
        c "Yeah."
        show adine normal b with dissolve
    elif food == "fish":
        c "Reza and I got the special, but I'm really not sure I--"
        Mv "Two specials, then."
        menu:
            "Can we have coffee in reserve?":
                $ renpy.pause (0.5)
                c "For after we finish the part about trying to remember."
                $ renpy.error("TODO: coffee in reserve")
            "Can we have scrambled eggs and bacon in reserve?":
                $ renpy.pause (0.5)
                c "For after we finish the part about trying to remember."
                $ renpy.error("TODO: scrambled eggs and bacon in reserve")
            "Alright, fine.":
                $ renpy.pause (0.5)
                $ mavdp_four_store.mav3mood += 1
        Ad think b flip "Are you actually planning to eat the special this time, or...?"
        Mv annoyed flip "Just bring them out, please."
        show adine annoyed b with dissolve


    Ad "Coming right up."
    $ renpy.pause (0.3)
    hide adine with easeoutleft
    $ renpy.pause (0.5)

    Mv normal flip "What next?"

    window show
    n "I recounted my conversation with Reza as best I could recall."
    n "I told Maverick about how Reza thought something was wrong with this place, that it matched our world too well, that it didn't make sense for it to be a different planet, much less a different dimension."
    if c3arcques1 == False:
        n "Remembering the blueprint I'd seen in the police archives, I told Maverick about how the corporation that created the blueprint had come from our world, too."
        n "He told me to stay on topic with the conversation, first."
    n "Then I recalled Reza complaining about being followed by Maverick some more, and finally how Reza had hushedly told me that he'd send a coded letter, but not even how to read it."
    window hide
    nvl clear

    $ renpy.pause(0.5)

    Mv nice flip "I see."
    c "Yeah."

    $ renpy.pause(0.5)

    show maverick normal flip with dissolve
    show adine normal b flip at left with easeinleft
    Ad "There you go."
    play sound "fx/dishes.wav"

    m "Maverick didn't acknowledge her, his attention focused solely on me."
    menu:
        "Thanks.":
            $ renpy.pause (0.5)
            $ mavdp_four_store.mav3mood += 1
            Ad "You're welcome."
        "[[Say nothing.]":
            $ renpy.pause (0.5)

    show adine normal b
    $ renpy.pause (0.3)
    hide adine with easeoutleft

    Mv "How did you figure out how to read the letter?"
    c "I saw lemons in the pantry and remembered a science class Reza and I once took together."
    $ renpy.pause (0.5)
    Mv "Let's move ahead. When you met Reza at the portal."

    window show
    n "I told Maverick about meeting Reza to send the generator home."
    n "Maverick pressed me for details, had me start over."
    window hide
    nvl clear
    window show
    n "I told Maverick about climbing the hill, and Reza complaining at me for not being early."
    n "Reza had said something more, about humanity not looking in the right place for alien life and pollution not lingering in the atmosphere like it did in our world."
    n "When I asked why we were meeting, he'd said it was for two reasons. The first was sending the generator home."
    n "The second reason for meeting was the threat."
    n "He'd said the threat had to do with {i}this place{/i}, that it would be gone soon, and that we shouldn't be here {i}when{/i} it happened."
    window hide
    $ renpy.pause (0.5)

    Mv "..."
    c "I have no idea what he meant."
    Mv "Neither do I."
    Mv "You're certain that's all he said before you spotted me?"
    c "He said it would take a while to explain. That was the last thing."

    if food == "coffee":
        m "I shifted my coffee mug, which was nearly empty at this point in the conversation. Maverick hadn't touched his."
    elif food == "eggs":
        m "I prodded some eggs across my plate, appetite waning with the weight of the subject matter. Maverick hadn't touched his food."
    elif food == "fish":
        m "I prodded some fish across my plate, the smell not doing any favors for my desire to eat it, especially with the weight of the subject matter."
        m "Maverick had stripped off and eaten a few small chunks of his, but otherwise focused on me with rapt attention."

    # Mv "Did you have any other contact with Reza? Anything at all?"
    # TODO: Maybe note the Chapter 2 Tatsu Avenue paper scrap, planted by the administrator?

    Mv "I'll have to take all of these notes back to the station and consider what we know."

    menu:
        "Sure. Hope it helps.":
            $ renpy.pause (0.5)
            play sound "fx/chair.wav"
            show maverick normal with dissolve
            $ renpy.pause (0.5)
            show maverick at left with ease
            # $ renpy.pause (0.3)
            hide maverick with easeoutleft
            stop music fadeout 2.0
            python in mavdp_four_store:
                maverickstatus = "neutral"
                mavscenesfinished = 2
                renpy.pause (1.0)
            scene black with dissolveslow
            jump ml_date_end
        "Stay?":
            if food == "coffee":
                c "You're not going to stay and finish your coffee?"
            else:
                c "You're not going to stay and finish your food?"


    $ renpy.error("TODO: Remainder of scnee.")