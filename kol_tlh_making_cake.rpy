#This file is going to be one *hell* of a mess. Be warned, ye who enter here.
#Also, super sorry for making this game. I already know ahead of time that there will be quite a lot of people that will hate it. XD

label kol_tlh_makingcake:
$ renpy.pause (0.5)
stop sound
hide screen kol_extradisplay
hide screen kol_extrainfo

menu:
    c "(What should I do?)"

    "Add dry ingredients." if kol_tlh_mixdry == False:
        jump kol_tlh_dryingredients

    "Add wet ingredients." if kol_tlh_mixwet == False:
        jump kol_tlh_wetingredients

    "Mix.":
        menu:
            c "(What should I mix?)"

            "Mix the dry ingredients." if kol_tlh_flouramount > 0 and kol_tlh_bakingsodaamount > 0 and kol_tlh_saltamount > 0 and kol_tlh_cocoapowderamount > 0 and kol_tlh_bakingpowderamount > 0 and kol_tlh_sugaramount > 0 and kol_tlh_mixdry == False:
                if kol_tlh_flouramount != 1.75:
                    $ kol_tlh_flourfail = True
                    $ kol_tlh_strikes += 1

                if kol_tlh_bakingsodaamount != 1.5:
                    $ kol_tlh_bakingsodafail = True
                    $ kol_tlh_strikes += 1
                
                if kol_tlh_saltamount != 1:
                    $ kol_tlh_saltfail = True
                    $ kol_tlh_strikes += 1

                if kol_tlh_cocoapowderamount != 0.75:
                    $ kol_tlh_cocoapowderfail = True
                    $ kol_tlh_strikes += 1
                
                if kol_tlh_bakingpowderamount != 1.5:
                    $ kol_tlh_bakingpowderfail = True
                    $ kol_tlh_strikes += 1

                if kol_tlh_sugaramount != 2:
                    $ kol_tlh_sugarfail = True
                    $ kol_tlh_strikes += 1
                
                $ renpy.pause (1.0)
                $ kol_tlh_mixdry = True

                play sound "fx/mixingdry_kol.mp3"
                m "I mixed all the dry ingredients together. It wasn't long before everything had been combined into a powdered mess of dull colours."
                $ renpy.pause (1.5)
                stop sound
                jump kol_tlh_makingcake


            "Mix the wet ingredients." if kol_tlh_eggamount > 0 and kol_tlh_oilamount > 0 and kol_tlh_milkamount > 0 and kol_tlh_wateramount > 0 and kol_tlh_vanillaamount > 0 and kol_tlh_mixwet == False:
                if kol_tlh_eggamount != 2:
                    $ kol_tlh_eggfail = True
                    $ kol_tlh_strikes += 1

                if kol_tlh_oilamount != 0.5:
                    $ kol_tlh_oilfail = True
                    $ kol_tlh_strikes += 1

                if kol_tlh_milkamount != 1:
                    $ kol_tlh_milkfail = True
                    $ kol_tlh_strikes += 1

                if kol_tlh_wateramount != 1:
                    $ kol_tlh_waterfail = True
                    $ kol_tlh_strikes += 1

                if kol_tlh_vanillaamount != 2:
                    $ kol_tlh_vanillafail = True
                    $ kol_tlh_strikes += 1

                $ renpy.pause (1.0)
                $ kol_tlh_mixwet = True

                play sound "fx/mixingwet_kol.mp3"
                m "I mixed all the wet ingredients together. It wasn't long before everything had been combined into a strange puddle of different ingredients."
                $ renpy.pause (1.5)
                stop sound

                jump kol_tlh_makingcake

            "Mix everything." if kol_tlh_mixdry and kol_tlh_mixwet == True:
                $ kol_tlh_mixfinal = True
                $ renpy.pause (0.5)

                play sound "fx/cakemixing_kol.mp3"
                m "I combined all the ingredients together and stirred until everything became a goopy, messy batter ready to be used for baking."
                $ renpy.pause (1.5)
                stop sound

                jump tlh_Chapter2B_continued

            "[[Go back.]":
                jump kol_tlh_makingcake


    "Ask Remy for the recipe.":
        $ kol_tlh_askremyamount += 1
        $ renpy.pause (0.5)
        c "Hey Remy? Could you remind me of the recipe?"

        if kol_tlh_askremyamount >=3:
            show remy look with easeinright
            $ kol_tlh_chapter2B_mood -= 1

        Ry "Of course. You need two eggs, half a cup of vegetable oil, one cup of milk, a cup of boiling water, and two teaspons of vanilla essence. Mix those well."
        Ry "After that, mix two cups of sugar, a teaspoon of salt, one and a half teaspoons of baking soda, just as much baking powder, one and three-quarters cups of flour and three-quarter cups of cocoa powder."
        Ry "Mix the dry ingredients, then add them to the mixed wet ingredients to make the batter."

        if kol_tlh_askremyamount >=3:
            show remy look flip with dissolve
            hide remy with easeoutright

            jump kol_tlh_makingcake
        
        Ry "Does this help?"
        c "Yeah, thanks."
        Ry smile "I'm happy to be of service."

        jump kol_tlh_makingcake
            
