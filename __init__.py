from modloader import modclass

from renpy.exports import has_label

import jz_magmalink as ml

def register_setup_scenes():
    ( ml.find_label('quest6')
        .search_say("Oh, it's the human!")
        .search_say("I suppose we'll head off too, unless- oh no.")
        .search_say("Right, let's just all sit idly by while the suspect's on the loose and planning his next move.")
        .search_say("I don't need to hear you, of all people, belittling me about this.")
        .hook_to('mavdp_four_c1aggravation')
        .search_say("Don't compare yourself to me. Your words mean nothing.")
        .link_from('mavdp_four_c1aggravation_dontcompare')
        .link_behind_from('mavdp_four_c1aggravation_end')
    )

    ( ml.find_label('waitmenu')
        .search_if('beer == False')
        .search_menu("I would, but I don't think I can beat someone like you.")
        .search_menu("That sounds easy enough.")
        .search_menu("Heck, no.")
        .search_menu("That's not a blush!")
        .search_menu("I'm having a drinking contest with a dragon. How could I not love this?")
        .search_menu("That's my tactic, make you think that I'm struggling so you'll let your guard down.")
        .search_menu("Maybe. Having a lil' fun doesn't hurt, right?")
        .add_choice("I also wanted to ask about Maverick.", jump='mavdp_four_bryce1_otherreason', condition='mavdp_four_store.c1investigation_said != "aggressive"')
        .link_behind_from('mavdp_four_bryce1_otherreason_end')
    )

    if has_label('tt_bryce1_drink2_lightordry'):
        ( ml.find_label('tt_bryce1_drink2_lightordry')
            .search_menu()
            .add_choice("I also wanted to ask about Maverick.", jump='mavdp_four_bryce1_otherreason_teetoaller', condition='mavdp_four_store.c1investigation_said != "aggressive"')
            .link_behind_from('mavdp_four_bryce1_otherreason_teetotaller_end')
        )

    ( ml.find_label('_call_skiptut_11')
        .search_if('brycebar == True')
        .search_if('inv == "low"')
        .search_scene('town4')
        .search_say("Damn, not again.")
        .search_say("What are you doing here, Maverick?")
        .search_say("A second victim, huh?")
        .search_say("Tchk. Have your fun without me, then.")
        .search_show('maverick normal')
        .hook_to('mavdp_four_c2aggravation', condition='mavdp_four_store.bryce1_said == True', return_link=False)
        .search_say("We better check out that power outage now.")
        .link_from('mavdp_four_c2aggravation_end')
    )

    ( ml.find_label('_call_skiptut_12')
        .search_say("Look who we have here.")
        .hook_to('mavdp_four_c2reinstated', condition='mavdp_four_store.bryce1_said == True', return_link=False)
        .search_hide('maverick')
        .link_from('mavdp_four_c2reinstated_damnhero')
    )


