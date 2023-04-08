label tlh_Chapter3A:

$ save_name = (_("TLH - Chapter 3A"))
$ renpy.pause (2.0)

Lg annoyed "Hey. Time to get up. We’ve got a long day today."

$ renpy.pause (3.0)
scene o4 at Pan((0, 0), (0, 150), 4.0) with dissolveslow
$ renpy.pause (3.0)
show logan normal with dissolve
$ renpy.pause (1.5)

c "What...{w=0.8} time is it even?"
Lg "If the time here is aligned to back home, then just after seven in the morning."
m "I groaned, my mind still foggy from last night’s deeper-than-usual sleep. Logan seemed to smirk, as if he took pleasure in seeing me slowly wake up and orient myself to reality."

play music "mx/couch_kol.ogg" fadein (2.0)

Lg "Perhaps you wouldn’t be so slow if you just went to bed earlier." #Logan being cocky about being an early bird? Gee, what's new...

menu:
    "I literally went to bed at the same time as you.":
        $ renpy.pause (0.5)

        Lg "You’re dodging my statement here, [player_name]. Just because you went to sleep at the same time as me doesn’t mean that you got enough."
        Lg smiling "Clearly, you need to go to sleep earlier."
        c "Says the one who’s greatest desire in the world is getting as little sleep as physically possible."
        Lg annoyed "No comment."
        c "Figured."

    "As if being a morning person would help with anything.":
        $ renpy.pause (0.5)

        Lg smiling "Oh, but it does. The early bird gets the worm, after all."
        c "Only if the worm doesn’t decide to sleep in."

        $ renpy.pause (0.5)
        show logan annoyed with dissolve
        $ renpy.pause (0.5)

        Lg serious "You really are a slacker, aren't you?" #No, the MC just has more logic than you. What an insult considering they just woke up as well. :)
        c "Only at the times when it annoys you the most, it seems."

    "Sometimes you just have an extra hard time waking up. Today is one of those times.":
        $ renpy.pause (0.5)
        show logan serious with dissolve
        $ renpy.pause (0.5)

        Lg "I see. Sometimes your body just doesn’t want to do stuff when you want it to. Sorry if you just feel extra groggy today, then."
        c "It’s alright."

$ renpy.pause (1.5)
c "Now, why exactly did you wake me up so early?"
Lg normal "Well, I’m supposed to get my response from the council about the ultimatum. As for you, I want you to do a bit of scouting work around that one place where the generators are being made."
Lg serious "I’m guessing that the dragons aren’t really going to send you back or give the generators we’re owed for some time. They most certainly will {i}not{/i} cancel the trade though, so I’ll use that to try and negotiate {i}something,{/i} even if it’s a bit small."
c "Logan, are you planning to steal the generators from the production facility?"
Lg surprised "Are {i}you{/i} of all people accusing me of being like Reza?" #Yes. Yes they are.
Lg serious "You do know that Reza is the reason we’re even going through all of this, right?"
$ renpy.pause (0.5)
Lg "*sigh*"
Lg "I want you to scout the production facility for parts, not generators. If there’s anything vaguely familiar that you can recognise, then I ask you to make a mental note of said part. This will serve as a backup until we’ve figured out what to do." #Relying on the MC's mental notes is a hige mistake, Logan

if persistent.kol_tlh_goodendingcheck == True and persistent.kol_tlh_badendingcheck == True:
    menu:
        "Why go through the effort of scouting?": #Unlocks ending A
            $ kol_tlh_endingA_route = True
            stop music fadeout (1.0)
            $ renpy.pause (1.5)
            play music "mx/judgement.ogg" fadein (1.0)

            Lg annoyed "What..."
            $ renpy.pause (1.0)


            if persistent.kol_tlh_chapter3A_5_skip:
                $ renpy.pause (1.75)
                c "(Wait, haven't I seen this before at some point?)"

                menu:
                    s "(Do you want to skip forward?)"

                    "Yes.":

                        stop sound fadeout (1.0)
                        stop music fadeout (1.0)
                        scene black with fade
                        jump tlh_Chapter3_EndingA

                    "No.":
                        pass

            $ renpy.pause (1.0)
            Lg "I’m lost. What do you mean we shouldn't scout for spare parts? How else are we going to help humanity while also keeping the trade going?"
            Lg serious "The parts are the only way we can stall for time without causing chaos."
            c "Yet, there’s a far more effective way to stall for time without even needing to break into the production facility."
            Lg "Then please, do inform me."
            c "Think about it this way: do you really think it would be possible to get every generator on the planet connected to redirect the comet? After all, what would happen if, say, a single generator were to break during the comet’s redirection? Would that really cause the entire world to end?"
            $ renpy.pause (1.5)
            Lg "[player_name]."
            $ renpy.pause (0.5)
            Lg smiling "You are an absolute genius. If I were able to, I would’ve given you some sort of compensation for that idea." #How about letting the MC sleep in for once? That would be a start.
            Lg normal "Do you realise {i}how much{/i} of an impact a single generator could have back home? Not only would it stall for time, but the city's engineers could probably use the extra power to test some of the new equipment we discovered."
            c "Which could lead to even more important breakthroughs."
            Lg smiling "You read my mind."
            Lg serious "Just one tiny problem, though. {w}Where the hell are we getting this generator from? I highly doubt that you want me to steal it judging from your vehement reaction from me suggesting the possibility of getting a few parts."
            c "Shouldn’t Reza’s former apartment still have one? And if not, you could use the generator in any old abandoned apartment."
            Lg "And why should it have to be an abandoned apartment and not yours? It sure as hell would be a lot easier."
            c "Because it would look far too sketchy if I suddenly had lost a generator that just vanished without a trace. With you, it would be less conspicuous."
            Lg "You’re not making any sense here, [player_name]."
            c "Trust me. It would raise a lot more questions if the older ambassador who, mind you, had been working with dragonkind to help out with the Reza case suddenly stole a generator."
            c "You, on the other hand, don’t have a reputation to maintain yet. Besides, your stay is way shorter than mine. It would just be smarter to take from wherever and hope that nobody notices."
            Lg "Dunno why you want to paint me the villain here, but I guess I have to agree to an extent. I’ll see what I can find from Reza’s old place first, and if all else fails, then hopefully there will be a spare that had been forgotten about somewhere." #Bruh you're literally going to steal some stuff later on of course you're gonna be the villain here.
            Lg "I guess that I can just ask the officers where Reza lived, then?"
            c "Yeah. They’d be able to show you exactly where Reza’s apartment was."
            Lg "Good."
            $ renpy.pause (1.0)
            show logan annoyed with dissolve
            $ renpy.pause (0.5)
            Lg "Though, scouting regardless would still be good for a backup plan. I mean, maybe you could find something that would be also pretty useful for us."
            Lg serious "And before you say anything: no, I didn’t say anything about stealing. Just looking around will suffice for now. Got it?" #You didn't say anything about stealing *yet*.
            $ renpy.pause (0.5)
            c "Alright."
            stop music fadeout (1.0)
            $ renpy.pause (2.5)

            jump tlh_Chapter3A_continued

        "Logan, do you realise how much the dragons need every single generator they can get?":
            jump kol_tlh_noendingA


label kol_tlh_noendingA:

if persistent.kol_tlh_chapter3A_skip:
    $ renpy.pause (1.75)
    c "(Wait, haven't I seen this before at some point?)"

    menu:
        s "(Do you want to skip forward?)"

        "Yes.":
            stop sound fadeout (1.0)
            stop music fadeout (1.0)
            scene black with fade
            jump tlh_Chapter3B

        "No.":
            pass


c "Logan, do you realise how much the dragons need every single generator they can get? That includes generators that haven’t been produced yet."
Lg annoyed "Did you even hear me saying the word {i}backup{/i} just now?"
Lg serious "I’ve been formulating a plan while you were snoring away in Dreamland, so I know what I’m doing. At least, for the foreseeable future." #"I made a plan and you didn't so I am more qualified than you". Your logic is wacky here, Logan.
Lg "You need to trust me on this one, [player_name]. I genuinely don’t think there’s anything else we can do right now."
c "Then so be it. I don’t like it, but if all else fails, then we’ll go through with that backup."
jump tlh_Chapter3A_continued

label tlh_Chapter3A_continued:
if kol_tlh_endingA_route == True:
    play music "mx/couch_kol.ogg" fadein (0.5)

$ renpy.pause (0.5)
c "Considering you've woken up so early, I assume you’ve already called for our escorts?"
Lg annoyed "I tried to call them. They…{w=1.0}{nw}"
$ renpy.pause (0.75)
Lg serious "…didn’t pick up."
c "Just {i}how{/i} early did you–{w=0.85}{nw}" #Yes.
Lg "Early enough to warrant me trying to call them again right about now."

hide logan with dissolve
m "Logan walked to the phone, slightly embarrassed, and dialled the police station. Logan and whoever was on the other end of the line exchanged a few words before the call ended."
show logan normal with dissolve
$ renpy.pause (0.5)
Lg "Done. They’ll be here soon."
Lg serious "Personally, I think it’s a bit redundant to have the escorts now when all the danger has already passed, but I suppose that we can’t really do anything about that. I just want to explore on my own without someone constantly looking at me behind my back."
c "Speaking of someone looking behind you, how did your evening with Bryce go?"
Lg smiling "Pretty good. We definitely bonded over some beer if that’s what you’re wondering."
c "...and?"
Lg normal "I woke up in the bar just like the good ol’ days."
Lg thinking "Apparently I wasn’t out for too long, either; just long enough before the bar closed. Poor waiter had to ask me if I could take Bryce back to his apartment due to some “unwritten rule” that all Bryce’s drinking buddies are obligated to take him back home if he can’t get there himself."
Lg annoyed "Looking back at it now, it was just a bit unfair considering he’s probably like ten times my weight or something. Still, I definitely surprised him with how much booze I could take."

if nodrinks == False:
    Lg normal "More than you, according to him." #Ouch.

menu:
    "Well at least you both enjoyed yourselves.":
        $ renpy.pause (0.5)

        Lg normal "I suppose we did, even if I definitely wasn’t as capable as I used to be back in university."
        Lg smiling "Bryce {i}definitely{/i} enjoyed every single second of our evening. Alcohol flowing through your head really does lead to some of the most interesting things imaginable."

    "Just don’t go overboard next time.":
        c "It was a bit rash to drink that much beer knowing that you have a complicated plan in the works, Logan. Remember to not drink as much next time so that you could have a somewhat clear head."
        Lg serious "Yeah yeah, I get it. Still, a little beer helps with the enormous responsibility we now have on ourselves."

    "This isn’t the last time, is it?": #Foreshadowing!
        $ renpy.pause (0.5)

        Lg serious "[player_name], I spent the evening drinking booze with a {i}dragon{/i}. Do you really think that I’ll be passing the opportunity to have another drinking competition?"
        Lg annoyed "That…{w=0.5} was something I’d never think I’d say in my life. Huh."
        Lg normal "Uh, anyway; yeah, there will probably be more to come."

$ renpy.pause (1.0)
play sound "fx/door/doorbell.wav"
$ renpy.pause (1.0)
c "I'll get it."
$ renpy.pause (0.5)
play sound "fx/door/door_open.wav"
stop music fadeout (2.5)
$ renpy.pause (1.5)

show sebastian normal b at Position(xpos = 0.85) with easeinright
show logan at Position(xpos = 0.25) with ease
show logan normal flip with dissolve

$ renpy.pause (1.0)
play music "mx/depths_kol.ogg" fadein (1.5)

Sb "Morning, [player_name]."
Sb drop b "And Logan."
Lg normal flip "Morning. I believe you slept well?"

if kol_tlh_bryce_escort == True:
    Sb "You could say that. I believe you’re ready to go to Emera, correct?"
    Lg "Yeah. Best to not waste any more time."
    Sb disapproval b "I see. Well, let’s go."

    show sebastian disapproval b flip with dissolve
    hide sebastian
    hide logan
    with easeoutright
    $ renpy.pause (3.5)
    show bryce normal b with easeinright

    Br "Hey."
    c "Hey, Bryce."
    Br "I’ve been told you want to go to the production facility, right?"
    c "Yeah. I want to check up on the progress that has been made with humanity’s generators."
    Br stern b "From what I’ve heard, things have slowed down significantly due to the situation surrounding Reza. I’m pretty sure they’ll be going back at full speed soon, though."
    c "Only one way to find out, I suppose. Ready?"
    Br smirk b "Always."

    scene black with fade
    play sound "fx/steps/clean2.wav"
    $ renpy.pause (1.5)
    m "We walked out of my apartment and into the streets. Bryce strolled down the roads while my eyes adjusted to the increased brightness. Bryce looked around as if he was searching for any potential problems."
    scene town2 with fade
    $ renpy.pause (1.5)

    show bryce normal b with dissolve
    $ renpy.pause (1.5)

    c "Bryce?"
    Br "Yes?"
    c "I’ve heard that you had another drinking competition recently. Mind telling me more about that?"
    Br laugh b "Yeah, I did."
    Br normal b "I wanted to try and get to know Logan to see what exactly his deal was."
    Br stern b "Sure, his first impressions were rough, but I had this strange feeling that he almost didn’t want to be the one to do humanity’s dirty work back there in Emera’s office."
    Br normal b "So, I wanted to learn more about him to see whether my feelings were justified."
    Br smirk b "Turns out, I found something far more than that."#He found a drinking buddy! And... maybe something more. ;)
    c "I figured. When you get to know Logan for a bit, he can be pretty… {w=0.8}interesting."
    Br laugh b "That’s one way of putting it."

    $ renpy.pause (1.5)
    scene fac1 with dissolve
    $ renpy.pause (1.5)

    m "In due time, we eventually reached the outside of the production facility. I looked at the building in a different light than when I first came here. Now, whatever I might find could determine whether Logan’s plan would be a success or the cause of humanity’s demise."

    show bryce stern b with dissolve
    $ renpy.pause (1.0)

    Br "Well, here we are. Anything specific that you need help with?"
    c "I'm good, thanks."
    Br "Right. You know what to do if you need me."
    c "Yeah. See you later, Bryce."

    hide bryce with dissolve
    $ renpy.pause (0.75)

    m "Bryce left the facility grounds, leaving me alone in the midst of the manufacturing facility. I considered what I now needed to do, assuming that sneaking around would be difficult if I only relied on the lie of getting updates on the production of our generators."

else:
    Sb "You could say that. Bryce is waiting for you outside."
    Lg serious flip "Got it. Well, let’s not waste any more time and get this entire ordeal over with."

    hide logan with easeoutright
    show sebastian at center with ease
    $ renpy.pause (0.5)

    Sb smile b "You wanted to go to the production facility, right?"
    c "Yeah. I need to check up on how the dragons are faring with the production of our generators."
    Sb normal b "I see. I haven’t heard too much about the situation revolving around that, but apparently they had some supply issues recently. Bryce would probably be able to tell you more about it."
    Sb smile b "Well, are you going to stand there all day or follow me?"
    c "Yeah, let's go."

    scene black with fade
    play sound "fx/steps/clean2.wav"
    $ renpy.pause (1.5)
    m "We both left my apartment without much haste. As we wandered through the streets, Sebastian seemed to be more relaxed than usual, slowly looking across the scenery and taking in the fresh air."
    scene town2 with fade
    $ renpy.pause (1.5)

    show sebastian normal b with dissolve
    $ renpy.pause (1.5)
    c "You seem to be in a more positive mood today."
    Sb "Yeah, I am. At least for now."
    c "How so?"
    Sb disapproval b "It’s because I can enjoy myself without having to worry about suddenly bumping into Logan by some random chance."
    Sb drop b "I don’t mean to sound rude here [player_name], but I don’t like the guy."
    Sb disapproval b "At least, not after our first encounter."
    c "Did something happen between the two of you that I’m not aware of?"
    Sb drop b "I’d rather not talk about it. Getting my personal thoughts involved when I’m supposed to be working throws my entire rhythm off." #Hmm, I wonder if Logan did a typical Logan thing and made Seb upset? We'll never know...
    c "I see."

    $ renpy.pause (1.5)
    scene fac1 with dissolve
    $ renpy.pause (1.5)

    m "In due time, we eventually reached the outside of the production facility. I looked at the building in a different light than when I first came here. Now, whatever I might find could determine whether Logan’s plan would be a success or the cause of humanity’s demise."

    show sebastian normal b with dissolve
    $ renpy.pause (0.5)
    Sb "Alright, we’re here. Need anything else?"
    c "I’ll be able to manage on my own."
    Sb smile b "Got it. I’ll be at the police station if you need my help. See you later, [player_name]."
    c "Goodbye, Sebastian."

    hide sebastian with dissolve
    m "Sebastian left the facility grounds, leaving me alone in the midst of the manufacturing facility. I considered what I now needed to do, assuming that sneaking around would be difficult if I only relied on the lie of getting updates on the production of our generators."

$ renpy.pause (2.5)
c "(Alright. Let’s see how this goes, shall we?)"
$ renpy.pause (1.5)

scene facin2 at Pan ((0, 250), (128, 250), 3.0) with dissolveslow

m "I walked into the production facility, hoping to find a somewhat easy way for me to scout for potential parts. After wandering through the halls, I eventually found someone who could point me to the area where the generators are being produced."
$ renpy.pause (1.0)
m "I carefully looked around to make sure nobody was nearby and entered a room presumably used for storing excess parts." #You're an ambassador. You could literally just ask and not provide a reason.

play sound "fx/door/door_open.wav"
$ renpy.pause (3.0)
scene kolfacilitysearch at Pan((0, 0), (0, 180), 4.0) with dissolve
$ renpy.pause (2.5)

m "The room was quite large, with several counters and cabinets containing what I assumed were various parts for various types of technological equipment, as well as some paperwork documenting them. It took some searching before I discovered a relatively secluded spot containing spare generator parts."
$ renpy.pause (1.5)
c "(Bingo. Now, let’s see here…)"
$ renpy.pause (0.5)
m "I went through all of the available parts. Unsurprisingly, I didn't recognise most of them, though there were a few that looked vaguely familiar. There also appeared to be blueprints documenting some of the parts as well as how a generator is supposed to be constructed."
m "Even if Logan can't do anything with these parts, the blueprints should be more than enough for whatever Logan has planned. A wave of relief washed over me as I realised there was still hope of avoiding the entire conflict between humanity and dragonkind."
m "Satisfied with my findings, I decided to leave the production facility and report back to Logan."

$ renpy.pause (0.5)
scene facin2 at Pan ((128, 250), (128, 250), 3.0) with dissolve
$ renpy.pause (0.5)
m "I casually walked through the many halls of the facility, making sure that I didn’t arouse too much suspicion from anyone. After a few minutes, I was back at the entrance."

$ renpy.pause (1.5)
scene fac1 with dissolve
$ renpy.pause (1.5)

stop music fadeout (2.0)
$ renpy.pause (0.5)
m "However, when I went outside, I noticed Logan standing next to a tree, whistling a vaguely familiar tune."

$ renpy.pause (0.5)
c "Logan."
$ renpy.pause (0.5)

show logan normal with dissolve
play music "mx/path.ogg" fadein (2.0)
Lg "And here you are. I thought I’d actually have to wait for some time, but it seems that our timing matched up quite well."
c "What’s the verdict?"

$ renpy.pause (0.5)
show logan serious with dissolvemed
$ renpy.pause (2.0)

Lg serious "The council has announced that the generators won’t be given to us as of right now, neither will you return to humanity."
Lg "The trade is, unfortunately, now cancelled."
c "Why? I don’t understand how this would benefit the dragons at all." #Because the dragons are playing Extinction Bingo and they're placing all their bets on you, MC.
Lg annoyed "Emera told me that everything would have to be used for and I quote: \"a very crucial turning point in our society very soon.\" The thing is, I understand her reasoning for keeping every generator she can while also keeping you here as some sort of all-knowing wizard or something."

$ renpy.pause (0.5)
show logan serious with dissolve
$ renpy.pause (0.75)

Lg "Now I need to resort to my backup plan. I’m not letting everyone die at home while I idly stand by and try to reason with brick walls."
Lg "Tell me, [player_name]. What did you find?"
c "There were quite a wide selection of parts, many of them I don’t recognise."
Lg "Anything familiar?"
c "A few parts looked somewhat like some of the things we had back home, but I can’t say much. You’d have to find out for yourself."

$ renpy.pause (0.5)
hide logan with dissolvemed
$ renpy.pause (0.3)
m "Logan walked around in circles, deep in thought over the news that I had given him. Suddenly, he stopped and closed his eyes, then looked at me with a dire expression."
$ renpy.pause (0.3)
show logan serious with dissolve

Lg "Was there anything else that you found that might be useful?"
c "Yeah. Blueprints."

show logan surprised with dissolve
stop music fadeout (1.5)
$ renpy.pause (0.75)

m "Logan’s face suddenly shifted to one of immense shock, as if this information had been a revelation that mortals shouldn’t be able to bear."

