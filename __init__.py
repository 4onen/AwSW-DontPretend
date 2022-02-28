from modloader import modclass, modinfo


@modclass.loadable_mod
class DontPretendMod(modclass.Mod):
    name = "Don't Pretend"
    author = "4onen"
    version = "v0.0"

    @staticmethod
    def mod_load():
        ml = modinfo.get_mod("MagmaLink").import_ml()

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
            .hook_to('mavdp_four_c2reinstated')
        )

    @staticmethod
    def mod_complete():
        pass