def register_consequences():
    # It's known Maverick is the night patrol if he's reinstated.
    ( ml.find_label('_call_skiptut_4')
        .search_say("And who was patrolling last night?", depth=1200)
        .hook_to('mavdp_four_c3investigation_patrol_fix', condition='mavdp_four_store.maverickstatus in ["good","neutral","reinstated"]', return_link=False)
        .search_say("Why would he have done it? He'd be cutting off his only way out.")
        .link_from('mavdp_four_c3investigation_patrol_fix_end')
        .search_say("I'm sure that wouldn't be the only reason they'd benefit, though. There must be something we're not aware of.")
        .hook_to('mavdp_four_c3investigation_patrol_fix2', condition='mavdp_four_store.maverickstatus in ["good","neutral","reinstated"]', return_link=False)
        .search_say("But they still have the greatest motives.")
        .link_from('mavdp_four_c3investigation_patrol_fix2_end')
    )

    # Bryce3 doesn't happen if Maverick is reported.
    ( ml.find_label('bryce3')
        .search_scene('black')
        .search_with()
        .hook_to('mavdp_four_bryce3_cancelled', condition='mavdp_four_store.maverickstatus == "reported"', return_link=False)
        .search_menu("Sure.")
        .add_choice("I-I can't. I--", jump='mavdp_four_bryce3_report', condition='mavdp_four_store.maverickstatus == "neutral"')
    )

    # In Chapter4, Maverick gets his private meeting with Bryce if things aren't peachy.
    ( ml.find_label('_call_skiptut_20')
        .search_show("maverick normal flip").search_with()
        .hook_to('mavdp_four_c4meeting.ontheteam', condition='mavdp_four_store.maverickstatus in ["reinstated","neutral","good"]', return_link=False)
        .search_say("Chief, can I talk to you? Alone?")
        .hook_to('mavdp_four_c4meeting.nowherenear', condition='mavdp_four_store.maverickstatus == "reported"', return_link=False)
        .search_say("Reza.")
        .link_from('mavdp_four_c4meeting.nowherenear_end')
        .search_say("I think I know where Reza is.")
        .link_from('mavdp_four_c4meeting.know_where_reza_is')
        .search_say("Just a few minutes ago. When I did, I immediately came here.")
        .hook_to('mavdp_four_c4meeting.forgot_badge', condition='mavdp_four_store.maverickstatus in ["reinstated","neutral","good"]', return_link=True)
        .search_say("As if we had one to spare. Heck, we're going there right now.")
        .hook_to('mavdp_four_c4meeting.going', condition='mavdp_four_store.maverickstatus != "suspicious"', return_link=False)
        .search_say("How about you, [player_name]?")
        .link_from('mavdp_four_c4meeting_how_about_player')
        .search_say("After you, Chief.")
        .hook_to('mavdp_four_c4meeting.after_you', condition='mavdp_four_store.maverickstatus != "suspicious"', return_link=False)
        .search_say("Then I had to wait. Bryce and Sebastian were observing the farm now, and if anything new happened, I would be the first to know.")
        .link_from('mavdp_four_c4meeting_after_you_end')
    )

    # In Chapter4, at the farmhouse, if Maverick is on the team, he'd have spotted Reza.
    ( ml.find_label('didit')
        .search_say("Maybe he ran when he saw us approach.")
        .hook_to('mavdp_four_c4farmhouse.mayberan', condition='mavdp_four_store.maverickstatus in ["good","neutral","reinstated"]', return_link=True)
    )


def register_dates():
    ( ml.CharacterRoute('mavdp','Maverick')
        .add_date(jump='mavdp_four_mav2',chapters=[2], condition='mavdp_four_store.maverickstatus == "reinstated"')
        # .add_date(jump='mavdp_four_mav3',chapters=[3], condition='mavdp_four_store.maverickstatus != "reported"')
        .build()
    )


@modclass.loadable_mod
class DontPretendMod(modclass.Mod):
    name = "Don't Pretend"
    author = "4onen"
    version = "v0.0"
    dependencies = ["MagmaLink", "?Teetotaller", "?Side Images"]

    @staticmethod
    def mod_load():
        register_setup_scenes()
        register_consequences()
        register_dates()

        ( ml.StatusBox('mavdp_four_store.mavscenesfinished', 'mavdp_four_store.c1investigation_said != "aggressive"')
            .add_status("image/ui/status/maverick_status_dead.png", "--", 'mavdp_four_store.maverickstatus == "dead"')
            .add_status("image/ui/status/maverick_status_neutral.png", "Neutral", 'mavdp_four_store.maverickstatus == "neutral" or brycegoodending')
            .add_status("image/ui/status/maverick_status_suspicious.png", "Suspicious", 'mavdp_four_store.maverickstatus == "suspicious"')
            .add_status("image/ui/status/maverick_status_suspicious_b.png", "Suspicious", 'mavdp_four_store.maverickstatus == "reinstated"')
            .add_status("image/ui/status/maverick_status_reported.png", "Bad", 'mavdp_four_store.maverickstatus == "reported"')
            .add_status("image/ui/status/maverick_status_good.png", "Good", 'mavdp_four_store.maverickstatus == "good"')
            .build()
        )

    @staticmethod
    def mod_complete():
        pass