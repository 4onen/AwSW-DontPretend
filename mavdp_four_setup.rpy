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
            c "I talked with Bryce about why Maverick is on sick leave."
            c "It didn't make sense to me to run parallel investigations, and it's clear he's not just resting."
            $ renpy.pause (0.5)
            Sb drop b "I see."
            $ renpy.pause (0.5)
            show sebastian normal b with dissolve
        "[[Say nothing.]":
            $ renpy.pause(0.8)
            m "It took a little while for Bryce to return."
    $ renpy.pause (0.9)
    $ mavdp_four_store.maverickstatus = "reinstated"
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
    $ mavdp_four_store.maverickstatus = "reinstated"
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

    Mv "I know you talked to Bryce. He only mentioned offhandedly, but this isn't like him."
    Mv "Just tell me one thing: Why?"
    Mv "What is your goal in all of this?"
    Mv "Why get me reinstated, when you know I {i}will{/i} get to the bottom of whatever it is you're doing?"

    menu:
        "Because working together is the best way to find the truth.":
            c "I came as an ambassador and that's what I'm here to be. I want to know why Reza's doing what he's been doing just as much as you do."
            Mv "No, no, no. That won't do."
            Mv "That's simply not true. You know it, and I know it. You convinced Bryce to take me off sick leave, under the guise of sharing information, yet now you tell me nothing?"
            $ c2mav = "ambassador"
        "You wouldn't understand.":
            Mv "What would I not understand?"
            Mv "You convinced Bryce to take me off sick leave, under the guise of sharing information, yet now you tell me nothing?"
            $ c2mav = "understand"

    c "I'm being honest with you. You're too close to this emotionally to--"
    Mv angry b "There are no emotions to this. Only the fact that Reza is doing what he's doing."
    Mv normal b "As are you."
    Mv "Was getting me reinstated a way to place me back on guard duties? To slow me down? Or to place me in the way of your future attacks?"
    Mv normal b "I just don't get why you won't tell me anything, even when you know no one else is listening."
    Mv "You know I can't touch you. If I did, it would be over for me. At least, as long as I don't have any proof."
    Mv "I could've saved the world with what I did that day and it still wouldn't matter when no one believes me. Just because I don't have any proof."
    $ renpy.pause(0.8)
    Mv "..."
    show maverick nice b with dissolve
    $ renpy.pause(0.3)
    m "A slight light seemed to come on behind his eyes."
    Mv normal b "Maybe this is still too public for you. Is that it?"
    Mv "Fine."
    m "He scratched some digits into the dirt path."
    Mv "Call, and I will give you a time and place even more remote. Or do not, and continue your charade."
    Mv angry b "If you won't tell me, I won't stop until I find out what you're planning."
    Mv normal b "And when I do, I'm gonna be a damn hero."
    jump mavdp_four_c2reinstated_damnhero