init python in mavdp_four_store:
    c1investigation_said = "aggressive"
    bryce1_said = False

label mavdp_four_c1aggravation:
    menu:
        "What's your problem?":
            $ mavdp_four_store.c1investigation_said = "aggressive"
            jump mavdp_four_c1aggravation_return
        "I'm sorry.":
            $ mavdp_four_store.c1investigation_said = "sorry"
            c "I'm sorry. I'm not trying to belittle you. I'm as stressed by this as you are."
            c "And we're not sitting idly by. We're trying to find him, just like you."
            jump mavdp_four_c1aggravation_dontcompare
        "[[Say nothing.]":
            $ mavdp_four_store.c1investigation_said = "nothing"
            jump mavdp_four_c1aggravation_end

label mavdp_four_bryce1_otherreason:
    Br stern "I see."
    c "No, no. This isn't that serious."
    Br brow "Everything going on right now is serious, and you and I both know Maverick is intent on putting himself in the middle of it."
    Br stern "But fine. What's your question?"
    c "Why is he on sick leave?"
    Br brow "You're kidding, right? You saw Reza injure him."
    c "You also saw that he doesn't care about that wound. He's out looking anyway."
    c "You were threatening to take disciplinary action against him, and he was making pretty clear he'd keep looking despite that."
    Br stern "I'm not locking him up unless he does something truly stupid. But he needed to understand the stakes of this situation."
    c "I watched Reza shoot him. Can't get it out of my head, really."
    c "I think he understands what's going on."
    show bryce brow with dissolve
    $ renpy.pause(1.0)
    c "Wouldn't it be better to share information with him, about what I'm doing and about what you're doing, and in return get information about what he's doing?"
    c "It seems a lot better for everybody if we all work together to find Reza and sort this out."
    $ renpy.pause(1.0)
    Br "You're telling me to reinstate him."
    c "I'm not telling you to in any official sense. Obviously you know him better than I do, and you know police work better than I do."
    c "I'm just suggesting: think about it. And letting you know that I'm not opposed, and that I don't take his tackling of me after he was shot as seriously as you do."
    $ mavdp_four_store.bryce1_said = True
    $ renpy.pause(0.8)
    c "Sorry, that was a lot. Want to get back to our game?"
    show bryce normal with dissolve
    $ renpy.pause(0.3)
    Br normal "Heck yes, I do!"
    jump mavdp_four_bryce1_otherreason_end

label mavdp_four_c2aggravation:
    with dissolve # Missing from base game
    Br stern b "Maverick, wait."
    Mv angry "Why? So you can threaten me off the trail some more?"
    $ renpy.pause (0.3)
    hide maverick with easeoutleft
    show bryce at left with ease
    m "As Maverick left, Bryce ducked under the police line to follow."
    hide bryce with easeoutleft
    $ renpy.pause (1.2)
    Sb drop b "That's hard to see."
    c "Hm?"
    Sb disapproval b "Maverick and Bryce have known each other for a long time. Been through some serious trouble together."
    menu:
        "I hope Maverick isn't dragging Bryce to any conclusions.":
            Sb drop b "This isn't their first tough investigation, nor their first with personal connections."
            Sb disapproval b "I'm sure Bryce is being professional about it."
            c "But not Maverick."
        "I think they'll patch things up.":
            Sb "Why?"
            c "I asked Bryce to take Maverick off sick leave."
            $ renpy.pause (0.5)
            Sb drop b "If you think that's a good idea."
            $ renpy.pause (0.5)
            show sebastian normal b with dissolve
        "[[Say nothing.]":
            pass
    $ renpy.pause (0.9)
    hide sebastian with easeoutright
    show sebastian normal b flip at left with easeinleft
    show bryce stern b at right with easeinright
    Br "I've talked to him. If you see him at the station later, know I'm sanctioning it."
    Sb disapproval b flip "If you say so."
    show sebastian normal b flip with dissolve
    jump mavdp_four_c2aggravation_end

label mavdp_four_c2reinstated:
    play music "mx/mysteryambience.ogg"
    show maverick normal b with dissolve
    m "I turned around to see Maverick. His intense gaze confirmed that there was no one else his words could have been directed at. To my surprise, his police badge once again swung from his neck."
    c "What do you want from me?"
    Mv "Answers."
    menu:
        "What if I don't have any for you?":
            $ renpy.pause (0.5)
            Mv angry b "Then you will listen."
            $ evilpoints += 1
            show maverick normal b with dissolve
        "Okay. Then start talking.":
            pass
    
    Mv "Just tell me one thing: Why?"
    Mv "What is your goal in all of this?"
    Mv "Why get me reinstated?"
    $ renpy.error("TODO: Remainder of meeting.")