play music "mx/intrigue.ogg" fadein (1.0)

Lg "No, that can’t be right. Why would they…{w=1.4}{nw}" #Yes, I know this scene falls flat, okay? Visual novels are limiting.
$ renpy.pause (0.5)
Lg "But, perhaps it could’ve been…{w=1.5}{nw}"
$ renpy.pause (0.3)

show logan annoyed with dissolvemed
m "Logan started to ramble with himself, making mental note after mental note and speaking in a way that I generally couldn’t fully understand."
$ renpy.pause (0.3)
c "Logan! You alright?"
$ renpy.pause (0.5)
Lg "Oh? Uh, yeah, yeah."
Lg serious "[player_name], you have no idea how vital those blueprints would be. With them, I would be able to convince the authorities to give us just a bit more time while the dragons sort out their own astronomical problem." #Yes, that's a pun alright!

if kol_tlh_endingA_route == True:
    Lg normal "That’s not even considering the whole generator idea that you had."

Lg annoyed "Combined with the scrap that we’ve found back at home, we might be able to build a generator that has the potential to last long enough for the comet to be deflected while also keeping everyone back home alive."
Lg "No, wait. If we couple it with the spare parts, then people back home might be able to reverse engineer them as well."

if kol_tlh_endingA_route == True:
    Lg "And with that generator from Reza’s place, we might be able to somehow power everything and reconstruct several generators on our own. It probably won’t be enough to keep the entire city afloat, but it will be able to keep the vital stuff going on for long enough for the trade to be fully completed."
    Lg normal "[player_name], you’ve just given us a shot here." #I thought that they already did by suggesting that whole generator plan, though...
    c "Wait, but what about the dragons? I mean, they did formally announce that they won’t budge to humanity’s ultimatum, so in their eyes the trade is over."
    Lg smiling "Nothing about a potential \“reconsideration\” from humanity's side after I give them a new, current status."
    c "Smart."
    Lg normal "Nope. Just practical." # *Sure...*

$ renpy.pause (0.5)
menu:
    "So, what now?":
        $ renpy.pause (0.5)

        Lg serious "Now we'll have to try to make copies of those blueprints and send them back home to the authorities. Because I'm now the one who must inform everyone that the trade agreement has been \"cancelled,\" I may be able to persuade the authorities to extend the deadline we have with a few choice words."
        Lg "For you, I suppose you’d have to do whatever you can to keep humanity in a positive spotlight for as long as possible. If either side were to cut contact due to miscommunication…"
        c "I get it. I’ll do whatever I can to keep relations as good as possible."
        Lg normal "Thanks. I owe you one."

    "And now it’s all up to you to not mess this up.": #...why would you even say this? It doesn't even make sense...
        $ renpy.pause (0.5)

        Lg annoyed "…what?"
        Lg serious "You do know that I’m trying everything I can without provoking a war here, right?"
        Lg "This is {i}not{/i} something that I’m going to mess up just because I forgot to do something or accidentally said something that I wasn’t supposed to."
        c "Then keep it that way."
        Lg "..."

    "It’s only because of what you’ve told me to do.":
        $ renpy.pause (0.5)

        Lg "And yet you did the thing I told you to do flawlessly. It’s almost as if you actually want to help both humans and dragons and not just be a so-called traitor."
        c "Since when wasn’t helping everyone the thing that I’ve been trying to do?"
        Lg serious "Yeah, you do have a point. This will just make things harder on the convincing front, unfortunately."

$ renpy.pause (1.5)
c "I’ve just realised something. We’re not any better than Reza. I mean, here we are, planning to steal a few important things to benefit humanity." #Here we go...
Lg serious "Look, I know that this isn’t right, but we don’t have another choice. If we can’t convince the authorities back home, then our city will fall. Dragonkind will most likely be able to live on if they cut contact, leaving us the only losers in this deal."
Lg "Sometimes, you have to do something morally wrong so that many will be able to benefit from your actions. \"You have to be cruel to be kind\", as the saying goes."
Lg "If there was a better way to go about this, then I would go through with that. Thing is, I can only do so much without becoming a second Reza. Who knows what kind of hell would be caused then?"
c "..."
Lg "..."
$ renpy.pause (1.5)
c "There really isn’t any other choice, is there?"
Lg "I'm afraid not."
$ renpy.pause (1.0)
c "Alright, fine. We’ll do this." #If only Reza was as successful as Logan...
Lg normal "Good. Thanks, [player_name]. I know this isn't exactly easy for you to do."

stop music fadeout (4.0)
$ renpy.pause (0.5)

Lg "I'll have to leave right now to rethink my strategy. If everything goes as planned, you can expect a knock on the door tonight."
Lg "I’ll be at my apartment if you suddenly come up with any new ideas that can help."

show logan normal flip with dissolve
hide logan normal with easeoutright
$ renpy.pause (0.5)

c "Wait!"

$ renpy.pause (1.5)
show logan normal with easeinright
Lg "Yeah?"
c "Where {i}is{/i} your apartment? You’ve never told me where Emera made you live."
Lg "It’s on the other side of town. Pretty close to the university, actually. You’d be able to find it."
c "University? What are–{w=0.65}{nw}" #Ditchin' confused slackers since 20XX

show logan normal flip with dissolve
hide logan with easeoutright
$ renpy.pause (0.5)

m "Logan had already started walking before I could finish my sentence, leaving my unspoken confusion hanging around me. I tried to recall if a university was mentioned at any point during my stay, but nothing came to mind."

if kol_tlh_bryce_escort == True:
    c "(I suppose that I’ll just have to ask Bryce where he lives, then.)"

else:
    c "(I suppose that I’ll just have to ask Sebastian where he lives, then.)"

$ renpy.pause (0.45)
m "With nowhere else to go, I decided that I should go to the library and ask Remy for help in figuring out any useful information that could help me with my new mission."

play sound "fx/steps/rough_gravel.wav"
scene black with fade
$ renpy.pause (4.0)
stop sound fadeout (2.0)
scene library at Pan ((640, 228), (0,228), 10.0) with dissolveslow
$ renpy.pause (3.0)
play music "mx/genesis_kol.ogg"

m "As was routine by now, the library was desolate this early in the morning. An eerie feeling of tranquillity permeated the floors of the library, making the entire building feel almost nostalgic."
m "I looked around to see if I could find Remy, but my efforts were futile. Finally, I decided that I should look for any resources myself. I went through hall after hall, browsing through the library's categories. I eventually came across something that caught my eye."
m "I found a small section filled with scrolls and small books that appeared to be from the \"Human Literature\" section. Further inspection showed that there were claims that some of the stories were written by the human creator of dragonkind itself."
m "Unfortunately, I had no idea whether these stories were written down and mass-produced for the general public's entertainment or education, nor whether these claims had any credibility at all."

menu:
    "Browse through the section.":
        $ renpy.pause (0.5)

        m "Despite my apparent scepticism, I was mildly intrigued by what literature the dragons had, regardless of whether they were actually written by humans or not."
        jump tlh_readingstuff

    "Keep searching.":
        $ renpy.pause (0.5)
        m "Regardless of how interested I was in seeing what this section of the library had to offer, I had no time to waste going through unnecessary things."
        jump tlh_Chapter3A_continued2



label tlh_readingstuff: #USE {size=30}text_here{/size} if you want to get it to fit into one screen
scene library at Pan ((0, 228), (0,228), 3.0) with dissolvemed
$ renpy.pause (1.0)
stop music fadeout (1.0)
$ renpy.pause (1.0)

menu: #Yes, these are all horrible stuff that I wrote in the past. Why didn't I write some stories that are more fitting for the game? Because I'm one hell of a lazy bastard, that's why.

    "[[Starlight]":
        $ kol_tlh_read_stories = True
        scene black with dissolveslow
        nvl clear
        window show

        play music "mx/starlight.ogg" fadein (1.0)

        n "Look, for the world has turned dark once more. Just like it has for countless eons, and will continue to do so for countless more. I remember when you asked me for the first time about why such a thing could ever matter, and I answered that question the same way I still do now; The way I always have:"
        n "\"Time is all around us, whether it be in our conscious mind, our dreams or our memories. Often the passage of time corrodes us on who we are and who we were, leaving us as nothing more than hollow shells when our time has run out. All you can do is to try and resist this; never can you stop the degradation that happens with time. My favourite of these ways is by forming important memories."

        window hide
        nvl clear
        window show

        n "\"Time can fly away like a forgotten breath in a whirlwind of laughs or stand strong and slowly erode into rubble, but memories linger with you for as long as you can hold on to them. With memories, one can recall thousands of instances of joy, of grief, and of nostalgia. Through these, time will appear to slow for as long as you desire. Thus, it will always be wise to create memories to ward off the ruining of time.\""
        n "You looked confused after I told you that. You always did. Do not worry; I believe that you will understand what I said one day. Hopefully before it is too late."

        window hide
        nvl clear
        window show

        n "Come now, for the clock has struck twelve. You tell me that you need to sleep; tomorrow will be a busy day. I plead, for you know that I cannot accept that. This is the last time I will see you. Maybe forever."
        n "Of all the experiences that I have made important memories of, I believe that I made the least with you. I always figured that you would never leave my side until the day I die. Alas, how the burden of hindsight pains me now, knowing that it was my ignorance that led to my regret!"
        n "Do you hear that? Rain has started to fall, rejuvenating the earth and all that dwell upon and beneath it. Now, only this moment remains. You tell me that you shall return when you have finished your obligations, but I know better. You smile, thinking of all the opportunities and fun you will have out there, not knowing that those same opportunities will cause you to fall."

        window hide
        nvl clear
        window show

        n "I ask you to dance with me during this idyllic night. You reluctantly agree, if only to see me happy, and you would be correct; I am beyond delighted! I played that one album which you constantly rave about, and smiled. Our tastes in music may differ, but I'll sacrifice anything for that beautiful smile of yours."
        n "We slowly walk around the room, dancing around in the grasp of each other to the calming flow of the music. I smile, hoping that this moment will live on in the form of memory for as long as I live; something to revisit in my darkest of hours. May the moonlight shine through the window and this music softly play in the background while the heavens are illuminated by starlight wherever you go, and may I remember you in this moment for all eternity; long after you're gone."

        window hide
        nvl clear

        jump tlh_readingstuff

    "[[Gravity]":
        $ kol_tlh_read_stories = True
        scene black with dissolveslow
        nvl clear
        window show
        play music "mx/gravity.ogg" fadein (1.0)

        n "Your time has come. The state has found you guilty for treason, and thus you should be put to death. According to the law, you shall now be hanged at the gallows in one hour’s time by me. Chances are, you think me a heartless monster; a beast that thrives off of the torment of those about to take their last breath. If you believe that, then you cannot be further from the truth."
        n "The public always see the executioner as someone who should be feared; someone who shall seal your fate if you do anything incorrect, such as breathing strangely in the presence of one. Do you not think that I am as human as you are with my own thoughts, feelings and morals?"

        window hide
        nvl clear
        window show

        n "Many would think that after so many deaths, one would become desensitised by such a thing, but one never does. Death is the one thing no mortal can ever become used to, regardless of the amount. No man should ever have the power over hundreds of lives with something as simple as a pull of a lever, or of a swing of an axe."
        n "Sometimes, I can still hear their cries and thoughts during my slumber; the intense panic just before their deaths, or the struggles and gasps for air of those hanging by a noose. Those who were innocent hurt the most for me. I knew that they did nothing wrong, and yet I still needed to fulfil my duty in the name of the state. And yet, who am I to resist, especially if I’m as expendable as the victims of my work?"

        window hide
        nvl clear
        window show

        n "I have long since abandoned the concept of hate towards an individual. Whether they have committed an egregious act or not, they still deserve to live. Think about it: from your perspective, you did nothing wrong, as you did what you believed was the morally correct choice. The state, unfortunately, saw your acts as the acts of one who commits treason, and thus here you are before me. It would make you innocent from your perspective, but guilty from that of the state. Quite the predicament we find ourselves in, correct? I believe that no man can ever truly be considered guilty as long as their reason can be justified via morals, or perhaps something else entirely. Sadly, not many share my views."

        window hide
        nvl clear
        window show

        n "We all have our own personal code in life, and only the one who follows it can ever hope to change it. If you’re lucky, your laws might align with those of the state, leading to both parties being satisfied. More often than not, however, this is not the case. The fact that both of us are speaking now proves that theory. So few can ever truly understand the gravity of such a situation until the shining clarity one receives right before death, or if one witnesses the petrifying gaze of annihilation for so many times in one’s life. I guess it truly is better if one persists in the ignorance of one’s own actions and beliefs to escape the harsh reality of enlightenment."

        window hide
        nvl clear
        window show

        n "I do wish I could redirect a sense of hatred towards something. Anything. It would make my job so much easier, and far less horrifying. Sadly, I bear the cruel wisdom of morals and the justification thereof, which you now bear with me. Not that it would matter soon for you. To be able to channel your hatred into an object before its extermination from the face of the earth is a blessing in disguise that few ever seem to be able to comprehend. I envy them."
        n "..."
        n "It seems that your time has now come. Follow me, for a crowd is waiting for us at the gallows. Do not panic, for it shall avail you nothing, and bring joy in the faces that will take pleasure in your departure. Do not fear, for I shall remain at your side until the very…"

        nvl clear
        n "...last…"
        nvl clear
        n "...second."

        window hide
        nvl clear

        jump tlh_readingstuff

    "[[Ethereal]":
        $ kol_tlh_read_stories = True
        scene black with dissolveslow
        nvl clear
        window show
        play music "mx/eveningmelody.ogg" fadein (1.0)

        n "It seems that the day has finally arrived; the day you constantly fantasise about. And yet, I can’t help but share your enthusiasm. To a certain degree, naturally. You always had an effect like that on me. Just goes to show how much I’ve changed when I first met you."
        n "The day of Lady Romance is upon us once more, being an ever constant reminder of the wonders of love, and the compassion we share to those we deeply care about. For me, I do not need such reminders; not when you are by my side, guiding me through life’s fire and war; through euphoria and melancholy."
        n "I recall the day you first shone your glamorous smile my way; the same way you still continue to do now. One would think that much would change between now and then, but time has proven for that not to be the case. Your actions, your love, your smile; they all still reignite the same hearth in my soul as they first did so many years ago."

        window hide
        nvl clear
        window show

        n "In all honesty, I would most likely be lost without your gentle guidance. Through the smoke and the fading embers of the world, you always seem to be within arm’s reach should I fall. For how could the world shatter that which has been bound with ties stronger than steel? Regardless of this world’s efforts, you’re always gently nudging me through storms and hardships. Just another case of your love being more pure than the world’s most evil corruptions."
        n "Your love sets me free from agony and from despair. How could I ever go on to how I was before? This might sound strange, but to me, you are the embodiment of hope; both for the present and the future. Without you, life will lose its meaning; its colour fading away to a monotonous grey, eventually reverting to its true nature; an uncanny black void."

        window hide
        nvl clear
        window show

        n "You mean far, far more to me than you could ever imagine."
        n "..."
        n "Oh, but forgive my rambling. You most likely already know all of this. Love causes us to share one soul; what I feel, you know, and vice versa. Let’s not waste any more time on this valuable day. Come; let the ethereal roads of love guide us to prosperous beauty. Come; for I cannot leave without someone like you at my side."

        window hide
        nvl clear

        jump tlh_readingstuff

    "[[Solitude]":
        $ kol_tlh_read_stories = True
        scene black with dissolveslow
        nvl clear
        window show
        play music "mx/martyr.ogg" fadein (1.0)

        n "Here you are, alone in your room once more. Isn’t it comforting? To stay awake in the dead of night while being alone, pondering about your reality, your circumstances, and what you’ve done and will do? The darkness is tempting in this regard, I know. It’s almost sweet in a sense, for it consistently feeds you half-lies and warped perceptions."
        n "After all, it’s in these twisted concepts that comfort is found, no? One rarely ever finds full peace in truth alone. There’s always something hidden; something to turn you biassed. Why do you think that the raw truth hurts and that lies create a sense of false confidence? Surely you can’t believe that it’s because of what is being said to you, right? No, it’s more than that. You don’t want to escape the half-baked world you made for yourself."

        window hide
        nvl clear
        window show

        n "You would be surprised at the damage that this had caused to many a poor soul, and you’d be surprised to know how many still continue with this, even when knowing better. I do not envy them, nor should you. Follow me, will you? I need to take you to some place. A place you know all too well, yet one that feels alien to you."
        n "You ask me why, and I say this: you cannot be shrouded in your own lies like a lead linen around yourself. You are too special for such a cloak. This is why I’m taking only you, and not one that shares your type of burden. For you, change is still possible. You have yet to fall as deep as some of the souls that I had the misfortune of encountering."
        n "I know that you’d detest me for what you’re about to see, but so had many before you. No, I won’t tell you. Why ruin the surprise already?"

        window hide
        nvl clear
        window show

        n "Here we are."
        n "Figured. Your face says it all. Trust me when I say that this is the best cure for your ailment. All these individuals had gone through similar thoughts that you did, and look at them now. Do you not feel envy for their glee, their carelessness, their contentment? Of course you do. You crave an escape. After all, why would you sit alone in your room at such an unorthodox time in the first place were it not the case?"
        n "Go now, break your solitude and find support. These individuals will slowly chip away at your half-lies until you can find solace once more. Shed away your depraved mind that had been dipped in untruth’s chaos and become whole once more. Feel the light of hope, and bask in it."

        window hide
        nvl clear
        window show

        n "I shall give you a final gift before I leave your sight. Stay with these individuals during times of strife, and fall back to them whenever the void of immorality sets in. Father Circumstances cannot be bested by one knight. This was never how any story had ended. May your lonely half-lies be replaced by a communion of full-truths, my old friend."

        window hide
        nvl clear

        jump tlh_readingstuff

    "[[More options.]":
        menu:
            "[[Guardian]":
                $ kol_tlh_read_stories = True
                scene black with dissolveslow
                nvl clear
                window show
                play music "mx/library.ogg" fadein (1.0)

                n "Rain crashes upon the fertile soil of this land while the darkness of dusk slowly grows. I can feel the wild calling to me, and yet falling to that seductive call will break the very oath I swore to you. You probably can’t even remember it, can you? Well, I suppose that it simply won’t matter anyway. Oh, don’t try to think about that now, dear. Bask in the glory of the scene which we find ourselves in right now."
                n "My past is one of troubles, yes, but that simply won’t be the thing that will lead to my eventual downfall. Letting fears, agonies, and temptation’s grip of previous times of strife take their hold of me will cause me to fail in my duties. I bet you wouldn’t want that, now do you? No, you still have those blissfully ignorant cheeks contorting into joy when I’m here with you. Heh. I suppose that just means I’m doing my job correctly."

                window hide
                nvl clear
                window show

                n "Hush now. Listen to the soft pattering of Heaven’s grace cleansing us of our sins while we stay here, gazing at the setting of humanity’s hope, turning to an illuminated void. Enjoy this while you can; at least, while I’m still able to enjoy it with you. Your peaceful mind shouldn’t bear witness to what will happen to me; only the things that have happened between us should be remembered. All those wonderful times we’ve spent in similar moments like these? Hold on to those memories as tight as you can and never let go. They shall serve you faithfully when realisation has arrived."

                window hide
                nvl clear
                window show

                n "Yes, the fact of what will happen to me will cause the very foundation of my oath to shatter into a million grey shards, piercing the souls of many a future historian looking back upon this tragic tale of a justified false hope. Well, at least you’ll be remembered for as long as I’m being studied for. A double edged sword, to an extent; you get to live on in legend for all eternity as one who was able to convert one as wretched as me, but only due to the pain that you’ve endured when you were still an unconscious babe."

                window hide
                nvl clear
                window show

                n "No, no. Do not look at me with melancholia painted within your eyes. I have done all that I could, and will do all that I am able to do now. Or tomorrow. Or whenever the time to break my oath comes. At the latest? Soon. Now, take solace in the depravity that you will find yourself in within due time. Know that, whether you’ll be, I was able to have finished my job to the best of my ability."
                n "..."

                window hide
                nvl clear
                window show

                n "Rest. The heathen-oathkeeper needs to prepare for the forsaking of his duties; for the betterment of all. Despite the pain that I have sown across the land, I shall serve as your guardian still, protecting the hope of your survival for one last time. Rest, for not only have you caused me to turn, but you have given me the will to protect that which I would have otherwise destroyed. For as long as I have you in my memory, I shall bleed, knowing that I can protect you from the same wrongdoings that I have committed against those you admired."
                n "Rest, friend."

                window hide
                nvl clear

                jump tlh_readingstuff

            "[[More options.]":
                jump tlh_readingstuff

    "Finish reading." if kol_tlh_read_stories == True:
        jump tlh_Chapter3A_continued2


label tlh_Chapter3A_continued2:

if kol_tlh_read_stories == True:
    play music "mx/genesis_kol.ogg" fadein (2.0)