#-------------------------------------------
label kol_tlh_dryingredients:
$ renpy.pause (0.5)
stop sound

#Menu stuff
hide screen kol_extrainfo
show screen kol_extrainfo
$ kolextradisplay = 7

$ koldisplayvar1name = "Amount of flour:"
$ koldisplayvar1 = kol_tlh_flouramount
$ koldisplayvar1unit = " Cup(s)"
$ koldisplayvar2name = "Amount of baking soda:"
$ koldisplayvar2 = kol_tlh_bakingsodaamount
$ koldisplayvar2unit = " Teaspoon(s)"
$ koldisplayvar3name = "Amount of salt:"
$ koldisplayvar3 = kol_tlh_saltamount
$ koldisplayvar3unit = " Teaspoon(s)"
$ koldisplayvar4name = "Amount of cocoa powder:"
$ koldisplayvar4 = kol_tlh_cocoapowderamount
$ koldisplayvar4unit = " Cup(s)"
$ koldisplayvar5name = ""
$ koldisplayvar5 = ""
$ koldisplayvar5unit = ""
$ koldisplayvar6name = ""
$ koldisplayvar6 = ""
$ koldisplayvar6unit = ""
$ koldisplayvar7name = ""
$ koldisplayvar7 = ""
$ koldisplayvar7unit = ""

# End of menu stuff

menu:
    c "(What should I add?)"

    "Flour.":
        hide screen kol_extrainfo
        $ renpy.pause (0.75)
        menu:
            c "(How much flour?)" #one and three-quarters

            "One cup.":
                $ kol_tlh_flouramount += 1

            "Half a cup.":
                $ kol_tlh_flouramount += 0.5

            "A quarter cup.":
                $ kol_tlh_flouramount += 0.25

        $ renpy.pause (1.0)
        play sound "fx/flour_kol.mp3"
        $ renpy.pause (2.0)
        jump kol_tlh_dryingredients

    "Baking soda.": #No sfx
        hide screen kol_extrainfo
        $ renpy.pause (0.75)
        menu:
            c "(How much baking soda?)" #One and a half teaspoon

            "One teaspoon.":
                $ kol_tlh_bakingsodaamount += 1

            "A quarter teaspoon.":
                $ kol_tlh_bakingsodaamount += 0.25

            "Two teaspoons.":
                $ kol_tlh_bakingsodaamount += 2

        $ renpy.pause (1.0)
        c "(And now...)"
        $ renpy.pause (1.0)
        jump kol_tlh_dryingredients

    "Salt.":
        hide screen kol_extrainfo
        $ renpy.pause (0.75)
        menu:
            c "(How much salt?)" #One teaspoon

            "A quarter teaspoon.":
                $ kol_tlh_saltamount += 0.25

            "One and a half teaspoons.":
                $ kol_tlh_saltamount += 1.5

            "One teaspoon.":
                $ kol_tlh_saltamount += 1
        
        $ renpy.pause (1.0)
        play sound "fx/salt_kol.mp3"
        $ renpy.pause (2.0)
        jump kol_tlh_dryingredients

    "Cocoa powder.":
        hide screen kol_extrainfo
        $ renpy.pause (0.75)
        menu:
            c "(How much cocoa powder?)" #one and three-quarters

            "One cup.":
                $ kol_tlh_cocoapowderamount += 1

            "Half a cup.":
                $ kol_tlh_cocoapowderamount += 0.5

            "A quarter cup.":
                $ kol_tlh_cocoapowderamount += 0.25

        $ renpy.pause (1.0)
        play sound "fx/flour_kol.mp3"
        $ renpy.pause (2.0)
        jump kol_tlh_dryingredients

    "[[More options.]":
        jump kol_tlh_moredryingredients

    "[[All options.]":
        jump kol_tlh_makingcake


label kol_tlh_moredryingredients:
$ renpy.pause (0.5)
stop sound

hide screen kol_extrainfo
show screen kol_extrainfo
$ kolextradisplay = 4


$ koldisplayvar1name = "Amount of baking powder:"
$ koldisplayvar1 = kol_tlh_bakingpowderamount
$ koldisplayvar1unit = " Teaspoon(s)"
$ koldisplayvar2name = "Amount of sugar:"
$ koldisplayvar2 = kol_tlh_sugaramount
$ koldisplayvar2unit = " Cup(s)"
$ koldisplayvar3name = ""
$ koldisplayvar3 = ""
$ koldisplayvar3unit = ""
$ koldisplayvar4name = ""
$ koldisplayvar4 = ""
$ koldisplayvar4unit = ""



