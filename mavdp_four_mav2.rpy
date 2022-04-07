init:
    image mavdp_forestcanopy = "bg/mavdp_forestcanopy.png"
    image mavdp_highbranchdown = "bg/mavdp_highbranchdown.png"

    default mavdp_four_store.called_for_help = 0
    default mavdp_four_store.tried_to_run = False

label mavdp_four_mav2:
    m "I picked up the phone, pulling out the scrap of paper on which I'd written down Maverick's number."
    c "(I might as well try, right?)"
    play sound "fx/phonepickup.ogg"
    $ renpy.pause(0.8)
    m "Before I could say anything, Maverick spoke."
    Mv normal b "The forest behind your apartment. Just after sunset."
    play sound "fx/phonesetdown.ogg"
    $ renpy.pause(0.8)
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
    play soundloop "fx/steps/rough_gravel.wav"
    scene forestx at Pan((0, 360), (0, 0), 8.0) with dissolveslow
    $ renpy.pause(3.0)
    m "I wasn't clear on exactly how far into the forest to walk, nor what would await me when I got there."
    $ renpy.pause(1.0)
    stop soundloop fadeout 0.5
    stop music fadeout 5.0
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
    play music "mx/mavdp_deep_judgement.ogg" fadein 4.0
    Mv "Will you at least tell me your end-game?"
    Mv "What was important enough about your information to you, that you would turn on us and steal the generators you wanted, rather than accept the deal we had?"
    menu:
        "I don't know.":
            c "If I knew, I'd tell you. But I really don't."
            $ renpy.pause(0.5)
        "Reza's doing this on his own.":
            $ renpy.pause(0.5)
    
    show maverick annoyed dk with dissolve

    $ renpy.pause (0.5)
    Mv "Even now..."

    $ renpy.pause (0.8)
    Mv normal dk "All I want is to know. That's why I set this up."
    Mv "That's why I'm letting you do this."
    Mv "What possible reason could you have for not telling me {i}now{/i}?"
    c "Because I'm telling the truth."

    $ renpy.pause (0.8)

    Mv annoyed dk "You're telling me the truth you want me to hear."
    Mv irritated dk "Why? Why lie now?"
    Mv annoyed dk "I'm not trying to run. Reza doesn't have to sneak up with that weapon of his."

    menu:
        "Reza? What are you talking about?":
            $ renpy.pause(0.5)
            Mv angry dk "Don't pretend you're not working with him."
            c "I'm not!"
            jump mavdp_four_mav2_workingwithreza
        "You're not listening to me.":
            $ renpy.pause(0.5)
            c "I'm not lying. It's the truth I want you to hear because it's {i}the truth{/i}."
            label mavdp_four_mav2_workingwithreza:
            Mv angry dk "Reza was working with you, colluding with you -- sent you the secret message to meet him at the portal."
            Mv annoyed dk "When he hurt me with his weapon, he told you to run."
            Mv angry dk "I barely caught you."
            c "Because I wasn't trying to run!"
            stop music fadeout 1.0
            play sound "fx/snarl.ogg"
            Mv rage dk "Stop treating me like a fool!"
        "[[Go home.]":
            m "It was clear Maverick wasn't going to change his mind, no matter what I said."
            m "His thought that Reza might be sneaking up was evidence of that."
            c "I'm not lying. If you're not going to listen, that's really not my problem."
            m "I took a few steps back, turning to go."
            stop music fadeout 1.0
            play sound "fx/snarl.ogg"
            Mv rage dk "Don't walk away from me!"

    play sound "fx/wooshimpact.wav"
    show maverick rage dk:
        zoom 1.0
        linear 0.8 zoom 2.0
    with None
    $ renpy.pause(0.8)
    scene black with hpunch
    m "Before I could react, Maverick pounced at me forepaws-first."

    scene mavdp_forestcanopy at Pan((200, 300), (0, 0), 2.0) with dissolveslow
    $ renpy.pause(1.0)

    show maverick angry dk:
        zoom 1.2
        align (0.5, 0.0)
        pos (0.5, 0.0)
        ease 0.5 ypos 0.3
    with None

    m "Dazed, I came to my senses on my back, Maverick standing on my chest."

    Mv angry dk "Enough of this."
    Mv rage dk "Cry for help! Bring Reza out here and finish me off!"

    c "(C-Can't breathe!)"
    m "I batted weakly at his forepaws, trying to get him to take some weight off."
    show maverick angry dk with dissolve
    show maverick at Transform(ypos=0.2) with ease
    m "Thankfully, he moved his paws to either side of me, allowing me to get some full breaths in."

    label mavdp_four_mav2_call_for_help_menu:
    show maverick angry dk with dissolve
    menu:
        "[[Call for help.]" if mavdp_four_store.called_for_help == 0:
            $ mavdp_four_store.called_for_help = 1
            $ renpy.pause(0.5)
            c "S-Someone help! Please!"
            if mavdp_four_store.tried_to_run == True:
                m "My chest and throat hurt, voice unable to carry even a dozen yards through the deafening forest canopy."
            else:
                m "My chest hurt, voice not nearly loud enough to reach through the deafening canopy."
            $ renpy.pause(0.5)
            Mv "..."
            $ renpy.pause(0.5)
            m "... Nobody came."
            jump mavdp_four_mav2_call_for_help_menu
        "[[Call for help.]" if mavdp_four_store.called_for_help == 1:
            $ mavdp_four_store.called_for_help = 2
            $ renpy.pause(0.5)
            c "A-Anyone? P-Please..."
            $ renpy.pause(0.8)
            Mv "..."
            jump mavdp_four_mav2_call_for_help_menu
        "[[Try to run.]" if mavdp_four_store.called_for_help < 1 and mavdp_four_store.tried_to_run == False:
            $ mavdp_four_store.tried_to_run = True
            play sound "fx/growl.ogg"
            show maverick rage dk with dissolve
            $ renpy.pause(0.8)
            m "I barely shuffled a few inches backward before his forepaws were back on my chest and, this time, neck, pressing down with more vehemence."
            m "I grabbed his leg, struggling to hold up his weight as my windpipe strained against the crushing force."
            show maverick angry dk with dissolve
            $ renpy.pause(0.8)
            m "After a few seconds, he let off. The threat, however, was clear."
            jump mavdp_four_mav2_call_for_help_menu
        "[[Plead.]":
            c "Maverick, please. I'm not working with Reza. He's not here."
            if mavdp_four_store.called_for_help < 1:
                Mv rage dk "Call for him!"
                jump mavdp_four_mav2_call_for_help_menu
            Mv rage dk "Where is he?!{w=0.8}{nw}"
            c "I don't know! {w}Just let me up! Please!"
        "[[Threaten.]":
            c "You just attacked an ambassador unprovoked, Maverick. You'll pay for this..."
            if mavdp_four_store.called_for_help < 1:
                Mv angry dk "As if that will matter when you have him kill me."
                Mv rage dk "Call for him!"
                jump mavdp_four_mav2_call_for_help_menu
            c "Now let me up."

    show maverick despair dk with dissolveslow
    m "It finally seemed to dawn on Maverick what he'd done: that he'd attacked me, unprovoked, out in the woods, without proof."
    show maverick lost dk with dissolve
    m "Reza wasn't there to kill him, like he expected, because I wasn't working with Reza."
    show maverick angry dk with dissolve
    m "It was too much to hope that last point made it through to him."
    play music "mx/mavdp_dire_politics.ogg" fadein 2.0

    show maverick angry dk:
        linear 0.5 ypos -2.0 zoom 4.0
    with None
    scene black with dissolvemed
    c "M-Maverick!"

    stop music fadeout 2.0
    play sound "fx/wooshes.ogg"
    m "Grabbing me to his chest, Maverick took to the sky, hauling me nearly straight up."
    c "What are you doing? Mav--"
    play sound "fx/door/creaky.wav"
    $ renpy.pause(0.3)
    scene mavdp_highbranchdown:
        zoom 1.1
        align (0.5, 0.0)
        pos (0.5, 0)
        parallel:
            ease 0.8 xpos 0.51
            ease 0.8 xpos 0.49
            repeat
        parallel:
            linear 3.0 ypos -160
            block:
                ease 0.6 ypos -100
                ease 0.8 ypos -160
                repeat
    with dissolvemed
    $ renpy.pause(1.5)
    m "Maverick alighted on a high branch, dumping me on thinner wood in front of him. The whole tree creaked under our combined weight."

    c "(I-If I fell from up here, I'd die!)"

    Mv normal dk "Tell me everything you know."

    c "I don't know anything--"

    Mv rage dk "{size=+6}Everything!{/size}"

    c "I-- I came as an ambassador to oversee the trade deal!"
    c "Our PDAs for your generators!"
    c "That's it!"

    Mv angry dk "And the murders? The thefts?"

    c "I don't know!"

    Mv angry dk "What you and Reza talked about? All of it!"

    c "He was being vague, saying we were in danger here! I don't know what he meant!"
    $ renpy.pause (0.5)
    c "Maverick, {i}please{/i}!"

    stop music fadeout 10.0

    $ renpy.pause (0.8)

    Mv lost dk "..."
    $ renpy.pause (0.5)
    Mv nice lost dk "I'm going to pick you up and take us down."
    menu:
        "Please do, asshole!":
            $ renpy.pause (0.5)
            Mv lost dk "..."
        "Th-Thank you!":
            $ renpy.pause (0.5)
    play sound "fx/undress.ogg"
    scene black with dissolvemed
    $ renpy.pause (0.5)
    play sound "fx/woosh2.ogg"
    queue sound "fx/wooshimpact.ogg"
    $ renpy.pause(2.0)
    m "The descent from the tree was fast, and clearly a little less controlled than Maverick intended."
    scene forestx
    show maverick lost dk
    with dissolveslow
    m "Nothing felt broken, though, as I picked myself up off the ground."

    start music "mx/mavdp_deep_judgement.ogg"
    $ renpy.pause(0.5)

    Mv "I..."
    Mv despair dk "I have no excuse for my actions tonight, [player_name]."
    Mv lost dk "I was convinced in your collusion with Reza, and thought any means of getting a confession would be justified."
    Mv lost dk "I was wrong."

    menu:
        "Seriously, fuck you.":
            c "You nearly killed me like three times, gave me a hell of a lot of laundry to do tonight, and for what?"
            c "Exactly what I've been telling you this {i}whole{/i} time."
            c "Bryce is going to be hearing about this."
            Mv lost dk "..."
            c "Which way is my apartment?"
            show maverick lost dk at Position(xpos=0.49) with ease
            play sound "fx/steps/rough_gravel.wav"
            scene black with dissolve
            stop music fadeout 5.0
            $ renpy.pause(0.8)
            m "Without another word, I left him in the woods, already planning what I'd say to Bryce on the phone."
            $ mavdp_four_store.maverickstatus = "reported"
            jump _mod_fixjmp
        "Yeah. You were.":
            c "This... Maverick, this was too much."
            $ renpy.pause (0.5)
            c "This {i}hurt.{/i}"
            c "I need some time to think."
            c "Are you going to jump on me if I try to leave again?"
            $ renpy.pause (0.8)
            Mv "No."
            $ renpy.pause (0.5)
            play sound "fx/steps/rough_gravel.wav"
            scene black with dissolveslow
            $ renpy.pause(0.5)
            Mv "{size=-4}I'm sorry.{/size}"
            $ mavdp_four_store.maverickstatus = "neutral"
            stop music fadeout 1.0
            $ renpy.pause(0.5)
            jump _mod_fixjmp
        "I understand.":
            c "You... I mean, strange people from another world? People turning up dead? In your shoes, I probably would have had the same reaction."
            $ renpy.pause (0.5)
            Mv lost dk "It doesn't excuse my actions."
            Mv nice lost dk "This whole time, you were telling me what you knew."
            Mv lost dk "You were sharing your information. I was too foolish to listen."

            $ renpy.pause(0.8)
            c "You're not wrong. But I don't blame you."
            c "I don't want to lose this chance to work together on the investigation over this."

            Mv nice dk "Even after I assaulted you? You would seek to be my friend?"

            c "I don't know. But I'm not slamming the door over this misunderstanding."
            m "I winced, chest throbbing from where he'd pounced me."
            c "Would you... do you mind helping me home? I'm, uh, not sure if I can make it."

            stop music fadeout 5.0
            scene black with dissolveslow
            $ renpy.pause(0.5)
            m "Wordlessly, Maverick came to my aid, helping me limp the moderate distance back to the apartment."
            $ mavdp_four_store.maverickstatus = "good"
            jump _mod_fixjmp

    $ renpy.error("TODO: Remainder of the scene.")