m "As I turned around to continue my search, I noticed Remy walking towards the bookshelf I was standing next to."

show remy normal with dissolve

Ry "Good morning, [player_name]. Are you perhaps making a habit of visiting the library so early?" #Yes, because yes.
c "Well, the library is a pretty relaxing place to be in before I start the day."
Ry smile "I suppose it is."
Ry normal "Oh, I see you were looking through the human literature section. Was there something that caught your interest, by any chance?"

if kol_tlh_read_stories == True:
    c "I did read some of the things in there, yes. It’s interesting to see what dragons would consider as human literature."
    Ry "I suppose it is. Considering that we don’t know what humans are actually like, I would put my guess that those stories were some of the best insights that we had about humans in general."
    Ry "I even went through all of them when originally preparing for your arrival. Though, now that I got to meet you, I don’t think that those stories are entirely accurate."
    c "It depends. Some of them are more accurate than others in terms of delivering a message, sure, but I wouldn’t discredit all of them. If they were written slightly differently, they could pass for professionally human-written material. I think they're probably meant to teach dragonkind a lesson or something like it."
    Ry smile "Very interesting, then."

else:
    c "The fact that there is an entire category dedicated to human literature caught my interest."
    Ry "Is that so?"
    Ry smile "Well, I suppose that you would have a great interest in seeing what we as a species perceived humans as, especially if there were claims that some of those stories were written by an actual human."
    c "Yeah."

Ry normal "Now, was there anything that I could help you with?"
c "Actually, yes. I’m looking for a specific resource regarding electronic parts."
Ry smile "We have many resources."
c "Anything about generators?"
Ry normal "We do. Please, follow me."

$ renpy.pause (2.0)
scene kolextralibrary with dissolve
$ renpy.pause (2.0)
m "Remy led me through the halls of the library, making turn after turn past the corridors as elegantly as an ice skater. Eventually, we reached a corner far from the initial entrance of the library with a few tables and several bookcases."
$ renpy.pause (1.5)
show remy normal with dissolve

Ry "Here we are. Here you’ll find many resources about generators, such as part names, how they are used and how they are manufactured."
Ry look "Forgive me for asking, but might I ask why you’re interested in researching generators?"
c "I figured that I should try to expand my knowledge about generators should something pop up in the future."
Ry "I...{w=0.4} understand." #He's already on to you and he won't even admit it.

if kol_tlh_2Bplayed == True:
    $ renpy.pause (0.5)
    c "Out of curiosity, have you met Logan yet?"
    Ry "No, not yet. I’ve been too busy as of late."
    Ry shy "As you might already have figured out by now."
    Ry normal "Though, since I’m mostly finished with my work for the council for the time being, I should be able to make some time. Maybe you should come along when we meet up. Just in case."
    c "Sure."
    Ry "Thanks, [player_name]."

Em ques "REMY!" with vpunch
Ry look "I’m sorry, but I need to go now."

$ renpy.pause (0.5)
hide remy with easeoutleft
$ renpy.pause (0.5)

m "Remy hastily went through the halls again without uttering a further word, leaving me alone with the books I had at my disposal."
$ renpy.pause (0.5)
c "(Well, I better start working. I won’t learn anything if I just stare at closed books.)"

scene black with fade
$ renpy.pause (1.5)
m "Several hours of studying later, I started to grow weary going through all the books at my disposal. Despite trying my best to understand what had been said, most things were simply beyond my comprehension. I did however make a few notes on a piece of paper to show to Logan, in the hopes that it would help him out in any way."

$ renpy.pause (1.5)
scene kolextralibrary with dissolvemed
$ renpy.pause (1.5)
m "I eventually got all my things ready and left the library."
$ renpy.pause (1.5)

scene library at Pan ((0, 228), (0,228), 10.0) with dissolve
$ renpy.pause (3.0)
scene koloutsidelibrary at Pan ((0, 180), (0, 180), 5.0) with dissolve
$ renpy.pause (2.0)

m "I strolled through the streets, letting my mind wander about the stressful times I had found myself in. If I make a single error, then it might cost me in ways that I cannot even begin to imagine. My resolve to do everything I can for dragonkind was boosted, as I hoped that there could still be something negotiated between the dragons and humanity."

$ renpy.pause (2.0)
scene town3 with dissolve
$ renpy.pause (2.0)

m "As I continued on my walk, I started to hear footsteps coming my way from behind. I stopped and turned around to see who was following me."
c "You know that you could just greet me normally, Maverick." #Heh, even the MC is getting tired of Mav trying to turn AwSW into a stealth game. SHould've used a cardboard box tbh.

show maverick normal with dissolve

if kol_tlh_bryce_escort == True:
    Mv "And shouldn’t you be accompanied by Bryce?"
    c "I was, though Bryce had to-{w=0.7}{nw}"
else:
    Mv "And shouldn’t you be accompanied by Sebastian?"
    c "I was, though Sebastian had to-{w=0.7}{nw}"

Mv "Rhetorical question. I know what’s going on back in the office."
Mv "That’s why I’m here. The Minister herself wants to talk to you as soon as you are able to."
c "I see. Best be on my way, then. What a shame that I was just going from the library as well."
Mv nice "You poor soul."
Mv "Now, best you be going."

hide maverick with dissolve
$ renpy.pause (2.0)
c "Before you go, I need to ask you something."
stop music fadeout (4.0)

show maverick annoyed with dissolve
Mv "What is it with you and questions? Are all regular human ambassadors so nosy, or is it just a trait that you seem to wear with pride?"
Mv normal "Very well. Ask."
c "Did Bryce ever talk to you about Reza?" #What a touchy subject that totally needs to be talked about right now. Totally.
Mv angry "That is none of your business. All you need to know is that I’m still here for the foreseeable future."
Mv normal "It would be wise not to ruin this peace between us." #Stalking and creeping up on you from behind is peace, right?
Mv "Now, stop wasting time and go to Emera. This is supposedly a critical meeting about what we’re supposed to do with the comet."

hide maverick with dissolve
m "Maverick walked away in the direction that he came from. Even though I still wanted to ask him more questions, I figured that it wouldn’t be a good idea to do so, even if I didn’t have to see Emera. Regardless of my feelings, I made my way to Emera’s office with haste."

$ renpy.pause (1.5)
scene buildingoutside at Pan((0, 0), (0, 0), 0.0) with dissolvemed
$ renpy.pause (0.5)

c "(Well, here’s the building. I don’t think that I’ll ever get used to being here.)"

$ renpy.pause (0.5)
show corridor with dissolvemed
$ renpy.pause (1.75)

m "I made my way to Emera’s office with the help of some directions from the receptionist. Anxiety filled me as I dreaded what Emera might say despite already knowing what our meeting will be about. Eventually, I had enough courage to knock on the door."

play sound "fx/knocking1.ogg"
$ renpy.pause (2.0)
Em normal "Come in."
$ renpy.pause (1.0)
play sound "fx/door/door_open.wav"
$ renpy.pause (1.0)
scene emeraroom at Pan ((0, 0), (0, 180), 5.0) with dissolveslow
$ renpy.pause (2.5)
play music "mx/decay_kol.ogg" fadein (3.0)

m "I walked into Emera’s office. A sense of formality hung in the air which, combined with Emera’s steady gaze at her office desk, made my supposed welcome feel all the more artificial."

show emera frown with dissolve
Em "Good day, [player_name]. My apologies for bringing you here on such a short notice, but this is of the utmost importance."
Em "It concerns about the supposed ultimatum that humanity has declared, and our plans against the impending comet."
c "So I've heard."
Em ques "I see that Logan has already talked with you, then. I’ll give you the short version of the speech I gave him to save us both some time."
Em frown "We have decided to decline the trade altogether. Having all the generators that we can muster will prove essential in stopping the comet. Returning you would also prove quite difficult, as you are a valuable part in our plans to redirect the comet thanks to your knowledge."
Em "Returning you would pose a significant risk to our success."
c "..."
Em normal "Thus, we have informed Logan that we will return all the PDAs that we had received from humanity. Any knowledge we have extracted from them up until now will also be destroyed to keep the cancellation of the trade as fair as possible."
Em "We believe that having you here will help us with the deflection of the comet more than what the PDAs would, especially if you were to take the time we have left into consideration."
Em "I hope that you can understand this situation, and I apologise for any inconveniences that this might cause."

menu:
    "Why didn’t you ask me before making such a decision?":
        c "My apologies if I’m speaking out of line, Minister, but I need to ask: why did you decide to keep me here regardless of how I felt about the situation? What if I wanted to voluntarily offer myself so that the trade could continue?"
        Em ques "I wanted you to go back to humanity to continue the trade, but the council had decided otherwise."
        Em "Everyone agreed that having you gone would be too dangerous. There would have been chaos between humanity and dragonkind if there had been no bridge between the two, leading to misunderstandings that could have resulted in the trade being cancelled despite our decision."
        c "You know that such reasoning is mental gymnastics, Minister. Why didn’t you oppose this with everything you had?"

        show emera frown with dissolve
        $ renpy.pause (1.0)
        Em "It’s too late to do anything now, [player_name]. It is what it is."

    "Cancelling the trade has made Reza’s victims die for nothing.": #Such a harsh truth, but accurate nonetheless.
        c "Having the trade cancelled means that everything that both me and the police force had done in the investigations were for nothing. Reza’s victims had died in vain."

        show emera mean with dissolve
        $ renpy.pause (1.0)

        Em "Do you think that I wanted this outcome, Ambassador? I tried to continue the trade as is, but the council disagreed with every statement that I had made, claiming that every argument against the cancellation of the trade would put our plan to stop the comet in jeopardy."
        Em "I wanted the best for our people, and so did the council. It is tragic that Reza’s victims had died, yes, but if we wanted to save any more lives, then we had to minimise the risk that had possessed our society."
        Em "Sending you home or delivering our generators at this time would have significantly increased said risk."

    "How could a single human have more knowledge than all the PDAs?":
        c "How did you and the council think that I would be more helpful in your plan to redirect the comet than all of humanity’s knowledge combined?"
        Em ques "It was because we believed that your insight to the comet would prove more valuable than knowledge alone. Knowledge would have helped us more, yes, but we could not have determined whether the information stored in the PDAs would have been fully relevant."
        Em normal "With you, we could validate our plan’s estimated success based on your insight and unique perspective. Besides, we have more than enough resources to construct a plan to redirect the comet."
        Em "The PDAs would have only confirmed what we already knew and given improved ways of utilising the resources that we have at our disposal, not necessarily guarantee the success of our plan."
        Em "Do you now understand why we kept you here instead?"
        c "I suppose."
        Em "Good. That will make the rest of this meeting easier for the both of us."


$ renpy.pause (1.0)
Em normal "Now, to address the other blatant problem that I’ve called you for."
c "Did the council come up with a plan yet?"
Em ques "If we hadn’t, I would not have called you here, [player_name]." #Yes you would. You would've needed to talk about the cancellation of the trade regardless.
Em normal "As you might have guessed, we’ll be using any generator in the underground facility like you have mentioned. That will be our main source of power."
Em "Once the generators are secured, we will issue a public call to connect any spare generator to the public power grid by installing ports in every city and town in our society. The power generated by these generators would then be routed through these ports to a large station, which would use the collected energy to reroute the comet's path."
c "How would you be able to convince every dragon to connect their generators to the public grid?"
Em frown "That’s the part where we are still stuck on. Options range from propaganda to potentially causing mass hysteria by telling the truth."
$ renpy.pause (1.0)
c "How well does the public know about what Reza had done?"
Em "What do you mean?"
c "Does the public know about the murders?"
Em "No. The situation that had surrounded Reza is still classified information."
c "And would you say that most dragons expect some kind of miracle from me and Reza like the supposed human that had created dragonkind?"
Em "Most, but not all."
c "Then use that to your advantage. Make a story about there being a huge threat coming, but the two so-called mystical humans can stop this threat if only the dragons had connected their generators to the main grid for the humans to somehow use."
$ renpy.pause (1.5)
Em normal "I will forward that idea to the council for debate. Perhaps we could come up with something similar that would be able to work on a scale large enough for us to gather all the energy we need."
Em "I thank you for the idea, Ambassador. This is evidence that the council had not made the wrong decision."
c "As long as this works, Minister. I just hope that everybody back home would be able to hold on long enough so that something could be worked out."
Em ques "Yes, it is a shame what fate humanity might potentially succumb to, but I believe that they will somehow find a way. Humans seem to be quite the tenacious species."
Em normal "Now, I believe that it is time to inform the rest of the council what has transpired here. Good day, [player_name]."
Em "You are dismissed."
c "Good day, Minister."

hide emera with dissolve
$ renpy.pause (0.5)
show corridor with dissolvemed
$ renpy.pause (1.75)

m "I left Emera’s office with an unusual sense of relief knowing that, despite the cancellation of the trade without my voice being heard, there was a plan in the works to redirect the comet."
stop music fadeout (5.0)
$ renpy.pause (0.5)
scene black with fade
$ renpy.pause (0.5)

m "As I walked home, I still couldn’t find comfort in knowing what would happen to everybody back in the city. Sure, they might be able to do something with all the scrap resources that they now had as well as the PDAs to guide them, but I felt that everything they had wouldn't be able to indefinitely sustain the city."
m "I entered my apartment and took a seat, wondering about the future of both humanity and dragonkind. Failing to see how the cancellation of the trade would do any true good in the long run, I eventually let my thoughts wander for a few moments."

$ renpy.pause (1.75)
scene o at Pan((0, 0), (0, 250), 5.0) with dissolveslow
$ renpy.pause (4.0)
play sound "fx/phonering.ogg"
stop music fadeout (4.0)
$ renpy.pause (3.0)
stop sound
play sound "fx/phonepickup.ogg"
$ renpy.pause (1.75)

c "Hello?"
play music "mx/stride_kol.ogg" fadein (2.0) #Yo look, it's the classic Logan theme! I'm sure what's about to happen will totally be fun!
Lg normal "Why, hello [player_name]. I was wondering if I would catch you in time or whether I would have to leave a message."
c "Wait, you knew about my meeting with Emera?"
Lg smiling "Only because I heard it from someone who heard from the same someone who told you."
c "That’s totally not confusing."
Lg normal "I’m just pulling your leg. Don’t you think that it’s obvious that Emera would want to talk with you after she already spoke to me?"
Lg smiling "But that’s irrelevant now. I assumed that today must have been absolutely nerve-wracking for you, no? Life must have caused you a clouded mind."
c "What are you implying, Logan?"
Lg normal "Well, I’ll be going to the bar soon with Bryce. You coming?"

menu:
    "I’ve got better things to do.":
        $ kol_tlh_nodrinkingwithlogan = True
        $ renpy.pause (0.5)

        Lg annoyed "Oh, that’s a real shame. I would’ve thought that the booze would do you some good to relieve your stress."
        c "I’d rather stay sober for now. Got some things on my mind that need clearing up." #Oh, the irony.
        Lg "Fair enough. Well, see you tonight if I’m able to. Emphasis on {i}\"if I'm able to.\"{/i} If I'm not at your place by one o' clock, then go to sleep and pretend that nothing had happened."
        c "Yeah..."
        Lg normal "Welp, see you around."
        c "The same to you, Logan."
        $ renpy.pause (1.75)

        if kol_tlh_endingA_route == True:
            c "(Let’s just hope that Logan doesn’t mess his entire plan up when he gets the generator. Or the spare parts and blueprints, for that matter.)"
            m "I wished that we didn’t have to resort to stealing to save both societies, but this was the best option that we had now that Reza had jeopardised our mission with his drastic actions, or with the council’s decision to cancel the trade."
        
        else:
            c "(I still can’t believe that Logan wants to steal the spare parts and blueprints I found. There just has to be a better way somehow…)"
            c "(Well, I suppose it’s too late now.)" #Reference to another route?! Here?!?!?! MADNESS!!!

        

        $ renpy.pause (0.5)
        m "With nothing better to do until the fateful moment where Logan would knock on my door late at night, I decided to have the rest of the day to myself by reading the now slightly dusty books on my bookshelf."

        $ renpy.pause (0.5)
        scene black with fade
        $ renpy.pause (0.5)
        stop music fadeout (2.5)
        $ persistent.kol_tlh_chapter3A_skip = True

        if kol_tlh_endingA_route == True:
            jump tlh_Chapter3_EndingA #Start of the Ending A route

        else:
            jump tlh_Chapter3B
            # ===========================================
            # END OF CHAPTER 3A
            # ===========================================

    "I suppose I can come along for a bit.":
        $ renpy.pause (0.5)

        Lg smiling "Good to hear that you’re willing to have some fun."
        c "Just remember to not drink so much that you pass out. You wouldn’t want to put your own plan at risk due to being blackout drunk."
        Lg normal "I’ll try to keep it in mind. See you in about an hour, if that’s alright with you."
        c "Yeah, it should be good. See you."
        Lg "Right. Goodbye."
        $ renpy.pause (1.75)
        c "(I’m going to have to drag him back to his home, aren’t I?)" #Well yes, but actually no.
        m "Considering that I had some time left until I had to go, I spent what little time I had to myself wondering about how everyone was doing back home and how they would take the news of the trade being cancelled."

        $ renpy.pause (0.5)
        scene black with fade
        $ renpy.pause (0.5)
        stop music fadeout (2.5)
        $ renpy.pause (0.5)

        if kol_tlh_bryce_escort == True:
            m "Eventually, the time had arrived to go to the bar and meet up with Logan and Bryce. I called for Bryce to escort me to the bar, and within minutes he had arrived at my door."
        else:
            m "Eventually, the time had arrived to go to the bar and meet up with Logan and Bryce. I called for Sebastian to escort me to the bar, and within minutes he had arrived at my door."

        $ renpy.pause (1.5)
        scene o4 at Pan ((0, 250), (128, 250), 3.0) with dissolveslow
        $ renpy.pause (1.5)
        play music "mx/vines_kol.ogg" fadein (1.0)

        if kol_tlh_bryce_escort == True:
            show bryce normal with dissolve

            c "Hey, Bryce."
            Br "Hey. You ready to go?"
            c "Sure am."
            Br smirk "Good to hear. Let’s have some fun, shall we?"

            $ renpy.pause (0.5)
            scene koltowndusk with dissolve
            $ renpy.pause(1.0)

            c "It’s interesting that you’re willing to spend another evening at the bar with Logan."
            show bryce normal with dissolve

            Br laugh "What can I say? I’m starting to really like the guy."
            Br stern "It’s just a shame that he’s been thrown right in the middle of this mess with the comet and whatnot."
            Br smirk "At least we can keep the beer flowing."
            c "I don’t want to sound rude, but don’t you think that you’ve been drinking quite a lot recently? I mean, it was just a while ago when you had a drinking competition with Logan, and now you’re presumably back to do some more heavy drinking. I can’t imagine that it would be good for you."
            Br stern "Trust me, I’m fine. I just like spending time at the bar, that’s all. You should know me by now." #Drink the sorrows of the future away...
            c "Alright, alright. Let’s just hope that I don’t have to drag you back to your apartment again."
            Br laugh "I won’t drink that much this time. I’m supposed to be working an extra shift later today."
            c "If you’re still working, then why are–{w=0.8}{nw}"
            Br stern "I can take it, alright? It’s just gonna be a few bowls, that’s all. Something that will get me through."
            c "…if you say so, Bryce."

            $ renpy.pause(1.0)
            scene koloutsidebar with dissolve
            $ renpy.pause(1.0)
            show bryce normal with dissolve
            $ renpy.pause(1.0)
            stop music fadeout (3.0)

            Br "In any case, we’re here. Ready for some lighthearted banter around a few glasses?"
            c "If I wasn’t, I wouldn’t be here."
            Br laugh "Fair point."

            $ renpy.pause(1.0)
            scene koleveningbar with fade
            $ renpy.pause(1.0)
            m "Me and Bryce entered the bar and found that Logan had already found a seat in one of the corners, waiting patiently for our arrival."

            play music "mx/clouds.ogg" fadein (2.0)
            show logan normal at Position (xpos = 0.75)
            show bryce normal flip at Position(xpos = 0.25)
            with dissolve

            Lg "Hey. I was wondering if you’d even show up at this point."
            c "Well, you’re here quite early, so it’s your own fault for waiting so long."
            Lg annoyed "True."
            Br smirk flip "Well, the wait is now over. It’s time to have some good ol’ fashioned fun."
            Lg normal "Agreed."

        else:
            show sebastian normal b with dissolve

            c "Good evening, Sebastian."
            Sb "Good evening. Are you ready to go?"
            c "Yeah."
            Sb "Then follow me."

            $ renpy.pause (0.5)
            scene koltowndusk with dissolve
            $ renpy.pause(1.0)
            show sebastian disapproval b with dissolve
            $ renpy.pause (1.5)

            Sb "You know, I’m starting to get more and more concerned about Bryce. The fact that he’s willing to drink again so soon this evening is unsettling."
            c "How so? I thought that Bryce always drank this much."
            Sb drop b "Luckily not."
            Sb "That’s the thing, though. He has started to drink more and more as of late. He’s even started to get drunk twice a day every once in a while. To add to the concern, he drank until he passed out right before he went to work today, causing him to be late."
            Sb "This has never happened {i}once.{/i}"
            Sb disapproval b "I just hope whatever is on his mind will go away soon." #It will, though the method will, uh, depend...
            c "You know, I hope so too. I can’t imagine that drinking more than Bryce already does would do any good."
            Sb "Agreed. That’s why I want to ask you a favour."
            c "How can I help?"
            Sb normal b "Can you try and cut Bryce off if he starts drinking too much? I don’t want his health to potentially degrade even more."
            $ kol_tlh_seb_ask_nobooze = True

            menu:
                "I can try, but I can’t promise how the evening will go.":
                    Sb smile b "Thanks, [player_name]. This means quite a lot, you know."

                    $ kol_tlh_preventbooze = True

                "I’d rather not get in the way of Bryce’s drinking if I can help it.":
                    Sb disapproval b "I understand. Bryce can be a bit…{w=1.0}{nw}"
                    Sb drop b "…hot headed, if you cut him off at times."
                    Sb disapproval b "Will you at least take him home if he’s knocked out cold again like last time?"
                    c "I will."
                    Sb smile b "Thanks."

            $ renpy.pause(1.0)
            scene koloutsidebar with dissolve
            $ renpy.pause(1.0)
            show sebastian normal b with dissolve
            $ renpy.pause(1.0)

            Sb "Well, we’re here. Enjoy the evening."
            c "You too."
            Sb disapproval b "I'll try to."

            $ renpy.pause(1.0)
            hide sebastian with easeoutleft
            $ renpy.pause(1.0)
            stop music fadeout (3.0)

            m "Sebastian left me alone in front of the bar, running back to the police office to finish his day of work. I entered and saw that Bryce and Logan had already been waiting for me at a table that had been tucked away in one of the bar’s corners."

            $ renpy.pause(1.0)
            scene koleveningbar with fade
            $ renpy.pause(1.0)
            play music "mx/clouds.ogg" fadein (2.0)
            show logan normal at Position (xpos = 0.75)
            show bryce normal flip at Position(xpos = 0.25)
            with dissolve
            $ renpy.pause(1.0)

            c "You two are here early."
            Lg "Hello to you too, [player_name]. I almost started to wonder if you’d change your mind at the last minute and ditch us."
            Br smirk flip "Hey, [player_name]. I was wondering when you’d show up."
            c "I {i}just{/i} said that you two are here early. Do you not know what early means?"
            Lg smiling "Time won’t matter soon anyway. Let’s have some fun, shall we?"
            Br laugh flip "Finally."
            c "Logan really does have an influence on you, doesn’t he?"
            Br smirk flip "I just like to hang around him, alright?"
            c "(Sure, Bryce.)"

            show logan normal with dissolve

