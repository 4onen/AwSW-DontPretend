init:
    # Status enumeration:
    default mavdp_four_store.maverickstatus = "suspicious"
    # States:
    #    "suspicious" - Still suspicious of you.          Display in menu: Suspicious
    #    "reinstated" - Reinstated, but still suspicious. Display in menu: Suspicious
    #    "reported"   - Reported for attacking you.       Display in menu: Bad
    #    "neutral"    - Neutral.                          Display in menu: Neutral -- should also be unlocked by Bryce goodending path.
    #    "good"       - Good.                             Display in menu: Good
    default mavdp_four_store.mavscenesfinished = 0
    # 0 - No dates.
    # 1 - Finished forest date.
    # 2 - Finished cafe date.
    # 3 - ???

init python in mavdp_four_store:
    def has_side_images():
        from modloader import modinfo
        return modinfo.has_mod("Side Images")