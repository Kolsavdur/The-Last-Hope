label kol_tlh_boosting_generator:

# Checks for the state of the generator before looping to options
if kol_tlh_stability_value > 80:
    $ kol_tlh_stability = "{color=#ff0000}Critical{/color}" #Red colour
elif kol_tlh_stability_value > 60 and kol_tlh_stability_value <= 80:
    $ kol_tlh_stability = "{color=#ffa500}Highly Unstable{/color}" #Orange colour
elif kol_tlh_stability_value > 40 and kol_tlh_stability_value <= 60:
    $ kol_tlh_stability = "{color=#ffff00}Unstable{/color}" #Yellow colour
else:
    $ kol_tlh_stability = "{color=#00ff00}Stable{/color}" #Green colour

if kol_tlh_temperature_value > 80:
    $ kol_tlh_temperature = "{color=#ff0000}Critical{/color}"
elif kol_tlh_temperature_value > 60 and kol_tlh_temperature_value <= 80:
    $ kol_tlh_temperature = "{color=#ffa500}Very High{/color}"
elif kol_tlh_temperature_value > 40 and kol_tlh_temperature_value <= 60:
    $ kol_tlh_temperature = "{color=#ffff00}High{/color}"
else:
    $ kol_tlh_temperature = "{color=#00ff00}Stable{/color}"

if kol_tlh_electrical_output_value > 80:
    $ kol_tlh_electrical_output = "{color=#ff0000}Critical{/color}"
elif kol_tlh_electrical_output_value > 60 and kol_tlh_electrical_output_value <= 80:
    $ kol_tlh_electrical_output = "{color=#ffa500}Very High{/color}"
elif kol_tlh_electrical_output_value > 40 and kol_tlh_electrical_output_value <= 60:
    $ kol_tlh_electrical_output = "{color=#ffff00}High{/color}"
else:
    $ kol_tlh_electrical_output = "{color=#00ff00}Stable{/color}"

if kol_tlh_spark_risk_value > 80:
    $ kol_tlh_spark_risk = "{color=#ff0000}Extremely High{/color}"
elif kol_tlh_spark_risk_value > 60 and kol_tlh_spark_risk_value <= 80:
    $ kol_tlh_spark_risk = "{color=#ffa500}Very High{/color}"
elif kol_tlh_spark_risk_value > 40 and kol_tlh_spark_risk_value <= 60:
    $ kol_tlh_spark_risk = "{color=#ffff00}High{/color}"
else:
    $ kol_tlh_spark_risk = "{color=#00ff00}Low{/color}"


$ renpy.pause (0.5)
show screen kol_extrainfo
$ kolextradisplay = 6

$ koldisplayvar1name = "Stability: "
$ koldisplayvar1 = kol_tlh_stability
$ koldisplayvar1unit = ""
$ koldisplayvar2name = "Temperature: "
$ koldisplayvar2 = kol_tlh_temperature
$ koldisplayvar2unit = ""
$ koldisplayvar3name = "Levels of Electrical Output: "
$ koldisplayvar3 = kol_tlh_electrical_output
$ koldisplayvar3unit = ""
$ koldisplayvar4name = "Risk of Sparks: "
$ koldisplayvar4 = kol_tlh_spark_risk
$ koldisplayvar4unit = ""
$ koldisplayvar5name = ""
$ koldisplayvar5 = ""
$ koldisplayvar5unit = ""
$ koldisplayvar6name = ""
$ koldisplayvar6 = ""
$ koldisplayvar6unit = ""


if (kol_tlh_stability_value > 80) or (kol_tlh_temperature_value > 80) or (kol_tlh_electrical_output_value > 80) or (kol_tlh_spark_risk_value > 80): #Checks if one of the generator stats is in critical condition
    $ kol_tlh_critical_count += 1

    if kol_tlh_critical_count > 2: #Fail

        $ renpy.pause (0.5)
        stop sound
        hide screen kol_extradisplay
        hide screen kol_extrainfo

        jump tlh_Chapter4A_continued

    else:
        pass

else:
    $ kol_tlh_critical_count = 0