$ renpy.pause(1.0)

c "So, I guess that we should place our orders, then."
Br normal flip "Yeah. I’ll take the usual. I’m guessing you want the same as last time, Logan?"
Lg "Definitely."
Br "And you, [player_name]? What do you want?"

menu:
    "We're at the bar, so a beer would make sense.":
        $ renpy.pause(0.5)

        Br smirk flip "If you say so. Don’t worry about any competitions, though."
        Br laugh flip "At least, not between me and you."
        c "I don’t have the strength to drag the both of you out of the bar, you know."
        Br smirk flip "I’m sure that it won’t come to that."
        $ kol_tlh_drinkchoice = "beer"

    "Soda. I’d rather stay sober for a while.":
        $ renpy.pause(0.5)

        Br brow flip "You sure?"
        c "Why wouldn’t I be?"
        Br "I was just wondering, that’s all. I mean, there’s nothing important going on soon, so you might as well have something to drink."
        c "Like I said, Bryce: I’d rather not."
        Br stern flip "Suit yourself, then."
        $ kol_tlh_drinkchoice = "soda"

    "A glass of water would be good.":
        $ renpy.pause(0.5)

        Br stern flip "Really? Water?"
        Lg annoyed "How mundane of you, [player_name]."
        Br laugh flip "Well said, Logan."
        Br smirk flip "I suppose that just leaves more beer for the rest of us."
        $ kol_tlh_drinkchoice = "water"

$ renpy.pause(0.35)
Br normal flip "Waiter! We’d like to make our orders!"

show zhong serv b at Position(xpos = 0.95) with easeinright
$ renpy.pause(0.5)

Zh "Good evening. What can I bring you three?"
Br normal flip "The usual for me and Logan."
Zh normal b "Never a dull moment, huh?"
Zh serv b "What would you like, [player_name]?"
c " A glass of [kol_tlh_drinkchoice] would serve me well."
Zh "Noted. I’ll return with all your orders soon."

show zhong serv b flip with dissolve
hide zhong with easeoutright

$ renpy.pause(0.5)
Lg thinking "You know, the beer here is really unlike what we have back home. The stuff here is far stronger than what I expected it to be."
Br smirk flip "Yep. Only the strongest beer in the town here. You’d have to know how much you can take beforehand or you’d get swept under the table."
Lg normal "Agreed. A swig alone could make you tipsy if you aren’t prepared."
Lg "And may mercy be shown to the one who drinks here on an empty stomach."
Br laugh flip "I tried doing that once with some of the strongest alcohol here in the bar. Can’t say that it ended well for me. Poor Zhong had to take care of me for the next several hours due to how much alcohol was in my system."
Lg annoyed "Zhong?"
Br normal flip "The waiter."
Lg normal "Ah."
c "Bryce, on a scale of one to ten, how strong is the beer you tend to drink?"
Br brow flip "What kind of question is that?"
c "I need to know, that’s all."
Br stern flip "What do you mean by \“need?\”"
c "Just answer me."
Br "I’d say a seven, though depending on the day I’d even go for a solid nine. As of late, though? Probably a ten or eleven if we bend that scale a bit."
Br brow flip "Now, my turn. Why do you want to know?"
c "I needed to know for reference’s sake. I wanted to paint a picture of your drinking habits." #Of course, because that makes total sense.
Br stern flip "..."
c "..."
Lg normal "[player_name] just wanted to measure you out should you two ever hold a drinking competition, that’s all. You are quite the drinker, Bryce."

if nodrinks == False:
    Lg "The [player_name] I know doesn’t like to fail a challenge twice."

c "…yeah. I suppose that’s one way of putting it."
Br brow flip "Sure."

$ renpy.pause(0.5)
show zhong serv b at Position(xpos = 0.95) with easeinright
$ renpy.pause(0.5)
play sound "fx/glasses.wav"
$ renpy.pause(0.5)

Zh "Your orders have arrived, oh esteemed patrons."
Br normal flip "Thanks."
Zh normal b "You can call me if you need me."
Br "Will do."
Zh serv b "Oh, and do try to not drink too much right now. I’d hate to haul you to your shift."

if kol_tlh_bryce_escort == True:
    Br stern flip "Of course. Not the first time I’ve been reminded of that today."

else:
    Br "Of course."

Zh "In that case, I bid you three a good evening."
show zhong serv b flip with dissolve
hide zhong with easeoutright

$ renpy.pause (0.5)
Lg annoyed "Shift?"
Br stern flip "Yeah. I drew the short end of the stick, so now I need to be on guard duty at the portal tonight. All thanks to us being understaffed, as you know."

show logan surprised with dissolvequick
$ renpy.pause (0.3)
show logan serious with dissolvequick

Br brow flip "Something wrong, Logan?"
Lg "Just something that I remembered to change. Nothing to worry about." #Wink wink nudge nudge.
Lg normal smile "At least, not after this."

m "Logan held his glass of beer high in the air, beckoning for Bryce to do the same with his bowl. The two clanked, with a few drops of beer spilling over."

play sound "fx/2glasses.wav"
$ renpy.pause (0.5)

Br normal flip "Yeah. Bottoms up."
Br smirk flip "That includes you, [player_name]."
c "Alright, alright."

hide logan
hide bryce
with dissolve

$ renpy.pause (0.5)
m "I took a sip of my drink as both Logan and Bryce gulped their glasses down. It only took a few seconds for Bryce to finish his entire bowl, with Logan taking far longer to do so."
$ renpy.pause (0.5)

show logan normal at Position (xpos = 0.75)
show bryce normal flip at Position(xpos = 0.25)
with dissolve
$ renpy.pause (0.5)

Br smirk flip "Damn, that hit the spot."
Lg smiling "Yeah, same. That was definitely some good beer alright. Almost makes me want to have another one."
Br laugh flip "Definitely. Up for another one?"

if kol_tlh_preventbooze == True:
    menu:
        "[[Stop Bryce.]":
            c "Bryce, I don’t think that you should have another one. If you were to miss your shift due to you being drunk, then Emera might take notice that the portal was unguarded. Who knows what can follow after that?"
            c "Besides, I don’t think that you should be drinking as much as you do these days."
            Br brow flip "And you’re mentioning this now because?"
            c "Look, I’m not saying that you should stop cold. I’m just saying that perhaps you might need to tone the drinking down a bit with everything that’s been going on."
            c "Being constantly drunk to hide reality isn’t going to make that reality better; even more so with you-know-what approaching."
            $ renpy.pause (0.5)
            m "Bryce looked at me in a way that he never had before. Something resembling a desire of escapism flashed in his eyes momentarily as he looked away in consideration." #As if the word "escapism" didn't tell you everything you need to know...

            show bryce sad flip with dissolvemed
            $ renpy.pause (0.5)
            show logan serious with dissolve

            Br "Fine. I’ll try to limit myself so as to not endanger the force or anybody else that could help with what’s happening out there."
            c "Thank you, Bryce."
            $ kol_tlh_noextrabeer = True

            jump tlh_morebarstuff

        "[[Remain silent.]":
            pass

Lg normal "Hell yeah."
Br "Waiter! Two more, please!"

$ renpy.pause(1.5)
show zhong serv b at Position(xpos = 0.95) with easeinright
$ renpy.pause(0.5)
play sound "fx/glasses.wav"

Zh "Here you go. Do remember what I said earlier, Bryce."
Br normal flip "Yeah, I’ll keep it in mind."

show zhong serv b flip with dissolve
hide zhong with easeoutright
$ renpy.pause(0.5)

Lg smiling "Delightful. Well, you know the drill, Bryce."
Br smirk flip "That I do."
m "Logan and Bryce started to drink their beers at a slower pace than before, but were still considerably fast compared to what I could manage. Moments had passed before the first was finished with their drink, with the second finishing soon after."
m "All while I still had my first drink being barely touched."
jump tlh_morebarstuff


label tlh_morebarstuff:

$ renpy.pause(0.5)
Lg normal "Hey, are you going to finish your drink or what?"
c "Of course. I just like to take my time."
Lg smiling "Or you’re just boring by delaying any and all fun. Wouldn’t be the first time."
Br laugh flip "I wouldn’t exactly call [player_name] boring, Logan. Some pretty interesting things tend to arise everytime we chat, regardless of whether some work is involved or not."
Lg thinking "Yeah, I suppose you do have a point. I mean, it has been quite some time since I’ve been able to properly reconnect with [player_name] back home, so maybe I should, I don’t know, strike an interesting conversation soon or something."
c "That’s literally what you did the day you came here, though."
Lg annoyed "Huh? {w}Oh yeah...{w=0.4} all that stuff."
Br normal flip "Sounds interesting. Let me hear some of that \“stuff\”."
Lg normal "Oh, you know, how things are back home and how the authorities are dealing with the situation that erupted from Reza’s death. You know, stuff."
Lg "And then what everybody’s plan was and whatnot."
m "Not wishing for Logan to accidentally reveal any extra information that might sabotage his own plan, I gave him a light kick under the table. At first, he was confused, but eventually managed to figure my intentions out and stopped talking altogether."

show logan serious with dissolve
$ renpy.pause(0.5)

Lg "You know, I think that today’s beer was a bit stronger than what I had bargained for. I don’t think I’m even making sense right now."
Br brow flip "I thought that you wanted to have some stronger beer the last time we went to the bar." #Even though you didn't even order strong beer unless Zhong already knew beforehand. Somehow.
Lg annoyed "I... {w=0.4}said that?"
Br stern flip "I’m pretty sure, yeah."
c "You know, it’s getting late. Bryce, you should start to prepare for your shift before you eventually get even more drunk. I’ll take Logan home."

if kol_tlh_noextrabeer == True:
    Br "But I only had one beer! You can’t call that an evening at the bar!"
else:
    Br "But I only had two beers! You can’t call that an evening at the bar!"

c "But I am. Clearly the beer was way too strong for you tonight. I don’t want you to miss your shift just because you felt like you hadn’t had enough."
Br "Hrmph."
Lg normal "Don’t worry, Bryce. I’ll be fine. You go and sort your shift out."
Br "Alright. I’ll pay for the evening. You two stay safe, then."
c "Same to you, Bryce."

hide bryce
hide logan
with dissolve

stop music fadeout (5.0)
if kol_tlh_drinkchoice == "beer":
    m "I guided Logan out of the bar without finishing my beer. Deciding that it would be bad for him to stay alone in his state, I’d take him to my apartment so that he can spend the night there. We walked through the streets until there was nobody around us."

else:
    m "I finished the last of my drink and guided Logan out of the bar. Deciding that it would be bad for him to stay alone in his state, I’d take him to my apartment so that he can spend the night there. We walked through the streets until there was nobody around us."

$ renpy.pause(0.5)
scene koloutsidebarnight with dissolve
$ renpy.pause(0.5)

play music "mx/barren.ogg" fadein (1.0)
show logan annoyed with dissolve
$ renpy.pause(0.5)

Lg "I guess I got carried away, haven’t I?"

if kol_tlh_noextrabeer == True:
    c "It’s not your fault. You didn’t expect the beer to be that strong, after all."
    Lg serious "I’ll just have to try and sober up as much as I can before tonight. At least the fresh air is already starting to help."

else:
    c "Sort of. Even if you knew how strong the beer would be beforehand, you shouldn’t have gotten a second one on top of that."
    Lg serious "Yeah, my bad. I’ll just have to try and sober up as much as I can before tonight. At least the fresh air is already starting to help."

Lg "And to think I almost revealed my plan to Bryce of all people."
Lg annoyed "I appreciate the kicks. I’m just lucky that I managed to figure out that you were trying to warn me instead of my initial assumption of you wanting to be a jerk."
$ renpy.pause(0.5)
c "Thanks?{w} I just didn’t want you to sabotage your own plan, especially if you can somehow extend the time that humanity will give us for our mission."
Lg "It’s just gonna be harder to pull off now considering that Bryce—the Chief of Police himself—will be guarding the portal."

if kol_tlh_noextrabeer == True:
    Lg serious "Speaking of, maybe you shouldn’t have stopped Bryce. If he were to get so drunk that he’d not be able to guard the portal, then that would’ve made things way easier."

    menu:
        "I’m not letting Bryce put his health on the line.":
            c "I don’t know if you’ve noticed, but Bryce has drunk a lot of alcohol recently, especially since you’ve arrived. He may be a seasoned drinker, sure, but the amount that he’s consuming right now is extremely concerning."
            c "I’m not letting him risk his health like this."
            Lg normal "An alcoholic police chief? What a classic." #So insensitive...
            c "Logan, this is quite a serious matter."
            Lg serious "Yeah, sorry about it."

        "It’s better if he was at the portal tonight.":
            c "Answer me this, Logan: would you rather have Sebsatian, Maverick or Bryce be the guard for tonight? Who would be the one to most likely let you through should something go wrong?"
            Lg serious "Bryce. I guess I can kinda see where you’re coming from, then."

        "Because dragging you two home would be too much of a hassle.":
            c "Tonight is supposed to be the night where you perform your master plan, right? It would waste quite a lot of time if Bryce were to drink himself unconscious."
            c "And, knowing how these last few days played out, you’d probably be sleeping in Bryce’s arms under the table."
            Lg normal "About that…"
            $ renpy.pause(2.0)
            Lg serious "Uh, forget what I said. It was a very good idea that you stopped Bryce and I definitely thank you for it."

$ renpy.pause(0.5)
show kolnightwalk behind logan with dissolve
$ renpy.pause(0.5)
c "Speaking of, what even is your master plan for tonight? I mean, you’ve just been hyping it up without ever actually revealing it to me at all. The best you did was telling me that I might need to help you out later tonight."
Lg annoyed "Uh, should I really be talking about that right now when my head is still a bit foggy?"
c "You’ve started to significantly sober up, so I feel confident enough in you. Besides, we’re the only ones here right now, so you can talk as much as you want without anybody eavesdropping."
Lg "Yeah, I guess that I can agree with you. Looks like my body can still process all that extra strong booze after all." #Clearly, Logan has anime levels of superpowers if he could get *that* sober *that* quick after really strong beer.

stop music fadeout (3.0)

c "Don’t make a habit of it."
Lg serious "Yeah, yeah."
$ renpy.pause(1.5)

play music "mx/plan_b_kol.ogg" fadein (1.0)

Lg "So, remember that scouting work you did earlier today? With the help of my ever dear escort, I managed to convince my way to see the parts you mentioned."
Lg "…and they’re all completely useless with the tech at home. At least, on their own."
c "There’s a catch, isn’t there?"
Lg normal "You know me too well."
Lg "I made some copies of the blueprints you saw, as they were extremely useful when combined with those spare parts. As I thought, we’d be able to reverse engineer them to a degree where we could use the knowledge that we’ve learned and repair some of the spare scraps of tech that we found back at home."

if kol_tlh_endingA_route == True:
    Lg serious "I also asked Bryce where Reza’s old apartment was just before I went to the bar. He was suspicious at first, but seemed to chill down after I told him that I wanted to see if Reza might have left anything that humanity would want back."
    c "But shouldn’t the police have already searched through Reza’s place to see whether there would actually be anything that related to the murder case?"
    Lg normal "Hence the suspicion. Regardless, persuasion is a very mighty skill that I’ve learned from my training before coming here."
    Lg "Turns out, Reza somehow still had his generator there. So, I took it with me without anybody raising an eyebrow. Weird that he went out of his way to get every generator he could but still left his generator alone. Makes me wonder a few things about the case, actually."
    $ renpy.pause(0.5)
    Lg serious "With everything that we have now, it should be more than enough to keep humanity going in the short term."
    c "Enough for the dragons to direct the comet and recover?"
    Lg normal "Without a doubt."
    c "I just wished that we hadn’t resorted to blatant stealing to save everyone."
    Lg serious "Me neither. Thing is, this is about the best outcome that we could realistically get without being like Reza."
    c "But you are sort of like Reza in terms of stealing generators."
    $ renpy.pause(0.5)
    Lg "*sigh*"
    Lg "I’m way too tipsy to argue about that comparison, [player_name]. I didn’t kill anybody, so that’s good enough for me."
    c "And in the meanwhile you went through so many legal grey areas that your actions would make a politician envious of your cunning."

    $ renpy.pause(0.5)
    show logan annoyed with dissolve
    $ renpy.pause(0.5)

    Lg "Do you have any questions?"
    jump tlh_askingloganquestions

Lg serious "I’m hoping with all of that, we’d be able to somehow extend the city's lifespan by a few weeks."
c "Making it enough time for the dragons to redirect the comet."
Lg normal "Bingo."
Lg serious "Naturally, this all depends on the stuff back home, but this is better than nothing. I just wished that we actually had a generator instead."
c "So, I guess that makes you a criminal for stealing from the production facility now, right?"
Lg annoyed "Are we really going to go over this again? This is the best compromise that I could think of, [player_name]. Be happy that I didn’t kill anyone like Reza."
c "Being thankful for one crime rather than another won't solve the problem of why a crime was committed in the first place. I swear you and Reza will portray humanity in a negative light."
$ renpy.pause(1.5)
Lg "*sigh*"
Lg "I’m too tipsy to argue about philosophy, [player_name]. I did what I could. Now, do you have any questions?"

jump tlh_askingloganquestions