menu:
    c "(What should I add?)"

    "Baking powder.": #No sfx
        hide screen kol_extrainfo
        $ renpy.pause (0.75)
        menu:
            c "(How much baking powder?)" #One and a half teaspoon

            "A quarter teaspoon.":
                $ kol_tlh_bakingpowderamount += 0.25

            "Half a teaspoon.":
                $ kol_tlh_bakingpowderamount += 0.5

            "One teaspoon.":
                $ kol_tlh_bakingpowderamount += 1

        $ renpy.pause (1.0)
        c "(Alright, next up...)"
        $ renpy.pause (1.0)
        jump kol_tlh_moredryingredients

    "Sugar.":
        hide screen kol_extrainfo
        $ renpy.pause (0.75)
        menu:
            c "(How much sugar?)" #Two cups.

            "One cup.":
                $ kol_tlh_sugaramount += 1

            "One and a half cup.":
                $ kol_tlh_sugaramount += 1.5

            "Two cups.":
                $ kol_tlh_sugaramount += 2
        
        $ renpy.pause (1.0)
        play sound "fx/sugar_kol.mp3"
        $ renpy.pause (2.0)
        jump kol_tlh_moredryingredients

    "[[More options.]":
        jump kol_tlh_dryingredients

    "[[All options.]":
        jump kol_tlh_makingcake

#-----------------------------------------
label kol_tlh_wetingredients:
$ renpy.pause (0.5)
stop sound

#Menu stuff
show screen kol_extrainfo
$ kolextradisplay = 7

$ koldisplayvar1name = "Amount of eggs:"
$ koldisplayvar1 = kol_tlh_eggamount
$ koldisplayvar1unit = ""
$ koldisplayvar2name = "Amount of vegetable oil:"
$ koldisplayvar2 = kol_tlh_oilamount
$ koldisplayvar2unit = " Cup(s)"
$ koldisplayvar3name = "Amount of milk:"
$ koldisplayvar3 = kol_tlh_milkamount
$ koldisplayvar3unit = " Cup(s)"
$ koldisplayvar4name = "Amount of water:"
$ koldisplayvar4 = kol_tlh_wateramount
$ koldisplayvar4unit = " Cup(s)"
$ koldisplayvar5name = "Amount of vanilla essence:"
$ koldisplayvar5 = kol_tlh_vanillaamount
$ koldisplayvar5unit = " Teaspoon(s)"
$ koldisplayvar6name = ""
$ koldisplayvar6 = ""
$ koldisplayvar6unit = ""
$ koldisplayvar7name = ""
$ koldisplayvar7 = ""
$ koldisplayvar7unit = ""
#End of menu stuff

menu:
    c "(What should I add?)"

    "Egg.": #2 eggs
        hide screen kol_extrainfo
        $ renpy.pause (0.75)
        $ kol_tlh_eggamount += 1

        $ renpy.pause (1.0)
        play sound "fx/egg.ogg"
        $ renpy.pause (2.0)
        jump kol_tlh_wetingredients

    "Vegetable oil.":
        hide screen kol_extrainfo
        $ renpy.pause (0.75)
        menu:
            c "(How many cups of vegetable oil?)" #Half a cup

            "Half a cup.":
                $ kol_tlh_oilamount += 0.5

            "A quarter cup.":
                $ kol_tlh_oilamount += 0.25

            "One cup.":
                $ kol_tlh_oilamount += 1
        
        $ renpy.pause (1.0)
        play sound "fx/oil_kol.mp3"
        $ renpy.pause (2.0)
        jump kol_tlh_wetingredients

    "Milk.":
        hide screen kol_extrainfo
        $ renpy.pause (0.75)
        menu:
            c "(How many cups of milk?)" #One cup needed

            "Two cups.":
                $ kol_tlh_milkamount += 2

            "One cup.":
                $ kol_tlh_milkamount += 1

            "Half a cup.":
                $ kol_tlh_milkamount += 0.5
        
        $ renpy.pause (1.0)
        play sound "fx/milk_kol.mp3"
        $ renpy.pause (2.0)
        jump kol_tlh_wetingredients

    "Water.":
        hide screen kol_extrainfo
        $ renpy.pause (0.75)
        menu:
            c "(How many cups of water?)" #One cup

            "One cup.":
                $ kol_tlh_wateramount += 1

            "A quarter cup.":
                $ kol_tlh_wateramount += 0.25

            "Half a cup.":
                $ kol_tlh_wateramount += 0.5
        
        $ renpy.pause (1.0)
        play sound "fx/water_kol.mp3"
        $ renpy.pause (2.0)
        jump kol_tlh_wetingredients

    "Vanilla essence.": #No sfx
        hide screen kol_extrainfo
        $ renpy.pause (0.75)
        menu:
            c "(How many teaspoons of vanilla essence?)" #Two teaspoons

            "A quarter teaspoon.":
                $ kol_tlh_vanillaamount += 0.25

            "One teaspoon.":
                $ kol_tlh_vanillaamount += 1

            "Half a teaspoon.":
                $ kol_tlh_vanillaamount += 0.5

        $ renpy.pause (0.85)
        c "(Now, what's next...)"
        $ renpy.pause (1.0)
        jump kol_tlh_wetingredients


    "[[All options.]":
        jump kol_tlh_makingcake