show logan serious at Position(xpos = 0.3) with dissolve
$ renpy.pause (1.5)
$ kol_tlh_random_dialogue = renpy.random.randint(1, 3)




menu:
    "The generator could be more {u}stable{/u}.":

        $ kol_tlh_stability_value -= 15
        $ kol_tlh_temperature_value += 5
        $ kol_tlh_electrical_output_value += 10
        $ kol_tlh_spark_risk_value += 10

        $ kol_tlh_turn_count += 1


        if kol_tlh_random_dialogue == 1:

            $ renpy.pause (0.5)
            Lg normal "Alright, got it."

        elif kol_tlh_random_dialogue == 2:
            $ renpy.pause (0.5)
            Lg annoyed "Yeah, all these changes does take its toll. I'll see what I can do."

        else:
            $ renpy.pause (0.5)
            Lg serious "Really? I suppose I could try something like this..."

        play sound "fx/flicker.ogg" #How about you try to find a sound for "An unstable generator now returning to a more stable state" and see if you can find something better, hm? 


    "{u}Temperatures{/u} are getting too hot.":

        $ kol_tlh_stability_value += 5
        $ kol_tlh_temperature_value -= 25
        $ kol_tlh_electrical_output_value += 10
        $ kol_tlh_spark_risk_value += 10

        $ kol_tlh_turn_count += 1


        if kol_tlh_random_dialogue == 1:
            $ renpy.pause (0.5)
            Lg annoyed "What a coincidence. I just hurt my hand."

        elif kol_tlh_random_dialogue == 2:
            $ renpy.pause (0.5)
            Lg serious "No wonder I started to smell smoke from somewhere."

        else:
            $ renpy.pause (0.5)
            Lg normal "An astute observation for an obvious problem. Thanks."

        $ renpy.pause (0.35)
        play sound "fx/switch.wav" #Because this sounds close enough to tampering with a heat sink, I guess.

    "There's way too much {u}power{/u} flowing through the wires.":

        $ kol_tlh_stability_value += 10
        $ kol_tlh_temperature_value += 10
        $ kol_tlh_electrical_output_value -= 20
        $ kol_tlh_spark_risk_value += 10

        $ kol_tlh_turn_count += 1


        if kol_tlh_random_dialogue == 1:
            play sound "fx/magnetzap_kol.wav"
            $ renpy.pause (0.5)
            Lg annoyed "That would explain the buzzing I'm hearing."
            stop sound

        elif kol_tlh_random_dialogue == 2:
            $ renpy.pause (0.5)
            Lg serious "That's weird. Eh, it's easy to fix. Just a little bit of this..."

        else:
            $ renpy.pause (0.5)
            Lg normal "...done. Anything else?"


    "Redirect some of the open wires so that it doesn't {u}spark{/u}.":

        $ kol_tlh_stability_value += 10
        $ kol_tlh_temperature_value += 15
        $ kol_tlh_electrical_output_value += 5
        $ kol_tlh_spark_risk_value -= 15

        $ kol_tlh_turn_count += 1


        if kol_tlh_random_dialogue == 1:
            $ renpy.pause (0.5)
            Lg annoyed "Where's that electrical tape when you need it..."

        elif kol_tlh_random_dialogue == 2:
            $ renpy.pause (0.5)
            play sound "fx/zap_kol.wav"
            show logan surprised with dissolvequick
            Lg "DAMN IT!" with vpunch
            $ renpy.pause (0.5)

            Lg annoyed "Ugh, I'll never get used to zapping myself. Thank goodness for my rubber boots to help nullify the pain a bit."

        else:
            $ renpy.pause (0.5)
            Lg normal "And done. I thought that redirecting these wires would be a bit more difficult, but I'm not complaining."



if kol_tlh_turn_count == 15: #Success
    $ kol_tlh_chapter4_minigame_win = True

    $ renpy.pause (1.0)
    stop sound
    hide screen kol_extradisplay
    hide screen kol_extrainfo

    jump tlh_Chapter4A_continued

else:
    jump kol_tlh_boosting_generator