label tlh_askingloganquestions:
if not (kol_tlh_question1asked and kol_tlh_question2asked and kol_tlh_question3asked) == True: #if broken, then do if q1 or q2 or q3 == false
    menu:
        "How are you going to get past Bryce?" if kol_tlh_question1asked == False:
            $ renpy.pause(0.5)

            Lg normal "I still have to report the council’s decision about the ultimatum to the authorities. Going away in the cover of night by asking Bryce to use the portal would be far more convenient to report to my superiors than sneaking around, no?"
            Lg annoyed "Sure, hiding everything I brought will be a hassle, but at least Bryce knows that I’ll be there. That’s {i}basically{/i} fifty percent of the hassle solved."
            Lg serious "I can’t say that I know if I’d come back here once I’m through, though. All up to the authorities."

            $ kol_tlh_question1asked = True
            jump tlh_askingloganquestions

        "How are you even going to carry everything without arousing suspicion?" if kol_tlh_question2asked == False:
            $ renpy.pause(0.5)

            Lg normal "The blueprints are easy. I’ve saved ‘em all digitally to a card that I got from here, as well as taking a portable card reader to actually read them. Sure, it was a hassle scanning everything digitally, but I managed. At least the card reader has a pretty big battery, so I don’t need to worry about it running out of power."
            Lg "As for the spare parts, I’ve already hidden them near the portal."
            Lg serious "It’s still quite a while before it’s time to actually get them, after all."

            if kol_tlh_endingA_route == True:
                Lg annoyed "The generator is another story, though. It’s too bulky to be able to hide near the portal without anybody noticing. I’d have to somehow conceal it partially in the nearby bushes when I go through and fetch it when Bryce isn’t looking."

            $ kol_tlh_question2asked = True
            jump tlh_askingloganquestions

        "Where do I fit in to all of this?" if kol_tlh_question3asked == False:
            $ renpy.pause(0.5)

            Lg serious "If everything has been set up, then I’ll knock on your door tonight to ask for your help. You’ll have to come with me, but obviously not through the portal itself."
            Lg "As I pick the spare parts up, you would need to distract Bryce so that he doesn’t notice the extra stuff I’m carrying. You could lure him away, or just strike a conversation."

            if kol_tlh_endingA_route == True:
                Lg "The same with the generator. Thing is, you’d have to distract him for quite some time if I’m going to carry everything all at once. Multiple trips through the portal just won’t be happening."

            Lg "However, if other complications arose, then I’d have to use other methods of getting Bryce to ignore my haul. If I don’t knock on your door before one o’ clock, then you should go to bed and pretend that nothing happened. Chances are, it will be a {i}very{/i} busy day at the police station."

            $ kol_tlh_question3asked = True
            jump tlh_askingloganquestions

else:
    $ renpy.pause(0.5)

Lg serious "Anything else?"
c "Not much that I can think of."
Lg "Good."

stop music fadeout (2.0)

$ renpy.pause(0.5)
show kolmorenightwalk behind logan with dissolve
$ renpy.pause(1.5)

play music "mx/infinite_kol.ogg" fadein (3.0)

Lg normal "And it’s time for us to part ways."
c "Are you sure that you’d be able to go home in your current state? Sure, there aren’t any cars here that could hit you, but I don’t want you to put your own plan in danger before it even begins."
Lg serious "[player_name], my plan has been in danger since I thought it up. Besides, if I could explain my plan reasonably sensible to you, then I should be able to make it home."
Lg annoyed "That is, if I didn’t speak a bunch of gibberish just now."
c "You’re good. You sounded just like how you normally do."
Lg normal "Got it, then."
$ renpy.pause(1.5)
c "Actually, before you go; I wanted to ask you for an opportunity."
Lg annoyed "Do you have to ask it now?"
c "I don’t really have a choice here, Logan. If your plan works, then–{w=1.0}{nw}"
Lg serious "Yeah, yeah. Well, since you’ve already started, you might as well go on."
c "There’s someone that I’d like you to meet. Are you willing to go through with it?"
$ renpy.pause(1.0)
Lg "…and {i}why{/i} would I want to?"

menu:
    "He’s a close friend of mine.":
        $ renpy.pause(0.5)

        Lg thinking "I think I know where you’re going. You want to build allies so that the trade could go smoother, no?"
        c "That wasn’t what I–{w=0.75}{nw}"
        Lg normal "No need to explain, [player_name]. Sure, I’ll meet this supposed friend of yours."

    "He might prove useful in your plan.":
        $ renpy.pause(0.5)

        Lg "Hmmmmm..."
        Lg "I suppose I get what you’re saying. Having an insider might be a nice addition which I could use for the next step of my plan should tonight work out."
        c "I didn’t mean that you should–{w=0.75}{nw}"
        Lg normal "I should get to know this dragon friend of yours and potentially create a more successful plan for humanity. Got it."

    "Building contacts is always useful around here.":
        $ renpy.pause(0.5)

        Lg "I suppose you do have a point, especially if you take Bryce into consideration."
        Lg thinking "Having a vast network of dragons would probably be able to make things easier for me to manage whatever humanity wants."
        c "Nobody said anything about exploi–{w=0.75}{nw}"
        Lg normal "–tation, because that’s not what I’ll be doing. I have other things on mind now."
        Lg "Yeah, I’ll meet your friend to see what he’s like. Maybe I could learn something useful."

$ renpy.pause(0.5)
c "(...so, mission failed successfully? I think?)"
$ renpy.pause(0.5)
c "Glad to hear it. You can find him at the library during the day should you come back from your trip."
Lg serious "You know, a name would be more useful than just pointing at a vague direction."
c "Remy."
Lg thinking "Remy, huh? What a unique name for a dragon."
Lg normal "I’ll make a mental note of it. Just remember that I’m not certain whether I’ll actually return once I’m through the portal, so this potential meeting might not even happen."
Lg "Now, anything else you wanted to talk about?"
c "Nothing."
Lg "So be it. Remember, one o’ clock."

$ renpy.pause(0.5)
hide logan with dissolve
$ renpy.pause(0.5)

m "Logan parted ways and took his own path, presumably back to his apartment. He walked surprisingly normally for someone who was drunk, as if the alcohol had worn off completely. I stared at him for a moment, amazed that he could recover so quickly after drinking with Bryce."
m "I walked back to my apartment, deciding that I'd had more than enough excitement for the day so that I could wait for Logan to knock on my door for assistance tonight. That is, assuming he made it that far in the first place."

$ renpy.pause(0.5)
scene black with fade
$ renpy.pause(0.5)

m "In due time, I reached the outside of my apartment, with my legs starting to grow tired from all of the day’s walking around town."
$ renpy.pause(0.5)
m "Now, all that is left to do is wait and see if Logan's plan will work."

stop music fadeout (2.0)
$ renpy.pause(3.5)


if kol_tlh_endingA_route == True:
    jump tlh_Chapter3_EndingA

else:
    $ persistent.kol_tlh_chapter3A_skip = True
    $ renpy.pause(1.5)
    jump tlh_Chapter3B

    # ===========================================
    # END OF CHAPTER 3A
    # ===========================================


label tlh_Chapter3_EndingA:

$ save_name = (_("TLH - Chapter 3A.5"))

$ renpy.pause(2.5)
scene o2 at Pan ((0, 250), (128, 250), 3.0) with dissolveslow
$ renpy.pause(2.5)
play sound "fx/door/doorbell.wav"
$ renpy.pause (1.0)
play sound "fx/door/door_open.wav"
$ renpy.pause (1.5)

show logan serious with easeinright
$ renpy.pause (1.5)
play music "mx/ghost_town_kol.ogg" fadein (3.0)

Lg normal "Let’s go. Everything has now been set up for us to make our move."

if persistent.kol_tlh_chapter3A_5_skip:
    $ renpy.pause (1.75)
    c "(Wait, haven't I seen this before at some point?)"

    menu:
        s "(Do you want to skip forward?)"

        "Yes.":
            $ renpy.pause (1.5)
            if persistent.kol_tld_ending_achieved == True:
                menu:
                    s "(It seems that you have completed an ending of the mod called The Last Dragon. Do you wish to enable the bonus crossover content while skipping?)"

                    "Yes.":
                        stop sound fadeout (1.0)
                        stop music fadeout (1.0)
                        scene black with fade
                        $ kol_tlh_tld_crossover = True
                        jump tlh_Chapter3B

                    "No.":
                        pass

            stop sound fadeout (1.0)
            stop music fadeout (1.0)
            scene black with fade
            jump tlh_Chapter3B

        "No.":
            pass

c "Alright."

hide logan with dissolve
play sound "fx/steps/rough_gravel.wav"
scene np5 dk with dissolve

$ renpy.pause (1.0)
m "I left my apartment and walked through the dark of night, following Logan as he made a detour through the forest and away from the main path to the portal."
$ renpy.pause (1.0)

scene np4 with dissolve
$ renpy.pause (1.0)
scene np3 with dissolve
$ renpy.pause (3.0)
scene kolmoreforestnight at Pan ((0, 360), (0,0), 8.0) with dissolve
$ renpy.pause (0.5)

m "We went through the undergrowth, trying our best not to make too much noise and reveal our position to any that might be in the surrounding area."
c "I see the alcohol has worn off."

show logan serious dk with dissolve
Lg "Not now, [player_name]. Focus and save the idle chatter for later."
hide logan with dissolve

$ renpy.pause (1.0)
scene kolforestnight with dissolve
$ renpy.pause (3.0)

scene np1p at Pan((100, 100), (100, 100), 4.0) with dissolve

stop sound fadeout (2.0)
m "Eventually, we arrived relatively close to the portal. I could see that Bryce was patrolling the surrounding area. Logan tapped on my shoulder to grab my attention and pointed to the stash of resources he had gathered."

show logan serious dk with dissolve
$ renpy.pause (1.0)
Lg "Here’s all the stuff I’m taking with me. The generator is behind all of that."
c "You sure you’d be able to carry everything? It looks kinda heavy."
Lg annoyed dk "Thank you Captain Obvious for your astute observations."
Lg "Yes, I can carry all of it, but only if I walk really slowly. You’d have to try and distract Bryce for as long as possible and as far away as possible."
Lg "We'll wait until he's the farthest away from the portal. I'll reveal myself and tell him I'm returning to report to humanity. That's when you go out and keep him busy. Got it?"
c "Sure."
Lg "It’s crucial that he’s far away from the portal because not only will he notice me carrying the parts and the generator, but he’d also know that I’m taking too long to actually start the portal."
c "Makes sense."

hide logan with dissolve
$ renpy.pause (1.0)
m "We waited for a few minutes, concentrating on Bryce's route. He appeared to walk in an elliptical pattern, with a few abrupt turns here and there. We eventually found a time when he was far enough away from the portal that the likelihood of spotting Logan was low enough for him to pass through undetected."
$ renpy.pause (2.0)
m "Logan emerged from the bushes and approached Bryce. Fortunately for me, Bryce strayed even more from his planned path as he approached Logan, giving me even more leverage. I appeared from the bushes just as Logan finished speaking with Bryce to serve my purpose in Logan's plan."
$ renpy.pause (2.5)

show bryce brow b dk with dissolve
$ renpy.pause (0.5)

Br "[player_name]? Why are you all the way out here so late at night?"

menu:
    "I wanted to say goodbye to Logan.":
        $ renpy.pause (0.5)

        Br "You could have said goodbye to him earlier."
        c "I just forgot to do so, that’s all."
        Br stern b dk "That doesn’t explain why you’re still awake."
        c "Stress caused me to not be able to sleep as well as I could have. I'm guessing you know why."
        Br "I see..."

    "I wanted to check up on you.":

        if kol_tlh_drinkingwithlogan == False:
            c "You looked pretty rough earlier at the bar. I wanted to see whether you were still okay enough to work so late at night."
        else:
            c "I was wondering if you'd be okay after you went to the bar earlier today with Logan, that's all."

        Br stern b dk "I appreciate the concern, but you didn’t need to come out so late at night just to check up on me."

        if kol_tlh_bryce_escort == False:
            c "With the amount of alcohol you’ve been drinking recently, it just wouldn’t sit well with me if you passed out all the way out here in the middle of nowhere."
            Br brow b dk "How would you know how much I’ve been drinking?"

            menu:
                "Because you just told me.":
                    $ renpy.pause (1.5)

                    Br stern b dk "Damn it."
                    c "I’ve been sceptical of you for some time, Bryce. This was just the confirmation that I needed."
                    Br "So you’ve been keeping tabs on me."
                    c "I wouldn’t go that far. I just had a hunch that you seemed a bit more different as of late."
                    Br "Let’s not continue with this. I'm just not in the mood for this kind of talk."

                "Sebastian told me everything.":
                    Br "He did?"
                    c "Yeah. He was worried about you, so I came here to check on you."

                    if kol_tlh_noextrabeer == True:
                        c "Why did you think that I tried to stop you during our bar visit earlier?"
                    else:
                        pass

                    Br "..." #Looks like he realised just how much an impact of his drinking had on his friends. Poor guy.
                    $ renpy.pause (1.5)
                    show bryce stern b dk with dissolve
                    $ renpy.pause (0.5)

                    Br "Let’s not go on with this discussion. Please."

        else:
            $ renpy.pause (0.5)

        c "How come?"
        Br brow b dk "You know very well why, [player_name]. No need to play the fool."
        c "I suppose you do have a point. Still, this was the best opportunity I had to check up on you."
        Br "By waking up in the middle of the night to come here while I’m on duty?"
        Br stern b dk "What has gotten into you, [player_name]?"
        c "Perhaps it’s just my mind overthinking things again."
        $ renpy.pause (1.0)
        Br "{i}...sure.{/i}"

    "I wanted to take a walk so that I could clear my mind.":
        $ renpy.pause (0.5)

        Br "Then why didn’t you arrange an escort?"
        c "I figured that I wouldn’t need one so late at night. What chance would there be for something disastrous to happen during a walk at night?"
        Br stern b dk "You do have a fair point. It just makes me want to try and talk to Emera to drop this whole escort thing. I mean, it’s way too much hassle for what it’s worth. Besides, with Logan now going back, I don’t see the point in keeping this all up."
        c "All problems for tomorrow. For now, you’ve got a long night of patrolling ahead of you."
        Br "Yeah."


$ renpy.pause (0.5)
c "Now, my turn to ask a question."
Br brow b dk "Are we turning this into a game? You know that I should be on patrol about now, right?"
c "Just humour me this time, Bryce."
Br stern b dk "Fine. What’s your question?"
c "The same one I asked Maverick when he approached me earlier today: Did you talk to Maverick about the whole Reza situation? I mean, I’d assume that he would have already been discharged, but the fact that he’s still in the office contradicts that."

$ renpy.pause (1.5)
$ renpy.music.set_pause(True, channel="music") #Nice way to increase tension even if THERE'S NO DAMN WAY TO FADE THE THING AAAAAAAAAA
$ renpy.pause (0.5)

Br "Do you really want to know, [player_name]? Is the answer something that you really want?"
c "I’ve been wanting to know since the incident at the underground facility. We might as well stop beating around the bush."
Br "Alright, then..."

$ renpy.pause (2.5)
$ renpy.music.set_pause(False, channel="music")
$ renpy.pause (0.5)


Br "You are aware that Maverick was still on a mandatory sick leave when he killed Reza, right?"
c "Yeah."
Br "That means that his actions are outside of police regulations. However, since he killed a high-profile figure, he can’t be let off the hook. A police officer killing an ambassador—and a human one at that—isn’t something to be ignored."
Br "Since Emera is in charge of the whole human ambassador thing, she would get directly involved with Maverick’s punishment."
Br "We're looking at dischargement so far; that much is certain. However, given how politics is involved in every minute detail, Maverick could face even harsher punishment."
c "Isn’t dischargement the worst thing that could happen to Maverick?"

show bryce sad b dk with dissolvemed
$ renpy.pause (1.0)

Br "I wish that were the case, [player_name]. Emera would probably make sure that Maverick’s reputation would be ruined to a degree where he probably won’t be able to find a job anywhere, no matter how hard he tries. He’d be labelled as the one who killed a human ambassador."
c "Yet, that probably won’t happen unless Emera actually finds out that Maverick was the killer."

$ renpy.pause (1.0)
show bryce brow b dk with dissolvequick
$ renpy.pause (1.0)

Br stern b dk "Damn it, you just reminded me of something that I need to take care of tomorrow."
c "That being?"
Br "Back when Logan first introduced himself, Logan said that a feral dragon was the cause of Reza’s death, right?"
c "I think so, yeah."
Br "Meaning that either you or Maverick had forged the report to hide Maverick’s crime. Thing is, it couldn’t be possible for you to be the culprit, as Emera also said that a feral dragon was the cause of Reza’s death."
Br "So, Maverick must have somehow forged your report before sending it through to the humans. Not only did he kill Reza, but he also used corruption to hide his actions."

