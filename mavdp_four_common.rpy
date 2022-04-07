init:
    # Status enumeration:
    default mavdp_four_store.maverickstatus = "bad"
    # States:
    #    "bad"        - Still suspicious of you.          Display in menu: Bad       (image: maverick angry)
    #    "reinstated" - Reinstated, but still suspicious. Display in menu: Bad       (image: maverick angry b)
    #    "reported"   - Reported for attacking you.       Display in menu: Bad       (image: maverick lost)
    #    "neutral"    - Neutral.                          Display in menu: Good      (image: maverick neutral) -- should also be unlocked by Bryce goodending path.
    #    "good"       - Good.                             Display in menu: Impressed (image: maverick nice)