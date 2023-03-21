from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod):
    name = "The Last Hope"
    version = "v1.00"
    author = "Kolsavdur"
    dependencies = ["MagmaLink", "Kolsavdur Core Mod"]

    def mod_load(self):
        ml = modinfo.get_mod("MagmaLink").import_ml() #Checks if MagmaLink is installed

        #Searches for the last line in Reza's speech and hooks to it if Sebastian is kept alive, if Adine's second date had been done with an Impressed mood, if Bryce's second date had been done with an Impressed mood, if Remy's good ending is being done and if Remy is Impressed
        #Yeah... this is absurdly long, but whatever! Who doesn't like questionably long code? >:)
        ml.find_label("no") \
            .search_say("I mean, what are you going to do? You can't stop me now, anyway.", depth=800) \
            .hook_to("tlh_newrezaencounter", return_link=False, condition="persistent.sebastianfail==False and adinestatus==\"good\" and adinescenesfinished==2 and brycestatus==\"good\" and brycescenesfinished==2 and remygoodending==True and remystatus==\"good\"")


    def mod_complete(self):
        pass
