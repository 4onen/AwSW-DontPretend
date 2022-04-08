init:
    image maverick rage mavdp_four_dk = im.Recolor("cr/maverick_rage.png", 70, 70, 100, 255)
    image mavdp_forestcanopy = im.Recolor("bg/mavdp_forestcanopy.png", 70, 70, 100, 255)
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
            Mv rage mavdp_four_dk "Stop treating me like a fool!"
        "[[Go home.]":
            m "It was clear Maverick wasn't going to change his mind, no matter what I said."
            m "His thought that Reza might be sneaking up was evidence of that."
            c "I'm not lying. If you're not going to listen, that's really not my problem."
            m "I took a few steps back, turning to go."
            stop music fadeout 1.0
            play sound "fx/snarl.ogg"
            Mv rage mavdp_four_dk "Don't walk away from me!"

    play sound "fx/wooshimpact.wav"
    show maverick rage mavdp_four_dk:
        zoom 1.0
        linear 0.8 zoom 2.0 ypos 1.8 xpos 0.7
    with None
    $ renpy.pause(0.8)
    scene black with hpunch
    m "Before I could react, Maverick pounced at me forepaws-first."

    scene mavdp_forestcanopy at Pan((0, 200), (0, 0), 4.0) with dissolveslow
    $ renpy.pause(1.0)

    show maverick angry dk:
        zoom 1.4
        align (0.5, 0.0)
        pos (0.7, 1.0)
        ease 1.5 ypos 0.6
    with None

    m "Dazed, I came to my senses on my back, Maverick standing on my chest."

    Mv angry dk "Enough of this."
    Mv rage mavdp_four_dk "Cry for help! Bring Reza out here and finish me off!"

    c "(C-Can't breathe!)"
    m "I batted weakly at his forepaws, trying to get him to take some weight off."
    show maverick angry dk with dissolve
    show maverick at Transform(ypos=0.63) with ease
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
            m "... but nobody came."
            jump mavdp_four_mav2_call_for_help_menu
        "[[Call for help.]" if mavdp_four_store.called_for_help == 1:
            $ mavdp_four_store.called_for_help = 2
            $ renpy.pause(0.5)
            c "{size=-2}A-Anyone? P-Please...{/size}"
            $ renpy.pause(0.8)
            Mv "..."
            jump mavdp_four_mav2_call_for_help_menu
        "[[Blubber.]" if mavdp_four_store.called_for_help == 2:
            $ mavdp_four_store.called_for_help = 3
            $ renpy.pause(0.5)
            c "{size=-8}I-I don't want to die. I don't w-want to die.{/size}"
            $ renpy.pause(0.5)
            Mv irritated dk "..."
            Mv annoyed dk "..."
            jump mavdp_four_mav2_call_for_help_menu
        "[[Blubber.]" if mavdp_four_store.called_for_help == 3:
            $ mavdp_four_store.called_for_help = 4
            show maverick irritated dk with dissolve
            $ renpy.pause(0.5)
            c "{size=-8}P-Please don't kill me. I don't want to... I don't want to...{/size}"
            $ renpy.pause(0.5)
            Mv annoyed dk "..."
            Mv rage mavdp_four_dk "{size=+2}Just come out here and finish this!{/size}"
            jump mavdp_four_mav2_call_for_help_menu
        "[[Blubber.]" if mavdp_four_store.called_for_help == 4:
            $ mavdp_four_store.called_for_help = 5
            show maverick irritated dk with dissolve
            $ renpy.pause(0.5)
            c "{size=-8}P-Please--{/size}"
            play sound ["fx/snarl.ogg","fx/breathing.ogg"]
            Mv rage mavdp_four_dk "{size=+4}I am going to {i}kill{/i} [player_name]!{/size}"
            $ renpy.pause(3.0)
            m "... but nobody came."
        "[[Try to run.]" if mavdp_four_store.called_for_help < 1 and mavdp_four_store.tried_to_run == False:
            $ mavdp_four_store.tried_to_run = True
            play sound "fx/growl.ogg"
            show maverick rage mavdp_four_dk with dissolve
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
                Mv rage mavdp_four_dk "Call for him!"
                jump mavdp_four_mav2_call_for_help_menu
            Mv rage mavdp_four_dk "Where is he?!"
            c "I don't know! {w}Just let me up! Please!"
        "[[Threaten.]":
            c "You just attacked an ambassador unprovoked, Maverick. You'll pay for this..."
            if mavdp_four_store.called_for_help < 1:
                Mv angry dk "As if that will matter when you have him kill me."
                Mv rage mavdp_four_dk "Call for him!"
                jump mavdp_four_mav2_call_for_help_menu
            c "Now let me up."

    show maverick despair dk with dissolveslow
    m "It finally seemed to dawn on Maverick what he'd done: that he'd attacked me, unprovoked, out in the woods, without proof."
    show maverick lost dk with dissolve
    m "Reza wasn't there to kill him, like he expected, because I wasn't working with Reza."
    play music "mx/mavdp_dire_politics.ogg" fadein 2.0
    show maverick angry dk with dissolve
    m "It was too much to hope that last point made it through to him."

    play sound "fx/liftbody.ogg"
    show maverick angry dk:
        linear 0.5 ypos 0.0 zoom 2.5
    with None
    scene black with dissolvemed
    stop sound fadeout 0.5
    c "M-Maverick!"

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
            ease 1.6 xpos 0.501
            ease 1.6 xpos 0.499
            repeat
        parallel:
            linear 3.0 ypos -160
            block:
                ease 1.6 ypos -150
                ease 1.8 ypos -160
                repeat
    with dissolvemed
    $ renpy.pause(1.5)
    m "Maverick alighted on a high branch, dumping me on thinner wood in front of him. The whole tree creaked under our combined weight."

    c "(I-If I fell from up here, I'd die!)"

    Mv normal dk "Tell me everything you know."

    c "I don't know anything--"

    play sound "fx/snarl.ogg"
    Mv rage mavdp_four_dk "{size=+8}Everything!{/size}"
    stop sound fadeout 0.5

    c "I-- I came as an ambassador to oversee the trade deal!"
    c "Our PDAs for your generators! {w=1.0}That's it!"

    Mv angry dk "And the murders? The thefts?"

    c "I don't know!"

    Mv angry dk "What you and Reza talked about? All of it!"

    c "He was being vague, saying we were in danger here! I don't know what he meant!"
    $ renpy.pause (0.5)
    c "Maverick, {i}please{/i}!"


    $ renpy.pause (0.8)
    m "A few moments of silence passed, with only the swaying of the branch and the shuddering of my arms as I held on letting me know time was passing."
    if mavdp_four_store.has_side_images():
        Mv angry dk "..."
        $ renpy.pause (0.8)
        Mv irritated dk "..."
        $ renpy.pause (0.8)
    Mv lost dk "I..."
    stop music fadeout 10.0
    $ renpy.pause (0.8)
    Mv nice lost dk "I'm going to pick you up and take us down."
    $ renpy.pause (0.5)
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
    queue sound "fx/wooshimpact.wav"
    $ renpy.pause(2.0)
    m "The descent from the tree was fast, and clearly a little less controlled than Maverick intended."
    scene forestx at top
    show maverick lost dk
    with dissolveslow
    m "Nothing felt broken, though, as I picked myself up off the ground."

    play music "mx/mavdp_deep_judgement.ogg"
    $ renpy.pause(0.5)

    Mv "I..."
    Mv lost dk "I have no excuse for my actions tonight, [player_name]."
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
            $ renpy.pause(0.8)
            play sound "fx/steps/rough_gravel.wav"
            scene black with dissolve
            stop music fadeout 5.0
            $ renpy.pause(0.8)
            m "Without another word, I left him in the woods, already planning what I'd say to Bryce on the phone."
            stop sound fadeout 0.5
            $ mavdp_four_store.maverickstatus = "reported"
            $ mavdp_four_store.mavscenesfinished = 1
            jump ml_date_end
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
            Mv "{size=-8}I'm sorry.{/size}"
            $ mavdp_four_store.maverickstatus = "neutral"
            $ mavdp_four_store.mavscenesfinished = 1
            stop music fadeout 1.0
            stop sound fadeout 1.0
            $ renpy.pause(0.5)
            jump ml_date_end
        "I understand, though.":
            c "You... I mean, strange people from another world? People turning up dead? In your shoes, I probably would have had the same reaction."
            $ renpy.pause (0.5)
            Mv lost dk "It doesn't excuse my actions."
            Mv nice lost dk "This whole time, you were telling me what you knew."
            Mv lost dk "You were sharing your information. I was too foolish to listen."

            $ renpy.pause(0.8)
            c "You're not wrong. But I don't blame you."
            c "I don't want to lose our ability to work together on the investigation over this."
            c "We need to find Reza before anyone else gets hurt. That means every advantage we can get."
            c "Communicating openly is an advantage."

            $ renpy.pause(0.5)

            Mv nice dk "Even after I assaulted you? Threatened you? You could stand being around me?"

            $ renpy.pause(0.5)

            c "I don't know. But I'm not slamming the door over this misunderstanding."
            m "I winced, chest throbbing from where he'd pounced me."
            c "Would you... do you mind helping me home? I'm, uh, not sure if I can make it."

            stop music fadeout 5.0
            scene black with dissolveslow
            $ renpy.pause(0.5)
            m "Wordlessly, Maverick came to my aid, helping me limp the moderate distance back to the apartment."
            $ mavdp_four_store.maverickstatus = "good"
            $ mavdp_four_store.mavscenesfinished = 1
            jump ml_date_end