if persistent.kol_tld_ending_achieved == True: #The Last Dragon Route
    menu:
        "This sounds very serious. Shouldn’t you deal with it now?":
            $ kol_tlh_tld_crossover = True
            $ save_name = (_("TLH - TLD Crossover 1"))

            Br brow b dk "And ditch my post? You know that abandoning my duties wouldn’t just be irresponsible of me but would also set a bad example for the force."
            c "Yet, not writing a report right now could cause you to forget about it tomorrow. That would also be a bad example, no?"
            $ renpy.pause (1.0)
            Br "Damn it, you’re right."
            c "Bryce, writing a report would only take a few minutes. Besides, what are the odds that anybody will use the portal outside of Logan for the night?"

            $ renpy.pause (1.0)
            show bryce stern b dk with dissolve
            $ renpy.pause (1.0)

            Br "Alright, I’ll make that report. I should be back in half an hour at most. Do you mind keeping a watch on the portal for a bit?"
            c "Sure."
            Br "Thanks. I appreciate it."

            $ renpy.pause (0.5)
            show bryce stern b dk flip with dissolve
            hide bryce with easeoutright
            $ renpy.pause (0.5)

            m "Bryce began walking back to town quickly, leaving me and Logan alone at the portal. I waited until I couldn't see Bryce anymore before approaching Logan, who appeared to have a look of utter surprise on his face."

            show logan surprised dk with dissolve
            $ renpy.pause (0.5)
            Lg "Wait, did you just manage to get Bryce away just now or…?"
            c "Only for a bit. I’d say that we have about twenty minutes with a ten-minute grace period to account for Bryce’s travel times."
            Lg normal dk "Thirty minutes, huh? That just gave me another idea that might give humanity just an extra push." #Because this totally isn't a risky thing to do at all.
            c "(Here we go again…)"
            c "Logan, I don’t think that thirty minutes would be able to make much of a difference."
            Lg smiling dk "Not if you keep wasting time by spouting your unhelpful comments."
            c "What are you–{w=0.6}{nw}"

            stop music fadeout (2.0)
            hide logan with dissolve
            $ renpy.pause (2.5)
            play sound "fx/telbuttons.ogg"
            m "Logan put everything he carried down and activated the portal. As the portal started its normal routine of booting up, Logan looked at me in a playfully taunting way."

            show logan smiling dk with dissolve

            Lg "I’ll take the parts, while you take the generator. Delivering these things will go way faster with your help."
            Lg normal dk "And don’t try to rebuke here. Best to use every second we have."
            c "But why?"

            hide logan with dissolve
            m "Logan knelt, picked up the box of spare parts, and walked slowly through the portal."
            $ renpy.pause (0.5)
            Lg smiling "I’ll tell you on the other side."
            play sound "fx/telstart.ogg"
            $ renpy.pause (2.5)

            m "Logan quickly left, leaving me with the generator he stole from Reza's apartment. I reluctantly picked up the generator and walked through after Logan, not wanting to let this plan fail because of me."
            $ renpy.pause (0.5)
            stop sound
            play sound "fx/tel.wav"
            scene black with dissolve
            $ renpy.pause (1.0)

            $ _dismiss_pause = False

            scene port2 with dissolve
            scene port1 with dissolve
            scene port2 with dissolve
            scene port1 with dissolve
            scene port2 with dissolve
            scene port3 with dissolvequick2
            scene port4 with dissolvequick2
            scene port5 with dissolvequick2
            scene port6 with dissolvequick2
            scene port7 with dissolvequick2
            scene port8 with dissolvequick2
            scene port9 with dissolvequick2
            scene port10 with dissolvequick2
            scene port11 with dissolvequick2
            scene port12 with dissolvequick2
            scene port13 with dissolvequick2
            scene port14 with dissolvequick2
            scene port15 with dissolvequick2
            scene port16 with dissolvequick2
            scene port17 with dissolvequick2
            scene port18 with dissolvequick2
            scene port19 with dissolvequick2
            scene port20 with dissolvequick2
            scene port21 with dissolvequick2
            scene port22 with dissolvequick2
            scene port23 with dissolvequick2
            scene port24 with dissolvequick2
            scene port25 with dissolvequick2
            scene port26 with dissolvequick2
            scene port27 with dissolvequick2
            scene port28 with dissolvequick2
            scene port29 with dissolvequick2
            scene port30 with dissolve
            $ renpy.pause(1.0)
            scene porty with dissolveslow
            scene portz with dissolveslow
            scene black with dissolveslow
            hide screen my_scr
            $ _dismiss_pause = True

            stop sound fadeout 2.0

            $ renpy.pause (3.0)
            scene kolcitynight at Pan ((0, 360), (0, 0), 4.0) with dissolve
            $ renpy.pause (3.0)

            m "In the dead of night, I emerged on the other side of the portal and returned home. I could see that my surroundings had deteriorated significantly since I had left a few weeks before. The streets were deafeningly quiet, with only Logan and I awake at this hour."

            play music "mx/scrapyard_kol.ogg" fadein (2.0)
            show logan normal dk with dissolve

            Lg smiling dk "And welcome back, [player_name]."

            menu:
                "Good to be back, I guess?":
                    $ renpy.pause (0.5)

                    Lg serious dk "Yeah, I guess that it must be a bit unusual for you to be back here after all the luxuries back at the dragon’s side."
                    Lg normal dk "Regardless, things should definitely improve from here on out."

                "Things have definitely been better since I’ve left.":
                    $ renpy.pause (0.5)

                    Lg annoyed dk "For you, it would. Nothing has changed that much since I’ve left, though."
                    Lg normal dk "But that’s just upon initial inspection. I’m sure that a lot will change as we walk through the city."

                "Long time no see, Logan!": #All hail dad jokes, the god of this world!
                    $ renpy.pause (0.5)

                    Lg serious dk "..."
                    $ renpy.pause (1.5)
                    Lg "*sigh*"
                    $ renpy.pause (1.0)
                    Lg "Damn you, [player_name].{w=0.6} Damn you."

            $ renpy.pause (0.5)
            Lg annoyed dk "Let’s not waste any more time, shall we? You’re on a tight schedule, after all."
            Lg serious dk "We’ll be going to deliver these at the drop-off point. Follow me, please."
            c "Drop-off point?"
            Lg annoyed dk "If I got anything from the ultimatum, then I’d have to drop it off at the Sergeant’s house. Obviously, the parts and generator aren’t officially from the dragons, but a few choice words here and there would be able to cover it up enough."
            Lg serious dk "Speaking of, the reason why I suggested that you should come here. Do you have your PDA with you?"
            $ renpy.pause (1.0)
            c "No. It’s probably still either with Emera or at the police office, waiting for me to come and pick it up."
            Lg normal dk "Good. That’ll make things just a bit easier for the both of us."
            c "How so? I thought that the authorities wanted me back for the sole reason of getting my PDA in their hands again."

            $ renpy.pause (1.0)
            show kolcitycentrenight at Pan((0,180),(0,180),3.0) behind logan with dissolve
            $ renpy.pause (1.0)

            Lg "Exactly. Since we’ve brought so many resources to humanity, don’t you think it would almost be a bit too generous that dragonkind sent not only a generator and some spare parts but also our ambassador back with the PDA that the authorities wanted?"
            Lg "It would sound a bit too good to be true, right?"
            Lg annoyed dk "By leaving your PDA, I could play dumb and say that I didn’t know that the authorities wanted your PDA and not {i}you{/i} as a person."
            Lg normal dk "No offence, naturally." #"People don't want you. No offence haha."
            c "Are you sure the authorities would buy it? They aren’t as stupid as you think, Logan. I mean, there’s a reason why they’re in charge of the city and not somebody else."
            Lg smiling dk "They aren’t that smart either if they sent me through instead of some other lackey without exactly stating what they want while hiding behind vague assumptions." #In baby talk, this translates to "Haha officials dumb because they sent me aka someone who likes to bend the rules like a genie"
            c "Praise be to ambiguous loopholes, I guess."
            Lg normal dk "Truly the greatest discovery since sliced bread."

            $ renpy.pause (1.0)
            scene kolsergeanthouse at Pan ((0, 0), (0, 250), 5.0) with dissolveslow
            $ renpy.pause (3.5)

            show logan normal dk with dissolve
            $ renpy.pause (0.5)
            Lg serious dk "Here we are. I’m guessing that the Sergeant should still be awake at this hour, so prepare for a potential meeting."
            Lg annoyed dk "So strange that someone so important would still be awake by now."
            c "Look who's talking."
            Lg "You're not going to let that go any time soon, huh?"
            c "Nope."
            Lg "I guessed as much."
            $ renpy.pause (0.5)
            Lg serious dk "Let’s just get this over with. You ready?"
            c "I don’t really have a choice, Logan."
            Lg normal dk "I’ll take that as a yes."

            $ renpy.pause (0.5)
            play sound "fx/door/creaky.wav"
            $ renpy.pause (0.8)
            scene kolinsidesergeanthouse at Pan ((0, 220), (0,360), 3.0) with dissolveslow
            $ renpy.pause (2.5)

            m "I slowly walked in the house after Logan, anxious of what might happen should we find the Sergeant still awake. The interior was a dusty mess filled with all sorts of paperwork, strange objects that I didn’t recognise in this dark environment, and several guns."
            m "I put the generator down as gently as possible besides the doorway, with Logan putting the box of spare parts beside it. Afterwards, he took out a device and a card and put them on one of the nearby desks alongside some rolled-out blueprints."

            stop music fadeout (3.0)
            $ renpy.pause (0.5)

            Lg serious dk "And that’s the last of it. There should be a cable or two around here somewhere that can be used to access the card reader to whatever databases are still active."
            "???" "Ambassador Logan?"
            $ renpy.pause (0.5)
            Lg "...damn it."

            show logan serious dk flip at left with dissolve
            $ renpy.pause (0.5)
            show edmund dk at right with easeinright #Why a recoloured sprite? Because there weren't any spare sprites left to steal--uh, borrow from MBS. :)
            play music "mx/abandoned_lab_kol.ogg" fadein (0.5)

            "???" "And Ambassador [player_name] as well? What a late night surprise this is!"
            Lg "Greetings, Sergeant Edmund."
            Ed "Greetings to you too, Logan. I see your mission has been successful."
            Lg "I guess you could say that. Dragonkind has, as a sign of goodwill, sent a generator through, a few spare parts, and [player_name] as well. It seems that they are very desperate to keep the trade on."
            Ed "I see. That is a most kind gesture."
            Ed "Now, [player_name]. The dragons did not keep you as a hostage now, did they?"
            c "No. I was able to move around on my own free will. If you were looking for any signs of aggression, then there are none to be found."
            Ed "Except with Reza."
            c "That is another story, as you might know."
            Ed "Yes, yes. That is a matter that we are currently dealing with alongside a few other things. I imagine that Logan had already informed you about our discovery?"
            Lg "I have."
            Ed "Good. [player_name], do you have your PDA with you?"
            m "Wanting to give Logan some sort of leverage, I decided to respond in shock and confusion."
            $ renpy.pause (0.5)

            c "I...{w=0.35} think I left it back at my apartment in the dragon’s world."
            $ renpy.pause (0.5)
            Ed "...Logan."
            Lg "My apologies, Sergeant. I didn’t know that you wanted [player_name]’s PDA and not [player_name] specifically."
            Lg annoyed dk flip "I mean, you never said anything specifically about getting a PDA back, so I just assumed you only wanted [player_name]."

            $ renpy.pause (0.5)
            m "The Sergeant boiled silently, as if he wanted to throw a fit at any second. However, he managed to keep his cool and continued the conversation." #He knew he couldn't do anything lol
            $ renpy.pause (0.5)

            Ed "No matter. We have the generator and extra parts. We can make do without that PDA for now."
            Lg "I forgot to mention this, but I’ve also managed to grab a few blueprints and stored them in a card. You can find them all on the table with an appropriate card reader. I modified everything so that it should be able to connect to whatever databases that the scientists have left."
            Lg "You just need a cable somewhere to connect it."
            Ed "Most impressive, Ambassador."
            Ed "However, it would still be best if we get [player_name]’s PDA in our hands. It turns out that a large portion of information about the scrap that we had salvaged is stored within it."
            Ed "That’s why I need to send [player_name] back to retrieve it."

            show logan surprised dk flip with dissolve #Damn boi, why you surprised? Did you really think the MC was gonna be trapped here or something without going back to dergland?
            $ renpy.pause (0.85)

            c "So be it. I’m guessing that you also want me to stay on the other side to maintain the trade agreement, correct?"
            Ed "Indeed. If possible, I want you to send your PDA through as soon as you are able to. Do not worry, however: once we’re finished with it, we will send it back to uphold our end of the agreement."
            $ renpy.pause (0.4)
            Ed "Now, your turn, Logan. With all this going back and forth, we cannot spare the energy to send you back immediately. You will stay here until we have stored enough reserves of energy with the new generator to send you back."
            Ed "When we have the energy to spare, you will continue with your mission alongside [player_name]. It seems too difficult to uphold a trade with only one ambassador, no?"
            Lg serious dk flip "Thank you, Sergeant."
            Ed "In the meantime, we are in dire need of your skills. Your first assignment is to test which scrap parts are responsive enough to construct potential generators with. I recommend you use the old archive of blueprints that we have at the analyst centre."
            Ed "You will work until our remaining doctors have the potential to successfully heal someone far more fitting for this task."
            Lg "I’ll start as soon as possible."
            Ed "Then so it shall be."
            Ed "You two are dismissed."

            show edmund dk flip with dissolve
            hide edmund with easeoutright
            $ renpy.pause (0.75)
            show logan at center with ease
            show logan serious dk with dissolve
            stop music fadeout (1.0)
            $ renpy.pause (1.5)

            m "The Sergeant walked back to where he came from, leaving me and Logan standing alone in the dark, dusty interior."

            play music "mx/amb/night.ogg" fadein (4.0)

            Lg normal dk "Well, that could’ve been worse."
            menu:
                "Agreed.":
                    $ renpy.pause (0.5)

                    Lg serious dk "Yeah. Looks like you can still continue with the trade while everything is slowly rotting away here."
                    Lg normal dk "Hell, I’m even surprised that the Sergeant didn’t try to argue with me about that whole PDA assumption."
                    c "Quiet, Logan. Don’t ruin everything now."
                    Lg serious dk "Of course. Forgive me for my idiocy." #...I don't even understand why you would slip up like that and I was the person who wrote you. You baffle even your creator, Logan.

                "I wasn’t expecting the Sergeant to be so generous.":
                    $ renpy.pause (0.5)

                    Lg "Me neither. Well, I guess it’s better to not look a gift horse in the mouth."
                    Lg serious dk "I’m just happy that everything went so well."

                "I’m a bit confused, though.":
                    $ renpy.pause (0.5)

                    Lg annoyed dk "Why?"
                    c "The Sergeant isn’t the only person in charge of my mission. Shouldn’t he have consulted with the other authorities first?"

                    $ renpy.pause (0.5)
                    show logan serious dk with dissolve
                    $ renpy.pause (0.5)

                    Lg "I forgot to mention this, but the Sergeant is now the sole person in charge of the whole trade thing. Everybody else has been relocated to deal with the more desperate issues in the city."
                    Lg annoyed dk "That’s also a part of why my training was so rushed. There just weren’t enough people to teach me everything I needed to know. The Sergeant had to do everything himself, with the others popping in here and there to give some advice."
                    c "Oh..."
                    Lg serious dk "But that doesn’t matter now. We should just be grateful that everything went as well as it did."


            Lg annoyed dk "If you'll now excuse me, I will take my leave, because I sure as hell would hate staying here for another minute."
            c "Right behind you, Logan."

            $ renpy.pause (0.5)
            scene black with fade
            play sound "fx/steps/rough_gravel.wav"
            $ renpy.pause (4.5)

            scene kolcitynight at Pan ((0, 360), (0, 0), 4.0) with dissolve
            stop sound fadeout (5.0)
            $ renpy.pause (2.5)
            show logan serious dk with dissolve
            $ renpy.pause (0.85)

            Lg "Well, I guess this is goodbye for now."
            c "I suppose so. How long do you think you’ll be gone?"
            Lg "If I work overtime, then I should be back on the dragons’ side of the portal in around two days."
            Lg annoyed dk "Of course, this all depends on the energy reserves, but that’s another problem for another time."
            c "Got it. Anything that I need to do while waiting for you?"
            Lg serious dk "Yeah. Tell the dragon council that humanity has reconsidered their ultimatum and that the trade will now continue as normal. I’m sure that you’ll be able to wing it from there to suit Emera’s platter-sized ears."
            c "Will do as soon as I can. Better not to waste time with something like this."
            Lg normal dk "You know, speaking of time, you got about five minutes left before your so-called \“grace period\” starts." #Pulling a Sebastian, I see. Classic.
            c "..."
            Lg smiling dk "Better hurry up. You wouldn’t want to make the ol’ Chief suspicious, would you?"

            hide logan with dissolve
            $ renpy.pause (0.5)
            m "Logan chuckled softly under his breath as I hurried to the portal as fast as my feet could carry me, not even properly saying goodbye to Logan. Fortunately, it wasn’t long before I had reached the portal."
            $ renpy.pause (1.5)
            play sound "fx/tel.wav"
            m "I activated the portal and stood between the two pillars, ready to return to my mission after my visit to my home."

            $ renpy.pause (0.5)
            scene black with fade
            $ renpy.pause (8.5)
            stop sound fadeout (1.0)
            $ renpy.pause (2.5)
            scene np1p at Pan((100, 100), (100, 100), 4.0) with dissolve
            $ renpy.pause (1.5)

            m "I emerged from the other side, a bit dizzy from the portal’s side effects. As I started to look around, I spotted Bryce in the far distance slowly heading towards the portal."
            c "(And you made it in time. Congratulations, [player_name].)"
            $ renpy.pause (0.5)
            m "I walked towards Bryce, who gave me an eager smile."
            $ renpy.pause (0.5)

            show bryce normal b dk with dissolve
            $ renpy.pause (0.5)

            Br smirk b dk "Hey. Thanks for looking out for the portal for me. The report has now been sorted out."
            c "Glad to hear it, Bryce."
            Br stern b dk "Anything strange that happened while I was gone?"
            c "Only Logan that went through the portal."
            Br smirk b dk "Good job, [player_name]. I’ll take my shift back now. You can go home if you want."
            c "I think I will. Good luck with the rest of your shift."
            Br normal b dk "And good night to you, [player_name]."

            $ renpy.pause(0.5)
            scene black with fade
            $ renpy.pause(0.5)
            stop music fadeout (2.0)
            $ renpy.pause(3.5)
            $ persistent.kol_tlh_chapter3A_5_skip = True

            jump tlh_Chapter3B

            # ===========================================
            # END OF CHAPTER 3A
            # ===========================================



        "What will happen to Maverick now?":
            pass

c "What will happen to Maverick now?"
Br sad b dk "I…{w=0.3} don’t know. Maverick never seemed like the type of person who would even think of doing anything like this." #Oh, poor Bryce. The lad isn't even equipped to handle the comet, and now this as well? No wonder he's drinking himself ot death.
Br stern b dk "I’ll have to report this to Emera so that we can try to come up with something. This is too much for only one person to deal with."

$ renpy.pause (1.5)
m "Bryce paused and remained silent for a few seconds, questioning the impact of his discovery. As Bryce pondered what would happen to Maverick, I noticed an activated portal with Logan slowly passing through it."
$ renpy.pause (1.5)

m "My mission had been successful."
Br "Like I said, I’ll have to deal with it tomorrow. For now, I’ll have to continue with my patrol."
Br normal b dk "Thanks for the chat, [player_name]. It makes a night like this just a little less dull."
c "No problem, Bryce. See you tomorrow."

hide bryce with dissolve
m "Bryce walked away, returning to his patrol of the portal. With no sign of Logan or his parts, I began to walk back home, relieved that humanity now had a few extra weeks while the dragons worked on redirecting the comet."

$ renpy.pause(0.5)
scene black with fade
$ renpy.pause(0.5)
stop music fadeout (2.0)
$ renpy.pause(0.5)
$ persistent.kol_tlh_chapter3A_5_skip = True

jump tlh_Chapter3B

# ===========================================
# END OF CHAPTER 3A
# ===========================================



label tlh_Chapter3B:

$ save_name = (_("TLH - Chapter 3B"))

$ renpy.pause (2.0)
scene o4 at Pan((0, 0), (0, 150), 4.0) with dissolveslow
$ renpy.pause (2.0)

play sound "fx/phonering.ogg"
$ renpy.pause (3.0)
stop sound
play sound "fx/phonepickup.ogg"
$ renpy.pause (1.75)

c "Hello?"
Ry normal "Hello, [player_name]. This is Remy."
c "Hey Remy. How are you doing today?"
Ry "I’m fine. And you?"
c "I guess I’m fine as well."
Ry smile "That’s good to hear."
Ry normal "I’m calling you to ask you out again. Me and Adine will be spending the day at the orphanage, and I was hoping if you would be interested."

menu:
    "Of course.":
        $ renpy.pause (0.5)

        Ry smile "I’m happy to hear that, then. Would it be alright if we meet up in around two hours?"
        c "Sounds good."
        Ry normal "Alright. Goodbye for now, [player_name]."
        c "Goodbye, Remy."
        $ renpy.pause (2.0)
        c "(Now that I think about it, it’s been some time since I’ve last seen Adine. Guess it’s about time we meet up again.)"

        $ renpy.pause (0.75)
        scene black with fade
        $ renpy.pause(1.5)
        play sound "fx/steps/rough_gravel.wav"

        m "I walked to the orphanage when it was time. Looking around, I noticed that the streets and pathways were much busier than usual, with several dragons passing me by. Each of them gave me a strange look that ranged from awe to indifference. I ignored them all and continued on my way."

        $ renpy.pause(1.5)
        stop sound fadeout (2.0)
        scene hatchery at Pan ((0, 0), (0, 180), 3.0) with dissolveslow
        $ renpy.pause(1.5)

        m "Eventually, I could see both Remy and Adine waiting outside."

        if persistent.kol_tlh_chapter3B_skip:
            $ renpy.pause (1.75)
            c "(Wait, haven't I seen this before at some point?)"

            menu:
                s "(Do you want to skip forward?)"

                "Yes.":
                    $ renpy.notify("This outing with Remy, Adine and Amely had been successful.")
                    $ kol_tlh_chapter3B_mood = 2

                    stop sound fadeout (1.0)
                    stop music fadeout (1.0)

                    scene black with fade
                    $ renpy.pause (1.0)
                    $ kol_tlh_3B_played = True
                    jump tlh_Chapter4A

                "No.":
                    $ renpy.pause (1.0)

        play music "mx/fireplace.ogg"
        show remy normal flip at Position (xpos = 0.25)
        show adine normal b at Position (xpos = 0.75)
        with dissolve
        $ renpy.pause(0.85)

        Ry smile flip "Oh, hello [player_name]! I was wondering when you would arrive."
        Ad "I could say the same. We’ve been waiting for a while for you to eventually show up."
        c "Sorry about that. The streets were a bit busier than usual."
        Ry normal flip "That’s understandable. I’m guessing that everyone is a bit busy making preparations."
        c "Preparations?"
        Ad think b "Yeah. The council issued an order to connect all available generators to the main grid. What makes this strange is that all of this extra energy will, according to the council, somehow allow you to stop some sort of threat."
        Ad "I thought that humans weren’t supernatural beings."

        menu:
            "It’s a bit too complicated to explain now.":
                $ renpy.pause (0.5)

                Ad giggle b "I see. You’re trying to hide something from me, aren’t you?"
                c "Maybe I’ll explain it another time."
                Ry shy flip "Precisely. I mean, we {i}are{/i} here to visit Amely. It would be better if we didn’t waste the little time that Adine has."
                Ad "I have the entire day off, Remy. I have plenty of time."
                Ad normal b "Still, there’s no point in wasting all of it outside. Let’s go visit Amely."

            "We actually are. I just used my divine powers to deceive you this whole time.":
                $ renpy.pause (0.5)
                $ kol_tlh_chapter3B_mood += 1

                Ad giggle b "Then your powers must be pretty strong to keep that whole illusion up for so long."
                Ad think b "Though, if they are already so strong, then why would you need the power from all the generators?"
                Ry shy flip "I-It just so happened that the upcoming threat is too great for [player_name] to deal with alone. That’s why the generators are absolutely necessary."
                Ad "I see..."
                Ry "But that’s for another time. Let’s go visit Amely, shall we?"
                Ad normal b "Sure."

            "But we aren’t. Humans are still normal people.":
                $ renpy.pause (0.5)

                Ad "Then how are you planning to stop the threat that the council warned us about?"
                c "With the generators."
                Ad annoyed b "Well, {i}obviously.{/i} Let me rephrase the question: How are you supposed to use the generators to stop whatever threat is coming?"
                Ry shy flip "Adine, perhaps we should leave the questions for another time. We’re here to enjoy ourselves, not to play detective."
                Ry smile flip "At least, not without Amely."
                Ad normal b "Alright, alright. Let’s go visit her, then."

        stop music fadeout (1.5)
        c "After you."
        $ renpy.pause (1.0)
        play music "mx/orphanage_kol.ogg" fadein (1.0)
        scene kolorphanagehall with dissolve
        $ renpy.pause (1.0)

        m "The three of us walked into the orphanage. As we went through the narrow corridors, Adine talked to someone who I presumed to be a worker. Afterwards, she followed the worker to a separate corridor."

        show remy normal with dissolve
        $ renpy.pause (0.5)
        Ry "Adine has gone to get Amely from her room. We’ll be playing with her in the classroom at the end of the hallway. Just walk straight, then turn left at the first turn."
        c "Okay."

        $ renpy.pause (1.5)
        scene kolorphanage with dissolve
        $ renpy.pause (1.5)

        m "I walked even further and eventually wound myself in a small classroom that had been degraded by generations of hatchlings. Upon looking around, I noticed that there were many crayon marks across the walls."
        m "What little books were left on the bookshelves were all unsorted, with every book having crumpled up pages. There were also desks filled with what I assumed to be the hatchlings’ art, with each one having an assortment of crayons."

        show remy normal with dissolve
        $ renpy.pause (0.5)

        c "Well, this place is an absolute mess." #Hey, another TDOMI reference! Who could've saw that coming?
        Ry look "Unfortunately, yes. What’s even worse is that this is the cleanest that this classroom has been in some time."
        c "Really?"
        Ry "Yes. Just a few days ago, there were pieces of paper and binders everywhere. Even the lights for the classroom weren't working. Luckily, that had been fixed."
        Ry "The walls however, have been like this for years. Every time somebody tried to clean it, there would just be another drawing to replace it. The orphanage eventually just gave up cleaning altogether."
        c "Wait, don’t the hatchlings have somewhere else to play instead of this classroom?"
        Ry "Sadly, this is the only available space for the orphans. They spend the majority of the day here or outside playing, learning, studying, and eating. Sure, they have a few sleeping rooms, but that's about it."
        c "And I’m guessing that with the orphanage being understaffed as well, the hatchlings’ only real source of entertainment would be in this classroom with other hatchlings, correct?"
        Ry normal "Sort of. There is a park nearby that some of the hatchlings like to play with, but only under adult supervision."
        Ry smile "Me and Adine actually went there with Amely a few days ago. I always enjoy it when we can have a nice day at the park."
        Ry normal "I just wished that you were there. You would have definitely enjoyed it." #Yes, this is, in fact, a reference to A Day at the Park. :D
        $ renpy.pause (1.0)
        Ad normal b "Remy!"

        $ renpy.pause (0.5)
        show remy at left with ease
        show remy normal flip with dissolve
        show adine normal b at right
        show amely small at Position(xpos = 0.65)
        with easeinright
        $ renpy.pause (0.5)

        Ad "Sorry that I took so long. Amely took her sweet time when waking up."
        Ry smile flip "Oh, don’t worry. Amely is somebody who does need some extra rest, after all."
        Ad think b "Now, how should we start the day?"
        Ry normal flip "I guess that a good start would be to go outside, even if our original plan was to just stay here. I don’t think that we can do much here with Amely, to be honest."

        menu:
            "Definitely. This room is too cramped.":
                $ renpy.pause (0.5)
                $ kol_tlh_chapter3B_mood -= 1

                Ad "I wouldn’t say it’s {i}that{/i} cramped. This room can accommodate quite a lot of hatchlings running about and playing with each other."
                c "In that case, would you consider yourself a hatchling if you don’t feel cramped?"
                Ad giggle b "Don’t be silly, [player_name]."

            "Isn’t there enough stuff to do here to keep Amely busy?":
                $ renpy.pause (0.5)

                Ry shy flip "It would kind of defeat the purpose if we visited Amely just to watch her keep herself busy."
                Ad giggle b "Besides, do you really want to keep watch over Amely’s art skills for the whole day?"
                c "Fair enough."

            "Anything is possible if you’re creative enough.":
                $ renpy.pause (0.5)
                $ kol_tlh_chapter3B_mood += 1

                Ad "I suppose that’s true. I just can’t really think of anything to do that will last us for the entire day, though."
                Ry smile flip "Amely, what do you think we should do here?"
                Am "We no play here. Play outside!"
                Ad giggle b "You heard her, [player_name]."

                $ renpy.pause (0.5)
                Ry normal flip "Well, I suppose there would be no point in staying here, then. Adine, will you take Amely?"
        
        $ renpy.pause (1.0)
        Am "Carry!"
        Ad giggle b "Okay, Amely. Come here!"
        $ renpy.pause (0.3)

        hide adine
        hide amely
        with dissolve
        m "Adine lowered herself to the floor, readying herself to catch a dashing Amely. Amely jumped into her arms and made herself comfortable. Adine slowly rose to the ground and looked at a now-content Amely."
        $ renpy.pause (0.5)
        show adine annoyed b at Position (xpos = 0.75) with dissolve
        Ad "You know, I should have gotten my pouch. If I knew that Amely would want to be carried, I’d just put her in my pouch right about now."

        menu:
            "I could always carry Amely if you want.": #Behold! A pure scene to cleanse your heart and to fill you with laughter and merriment!
                $ renpy.pause (0.5)
                $ kol_tlh_carrying_amely = True
                $ kol_tlh_chapter3B_mood += 1

                Ad giggle b "If you think that you can carry her, then be my guest. Just a fair warning, though: she can be pretty feisty."
                c "I’m sure I can take it. At least, for a bit."
                Ad normal b "Don’t say I didn’t warn you, [player_name]."

                hide adine with dissolve
                m "Adine handed Amely towards me. As soon as I carried Amely, my arms started to grow slightly tired due to how heavy she turned out to be."
                $ renpy.pause (0.5)
                Am "Higher!"
                c "Uh..."
                show adine normal b at Position (xpos = 0.8) with dissolve
                show remy shy flip with dissolveslow
                $ renpy.pause (0.5)
                Ad "Let me help you."
                m "Adine slowly moved Amely higher up on my body until she sat comfortably around my neck. Not wishing for Amely to fall off, I held her tightly around her legs as she started to move excitedly."
                Am "Yay! Me super tall!"
                c "(At least she’s not pulling on my–{w=0.75}{nw}"
                c "OW!" with vpunch
                Ry "Amely, don’t pull on [player_name]’s hair, please."
                Am "Hair?"
                Ry "The fluffy things on [player_name]’s head."
                Am "Okay."
                Ad giggle b "Told ya."
                c "I think that I should have listened to your warnings."
                Ry smile flip "It’s too late to go back now, [player_name]. It looks like Amely has found a new liking to her throne."
                $ renpy.pause (0.5)
                m "Adine and Remy both chuckled while I stood with Amely around my neck clapping her hands."
                c "(This is going to be a long day, isn’t it?)"
                Ad normal b "Now let’s actually go out this time, okay?"
                Ry normal flip "Of course."

                $ renpy.pause (1.0)
                scene kolorphanagehall with dissolve
                $ renpy.pause (1.0)

                m "All four of us slowly went through the corridors back outside again, with me almost crouching to try and get Amely to fit through as well, despite my several warnings to tell her to duck. Eventually, with many chuckles from staff members, we got out of the orphanage."

                $ renpy.pause(1.5)
                scene hatchery at Pan ((0, 0), (0, 0), 3.0) with dissolveslow
                $ renpy.pause(1.5)
                show remy normal flip at Position (xpos = 0.25)
                show adine normal b at Position (xpos = 0.75)
                with dissolve

                Ad giggle b "Having fun, [player_name]?"
                c "I...{w=0.4} think?"
                Ad normal b "Well, you carrying Amely around is definitely a good start for her day out."


            "[[Remain silent.]":
                $ renpy.pause (0.5)

                Ad normal b "Oh well, I'll just have to manage. Let’s go."

                $ renpy.pause (1.0)
                scene kolorphanagehall with dissolve
                $ renpy.pause (1.0)

                m "We all walked through the corridors once more, with Adine slightly struggling to catch up to me and Remy. With more than enough struggle from Amely, Adine managed to carry Amely all the way until we left the orphanage."

                $ renpy.pause(1.5)
                scene hatchery at Pan ((0, 0), (0, 0), 3.0) with dissolveslow
                $ renpy.pause(1.5)

                m "However, Amely immediately jumped out of Adine’s arms as soon as we reached the outside of the orphanage."

                $ renpy.pause (0.5)
                show remy normal flip at Position (xpos = 0.25)
                show adine normal b at Position (xpos = 0.75)
                with dissolve
                $ renpy.pause (0.5)

                Am "Thank you."
                Ad normal b "Phew. I didn’t think that Amely would be so restless today. I guess that she must be really excited that she gets to spend some time with us."


        Ad think b "So, what now?"
        Ry normal flip "I wanted to treat Amely with something special. Do you think that she would like some ice cream?"
        Ad "Actually, I don’t think that the hatchlings ever had ice cream before."
        Ad normal b "But I can guarantee you that Amely likes sugar in any and all shapes and sizes."
        Am "Sugar!" with vpunch
        Ry smile flip "That says everything I need to hear, then. I know a dragon that sells the best ice cream I’ve ever tasted."

        menu:
            "Now you have me intrigued.":
                $ renpy.pause (0.5)

                Ry "Trust me, [player_name]. It beats the ice cream that you can get from the store a thousand times over."
                Ry normal flip "At least, that’s what I would rate it."

            "I’m sure that there would be an ice cream even better than what you had.":
                $ renpy.pause (0.5)

                Ry normal flip "There could be, but I doubt it. The ice cream from this dragon is pretty famous for how good it is. If better ice cream {i}does{/i} exist, then it would have already revealed itself."
                Ry smile flip "Besides, I think that you’ll agree with me once you have a taste or two."

            "Surely it can’t be {i}that{/i} good.":
                $ renpy.pause (0.5)

                Ry "Oh, but it is {i}that{/i} good. This is top notch artisanal ice cream we’re talking about, after all."
                Ry normal flip "Though, now I’m a bit curious about how it would compare to the ice cream you have back in your world."
                c "I guess we’ll just have to find out."
                Ry smile flip "I guess so."

        Ad think b "You know, the longer we stand here, the longer the line would probably get."
        Ry shy flip "Fair point. Let’s get going, then."

        $ renpy.pause (1.0)
        scene kolmoretown1 with dissolve
        $ renpy.pause (1.5)

        m "We all casually strolled through the town, keeping each other company in the process."

        $ renpy.pause (1.0)
        scene np3x at Pan((0, 40), (0, 220), 5.5) with dissolveslow
        $ renpy.pause (2.5)

        m "Before long, we reached a relatively desolate area, far from everything else. I spotted what I thought was a grey dragon in the distance, sitting next to what looked like an ice cream cart."

        if kol_tlh_carrying_amely == True:
            $ renpy.pause (0.85)
            play sound "fx/varafall.ogg"
            $ renpy.pause (0.7)
            m "Amely jumped off of my shoulders and landed neatly on the ground, finally bringing relief to my neck."
            $ renpy.pause (0.85)

            show remy look flip at left with dissolve
            Ry "Amely! Are you alright?"
            hide remy with dissolve

            show np3x at Position(xpos=0.0, xanchor='left', ypos=1.01, yanchor='bottom') with ease
            show amely normal at Position(xpos = 0.63) with dissolve
            Am "Was fun, but me walk now."
            hide amely with dissolve
            show np3x at Pan((0, 220), (0, 220), 5.5) with ease

            show remy look flip at Position (xpos = 0.25) with dissolve
            $ renpy.pause (0.5)
            show adine normal b at Position (xpos = 0.75) with dissolve
            $ renpy.pause (0.5)

            Ad giggle b "You’re worrying too much, Remy. Amely can take far more than just a light fall."
            $ renpy.pause (0.5)

            Ry sad flip "But..."
            $ renpy.pause (0.75)
            Ad think b "Remy?"
            Ry look flip "I-It’s fine. I just don’t want her to get hurt, that’s all." #Ooooo, Remy's getting over-protective of Amely. I wonder why...

            $ renpy.pause (1.0)
            Ry normal flip "At least [player_name] can finally get some sort of break."
            c "Yeah. Amely’s surprisingly heavy for her size."
            Ad normal b "She is a bit of a hefty hatchling, I’ll give her that."
            Ry "That she is."

        $ renpy.pause (1.5)
        Ry smile flip "And we’re here. Luckily for us, it seems that there isn’t any line today."
        Ry normal flip "So, what ice cream flavour does everyone want?"
        Ad normal b "I’m kind of in the mood for some mango. I’m guessing you want vanilla again, right Remy?"
        Ry shy flip "How did you guess?"
        Ad giggle b "You seem pretty loyal to your food choices. It wasn’t too much of a stretch to assume that you want vanilla." #I wonder if it could be argued that this loyalty is an allegory for staying loyal to Amelia after her death. Interesting to think about.
        Ry "I suppose you could say that."
        Ad think b "Though, what would Amely want?"
        Ry normal flip "Amely, is there a flavour of ice cream that you’d like?"

        hide remy
        hide adine
        with dissolve

        show np3x at Position(xpos=0.0, xanchor='left', ypos=1.01, yanchor='bottom') with ease
        show amely normal at Position(xpos = 0.63) with dissolve

        Am "Sugar!" with hpunch
        Ad annoyed b "But what {i}kind{/i} of sugar?"
        Am "..."
        $ renpy.pause (0.5)
        Am "Sweet sugar!" #Don't tell Amely that all sugar is sweet. ^^

        hide amely with dissolve
        show np3x at Pan((0, 220), (0, 220), 5.5) with ease

        show remy shy flip at Position (xpos = 0.25) with dissolve
        $ renpy.pause (0.5)
        show adine annoyed b at Position (xpos = 0.75) with dissolve

        Ry "I’ll just give her some toffee ice cream, if that’s alright."
        Ad "Please, Remy, do {i}not{/i} give her that. She’ll have so much energy that she could power the town for months." #Might be useful for redirecting the comet, then.
        Ad normal b "Chocolate ice cream should be more than enough for her."
        Ry normal flip "Alright. [player_name], is there anything you want?"
        c "I... {w=0.5}don’t know. What are my options?"
        Ry shy flip "A lot. Maybe you could just ask what's available while we finish up the rest of our orders?"
        c "Alright, then."

        stop music fadeout (2.0)
        hide remy
        hide adine
        with dissolve

        m "We made our way to the grey dragon. As we approached, his face visibly lit up in excitement."
        
        $ renpy.pause (0.75)
        show katsu normal at Position(xpos = 0.88) with dissolve
        $ renpy.pause (0.25)
        show remy normal flip at Position(xpos = 0.2)
        show adine normal b flip at Position(xpos = 0.05)
        with dissolve
        play music "mx/fun.ogg" fadein (1.0)
        $ renpy.pause (0.5)

        Ka smile "Well well, look who it is! It’s been quite some time since I’ve last seen you around, Remy." #And so, more TDOMI-inspired stuff!
        Ka excited "And you brought your friends as well? What an excellent opportunity this is!"
        m "The grey dragon turned to look at me with some resemblance to surprise, but quickly hid his emotions."
        Ka normal "You know, I didn’t expect that a human would be one of my customers today. It looks like I’ll have to serve my finest frozen confectionaries to make an impression on humanity’s ambassador."
        
        if seenkatsu == False:
            Ka smile "But I’m rambling too much. My name is Katsuharu, and I sell all kinds of frozen delights. How may I be of service to our esteemed guests?"
        else:
            Ka smile "But I'm rambling too much. How may I be of service to our esteemed guests?"

            if katsuavailable == True:
                Ka normal "As for you, [player_name], you still have an unredeemed opportunity from when you helped me with my cart."
                c "I kinda forgot about that, actually."
                Ka smile "Luckily for you, I rarely forget even in my day and age."
                Ka "Now, what are your orders?"

        Ry "We'll have a vanilla, mango, and chocolate cone without any toppings."
        Ka "Noted. What can I get for our dear human?"
        c "What are your options?"
        Ka excited "What are my options?! I have ice cream, gelato, frozen yoghurt, frozen custard, soft serve, sorbet, sandwiches, popsicles, mellorine, sherbet, cold taffy, snow cones and haluhalo in stock."
        Ka "I can also offer you waffles, sticks, pretzels, cups, wafer cones, cake cones, sugar cones, chocolate-coated cones, double cones or vanilla cones as sides."
        c "I…{w=0.35} don’t think that all those options helped me out in making my decision."
        Ka exhausted "My apologies. I suppose my large variety of options can be a bit overwhelming for new customers."
        Ka normal "But perhaps I can recommend something extra special for you."
        c "Oh?"
        Ka "Tell me, human: have you ever heard of spaghettieis?" #Like I said:
        c "I can’t say that I have. Is it some sort of frozen pasta dessert?"

        show katsu smile with dissolvequick
        $ renpy.pause (0.3)
        m "Katsuharu chuckled suddenly under his breath, trying to conceal his joy as best as he could."
        show katsu normal with dissolve
        $ renpy.pause (0.5)
        Ka "Oh no. It’s a frozen treat where vanilla ice cream is put through a spaetzle press. Afterwards, a rich strawberry sauce is drizzled over it. Add some coconut flakes and you have a frozen treat that looks like spaghetti."
        c "Sounds interesting. I think that I’ll have that, then."
        Ka normal "As you wish."

        hide katsu with dissolve
        $ renpy.pause (0.5)
        m "Katsuharu opened his cart and served us our orders, taking great care to make sure everything was perfect. When it came to my order, he ducked and appeared to pull out some sort of machine. My order was ready in a few moments."
        show katsu normal at Position(xpos = 0.88) with dissolve
        $ renpy.pause (0.5)

        Ka smile "There you go, human. I do hope that you enjoy what I have to offer."
        Ry smile flip "Thank you as always, Katsuharu."
        Ry normal flip "Now, how much do I owe you?"
        Ka smile "The human’s order is a gift, so no need to pay for the spaghettieis. The rest, though? The usual price."
        c "I’ll pay for the ice cream. No need to worry, Remy."

        if kol_tlh_mcpaid == True:
            Ry look flip "You already paid for our meals the other day, [player_name]. There’s no need to do it again, even if your finances are managed by the council. It just wouldn't sit right with me."

        else:
            Ry normal flip "It’s alright, [player_name]. Even if the council manages your direct finances, I would still rather want to pay. It wouldn’t sit well with me if I exploited the council’s funding like that."

        c "Alright..."
        $ renpy.pause (0.5)
        m "Remy went to pay for our desserts at Katsuharu's stand. Katsuharu pulled out a small piece of paper akin to a cheque, with Remy filling all the necessary pieces of information in. A few minutes passed before the grey dragon took the piece of paper and put it in his cart."
        $ renpy.pause (0.75)

        Ry smile flip "Thank you as always, Katsuharu."
        Ka smile "And thank {i}you{/i} for coming here, Remy."

        $ renpy.pause (0.5)
        hide katsu
        hide adine
        hide remy
        with dissolve
        $ renpy.pause (0.5)

        m "We walked for a little while, slowly eating our ice creams in silent bliss."

        show amely normal at Position(xpos = 1.5) #NYOOOOOOOOM
        $ renpy.pause (1.5)
        show amely normal at Position(xpos = -1.85) with ease 
        $ renpy.pause (1.0)

        m "Except for Amely, who sprinted wildly after she had gobbled her ice cream in just a few bites."

        hide amely
        show remy normal flip at Position(xpos = 0.15)
        show adine normal b at Position(xpos = 0.85)
        with dissolve
        $ renpy.pause (0.5)

        Ad annoyed b "Amely!"
        $ renpy.pause (0.5)
        Ad "Ugh, I’ll deal with her. [player_name], can you hold my ice cream real quick?"
        c "Sure."
        Ad "Thanks."
        
        $ renpy.pause (0.3)
        show adine annoyed c with dissolve
        $ renpy.pause (0.3)
        hide adine with dissolve
        play sound "fx/takeoff.ogg"
        m "Adine took to the skies and flew towards Amely, who was running in circles. Me and Remy were both silently amused by the unfolding spectacle, wondering how long Amely could withstand Adine's attempts to calm her down."

        $ renpy.pause (0.3)
        show remy at center with ease
        show remy normal with dissolve
        $ renpy.pause (0.5)

        Ry shy "Perhaps chocolate ice cream was a bit too much."

        menu:
            "You don’t say?":
                $ kol_tlh_chapter3B_mood -= 1
                Ry "In hindsight, I guess it was a bit obvious that anything sweet would make Amely so energetic."
                Ry "I… didn’t think this through enough."

            "Well, Adine did say that chocolate ice cream was more than enough.":
                Ry "I didn’t think that she meant it literally. I just thought that it was some sort of hyperbole to make me feel more certain about Amely’s choice of ice cream."

            "I can only imagine how Amely must be if she had toffee ice cream.":
                $ renpy.pause (0.5)

                Ry "I don’t think that I want to imagine it. Maybe Adine’s statement of Amely being able to power the town could have some credibility."
                Ry normal "I’ll just have to remember not to give her anything on that level of sweetness next time."

        Ad giggle c "Gotcha!" with vpunch
        $ renpy.pause (0.5)
        Ry normal "And it looks like Adine finally caught Amely."

        show remy at Position(xpos = 0.85) with ease
        show adine normal c flip at Position(xpos = 0.15) with easeinleft
        $ renpy.pause (0.15)
        show adine normal b flip with dissolve
        $ renpy.pause (0.5)

        Ad "Phew. That was exhausting."
        Ad giggle b flip "My ice cream, if you will."
        c "Here you go."
        Ad "Thanks."
        Ad think b flip "You know, Amely running off like that just gave me a pretty good idea. How about we go to the beach and unwind for a while?"
        Ad normal b flip "I’m sure that Amely would appreciate it."
        Ry shy "I think the beach is a bit too far for Amely to walk."
        Ad giggle b flip "After the ice cream she just had, I think that she has more than enough energy to make it to the beach and back."
        Ad normal b flip "Speaking of, we should really eat our ice creams faster. They’re starting to melt."

        menu:
            "Speak for yourself. I have a bowl.": #In the ice cream nobility, having a bowl makes you a lord and gives you permission to talk down to the peasants that use cones. Obviously.
                $ kol_tlh_chapter3B_mood -= 1
                $ renpy.pause (0.5)

                Ad annoyed b flip "Well, sorry that we’re not fortunate to have a bowl for our ice cream."
                Ry "It’s fine, Adine. We’ll just have to eat faster, that’s all."

            "I totally forgot about the fact that ice cream could melt.":
                $ renpy.pause (0.5)

                Ad giggle b flip "I’m glad to have reminded you of that, then."
                Ad think b flip "It’s a bit weird that you forgot that ice cream could melt, but I guess your mind must have been somewhere else for you to be able to forget something so trivial."
                Ad normal b flip "Oh, what am I saying? Let’s just keep quiet and eat."

            "Then less talking, and more eating.":
                $ renpy.pause (0.5)

                Ad giggle b flip "As you say, [player_name]."

        $ renpy.pause (1.5)
        stop music fadeout (2.0)
        scene black with dissolvemed
        $ renpy.pause (2.5)

        m "We changed our plans and headed to the beach, eating ice cream along the way. My mouth exploded in a swirl of sweet flavours with each bite I took, all combining to bring a delicate yet potent taste to my palate. Adine and Remy's expressions suggested that they had had a similar experience to mine."

        $ renpy.pause (1.5)
        play music "mx/lily_kol.ogg" fadein (1.0)
        scene beach at Pan ((0, 0), (300, 0), 5.0) with dissolveslow
        $ renpy.pause (3.5)

        m "In due time, we reached the beach just as the heat of the day started to announce itself. Unsurprisingly, Amely ran out into the sand gleefully, finally letting all that pent up energy of hers go."

        show remy normal at Position(xpos = 0.85)
        show adine normal b flip at Position (xpos = 0.15)
        with dissolve

        Ad giggle b flip "Looks like I’ve thought correctly."
        Ry smile "I should have known. After all, you're the one who is closest to Amely. It's only natural to assume you know what she would and would not like."
        Ad normal b flip "I suppose that’s true, but only because of how she seems to like me the most out of everyone that visits the orphanage. Because of that, we get far more time to bond compared to anyone else."
        Ry look "I just wished it would have been feasible to officially adopt Amely. The chances of her getting adopted are already so low…"
        Ad disappoint b flip "Yeah."
        c "Speaking of, where did Amely go?"
        Ad annoyed b flip "Did she run off {i}again?{/i} I swear, she’s {i}never{/i} this energetic."
        $ renpy.pause (0.5)
        play sound "fx/watersurface.ogg"
        m "Just as Adine prepared to take off again, Amely emerged from the ocean waters with a fish in her mouth. She stood proudly among the waves, waving her arms for us to notice her achievement."
        $ renpy.pause (0.3)
        Am "Hmnphnm!"

        show adine normal b with dissolve
        $ renpy.pause (0.3)
        show remy smile with dissolve
        Ad giggle b "You’ll have to take the fish out of your mouth before you talk, silly."

        $ renpy.pause (1.5)
        hide remy
        hide adine
        with dissolve
        show beach at Position(xpos=0.0, xanchor='left', ypos=1.2, yanchor='bottom') with ease #Have I mentioned how much I hate this transitions for not making sense? No? Cool, I hate these transitions for not making sense.
        $ renpy.pause (0.5)
        show amely normal flip at Position(xpos = 0.2) with dissolve
        $ renpy.pause (0.5)

        Am "Me catch fish!" #This was inspired by a peculiar artpiece. I wonder if you can guess which one. :)
        Ry smile flip "Wow Amely, I’m impressed!"
        c "I didn’t know that Amely {i}could{/i} catch a fish."
        Ad think b flip "Neither did I."
        hide amely with dissolve
        m "Before I could think of a response, Amely gobbled the entire fish up in just a few bites. I looked in amazement, wondering how Amely was able to eat anything so fast."

        $ renpy.pause (0.5)
        show amely normal flip at Position(xpos = 0.2) with dissolve
        $ renpy.pause (0.5)

        Am "Yummy!"
        $ renpy.pause (0.5)
        Am "Hmm…{w} me build sandcastle now!"

        $ renpy.pause (0.5)
        hide amely with easeoutright
        $ renpy.pause (0.5)
        hide remy
        hide adine
        with dissolve
        show beach at Position(xpos=0.0, xanchor='left', ypos=0, yanchor='top') with ease
        $ renpy.pause (0.5)
        show remy normal at Position(xpos = 0.85)
        show adine normal b flip at Position (xpos = 0.25)
        with dissolve

        Ry normal "And there she goes again."
        menu:
            "How on earth does Amely have the energy that she has?": #Did you forget how she was zooming around just a while ago, MC?
                $ renpy.pause (0.5)

                Ad think b flip "Your guess is as good as mine. I’ve never seen her this hyper."
                Ry smile "Maybe she’s just extra excited that she could get to hang out with all of us."
                Ad "Maybe. The thing is, the first time she saw [player_name], she was pretty shy. I guess that must have worn off."

            "We don’t have anything to build a sandcastle with.": #You have sand. That's all you need.

                c "One small problem: we don’t have anything that Amely could use to make a sandcastle."
                Ad giggle b flip "Don’t worry about that. Amely will scrape a bunch of sand together and call that a sandcastle."
                Ry normal "How imaginative the mind of a child can be."
                Ad normal b flip "Indeed."

            "Let’s hope that she doesn’t get lost for a third time.":
                $ renpy.pause (0.5)
                $ kol_tlh_chapter3B_mood += 1

                Ad think b flip "You know, I don’t think that she’ll run off this time. If I had to make an educated guess, she’ll probably want to play in the sand until she wants to fall asleep."
                Ad normal b flip "That’s what usually happens when I take her to the park."
                Ry shy "Does that mean she’s fallen asleep in the sandbox before?"
                Ad giggle b flip "More often than not, actually. The sandbox is her favourite place to play after she had her fun everywhere else, which means she's pretty tired by then."
                c "(So, Adine carries Amely back to the orphanage after she’s fallen asleep. What a cute mental image.)"

        $ renpy.pause (1.5)
        c "You know, we could probably join her with her sandcastle."
        Ad think b flip "The last time I’ve built a sandcastle was probably ages ago. I don’t think that I’m capable of making one anymore."
        Ry shy "I don’t think I’ve ever made a sandcastle before."
        c "You haven't?"
        Ry "I spent most of my youth reading or playing video games. I didn’t like outside activities that much."
        c "Ah..."
        c "Well, I didn’t specifically say anything in {i}building{/i} a sandcastle. We could help Amely to decorate her creation with seashells or pebbles."
        Ry normal "I'm up for it."
        Ad normal b flip "Sure. It’s about time I’ve done something like this."
        c "Alright. I’ll try and get some seashells. Adine, will you try to find some pebbles?"
        Ad "Sounds doable."
        Ry shy "What should I get, [player_name]?"
        c "You could try to get a bit of both, or you can get whatever you consider worthy of decorating Amely’s sandcastle."
        Ry smile "I think that I already have an idea."
        $ renpy.pause (0.5)
        hide adine with dissolve
        hide remy with dissolve
        $ renpy.pause (0.5)

        m "Me, Remy, and Adine all scattered in different directions, scouring for whatever materials we could find around the different sections of the beach."
        $ renpy.pause (0.5)
        scene kolextrabeach1 with dissolvemed
        $ renpy.pause (2.5)

        m "After not too much searching, I found an entire area filled to the brim with seashells of different colours, shapes, and sizes."
        c "(I definitely won’t be able to carry all of these. I’ll just have to take the best out of the bunch.)"
        $ renpy.pause (0.5)
        m "After a few minutes of picking up seashells here and there, my arms were soon filled with different kinds of seashells. Satisfied, I returned to the area where me, Remy, and Adine had initially parted."

        $ renpy.pause (0.5)
        scene beach at Pan ((0, 0), (0, 0), 5.0) with dissolve
        $ renpy.pause (0.5)

        m "Adine already waited for me, though Remy was nowhere to be found."
        show adine normal b with dissolve
        $ renpy.pause (0.5)

        Ad giggle b "Looks like you’ve been pretty busy."
        c "Where's Remy?"
        Ad think b "I actually don’t know. I’m guessing he must’ve gone extra far somewhere, though I’m not too certain."
        Ad normal b "Well, I’m sure that whatever Remy brings will look good on Amely’s sandcastle over there."
        m "I turned around to see Amely happily sitting in the sand while creating a massive lump of sand nearly as tall as she was. There also seemed to be a trench of some sort around the castle, filled with ocean water that was quickly seeping into the sand."
        $ renpy.pause (0.5)
        c "Yeah, it will look great. I wonder if Amely will add some finer details herself, though."
        Ad giggle b "Maybe she will after we’ve started decorating for her. All it takes is a little nudge to get her wanting to impress everyone."

        show adine at Position(xpos = 0.8) with ease
        $ renpy.pause (0.25)
        show remy normal flip at Position(xpos = 0.2) with easeinleft
        $ renpy.pause (0.5)

        Ry smile flip "Sorry to keep you two waiting."
        c "Hey, Remy. I’m guessing by your wet tie, you flew over the sea, right?"
        m "Remy looked down and saw that his tie was completely soaked. Embarrassingly, he looked up again, yet avoided my direct eye contact."

        $ renpy.pause (0.55)
        show remy shy flip with dissolvemed
        $ renpy.pause (0.55)

        Ry shy flip "Yes. I wanted to get something special for Amely’s sandcastle, so I had no choice but to fly a bit offshore."
        Ry "Here. This should be a suitable addition to the sandcastle."
        m "Remy opened one of his paws and dropped a bundle of different kinds of seaweed on the sand."
        Ad think b "Seaweed?"
        Ry "You know, so that the sandcastle could look like it has some vines and whatnot."
        Ad giggle b "You know that you could find some seaweed on the shore, right Remy?"
        Ry "I know. The thing is, none of them really looked special enough for me, so I had to do a bit of swimming to get this."

        menu:
            "I didn’t know that you could swim.":
                $ renpy.pause (0.5)
                Ry normal flip "Most dragons can swim to some degree. However, there are a few species, like flyers, that struggle more than your average dragon. In contrast, there are the water types that excel at swimming."
                Ry "My skills at swimming are average; enough to keep myself afloat and to propel myself forward."

            "With how long you took, you could have just flown to town and bought something instead.":
                $ kol_tlh_chapter3B_mood -= 1
                $ renpy.pause (0.5)
                Ry look flip "I guess I could have, though then my contribution would have felt less authentic. Besides, I don’t want to pollute this pristine beach if I can help it."
                Ry "I’d rather get a bit soaked than simply buy something for the purpose of causing more rubbish to be spread everywhere."

            "It’s really thoughtful of you to go through the effort that you did.":
                $ kol_tlh_chapter3B_mood += 1
                $ renpy.pause (0.5)

                Ry normal flip "It’s nothing, [player_name]. Really. I just want to make Amely as happy as I can."

        Ad think b "Sorry to interrupt, but Amely is trying to get our attention."
        Am "Come!" with hpunch
        Ry smile flip "Then perhaps we need to obey."

        $ renpy.pause (0.75)
        scene kolextrabeach2 at Pan ((0, 140), (0,140), 4.0) with dissolveslow
        $ renpy.pause (0.75)

        m "We three walked slowly to Amely, taking care not to draw her attention to our decorations in an attempt to surprise her."
        $ renpy.pause (0.5)

        show kolextrabeach2 at Position(xpos=0.0, xanchor='left', ypos=1.01, yanchor='bottom') with ease
        $ renpy.pause (0.5)
        show amely small at Position(xpos = 0.9) with dissolve
        $ renpy.pause (0.5)

        Am "Look, I built sandcastle!"
        $ renpy.pause (0.3)
        m "Behind Amely stood quite a tall lump of sand that was surrounded by a surprising amount of semi-drained trenches. This sandcastle had a few hollowed out carvings, presumably in an attempt to recreate windows."
        m "At the base were a few smaller lumps of sand spiralling around the main sandcastle, though said lumps stopped around a quarter of the way there."

        $ renpy.pause (0.5)
        show adine normal b flip at Position(xpos = 0.25)
        show remy normal flip at Position(xpos=0.05)
        with dissolve
        $ renpy.pause (0.5)

        Ad giggle b flip "I’m impressed, Amely. This is definitely the prettiest sandcastle that you’ve made!"
        Ry smile flip "For sure! It really is something wonderful!"
        Ry normal flip "But, it needs a little something else, don’t you think?"
        Am "Hm?"
        Ry smile flip "How about some magical vines for your sandcastle?"
        m "Remy dropped the bundle of seaweed that he carried, causing it to spread out across the area. Amely looked at the plants in slight confusion, seemingly baffled by the lump before her."
        m "However, she soon turned to excitement, grabbing the seaweed to place on her sandcastle."
        Ad normal b flip "Amely, wait. Before you start, here’s a few extra things for your sandcastle."
        m "Adine dropped her pebbles neatly on the sand. Following everybody else, I also dropped the seashells that I had gathered gently next to the pebbles, afraid that they might shatter if I tossed them too hard."
        m "Amely, once again, stared at the newfound resources, wondering what to do with them."
        $ renpy.pause (0.5)
        m "And once again, she turned to excitement, grabbing a bit of everything and turned around to decorate her sandcastle."

        $ renpy.pause (0.5)
        hide amely with dissolve
        $ renpy.pause (0.5)

        m "Sadly, she placed her decorations a bit too roughly on the sandcastle, causing it to collapse. Despite this, she continued to place both pebbles and seaweed on the ruins, using the seashells as little roofs for the now broken remnants."

        $ renpy.pause (0.5)
        scene black with dissolve
        $ renpy.pause (2.5)
        show kolextrabeach3 at Position(xpos=0.0, xanchor='left', ypos=1.01, yanchor='bottom') with dissolve

        $ renpy.pause (1.75)
        m "After she had used the majority of her resources, she looked at her creation in awe for a few seconds, before gleefully kicking the sandcastle over, giggling as her foot collided with the sand."
        play sound "fx/sandcastlecollapse_kol.wav" #She's a kid. Of course they'll like to cause chaos once they're bored.
        show amely small at Position(xpos = 0.8) with dissolve
        $ renpy.pause (0.5)

        Am "Fun!"
        $ renpy.pause (0.35)
        show adine normal b flip at Position(xpos=0.25)
        show remy normal flip at Position(xpos=0.05)
        with dissolve
        $ renpy.pause (0.5)

        Ry smile flip "Did you enjoy building your sandcastle, Amely?"
        Am "Very yes!"
        Ad "I’m happy you liked it, Amely. But now, it’s time to go home. It’s getting pretty late, and you still have to finish that drawing of yours."
        Am "Carry?"
        Ad disappoint b flip "Sorry Amely, but not now. You need to walk to get all of that sand between your toes out."
        m "Amely looked down sadly as she slowly walked next to Adine’s side. Adine lowered her wing slightly, letting Amely hold Adine’s hand." #What an absolutely adorable scene. <3
        $ renpy.pause (0.5)

        hide amely
        hide remy
        hide adine
        with dissolve
        $ renpy.pause (0.5)
        show kolextrabeach3 at Pan ((0, 80), (0,80), 4.0) with ease
        $ renpy.pause (0.5)
        show remy normal flip at Position(xpos = 0.15)
        show adine normal b at Position (xpos = 0.85)
        with dissolve
        $ renpy.pause (0.5)

        Ad "I’ll be taking Amely back. I’ll catch you again later, Remy."
        Ry shy flip "Yes, of course. I haven’t forgotten."
        Ad giggle b "Amely, say goodbye to Remy and [player_name]."
        Am "Bye bye!" with vpunch
        Ad normal b "Goodbye, you two."

        $ renpy.pause (0.5)
        show adine normal b flip with dissolve
        hide adine with easeoutright
        $ renpy.pause (0.3)
        show remy at center with ease
        $ renpy.pause (0.5)
        stop music fadeout (2.5)

        m "Adine and Amely walked away from the beach into the town, hand in hand. Remy looked at me with a sense of wistfulness behind his eyes; a look I haven’t ever seen in Remy before." #And this as well. UUh, the walking away part, that is.
        $ renpy.pause (0.5)
        play music "mx/somber_kol.ogg"

        Ry "And there they go. I wonder if that is what it’s like to have children one day. To walk side by side, hand in hand throughout the streets…"
        c "Remy?"
        $ renpy.pause (1.0)
        c "Hey, Remy, are you there?"
        $ renpy.pause (0.3)
        show remy shy with dissolve
        $ renpy.pause (0.3)
        Ry "O-Oh, sorry. I was just daydreaming about something, that’s all."

        menu:
            "Was there more?":
                c "By the way you went on, I’m guessing that there was something more behind those words, right?"
                Ry "N-No, not at all. I can assure you of that. I just let some of my thoughts gain a voice, that’s all. Don’t pay any attention to it."

            "What were you daydreaming about?":
                $ renpy.pause (0.5)

                Ry "What it would be like to raise children and, to some extent, what it would be like to spend a day out with them, like today."
                Ry "Nothing else."

            "Sure you were…":
                $ kol_tlh_chapter3B_mood -= 1

        $ renpy.pause (2.5)
        Ry "I-I have to go home now. I still have to do some prep work for dinner this evening."
        $ renpy.pause (0.5)
        c "Remy."
        $ renpy.pause (0.25)
        Ry "Yes?"


        menu:
            "I’ll see you again some time.":
                $ renpy.pause (0.5)

                Ry "Likewise."

                $ renpy.pause (0.5)
                hide remy with dissolve
                $ renpy.pause (0.5)
                play sound "fx/takeoff.ogg"
                $ renpy.pause (0.5)

                m "Remy made some space for himself and took off with a beating of his wings into the sky, leaving me in a fairly refreshed mood after the day’s events."

                $ renpy.pause(0.5)
                scene black with fade
                $ persistent.kol_tlh_chapter3B_skip = True
                $ kol_tlh_3B_played = True
                stop music fadeout (1.0)
                $ renpy.pause(3.5)

                jump tlh_Chapter4A

                # ===========================================
                # END OF CHAPTER 3
                # ===========================================

            "What's wrong?":
                $ renpy.pause (0.5)
                $ kol_tlh_3B_remyasked = True

                c "I’ve noticed a few things recently. How you’ve experienced sudden mood changes out of nowhere. How you seem to be taken back by some things happening. Even your expression is sometimes unusual."
                c "What’s wrong? How can I help you out?"

                stop music fadeout (0.5)
                $ renpy.pause (1.0)

                Ry "..."
                Ry sad "..."
                $ renpy.pause (0.8)
                Ry "You don’t have to worry if that’s what you’re wondering, [player_name]. I can take care of myself." #The number one cause of making people worry is telling people not to worry.
                Ry "Goodbye."

                $ renpy.pause (0.5)
                hide remy with dissolve
                $ renpy.pause (0.5)
                play sound "fx/takeoff.ogg"
                $ renpy.pause (0.5)

                m "Remy made some space for himself and quickly took off with a beating of his wings, leaving me with even more questions than answers."
                m "Despite this, I felt strangely ignorant. Surely there had to be something obvious in Remy's behaviour that I'm overlooking..."

                $ renpy.pause(0.5)
                scene black with fade
                $ persistent.kol_tlh_chapter3B_skip = True
                $ kol_tlh_3B_played = True
                $ renpy.pause(3.5)

                jump tlh_Chapter4A

                # ===========================================
                # END OF CHAPTER 3
                # ===========================================





    "Sorry, but I’m a bit busy.":
        $ renpy.pause (0.5)

        Ry shy "Oh, but that’s alright. I’m guessing that your ambassador duties need to come first." #Proceeds to do nothing like a slacker. Huh, maybe Logan was right.
        Ry "See you some other time, then."
        $ renpy.pause (2.0)
        c "(Huh. Remy didn’t sound like he did when he started the call. Weird.)"
        c "(Well, I guess that I should get to work then. Whatever that entails.)"

        $ renpy.pause(0.5)
        scene black with fade
        $ persistent.kol_tlh_chapter3B_skip = True
        $ renpy.pause(3.5)

        jump tlh_Chapter4A

        # ===========================================
        # END OF CHAPTER 3
        # ===========================================




#MAX MOOD VALUE FOR 3B IS 5
#THE MINIMUM IS -5
#GET 2 TO PASS (lowered thanks to a bunch of neutral choices)
