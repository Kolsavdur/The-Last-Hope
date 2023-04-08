label tlh_Chapter5:

#Variable checks to make my life easier when routing the different endings.
#Why dm I doing this here? Because this was an afterthought.
#EDIT from future Kols: Yes, the datecounter variable is an afterthought of an afterthought.
#Screw planning ahead. We be ballin' as we go.

if kol_tlh_chapter1B_mood >= 1:
    $ kol_tlh_1B_success = True
    $ kol_tlh_datecounter += 1
if kol_tlh_chapter2B_mood >= 4:
    $ kol_tlh_2B_success = True
    $ kol_tlh_datecounter += 1
if kol_tlh_chapter3B_mood >= 2:
    $ kol_tlh_3B_success = True
    $ kol_tlh_datecounter += 1
if kol_tlh_remytherapywin == True:
    $ kol_tlh_4B_success = True



if kol_tlh_endingA_route == False:
    $ save_name = (_("TLH - Chapter 5"))

    $ renpy.pause (2.0)
    scene o2 at Pan((0, 0), (0, 150), 4.0) with dissolveslow
    $ renpy.pause (3.0)


    m "The moon and stars shine their silky silver rays of light throughout my apartment, waking me up from my apparent light sleep. Feeling tired, I tried to return to the world of dreams, but no matter how hard I tried, my brain refused."
    m "With no other options, I decided to take a small walk outside to bask in the tranquillity of the night. Yet, as I went to open my door, I heard a knock."

    $ renpy.pause (0.5)
    play sound "fx/knocking.ogg"
    $ renpy.pause (0.5)
    queue sound "fx/door/door_open.wav"
    $ renpy.pause (1.5)
    show logan normal with easeinright
    $ renpy.pause (0.5)

    Lg "Huh. Rare that you open your door so quickly. I guess my presence must have caused you to open the door as soon as I arrived or something."
    c "Why am I not surprised that you’d be the one to knock at my door?"
    Lg annoyed "And why am {i}I{/i} surprised that you’re awake at this time?"
    c "I woke up because I…{w=0.95} don’t know, actually."
    $ renpy.pause (1.0)
    Lg "Must be your body just wanting to get up and do stuff. Happens to all of us."
    Lg normal "Conveniently, that’s exactly what we’re going to do: stuff."
    Lg serious "Remember, we still have the generator in the underground facility. Better sort that out while we can. I don’t think that we’ll be able to get another chance to be alone there before the comet is due."
    c "How do you even know when the police will be on guard tonight?"
    Lg normal "Connections are a powerful thing, let me tell you." #What did you do with Bryce, Logan?
    Lg serious "Now, let’s go. We don’t have long."
    $ renpy.pause (0.5)
    m "I tiredly nodded my head in response and followed Logan outside."
    $ renpy.pause (1.0)

    scene np5 dk with dissolve
    play music "mx/amb/night.ogg" fadein (1.0)
    play sound "fx/steps/rough_gravel.wav"
    $ renpy.pause (2.5)
    scene np4 with dissolve
    $ renpy.pause (2.0)
    scene np3 with dissolve
    $ renpy.pause (2.0)
    show np2 dk with dissolve
    $ renpy.pause (2.0)

    m "The night sky seemed to be slightly brighter than usual, even if the moon was barely in the sky. I could practically see my way around town without too much hassle. Quickly, me and Logan went on our usual path to the underground facility."
    
    $ renpy.pause (0.5)
    scene np1n at Pan((100, 0), (500, 150), 6.0) with dissolveslow
    stop sound fadeout (1.0)
    $ renpy.pause (5.0)
    show logan serious dk with dissolve
    $ renpy.pause (0.5)

    Lg "And we’re here. Hopefully for the last time."

    if kol_tlh_chapter4_minigame_win == True: # ENDING B AND C SPLIT

        Lg "I’ll go and stabilise the upgrades while you go and get the backup generator. Send it through the portal as fast as you can."
        Lg "I'll make sure that this generator will at least be able to power the portal for you to do so. Can't really send the generator through if there's nothing powering it, now can we?" #DEUS EX MACHINA BABY!
        c "How will you be able to see?"
        Lg normal dk "I brought a small flashlight with me."
        c "Alright. In that case, I wish you the best of luck."
        m "Logan nodded as we hurridly went to the underground facility."

        stop music fadeout (1.5)
        $ renpy.pause (1.5)
        scene hallway at Pan((0, 0), (0, 150), 3.75) with dissolvemed
        $ renpy.pause (4.5)
        scene kolmorefacility with dissolve
        $ renpy.pause (1.0)

        m "Me and Logan went into the generator room once again to finish the last step in our convoluted plan. As I could hear Logan tinkering with the main generator, I took the backup generator with me, making sure not to damage any valuable connections or parts."
        
        $ renpy.pause (0.65)
        play sound "fx/metalbox.ogg" #Don't judge me.
        scene black
        $ renpy.pause (0.65)
        m "However, all the lights had immediately turned off as soon as I removed the generator. Despite that, I still managed to find my way through the halls."
        $ renpy.pause (4.0)
        scene np1n at Pan((100, 0), (100, 0), 6.0) with dissolvemed

        m "Making haste, I left the underground facility, keeping an eye out for anybody that might suddenly appear from the starlit shadows."

        $ renpy.pause (1.0)
        play sound "fx/telstart.ogg"
        m "With nobody in the vicinity, I put the generator on the ground and started the portal’s routine. After pressing a few buttons, the portal turned on and sent the generator back home."
        $ renpy.pause (1.5)
        c "(It’s finally done…)"
        $ renpy.pause (1.0)
        m "I stood in silence for a few moments, finding solace in knowing that, whatever might happen back home, everybody I knew would be safe, regardless if the worst were to happen."
        $ renpy.pause (0.5)
        m "A sense of accomplishment rose within the depths of my soul as I walked back to Logan, taking pride in each of my steps."

        $ renpy.pause (1.5)
        scene hallway at Pan((0, 0), (0, 0), 3.75) with dissolvemed
        $ renpy.pause (2.0)
        m "As I saw the lights having turned back on, I knew that Logan had succeeded."
        $ renpy.pause (2.0)
        scene kolmorefacility with dissolve
        $ renpy.pause (1.0)
        show logan normal with dissolve
        $ renpy.pause (1.0)

        Lg normal "It’s done."
        c "I can see that, considering the lights are back on."
        Lg annoyed "That's just a temporary thing. When I allowed you to turn the portal on, I needed to temporarily switch the lights on as well."
        c "Oh..."
        Lg serious "Let’s fully test the generator out together, shall we? Fingers crossed that we didn’t just doom dragonkind."
        c "You really have a way with words, Logan."
        Lg normal "Just as you have a way of pointing the obvious out."
        Lg serious "And, for the moment of truth..."

        $ renpy.pause (1.0)
        hide logan with dissolve
        $ renpy.pause (1.0)
        play sound "fx/fans.ogg"

        m "Logan connected one last wire to the generator and turned it on. Loud sounds of whirring could be heard, followed by something that sounded like a reaction of sorts, though I wasn’t sure."
        $ renpy.pause (2.0)
        stop sound fadeout (4.0)
        m "I held my breath as the generator made more and more weird sounds. After a few pops however, the generator ran as smoothly as it had before."
        m "Logan went over to the generator and checked on one of the panels. He removed a few external pieces, checked something that looked like a meter of some sorts, and put everything back together again."
        
        $ renpy.pause (1.0)
        show logan serious with dissolve
        $ renpy.pause (2.0)
        show logan smiling with dissolve
        play music "mx/scrapyard_kol.ogg"
        $ renpy.pause (1.0)

        Lg "Dragonkind will be safe, [player_name]. We did it."
        m "I sharply let my held up breath leave my lungs and felt the cold, refreshing air of calmness fill my body."
        $ renpy.pause (1.0)
        c "I can’t believe it, Logan. We actually managed to pull through with all of this."
        Lg normal "It was one hell of a journey, that’s for certain. Regardless, our journey yielded a generator that could produce almost three times as much energy as before, while we also scored some valuable stuff back home."
        Lg annoyed "Sure, I don’t think that this generator’s life span will be very long now, especially after the strain that it will endure soon, but it will get the job done."
        c "As long as it won’t explode, then everything is alright."
        Lg normal "Don’t worry about it. I may like zapping stuff, but I’ve put in extra measures to prevent that from happening." #Unintentional reference to TLD or something? Hmmmm...
        Lg annoyed "Heh. The past version of me would be very disappointed that I didn’t at least toy with the opportunity of creating some funny electric arcs, but it doesn’t take a rocket scientist to figure out that doing so would be one hell of a bad idea."
        c "Agreed."
        Lg normal "Now, how about we get out of here for good? This place has caused me more than enough stress."
        c "You and me both, Logan."

        $ renpy.pause (1.0)
        scene np1n at Pan((100, 0), (100, 0), 6.0) with dissolvemed

        m "The two of us left the underground facility and went into the night for the last time. We talked for a bit as we went along the roads to my apartment, discussing nonsensical topics and unnoteworthy banter."

        show np2 dk with fade
        play sound "fx/steps/rough_gravel.wav"
        $ renpy.pause (0.5)

        scene np3 with dissolve
        $ renpy.pause (1.0)
        scene np4 with dissolve
        $ renpy.pause (1.0)
        m "As I turned to the path that will take me back home, Logan stopped me."
        $ renpy.pause (0.5)
        show logan normal dk with dissolve
        $ renpy.pause (1.0)

        Lg "How about you spend the night at my place instead? I just so happen to have an extra bed, you know."

        menu:
            "Sure, I don't mind.":
                $ renpy.pause (0.5)

                Lg smiling dk "Great. You won’t regret that decision."
                $ renpy.pause (0.5)
                c "(Why do I already feel like I regret this decision?)" # *anti-slacker noises intensifies*
                Lg normal dk "My place is a bit far away, so we’ll have to walk quite a bit."
                c "You said it was close to the university, correct? I still don’t really know where in town the university would be, though."
                $ renpy.pause (1.5)
                Lg annoyed dk "..."
                $ renpy.pause (0.5)
                Lg "You need to get out more often." #The irony.
                c "I...{w=0.45}{nw}"
                $ renpy.pause (1.0)
                stop music fadeout (2.0)
                c "...sure, Logan."
                Lg normal dk "Guess I’ll be your tour guide. Follow me."

                $ renpy.pause (0.5)
                play music "mx/infinite_kol.ogg" fadein (1.0)
                hide logan with dissolve
                $ renpy.pause (0.5)

                m "Logan started to walk in front of me, leading the way through a part of town I didn’t initially recognise at night."

                $ renpy.pause (1.5)
                scene kolpathtologan1 with dissolve
                $ renpy.pause (0.5)
                show logan normal dk with dissolve
                $ renpy.pause (1.0)

                Lg annoyed dk "I wonder if the bar would be open right now."
                c "You’re starting to think more and more like Bryce, you know that?" #Maybe it's because Logan was technically just human Bryce? Who knows!
                Lg normal dk "I guess he has influenced me quite a bit while I was here. I can kinda see why everybody seems to have so much respect for the guy."
                Lg thinking dk "Not only does he seem like an amazing guy in general, but he really cares for the average person. Very few police officers are like that back home."
                c "Very few police officers are left back home." #That got dark quickly.
                Lg annoyed dk "You know what I meant."
                Lg normal dk "My point is, he seems like somebody that will go out and beyond to try and help everybody, whether that be somebody in a crisis, a pesky entitled mother, or Bryce’s closest friends."
                Lg serious dk "Sometimes I wonder how he must feel about cases that can’t be solved, or cases where he couldn’t have helped everybody."
                c "I can’t imagine that it must be easy for him."
                Lg "Precisely."
                $ renpy.pause (2.0)
                Lg "[player_name], can I ask you a question?"
                c "Go right ahead."
                Lg "I want you to answer this truthfully, alright?"
                Lg "What will you do when all of this is over and when everything goes back to normal?"

                menu:
                    "I’ll continue my job as ambassador in the dragon world.":
                        $ renpy.pause (0.5)

                        Lg annoyed dk "Even after the trade has been completed when you won’t be needed anymore?"
                        c "If I can strengthen relations as much as I can, then I need to so that everybody back home will still be able to survive."
                        Lg "I commend you for carrying such a heavy burden on your shoulders, but it’s risky."
                        c "Why?"
                        Lg "You could be seen as a runaway of sorts, abandoning everybody back in the city. You could fall into a well of stress feeling that the fate of humanity is all up to you while maintaining relations. You might even be called a traitor for choosing dragonkind over humanity."
                        Lg serious dk "All very realistic scenarios."

                    "I’ll go back home as is expected of me.":
                        $ renpy.pause (0.5)

                        Lg annoyed dk "Interesting that you’d say that."
                        c "How so?"
                        Lg "One would think that you’d at least try to continue to serve as an ambassador. After all, since you’re quite the well-known name in the council, I doubt that they’ll trust any other human to serve as an ambassador if they could just have you instead."
                        Lg serious dk "I’m more than enough evidence of that."
                        c "I could still serve as an ambassador on the other side, though."
                        Lg "If the authorities don’t relocate you to another part of the city instead first."

                    "I’m not certain.":
                        $ renpy.pause (1.5)

                        Lg annoyed dk "Why aren’t you certain?"
                        c "I’ve just been thinking of the short term: getting the comet redirected, getting humanity the generators that they need, serving as an ambassador…"
                        c "I never thought about what I’d do after all of this was over."
                        Lg "Perhaps it’s for the better that you don’t think about the future for now. You already go enough on your plate as is, so thinking about what could happen after all the things you’re currently stressing about would only cause more stress."
                        Lg serious dk "And I’m assuming you know just what stress could do to a person."
                        $ renpy.pause (1.5)
                        c "Yeah."

                $ renpy.pause (0.5)
                Lg normal dk "Luckily for you, those are whenever’s problems. For now, you got to focus on redirecting the comet."
                c "I mean, most of the things we need should be ready to go. It’s just a matter of timing."
                Lg "Good to hear, then."

                $ renpy.pause (0.5)
                show kolpathtologan2 behind logan with dissolve
                $ renpy.pause (0.5)

                c "So, what about you?"
                Lg annoyed dk "I’ll be honest and say that I have no bloody idea. I could do anything from hanging out with Bryce to returning back home."
                c "Both of which wouldn’t be the first time."
                Lg smiling dk "And it probably won’t be the last, either."
                Lg normal dk "But yeah, even if I do decide to go back, I’ll probably go back and forth through the portal, as I have actual ambassador experience now."
                Lg "I guess we’ll just see what the future holds, huh?"
                c "I guess so."

                $ renpy.pause (0.5)
                show tlh_kolloganhousenight behind logan with dissolve
                $ renpy.pause (0.5)

                Lg "Well, we’re here. Now you know where my apartment is."
                c "That's...{w=0.6} unusually large for an apartment, even if it's split in two."
                Lg annoyed dk "I thought so too until I stepped in. The place would be cramped like hell if an entire family lived here."
                Lg normal dk "But for one singular human? Practically feels like a mansion."
                c "I guess it's probably due to how different buildings are built to suit different dragon species."
                Lg "That's my guess as well."

                $ renpy.pause (1.0)
                play sound "fx/door/handle.wav"
                $ renpy.pause(1.0)

                Lg "After you, oh esteemed guest."
                c "How noble of you."
                Lg normal dk "Your bed should be just down the hall on the left hand side."
                c "Thanks. Night, Logan."
                Lg "Night, [player_name]."

                $ renpy.pause (1.5)
                scene black with fade
                $ kol_tlh_logan_apartment = True
                stop music fadeout (1.5)
                stop sound fadeout (2.0)
                $ renpy.pause (4.0)




            "I’m more comfortable in my own apartment.":
                $ renpy.pause (0.5)

                Lg annoyed dk "How boring, then. I really wanted to have a pillow fight with you and share our deepest secrets while we eat some pizza." #Feels a bit too forced for classic Logan attitude, but whatevs.
                c "It’s a tempting offer, but I’ll pass. I need to get as much rest as I can, so sleeping in another bed might cause me a restless night."
                Lg "Yeah, I hate how that happens. You get used to one bed and then find it hard to sleep in another one for some time."
                Lg normal dk "Whatever, then. Sleep well, [player_name]."
                c "The same to you. Whenever you go to sleep, that is."
                Lg smiling dk "You know me too well."

                $ renpy.pause (1.5)
                scene black with fade
                stop music fadeout (1.5)
                stop sound fadeout (2.0)
                $ renpy.pause (1.0)

                m "With those last words, we split our paths and walked alone towards our respective apartments."
                $ renpy.pause (1.0)
                m "Hoping to fall asleep quickly, I went straight to my bed and rested my head. Fortunately, it didn’t take long before I could continue my interrupted slumber."


        $ renpy.pause (3.0)
        if kol_tlh_4B_success == True and kol_tlh_datecounter >= 2:
            # ENDING B HERE

            $ save_name = (_("TLH - Ending B"))

            if kol_tlh_logan_apartment == True:

                scene tlh_kolloganbedroom at Pan((0, 0), (0, 250), 5.0) with dissolveslow
                $ renpy.pause (3.0)
                play music "mx/mountain_side_kol.ogg"

                m "I slowly woke up, initially being confused as to where I was, though I remembered that I spent the night at Logan's place after the fog of sleep had left my mind."
                
                $ renpy.pause (1.0)
                play sound "fx/bed.ogg"
                $ renpy.pause (2.5)
                scene tlh_kolloganhouseinside with dissolvemed
                $ renpy.pause (3.0)

                m "Not wanting to lie in bed all day, I stood up and went to the living room. Strangely, Logan wasn’t there."
                c "(Did I actually wake up before Logan for once? I never thought I’d live to see the day.)" #WITCHCRAFT!
                c "(Well, I better get going to my apartment first considering that I didn’t bring anything along with me when I spent the night here.)"

                $ renpy.pause (0.5)
                play sound "fx/door/door_open.wav"
                $ renpy.pause (1.5)
                scene tlh_kolloganhouse with dissolve
                $ renpy.pause (4.0)
                show sebastian normal b with easeinright
                $ renpy.pause (1.0)

                Sb "Hey."
                c "Sebastian? What are you doing here?"
                Sb "I was looking for you back at your apartment, but you weren’t there. I figured that you might’ve spent the night here instead, considering your…{w=2.5}{nw}"
                
                $ renpy.pause (0.5)
                show sebastian drop b with dissolve
                $ renpy.pause (0.5)

                Sb "...\"partnership\" with Logan." #"Partnership," eh?
                Sb normal b "You need to come with me, please."
                c "I'm guessing Emera."
                Sb smile b "You guessed right."
                Sb normal b "Follow me, please. It’s a long way from here."

            else:
                scene o4 at Pan((0, 0), (0, 250), 5.0) with dissolveslow
                $ renpy.pause (3.0)
                play music "mx/mountain_side_kol.ogg"

                m "My consciousness faded back into reality as I greeted yet another day. With my slightly sore limbs, I got up from my bed to tackle the presumably busy day ahead of me."

                $ renpy.pause (1.0)
                play sound "fx/door/doorbell.wav"
                $ renpy.pause (1.0)
                c "(Three guesses as to who that could be…)" #Logan, Bryce or Seb. Easy.
                $ renpy.pause (0.5)
                play sound "fx/door/door_open.wav"
                $ renpy.pause (1.5)
                show sebastian normal b with easeinright
                $ renpy.pause (1.5)

                c "Oh, hello Sebastian."
                Sb "Good day, [player_name]. I’m guessing that you slept well, correct?"
                c "To an extent."
                Sb smile b "Good. You’ll need the extra energy for today."
                Sb normal b "Would you mind following me, please?"
                c "I'm guessing Emera, right?"
                Sb "Yep. Let’s get going."
                c "Lead the way."
                Sb smile b "I’m fairly certain that you can manage on your own, but I’ll serve as your humble guide for old time’s sake."

            $ renpy.pause (1.5)
            play sound "fx/steps/clean2.wav"
            scene black with fade
            $ renpy.pause (1.5)

            m "We walked through the slightly busy streets without speaking much to each other. When I looked at Sebastian, I could see that he appeared to be stressed, but tried his best to hide it."

            $ renpy.pause (1.5)
            scene town2 with fade
            $ renpy.pause (1.5)

            m "Yet, as soon as we were away from all the surrounding dragons, Sebastian broke our awkward silence."

            $ renpy.pause (1.5)
            show sebastian drop b with dissolve
            $ renpy.pause (2.0)

            Sb "Today."
            c "Today?"
            Sb "The day that the comet gets redirected."
            c "I see.{w} Is everything in order, then?"
            Sb disapproval b "As much as it can be. The council just needs a little time to get everything operational, as well as some general guidance from Remy."
            Sb "The poor guy almost didn’t come, but luckily he managed to show up in the end."
            c "Why? What happened?"
            Sb normal b "From what I’ve heard, he overslept." #Because he's exhausted from work, that's why.
            c "Oh dear."
            Sb disapproval b "You shouldn’t worry about it, though. Happens to everyone."

            $ renpy.pause (1.5)
            show buildingoutside at Pan((0, 0), (0, 0), 0.0) behind sebastian with dissolvemed
            $ renpy.pause (1.5)

            Sb "Well, we’re here. Emera’s in her office. I need to handle a few things back at the police station, so I won’t be able to stay."
            c "It’s alright. See you around, Sebastian."
            Sb smile b "See you around, and good luck with whatever talks you might have with the minister."

            $ renpy.pause (1.0)
            hide sebastian with dissolve
            $ renpy.pause (2.0)
            show corridor with dissolvemed
            $ renpy.pause (1.75)
            play sound "fx/knocking1.ogg"
            $ renpy.pause (2.0)
            Em "Come in, please."
            $ renpy.pause (1.0)
            play sound "fx/door/door_open.wav"
            $ renpy.pause (1.0)
            scene emeraroom at Pan ((0, 0), (0, 180), 5.0) with dissolveslow
            stop music fadeout (5.0)
            $ renpy.pause (2.5)

            m "As I walked into Emera’s office, I saw Remy talking with Emera while holding a file in her hand. Upon close inspection, I could see that Remy looked somewhat tired while he talked. Emera, as usual, showed barely any emotion while she listened."
            m "It took a while before the conversation was redirected towards me, however."

            $ renpy.pause (0.5)
            show emera normal at Position(xpos = 0.8)
            show remy normal flip at Position(xpos = 0.2)
            with dissolve
            play music "mx/forge.ogg"
            $ renpy.pause (2.0)

            Em "Hello, Ambassador [player_name]. My apologies that I didn’t greet you as you entered my office. I was just finishing some discussions with my assistant here."
            Ry "The generator from the underground facility will soon go online, Emera. Once it does, we can start the redirection process."
            Em frown "I’m still upset about the fact that there seemed to be a generator missing. I’ll have the police look into it once this is all over."
            Ry "I have told you this before, Emera. The other generator–{w=1.0}{nw}"
            Em "Has enough power to cover the missing one. I know. This doesn’t excuse the fact that the other generator is missing." #Hmmmmmmmm...
            Ry shy flip "Perhaps it was just a false report, and there was never a second generator in the first place."
            Em mean "Quite frankly, I don’t have the time to discuss this with you any further, Remy. I don’t want to keep our guest waiting."
            Ry normal flip "Of course, Emera."
            Em normal "Now, for the reason I called you here, [player_name]. You see, since you were the one that informed us all of this, I wanted to personally thank you for your service. Without your warnings, we would have never prepared for a possible disaster."
            Ry "I don’t think it’s wise to celebrate just yet. The comet still needs–{w=1.0}{nw}"
            Em frown "Shush, Remy. Don’t you know that it’s rude to interrupt someone while they’re speaking to someone else?" #"You see, it's perfectly fine if I do it, but you? No no no, that won't do at all!"
            Ry shy flip "My apologies, Emera."
            Em normal "As I was saying, without your help, we would have been doomed. Yes, we have experienced several hiccups along the way, but we always managed to pull through."
            Em "That’s why, if we are able to successfully redirect the comet, we will give you full citizenship in our world, as well as permanent ownership of your apartment. In addition, the council would like to reward you for your heroic deeds by awarding you a large sum of money as well as building a statue in your honour in Tatsu Park." #That's... a bit over the top, but sure, I guess.'
            $ renpy.pause (1.0)
            c "Thank you, Minister. I am truly honoured."
            Em laugh "I’m sure that having your name recorded in our history books as the one who saved our entire civilization would make you feel honoured." #Yes, I also hate the fact that I used this sprite for Emera, but screw it.
            Em ques "But, that’s only after this is all over. It would be pointless to reward you if we failed to redirect the comet after all."
            Em normal "And for you, Remy, the council would like to reward you for your services as well."
            Em "After much consideration of your actions—and I do mean {i}much{/i}—the council has decided to give you an honorary position within the council body itself. If we survive, we’ll need somebody to manage the relationship between dragonkind and humanity."
            Em "Since you have the most experience dealing with humans thanks to your collaboration with [player_name], you’ll be granted the position of the Minister of Human Affairs." # :O
            Em "That is, if you are willing to accept this position."

            $ renpy.pause (1.0)
            show remy shy flip with dissolve
            $ renpy.pause (1.0)

            Ry "I am truly grateful for this offer, Emera. Never in my life have I thought that I would actually work with the council instead of for them."
            Em ques "I will forward your response to the other members."

            play sound "fx/phonering.ogg"
            $ renpy.pause (1.0)
            Em normal "Pardon me for a second."
            $ renpy.pause (1.5)
            stop sound
            play sound "fx/phonepickup.ogg"
            $ renpy.pause (1.75)

            Em "This is the Minister of Culture and Arts speaking. How may I help you?"
            $ renpy.pause (1.75)
            Em "If it’s ready, then contact the engineers at the power reserves. Do whatever you need to do according to the plan that the council has laid out for you."
            Em "I wish you the best of luck. Good bye."
            $ renpy.pause (3.0)
            Em ques "The generator is ready. Now we wait."

            $ renpy.pause (1.0)
            m "Remy sluggishly walked to me and stood at my side while sitting down. He then spoke softly to me, enough so that Emera couldn’t hear his words."
            $ renpy.pause (0.5)
            show remy shy flip at Position(xpos = 0.3) with ease
            $ renpy.pause (0.5)
            show remy look flip with dissolve
            $ renpy.pause (1.0)

            Ry "If this doesn’t work out..."
            c "No, Remy. It will. You’ve done enough research to practically guarantee it."
            Ry shy flip "Thank you, [player_name]. It means a lot."
            Ry "Do you think we can meet up at the portal after this?"
            c "Sure. For now, let’s just wait and see the results."
            Ry "Indeed."

            $ renpy.pause (1.0)
            scene black with fade
            nvl clear
            window show

            n "Soon, another call came in, this time from one of the scientists directly responsible for the redirection of the comet. As time passed, he kept us directly informed of the progress that was being made, as well as all the energy reserves left." #Foreshadowing for Ending A, mayhaps?
            n "Minutes soon transformed into hours as everybody sat still, waiting anxiously for the results. We heard updates about our power draining, but nothing about the progress of the comet. As I started to let gloom touch my mind, we heard news that the comet’s trajectory was slowly starting to shift. Apparently, the underground generator that Logan had improved was pulling its weight, but just barely. We heard reports of it struggling to keep up with the immense load that it had to deal with."

            window hide
            nvl clear
            window show

            n "Yet, after half the day had passed, we heard the news that the trajectory of the comet had changed to such an extent that it posed no more risk for dragonkind. The power levels, on the other hand, were so low that large portions of the emergency supply had to be used, leading to concerns about rolling blackouts having to be implemented."
            n "But, whatever would happen, it could be done without the risk of extinction."
            n "After some general supervision by Remy and Emera, the two of them agreed on a plan for how dragonkind would be able to recover from their energy loss. Exhausted, Emera sighed a sigh of immense relief and dismissed both me and Remy. As agreed, the two of us went to the portal as the sun was setting."

            window hide
            nvl clear

            $ renpy.pause (1.5)
            stop music fadeout (3.0)
            scene np1x at Pan  ((200,200), (450,100), 6.0) with dissolveslow
            $ renpy.pause (4.5)

            m "Yet, we weren’t alone. We encountered Logan standing at the portal’s terminal just as we arrived."

            $ renpy.pause (1.5)
            show remy normal flip at Position(xpos = 0.2)
            show logan normal at Position(xpos = 0.8)
            with dissolve
            $ renpy.pause (0.5)
            play music "mx/enigma_kol.ogg"
            $ renpy.pause (0.5)

            Lg "Hey, [player_name]. Didn’t expect to see you here."
            Lg annoyed "Nor your friend, for that matter. I’m guessing that this is Remy, correct?"
            Ry smile flip "Indeed. You must be the Logan that I’ve heard so much about."
            Lg normal "Looks like I’m famous. Such a shame that I’ll have to leave my reputation behind for now."
            c "How come? Aren’t you supposed to stay here to help maintain the trade agreement?"
            Lg annoyed "Well, if you stretch it, I kinda am. I’ll be going back to, uh, \"oversee\" some things that humanity might be up to. You’ll know what I mean."
            Ry normal flip "What will you be overseeing, if I may ask?"
            Lg "It’s complicated. Let’s just say that if somebody skilled doesn’t show up soon, then all the work that me and [player_name] put in will go to waste. Some people are just {i}that{/i} clueless about certain things." #Okay, why the hell did I make Logan an idiot here? *Whyyyyyyyyy?!?!?*
            Ry look flip "Work? What are you talking about? Should I be aware of something?"
            Lg normal "Eh, it doesn’t matter now. Just typical ambassador stuff, that’s all."
            $ renpy.pause (1.0)
            Ry "..."
            c "It’s alright, Remy. Logan probably didn’t get enough sleep again, so he’s just talking nonsense." #Oh that's why. Forgot about this.
            show logan serious with dissolve
            Lg "HEY! Do I {i}look{/i} tired to you? I’ll have you know that I got several hours’ worth of sleep!" with vpunch
            c "Does \"several hours\" translate to a few minutes?"
            Lg annoyed "Damn you, [player_name]."
            Ry shy flip "You seem like quite the interesting person, Logan. It’s a shame that I didn’t have the opportunity to properly meet you."
            Lg normal "The feeling is mutual. You seem like somebody who doesn’t like to sleep in and who actually puts effort into getting stuff done."
            c "Touché, Logan."
            $ renpy.pause (1.0)
            Ry look flip "I..."
            $ renpy.pause (0.5)
            Lg serious "You too, huh? Damn it, I’m surrounded by slackers, aren’t I?"
            Ry "Something simple as waking up late doesn’t necessarily make you a slacker, I’m afraid. [player_name] knows this all too well."
            Lg annoyed "I might have to follow up on that at some point. Sounds like quite an interesting story."
            Lg normal "Oh well, it’ll have to wait. I need to go back home to stabilise and manage a few things. I’ll probably be back, but don’t expect it to be any time soon."
            Lg "It was nice to finally be able to meet you, Remy. {w}Even if it had to be while I was leaving."
            Ry normal flip "The feeling is mutual, Logan. Stay safe."
            $ renpy.pause (1.0)
            m "Logan nodded in response and held out his hand toward Remy. After a bit of struggle, Remy managed to shake Logan’s hand."

            stop music fadeout (2.0)
            play sound "fx/tel.wav"
            $ renpy.pause (5.5)
            hide logan with dissolveslow
            $ renpy.pause (1.0)

            m "The portal started its typical routine as Logan stood between the two pillars, slowly fading away from this world. Once he fully disappeared, Remy looked at me with a grateful yet exhausted expression."

            stop sound fadeout (2.0)
            $ renpy.pause (1.0)
            show remy normal flip at center with ease
            show remy normal with dissolve
            $ renpy.pause (3.0)
            play music "mx/library.ogg"
            $ renpy.pause (1.5)

            Ry shy "It’s over. We did it."
            c "We did."
            Ry "I wouldn’t have been able to do half of the things I did without you, you know."
            Ry normal "And before you say anything, I’m serious here. Even when I felt on the verge of giving up due to exhaustion, I pushed through. Your kindness just gave me the inner strength that I needed to make it to the end of the day."
            c "Remy..."
            Ry shy "Do you know why I wanted us to meet at the portal?"
            c "Do tell."
            $ renpy.pause (1.0)
            Ry look "It was here that Vara died, and it was here that I felt the agony of grief once more. It was here that, once again, I felt my soul being torn apart, where wounds on top of wounds formed, where guilt overflowed, and where I lost my mind." #Why does this feel like a machine wrote this? Is it just me, or did a machine write this?
            Ry sad "All in front of you, no less."
            $ renpy.pause (1.0)
            Ry shy "But here is also the place where we first met—the place where I would meet the one who would save me from myself; the place that would kickstart my recovery."
            Ry "And, of course, the place where I can look back and say that all the suffering, all the torment, all the nights where I would stay awake and stare at the ceiling with tears in my eyes, longing for a future that I would never experience…"
            $ renpy.pause (1.0)
            Ry "All of that? It was worth it."
            c "Remy, I don’t think I can express how humbled I am to hear you say those words. Despite you having gone through so much in your life, to hear that life has started to finally look up for you after so long makes me happy."
            Ry normal "You don’t need to express anything, [player_name]. I just wanted to tell you how I felt, that’s all. Simply being able to speak and knowing that someone close to me will listen is a reward in and of itself. "

            menu:
                "Sounds like a pretty measly reward then.":
                    $ renpy.pause (0.5)

                    Ry "Perhaps it is, but it doesn’t matter to me. Yes, I might have a fancy new position and new responsibilities that come with it, but knowing that I accomplished it all with you? It means more to me than getting the position itself."

                "[[Hug Remy.]": #As if you didn't hug Remy enough in this mod...

                    c "Then let me give you another reward."
                    Ry shy "It really isn’t necessary, [player_name]. You don’t have to–{w=0.85}{nw}"

                    $ renpy.pause (0.5)
                    hide remy with dissolve
                    $ renpy.pause (0.5)

                    m "Interrupting Remy, I grabbed him and gave him a tight hug around his chest. Remy jerked back in surprise, but soon felt comforted by my embrace. After some hesitation, Remy unfolded his wings and wrapped them around me, protecting my back from the elements."
                    $ renpy.pause (0.5)
                    play sound "fx/purr.ogg" fadein (1.0)
                    m "Remy also started to move his tail around my waist to pull me in even closer, resting his head on my shoulder and started to softly purr."
                    $ renpy.pause (2.5)
                    m "We stood like this for several minutes, happily enjoying this special moment. Eventually, Remy unfolded his wings and let me go."
                    
                    stop sound fadeout (0.5)
                    $ renpy.pause (1.5)
                    show remy shy with dissolve
                    $ renpy.pause (0.5)

                    Ry "T-Thanks, [player_name]. That...{w=0.5} was most certainly a reward."
                    c "You’ve certainly started to give better hugs, you know. Have you been practising?"
                    Ry "Do I? I guess I just felt more comfortable returning the kind gesture."
                    c "As long as you enjoyed it, Remy."
                    Ry smile "I did."

                "You’re underselling yourself, you know. For the work you put in, you deserve far more than just a simple conversation.":
                    $ renpy.pause (0.5)

                    Ry normal "I do have a new position on the council. Isn’t that already more than enough?"
                    c "Not in the slightest."
                    Ry shy "How so?"
                    c "Let’s just say that being able to fight depression while also working yourself to the bone makes you deserve much more than a new job and the ability to have a conversation with someone you deeply care about."
                    $ renpy.pause (1.5)
                    Ry "I-I suppose you have a point."

            $ renpy.pause (0.5)
            if kol_tlh_3B_played == True:
                Ry normal "I know that this is a bit late and that the chance is slim, but would you like to get some ice cream? Just the two of us this time."
            
            else:
                Ry normal "I know that this is a bit late and that the chance is slim, but would you like to get some ice cream? Just the two of us."

            c "I’ll be happy to go with you, Remy."

            if kol_tlh_3B_played == True:
                Ry smile "I’m guessing you want some spaghetti again?"
                c "Remy, it’s called spaghettieis, not spaghetti."
                Ry "I’m glad to see that you're learning."

            else:
                Ry "What flavour would you like?"
                c "I have no idea. I guess I’ll just see what’s available first."
                Ry "I don’t think there will be too many options considering how late it is, but you can try your luck."
            
            Ry normal "Well, let’s go before it becomes too dark."
            c "Lead the way, Remy."
            
            $ persistent.kol_tlh_EndingB_done = "B"
            $ kol_tlh_endingB = True

            jump kol_tlh_credits
            
                    












        

        else:
            # ENDING C HERE

            $ save_name = (_("TLH - Ending C"))


            if kol_tlh_logan_apartment == True:

                scene tlh_kolloganbedroom at Pan((0, 0), (0, 250), 5.0) with dissolveslow
                $ renpy.pause (3.0)

                m "As my body and mind drifted towards the realm of the conscious, I was initially confused as to where I was. Luckily, that confusion soon faded away after Logan stood next to me."

                $ renpy.pause (1.0)
                show logan normal with dissolve
                play music "mx/couch_kol.ogg"
                $ renpy.pause (0.5)

                Lg "What a coincidence. I was just about to wake you up, though it looks like your body decided to do that for me."
                Lg smiling "I guess you’re finally starting to become less lazy."

                menu:
                    "I honestly hope not.":
                        $ renpy.pause (0.5)

                        Lg annoyed "You’d…{w=0.4} rather stay lazy?"
                        c "I’d rather not wake up at the crack of dawn and lose the ability to sleep in."
                        Lg normal "So you’d rather be lazy."
                        $ renpy.pause (1.0)
                        c "Yes, Logan. I’d rather be lazy."
                        Lg "I figured as much."

                    "What’s next, you fixing your sleep schedule?":
                        $ renpy.pause (0.5)

                        Lg normal "The day when I’ll drink motor oil for a few bucks will arrive sooner than the day when I’ll fix my sleep schedule." #wut
                        c "I didn’t expect such a comparison."
                        Lg "But it had served its purpose effectively, no?"
                        c "I...{w=0.4} guess so."
                        Lg "Then nothing is the matter here."

                    "Sleeping in isn’t lazy, Logan.":
                        $ renpy.pause (0.5)

                        Lg annoyed "Yeah, it is. If you don't get up early, then you’re just wasting time by getting more sleep than you need instead of doing something productive."
                        c "Different people need different amounts of sleep."
                        Lg "My point still stands. If you sleep in, then you’re wasting time."
                        Lg normal "Thus, making you lazy."
                        $ renpy.pause (0.5)
                        c "…I’m not going to be able to change your mind, am I?"
                        Lg "Not in the slightest."

                $ renpy.pause (1.0)
                c "Speaking of, why did you want to wake me up in the first place?"
                Lg serious "Bryce delivered a letter just a bit ago for the two of us. I’m guessing that both of our letters are the same."
                Lg "And if so, then we’ll have to make another unfortunate visit to that old green hag."
                c "You {i}really{/i} don’t like Emera, do you?"
                Lg "Why should I? She fits the classical haughty stereotype of a politician who only cares about votes and the public's opinion of her. Sure, I haven’t known her as long as you have, but I know her type. Am I wrong?" #Don't worry, Logan: nobody likes Emera.
                $ renpy.pause (2.0)
                c "...no, you're right."
                Lg "So, why should I like somebody who only wants to do something for the sake of making people like them more? Actually helping people in the field instead is far better."
                $ renpy.pause (1.0)
                Lg "I guess that’s one thing that I like more about life after the solar flare than about life before it." #Interesting that Logan would say this if you take TLD into consideration.
                c "Reza shared the same sentiment, you know. We even had a long talk about how the solar flare made everybody equal."
                Lg annoyed "Interesting. You might want to tell me what Reza said at some point, then."
                Lg serious "But later, of course. We need to go."
                c "I’d like to read my letter first, though."
                $ renpy.pause (1.5)
                Lg "*sigh*"
                Lg "Fine."
                $ renpy.pause (1.0)
                m "I opened my letter and swiftly read through its contents."

                play sound "fx/envelope.wav"
                $ renpy.pause (0.5)

                nvl clear
                window show

                n "Greetings, Ambassador."
                n "The time has arrived for us to redirect the comet. You are requested to attend a final meeting with one member of the council to discuss any potential queries that need to be highlighted before the redirection process will start."
                n "Please make haste, as this is an incredibly urgent matter."
                n "Sincerely,"
                n "The Council of Dragonkind"

                window hide
                nvl clear

                $ renpy.pause (1.0)
                c "Well, this is the first time that the council addressed me directly."
                Lg annoyed "How peculiar. Was your previous messages sent to you by Emera herself, then?"
                c "Yeah."
                Lg "Odd."
                Lg serious "Eh, whatever. So, are you finally ready to go?"
                c "Yeah, let's go."

                $ renpy.pause (0.5)
                hide logan with dissolve
                scene black with fade
                $ renpy.pause (0.5)

                m "Both me and Logan set out for the day. As we went through the town, I wondered why Logan would be called by the council as well. I figured that it had something to do with the trade agreement between dragonkind and humanity, but somehow that idea felt… {w=3.0}wrong."



            else:

                scene o4 at Pan((0, 0), (0, 250), 5.0) with dissolveslow
                $ renpy.pause (3.0)

                m "Yet another sunny day packed with possible work ahead of me had arrived. Figuring that I had a bit of time left before I went out, I made myself breakfast with whatever hadn’t been cleared out by Remy the other day."
                $ renpy.pause (0.5)
                m "Looking through the available options of things that I could recognise, most of them didn’t look very appetising to me. Eventually, I settled on a breakfast classic: eggs on toast."
                $ renpy.pause (1.5)
                m "After several minutes of prepping and cooking, my breakfast was ready." #Why didn't I include sounds for this part? I swear, my laziness is gonna be the death of me...
                $ renpy.pause (2.5)
                m "Unfortunately, it didn’t taste as good as I hoped it would."
                c "(I probably should’ve just gone out to eat instead. Oh well.)"
                m "Just before I started to clean the dishes, I heard my doorbell ring."
                
                
                play sound "fx/door/doorbell.wav"
                $ renpy.pause (3.0)
                c "Coming!"
                $ renpy.pause (0.5)
                play sound "fx/door/door_open.wav"
                $ renpy.pause (1.5)
                show bryce normal b with easeinright
                $ renpy.pause (0.5)
                play music "mx/clouds.ogg"

                Br "Good morning, [player_name]."
                c "Hello, Bryce. Can I help you with anything?"
                Br smirk b "You could take this as a starter."
                $ renpy.pause (0.5)
                m "Bryce carefully handed me a small, sealed letter while trying his best not to shred it."
                $ renpy.pause (0.5)
                Br stern b "It’s from the council. I’m guessing that it had something to do with the comet."
                Br "The thing is, I had to deliver another letter from the council to Logan as well. Why he’s wanted makes me question a few things, but I suppose I should keep my nose out of political affairs unless requested to do so."
                c "It might just be that Emera wanted to talk to Logan about some stuff with the trade."
                Br "It's a possibility."
                Br normal b "Well, I’d love to chat a bit more, but things need to be done at the police office, so I need to go."
                c "It’s alright, Bryce. After all the chaos that went on with Reza, Logan, and Maverick, I can imagine that a lot of cases would have to be temporarily put on hold until all the internal affairs had been dealt with."
                Br stern b "It’s not the several cases that are the problem. Things are pretty calm now that Reza is gone. It’s those internal affairs that are still the problem."
                Br "Things are still a bit dicey after the whole Maverick situation we dealt with, but we’ll manage. We handled Reza, so we can handle this."
                c "I wish you the best of luck, Bryce."
                Br smirk b "Thanks, [player_name]. Good luck with whatever the council wants to speak to you about."
                c "Thanks Bryce."

                $ renpy.pause (1.0)
                show bryce smirk b flip with dissolve
                hide bryce with easeoutright
                $ renpy.pause (0.5)
                play sound "fx/door/doorclose.ogg"
                $ renpy.pause (0.5)
                m "As Bryce left my apartment, I opened the letter and started to read."

                play sound "fx/envelope.wav"
                $ renpy.pause (0.5)

                nvl clear
                window show

                n "Greetings, Ambassador."
                n "The time has arrived for us to redirect the comet. You are requested to attend a final meeting with one member of the council to discuss any potential queries that need to be highlighted before the redirection process will start."
                n "Please make haste, as this is an incredibly urgent matter."
                n "Sincerely,"
                n "The Council of Dragonkind"

                window hide
                nvl clear

                $ renpy.pause (1.0)
                c "(Why would the council address me directly this time, rather than Emera? And why would it feel so…{w=0.5} empty? Surely something had to be left out of the letter, right?)"
                c "(I guess I have no choice but to find out.)"

                $ renpy.pause (0.5)
                scene black with fade
                $ renpy.pause (0.5)

                m "As instructed, I hastily left my apartment and went towards Emera’s office."
                m "Somehow, the town felt different than usual, as if a feeling of isolation had descended on the streets. I tried my best to ignore it, instead focusing on my mission."

            
            $ renpy.pause (0.5)
            scene buildingoutside at Pan((0, 0), (0, 0), 0.0) with dissolvemed
            $ renpy.pause (0.5)
            stop music fadeout (5.0)

            if kol_tlh_logan_apartment == True:
                m "It wasn’t long before we arrived at the office building where the fate of dragonkind—and, by extension, humanity—would be dictated."

            else:
                m "It wasn’t long before I arrived at the office building where the fate of dragonkind—and, by extension, humanity—would be dictated."
                $ renpy.pause (0.5)
                m "Though before I entered the building, I spotted Logan off to the side. As I approached him, he seemed slightly surprised at my arrival."

                $ renpy.pause (0.5)
                show logan normal with dissolve
                $ renpy.pause (0.5)

                Lg "Well, hello [player_name]. Didn’t expect to see you here."
                c "I thought that Bryce told you that I would have to go to Emera as well."
                Lg annoyed "Did he tell you, then? Because he most certainly didn’t tell me." #Why?
                c "Yeah, he did."
                Lg "Oh well. It doesn’t matter now. Point is, we’re both here right now."
                Lg serious "So, are you ready for whatever we need to talk about in there?"
                c "As ready as I can be."
                Lg "Then you’re already more prepared than I am. I don’t think I’m able to describe how much I don’t want to be a diplomat right about now. Like I said, the life of bureaucracy doesn’t fit me."
                Lg "If I had a say in the matter, then I’d rather be working on some other stuff."
                $ renpy.pause (0.5)
                c "Logan, are you stalling?"
                Lg normal "What makes you think that?"
                c "I mean, here you are talking to me instead of actually going in. On top of that, you looked like you were just standing outside for a while before I arrived."
                $ renpy.pause (2.5)
                Lg "..."
                c "..."
                $ renpy.pause (0.5)
                Lg annoyed "Let’s go in and see what Emera wants." #Confirmation!

            m "Taking a deep breath, the two of us entered the office building and made our way to Emera’s office."

            $ renpy.pause (0.5)
            show corridor with dissolvemed
            $ renpy.pause (0.75)
            c "(Here we go.)"
            $ renpy.pause (1.0)
            play sound "fx/knocking1.ogg"
            $ renpy.pause (2.0)
            Em ques "Please enter."
            $ renpy.pause (1.0)

            play sound "fx/door/door_open.wav"
            $ renpy.pause (1.0)
            scene emeraroom at Pan ((0, 0), (0, 180), 5.0) with dissolveslow
            $ renpy.pause (3.5)
            show emera normal at Position (xpos = 0.8) with dissolve
            show logan normal flip at Position (xpos = 0.2) with easeinleft
            play music "mx/politics.ogg"
            $ renpy.pause (0.5)

            Em "Welcome, ambassadors. I didn’t think that the both of you would arrive in unison." #*Sure...*
            c "Do you want to talk to us separately then, Minister?"
            Em normal "Oh, no need. This matter will involve the both of you. If Logan was unaware of the threat that we face, perhaps I would have felt the need to talk to you separately."
            Em frown "All the energy we had gathered to redirect the comet is ready, though it seems that there was only one underground generator instead of the two that we were led to believe. Do you have any ideas about this?"

            $ renpy.pause (0.5)
            show logan annoyed flip with dissolve
            $ renpy.pause (0.5)

            c "I’m afraid not."
            Em "Strange. I was hoping that you would know considering that you were one of the last known people to enter the underground facility."
            Em ques "No matter. The generator that we were able to retrieve is more than enough to cover the missing generator."
            Em normal "I’ll still have the police investigate this matter, however."
            $ renpy.pause (1.0)
            Em "This brings us to the trade agreement."
            $ renpy.pause (1.0)
            Em frown "Ambassador Logan, due to our circumstances, we will have to put the trade on hiatus while we recover from our huge energy expenditure. If we don’t use every generator we have after we have redirected the comet, then we will face an enormous energy crisis."
            Em ques "It just wouldn’t work if both of our civilisations had extreme issues with a shortage of electricity, now would it?"
            $ renpy.pause (0.75)
            Lg serious flip "..."
            Lg "No, it wouldn’t."
            Em normal "However, I am acutely aware that sending you back and forth again would drain even more energy from humanity's reserves. Hence, I have decided that we shall send a letter to humanity while you continue to serve your duties as ambassador here."
            Em frown "Besides, that {i}was{/i} why you were sent back here, correct?"
            Lg "Indeed. I thank you for your decision, Minister. I will continue to serve my duties and oversee the trade agreement once everything is stable again."
            Em normal "Good. Now, are there any other matters that need to be dealt with?"
            c "Actually, yes. Shouldn’t Remy be present as well considering his contributions to redirecting the comet?"

            show emera frown with dissolve
            $ renpy.pause (1.5)
            Em "He should. However, Remy called in sick today. From what I’ve heard of him, his illness is a very serious matter."
            Em ques "All his research had been handed in, so Remy being absent isn’t too much of an issue."
            Lg "A question from my side, Minister."
            Lg annoyed flip "What am I supposed to do while humanity waits for our generators?"
            Em normal "We shall discuss it after the comet has been redirected. One problem at a time, Ambassador."
            Lg serious flip "So be it. I was hoping to be more productive while I wait, but it seems that I can’t be ahead of the gears of bureaucracy."
            Em ques "Politics really is a complicated game, I’m afraid." #"Politics is complicated," said the politician. Eeyup, totally nothing fishy here.

            play sound "fx/phonering.ogg"
            $ renpy.pause (1.0)
            Em normal "Please excuse me."
            $ renpy.pause (1.5)
            stop sound
            play sound "fx/phonepickup.ogg"
            $ renpy.pause (1.75)

            m "Emera turned her focus away from us to answer a phone call. After exchanging a few words, her face slowly became more and more stressed."

            $ renpy.pause (1.5)
            show emera frown with dissolvemed
            $ renpy.pause (1.5)

            Em "[player_name] and Logan, the time has come. Let us hope that our endeavours are successful."
            c "Let’s hope so."
            Lg serious flip "The moment of truth."

            $ renpy.pause (1.0)
            scene black with fade
            nvl clear
            window show

            n "The three of us waited for the occasional news that we would receive over the phone. As the minutes passed, anxiety started to consume my soul as I became more and more worried that something had gone wrong."
            n "However, that wasn’t the case. It was late in the evening when we heard that the comet had been successfully redirected, although at a severe cost. Not only had the emergency energy reserves been used, but the underground generator had also been damaged thanks to the strain that it had endured."
            n "Logan, upon hearing this news, was devastated—not because his ingenuity hadn't met his high expectations, but because he couldn’t use the portal while the generator was undergoing repairs. For the time being, we were both stuck here." #Huh. This will directly contradict the portal scene in Ending E. Will I fix this? ...nah.

            window hide
            nvl clear
            window show
            stop music fadeout (4.0)

            n "Exhausted from all the stress, me and Logan parted ways for the day, knowing that we'd have to meet again soon to discuss what we'd be doing in the dragons’ world. While Logan went to the bar to presumably have another outing with Bryce, I instead decided to check up on Remy."

            window hide
            nvl clear

            $ renpy.pause (1.5)
            scene remyapt at Pan ((0, 80), (0,80), 5.0) with dissolveslow
            $ renpy.pause (3.3)
            show remy look with dissolve
            play music "mx/lily_kol.ogg"
            $ renpy.pause (1.5)

            Ry "Hello, [player_name]."
            c "Hey, Remy. Everything alright?"
            Ry "For now, it should be. I just need some time to recover, that’s all. There’s only so much you can do before completely burning out to the point where you need to stay in bed."
            Ad annoyed b "Remy! What did I tell you about not resting?"

            show remy at Position(xpos = 0.85) with ease
            show adine annoyed b flip at Position(xpos = 0.15) with easeinleft
            $ renpy.pause (2.0)
            show adine normal b flip with dissolve
            $ renpy.pause (0.5)

            Ad "Oh, hey [player_name]. I didn’t know that you were visiting."
            c "What are you doing here, Adine?"
            Ad "Remy asked me to take care of him while he’s bedridden. The poor guy can barely do anything now that his body has completely crashed."
            c "Surely there has to be something I can help you with, right?"
            Ry shy "I’m afraid not. I already have all the help that I need right now, so any extra help would just be unnecessary."
            Ry normal "The extra conversation is appreciated, though."
            $ renpy.pause (1.0)

            if kol_tlh_4B_played == False:
                Ry look "You know, this entire thing with overworking has reminded me of something."

                $ renpy.pause (1.0)
                show remy sad with dissolvemed
                $ renpy.pause (0.5)

                Ry "No. Someone."
                Ad sad b flip "Remy, don’t bring it up if you’re not comfortable with it."
                Ry "No, I need to. [player_name] got me to this point, so it’s only fair that I talk about it."
                $ renpy.pause (1.0)
                Ry "The fact that I worked so much through both day and night reminds me a lot of Amelia. Perhaps I would have ended up like her as well if I had continued to work just a little bit longer or if I had started to take even more supplements to continue working on my research." #Supplements? Sickness from exhaustion? Yikes...
                Ry "I was {i}so{/i} close to making Adine lose someone important to her again, but I didn’t."
                Ry shy "And for that, I’m thankful."
                Ad disappoint b flip "Remy, I knew you felt bad about working so hard, but this? I wasn’t expecting this whatsoever."
                Ry "It’s alright. I’m just thankful that you were there for me when I called you the other night, and how you managed to talk me out of working even more than I already was."

            Ry shy "Still, it’s a bit of a shame that I wasn’t there to see the comet being redirected, but I guess knowing that I contributed is good enough for me."
            c "Well, rest is far more important for you now, Remy. Just take it easy and let Adine take care of you."
            Ad giggle b flip "That’s the plan."
            Ad normal b flip "Are you going back home now that the comet has been redirected, [player_name]?"
            c "I’m not entirely sure. I haven’t really given it much thought."
            Ry normal "Well, whatever your decision, I’ll support you regardless."
            Ry smile "Besides, I'm sure we'll run into each other again." #If only you knew.
            Ad "But for now, you need to go back to bed, Remy. It’s time to take your temperature again."
            Ry look "Again? I just measured my temperature."
            Ad annoyed b flip "I need to constantly monitor your body’s reaction to see if you’re starting to feel better, Remy. We’ll measure your temperature again."
            Ry "Alright..."
            $ renpy.pause (0.5)
            Ry normal "Well, I guess I’ll see you some other time then, [player_name]. Do stay safe for now."
            Ry shy "And, thank you."
            c "No worries, Remy."

            $ renpy.pause (0.5)
            scene black with fade
            $ renpy.pause (4.5)
            stop music fadeout (5.0)
            scene o at Pan((0, 250), (0, 250), 5.0) with dissolveslow

            m "I returned to my apartment, deciding that I needed as much rest as I could gather after the day’s events. Once I opened the door, I saw that a familiar figure was resting on my couch, as if waiting for me to return."
            
            $ renpy.pause (0.5)
            if persistent.kol_tld_ending_achieved == True:
                play music "mx/clocks_kol.ogg"

            else:
                play music "mx/clocks.ogg"

            show izumi normal with dissolvemed
            $ renpy.pause (0.5)

            As "Welcome back." #THE BITCH IS BACK! LONG LIVE THE BITCH!
            c "Good to be back. {w}Izumi."
            Iz "So you remember my name. I guess this won’t be necessary anymore."

            $ renpy.pause (0.5)
            hide izumi with dissolve
            $ renpy.pause (0.5)

            if persistent.annabadending == True:
                show izumi normal 4 scar with dissolve
            else:
                show izumi normal 4 with dissolve

            $ renpy.pause (0.5) #Also, this is the first time I've genuinely tried to write for Izumi *ever*, so bear with me if it's trash.
            Iz "Tell me, what else can you remember?"
            c "Enough to realise that this entire attempt is extremely unusual. Just where were you on the night of the fireworks?"
            Iz "You’re right in regards to this not being a normal timeline. If my sources prove to be correct, then you’d be in a coma right about now."
            Iz "But as we can obviously see, that is not the case."
            c "Wait, so you know how different this timeline is compared to others?"
            Iz "Yes{w=0.25}, and no. Frankly, I do not have the time nor the desire to explain this all to you."
            $ renpy.pause (0.5)
            Iz "Tell me, do you know what usually happens during the night of the fireworks when you confront Reza?"
            c "I think that I usually talk with Reza for a bit until Maverick shows up. I’m pretty sure you also appear from the shadows as well at some point."
            $ renpy.pause (1.0)
            c "…wait.{w=0.65} Neither of those two things happened this time."
            Iz "Correct. I decided to risk the integrity of this timeline by experimenting with whatever resources I had available. I sent a note to the chief of the police force to go to the underground facility while you were talking with Reza." #But *why* the hell would you do this on your own accord instead of having the MC do that???
            c "Leading to Remy finding Bryce instead of Maverick."
            $ renpy.pause (1.0)
            Iz "I stayed undercover near the portal just in case this plan were to fail. Luckily for us, it hadn’t. Now the comet has been redirected, and everything is good."
            c "Why are you telling me all of this?"
            Iz "You wouldn’t understand even if I spelled it out to you. Just be grateful that we got as favourable a result as we did, because there were a lot of places that it could have failed."
            c "If you say so. What will you be doing now? Surely the main reason for you staying here was to redirect the comet, right?"
            Iz "We shall see where the road takes us. You surely have your duties, and I have mine. Perhaps I’ll experiment with the portal a bit more; perhaps I’ll disappear from the face of the earth."
            $ renpy.pause (1.0)
            m "Izumi gave a slight smirk before looking directly in my eyes, filling my soul with a feeling of light fear."
            $ renpy.pause (0.5)
            Iz "Regardless, I thank you for your service, {i}Ambassador [player_name]{/i}. You’ve done well. Rest easy now. You deserve it."
            $ renpy.pause (1.0)
            c "..."
            $ renpy.pause (0.5)
            c "The same to you."
            Iz "Oh, I will. You have no idea how tired I am."

            $ renpy.pause (0.5)
            if persistent.kol_tld_ending_achieved == True:

                $ renpy.pause (0.5)
                hide izumi with dissolvemed
                $ renpy.pause (1.0)

                m "Izumi started to walk out the door, yet paused as soon as she turned the handle."

                $ renpy.pause (1.5)
                if persistent.annabadending == True:
                    show izumi normal 4 scar with dissolve
                else:
                    show izumi normal 4 with dissolve

                $ renpy.pause (1.0)
                Iz "Before I go, I need to ask you something. In one of your previous attempts, do you remember being stranded in the human world with one of your friends?{w} And, if you do, do you remember managing to convince me to take your place and try again in your stead?"
                c "I…{w=0.45} don’t know. My past attempts are hazy at best."
                Iz "I figured as much. Then, let me simplify it a bit: do you ever remember receiving a note with the letters \"TTT\" written on it? Maybe something related to asking you to send it through the portal, perhaps?" #And so, The Last Dragon's Ending C is revealed!

                if persistent.kol_tld_endingc == True:
                    c "I can't say. Maybe?"

                else:
                    c "No, nothing."

                Iz "Interesting."
                $ renpy.pause (0.5)
                m "Izumi took a notepad out of one of her pockets and wrote something down, then quickly put it back as fast as it had appeared."
                $ renpy.pause (0.5)
                Iz "This will prove to be a great help. Thank you."
                c "Wait, what do you mean?"
                $ renpy.pause (0.75)
                Iz "..."
                Iz "Never mind. Finding the truth will only hurt us in the long run, especially if this proves to be a success." #So, Izumi found a way to communicate with other timelines. Imagine the potential that something like this would have...

                $ renpy.pause (0.5)
                hide izumi with dissolvemed
                $ renpy.pause (1.5)

                m "As Izumi disappeared from my sight, I only stood still in confusion as to what Izumi had said. Something about it seemed too familiar to me, but I just couldn’t put my tongue on it."
                $ renpy.pause (0.5)
                c "(Hmmm…)"
                $ renpy.pause (0.5)
                c "(I wonder if Remy would know anything about this considering that Izumi pointed out that one of my friends is apparently involved. He’s probably the best shot I have.)"
                $ renpy.pause (2.0)
                c "(Eh, I’ll just wait until Remy recovers for now. In the meantime, I should make myself something to eat.)"

                $ persistent.kol_tlh_EndingC_done = "C"
                $ kol_tlh_endingC = True

                jump kol_tlh_credits


                

            else:
                
                $ renpy.pause (0.5)
                hide izumi with dissolvemed
                $ renpy.pause (1.0)

                m "Izumi started to walk out the door, and with a few slow steps, soon vanished into the surrounding shadows, leaving me alone and confused. In the end, I decided to just make myself something to eat while I thought over what Izumi had said."

                $ persistent.kol_tlh_EndingC_done = "C"
                $ kol_tlh_endingC = True

                jump kol_tlh_credits
























        
            

    else:
        if kol_tlh_4B_success == True and kol_tlh_datecounter >= 2:
            #ENDING D HERE

            $ save_name = (_("TLH - Ending D")) #Yes, this is an extremely short and low-effort ending, I know. Laziness strikes again, I'm afraid.

            Lg "I’ll go and see what I can do to fix the generator. Considering we had to leave it in a very critical state, it might take a while. I’ll still need your help like last time, though."
            c "Got it."

            stop music fadeout (1.5)
            $ renpy.pause (1.5)
            scene hallway at Pan((0, 0), (0, 150), 3.75) with dissolvemed
            $ renpy.pause (4.0)
            scene kolmorefacility with dissolve
            $ renpy.pause (1.0)

            m "We both went into the generator room to complete our tasks, with Logan soon getting back to where he originally left the generator. I took the file I had used and helped to guide Logan through the process of making repairs."

            $ renpy.pause (1.0)
            show logan annoyed at Position(xpos = 0.3) with dissolve
            $ renpy.pause (1.0)

            Lg "Damn, this isn’t looking good. The amount of time that had passed since we were last here really did a number on this thing. If I’m not careful, things will turn sour really quickly."
            c "But you’ll manage, right? You always do."
            $ renpy.pause (1.0)
            Lg "..."
            $ renpy.pause (1.0)
            Lg serious "I really hope so."
            $ renpy.pause (0.75)
            Lg annoyed "Now, let’s try to connect this here and rearrange some parts there. This should stabilise a few things. Does the file say anything about this arrangement?"
            c "Let me check…"
            $ renpy.pause (1.0)
            c "It does. Apparently, the wires shouldn’t be outputting to that port, otherwise critical overheating could occur."
            Lg "Alright then, I’ll just arrange and modify some parts instead. It should basically do the same thing." #Well, that's comforting.

            $ renpy.pause (1.0)
            play sound "fx/helmet.ogg" #Sounds are hard.
            $ renpy.pause (1.0)

            Lg "Alright, done. Anything else that I need to know?"
            c "It should be all, unless you somehow forgot about the electrical outputs."
            Lg serious "Of course. Just need to double-check this real quick…"

            $ renpy.pause (2.0)
            play sound "fx/highvoltzap_kol.wav"
            show logan surprised with dissolve
            play soundloop "fx/hiss.ogg" fadein 1.0
            $ renpy.pause (1.0)
            play music "mx/ashes.ogg"
            $ renpy.pause (1.0)

            c "Logan, what’s wrong?"
            show logan serious with dissolve
            Lg "GET THE BACKUP GENERATOR AND FUCKING RUN FOR IT!" with Shake ((0, 0, 0, 0), 2.5, dist=14) #You know things are about to go down when Logan drops the F-bomb.
            Lg "I’ll try my best to hold this generator long enough so you can run before it explodes!"
            $ renpy.pause (1.0)
            Lg "As for me, I’m a goner. If there’s one thing left for me to do, it’s to ensure that dragonkind at least stays safe. If the dragons are gone, then humanity will die as well, especially with that flimsy generator that I made for them." #How interesting of Logan to do this. Such a contrast from his original character...  EDIT FROM FUTURE KOLS: It's called "character development", idiot. You should check that out at some point.
            Lg "Everything is in your hands now, [player_name]. NOW RUN, DAMN YOU!" with hpunch

            $ renpy.pause (0.65)
            play sound "fx/metalbox.ogg"
            scene black
            $ renpy.pause (0.85)

            m "Logan switched all his attention to the now-hissing generator, hastily reconfiguring different parts and connections to give me as much time as possible. Without thinking, I grabbed the backup generator and dashed out of the underground facility, nearly tripping several times as the weight of the generator in my arms caused me to lose balance in the dark."

            $ renpy.pause (4.0)
            stop soundloop fadeout (1.0)
            scene np1n at Pan((100, 0), (100, 0), 6.0) with fade
            $ renpy.pause (1.0)
            play sound "fx/explosion.ogg"
            stop music fadeout (1.5)

            m "I was able to make it out far enough before I could hear the generator explode with a loud boom, sending a large sonic boom throughout the sky and causing me to momentarily lose my hearing." with Shake ((0, 0, 0, 0), 3, dist=30)
            $ renpy.pause (2.0)
            m "As I looked back, some of the surrounding ground had completely sunk into where the underground facility was. It almost looked like a small crater of sorts."
            m "I tried to see if I could go back to get Logan, but the entrance had now been sealed thanks to the rubble blocking it."
            $ renpy.pause (1.0)
            c "(Logan...)"
            $ renpy.pause (4.0)
            play music "mx/desolation_kol.ogg"
            $ renpy.pause (1.5)
            m "I stood in silence, the dust from the now-demolished underground facility blowing around the area. Fortunately, the portal seemed to have remained mostly intact."
            m "As I aimlessly stared at the undamaged portal, the sound of beating wings appeared next to me."
            play sound "fx/landing.ogg"
            $ renpy.pause (3.0)

            if kol_tlh_mavstillofficer == True:
                show maverick angry b dk with easeinright
            
            else:
                show maverick angry dk with easeinright

            $ renpy.pause (1.0)
            Mv "What happened?"
            c "The underground facility exploded."
            Mv "Stop playing games with me, [player_name]. I can see that. I’m asking why it exploded."
            c "Logan wanted to improve one of the generators in the underground facility so that a single generator could be more easily used to redirect the comet."
            Mv "That doesn’t make any sense whatsoever. Why put in the effort and risk of improving a generator when the existing generators will suffice?" #Because he was playing both games, that's why.
            Mv "Damn that excuse of an ambassador. He might have just killed us all." with hpunch
            
            $ renpy.pause (2.0)
            if kol_tlh_mavstillofficer == True:
                Mv normal b dk "Screw it. I’ll have to take your word at face value for now. You’ll still need to be taken to the police station so that I can officially record your statement, though."
            
            else:
                Mv normal dk "Screw it. I’ll have to take your word at face value for now. You’ll still need to be taken to the police station so that someone can officially record your statement, though."

            Mv "I don’t think we’ll be able to launch an investigation soon. Not with the comet on its way and whatnot."
            Mv "I take it that Logan is dead."
            $ renpy.pause (1.5)
            m "I only nodded in response."
            $ renpy.pause (0.5)
            Mv "Damn. I can imagine that this will be hell to explain to the authorities on both sides, then. So much for all the effort of forging the report with Reza."
            Mv "At least you managed to get one of the generators. Maybe we’ll still be able to redirect the comet, even if all our energy reserves are going to be put under severe strain."
            c "I’m sorry for all of this, Maverick. I should have stopped Logan when I could."

            if kol_tlh_mavstillofficer == True:
                Mv angry b dk "Yes, you should have. Hell, neither you nor Logan were even allowed in the underground facility in the first place, but here we are."
                Mv normal b dk "At least you’re safe. I can imagine that if you were the one to die instead, things would’ve been a lot more chaotic for us."

            else:
                Mv angry dk "Yes, you should have. Hell, neither you nor Logan were even allowed in the underground facility in the first place, but here we are."
                Mv normal dk "At least you’re safe. I can imagine that if you were the one to die instead, things would’ve been a lot more chaotic for us."

            $ renpy.pause (1.5)
            c "..."
            Mv "..."
            $ renpy.pause (1.0)
            Mv "Let’s go take your statement now. And bring that generator with you." #Is it me or did I write Maverick a bit too casual for this scene...

            $ renpy.pause (1.0)
            scene black with fade
            $ renpy.pause (1.0)

            if kol_tlh_mavstillofficer == True:
                m "After we arrived at the police station, Maverick interrogated me with hordes of questions relating to what exactly had happened in the underground facility. Hours had passed before the two of us were finished late at night, exhausted."
                
                $ renpy.pause (2.0)
                scene office at Pan ((128, 250), (0, 250), 3.0) with dissolveslow
                $ renpy.pause (1.0)
                show maverick normal b with dissolve
                $ renpy.pause (1.0)

                Mv "That should be it. Thanks for being willing to have your statement taken so late at night, [player_name]."
                c "It’s alright, Maverick. Better to get it all sorted out now while the memory is fresh so that things aren’t too hazy later on."
                Mv "I'm glad you see things like I do."
                Mv "I’m sure that the rest of the force will believe your word at face value considering the trust you’ve built up around here, but it’s still crucial to have your account judged considering your involvement with this."
                c "I understand."
                c "Do you think that the council will still be able to redirect the comet with only one generator?"
                Mv "You’re asking the wrong person here. I can make an educated guess, sure, but it’s probable that I’m wildly incorrect considering my inexperience on the matter."
                $ renpy.pause (0.5)
                Mv "Nevertheless, I do think it’ll be possible, but not without severe repercussions for our power grid."
                Mv "But let’s not discuss this right now. There's no point in instilling fear when none of this is even public knowledge."
                c "Fair enough. Well, if you need nothing else…"
                Mv "Nothing. Enjoy the rest of your night."
                $ renpy.pause (1.0)
                c "…alright then. Same to you, Mav." #...why the hell did I write this? Just a few minutes ago the underground facility exploded and then you're just being casual like nothing even happened! *sigh*
                Mv nice b "Mav, huh? Weird to see you become so casual."
                c "The same could be said to you."
                Mv normal b "True. Well, good night."
                c "Night."

            else:
                m "After we arrived at the police station, Maverick took me to an officer that I don't recognise. She bombarded me with hordes of questions relating to what exactly had happened in the underground facility. Hours had passed before the two of us were finished late at night."

            m "With nothing else to do, I returned back to my apartment, still shocked about what had happened at the underground facility."
            
            $ renpy.pause (1.0)
            scene black with fade
            stop music fadeout (3.0)
            $ renpy.pause (3.0)

            nvl clear
            window show

            n "A few days had passed, yet nothing happened outside of a brief message being sent through the portal thanks to an external generator we had used. I was left wondering about the state of humanity and how the generator that Logan had made for them was holding up. With nobody skilled left back home, I could only guess that they would only be able to last for so long until the generator would fail."
            n "Occasionally I wondered about how the authoroties back home reacted when they heard of Logan's passing. There was barely a moment where my soul hadn't been engulfed by an all-encompassing dread."
            n "Eventually, I received a letter from Emera asking me for an audience. Wondering why Emera would want to see me now instead of at an earlier date, I left my apartment and went to her office."

            window hide
            nvl clear

            $ renpy.pause (1.0)
            scene emeraroom at Pan ((0, 0), (0, 180), 5.0) with dissolveslow
            $ renpy.pause (2.5)
            play music "mx/burial_kol.ogg"
            show emera frown with dissolve
            $ renpy.pause (1.0)

            Em "Good day, Ambassador [player_name]. I hope you’ve been well these last few days?"
            c "I suppose."
            Em "That is good to hear. I received a letter from humanity that might be of interest to you. I’ll wait for you to read it before filling you in on our current plans for the comet."
            m "I went over to Emera’s desk as she handed me a small, crusty letter. I opened the letter and started to read, eager to hear about the news back home."
            
            play sound "fx/envelope.wav"
            $ renpy.pause (2.0)
            m "However, that eagerness slowly turned to dread as I continued to read."
            $ renpy.pause (1.0)

            c "(Unfortunately, due to Logan’s passing, our desire to maintain the trade agreement has dwindled to an all-time low. Despite this horrible, unfortunate accident that Logan had found himself in, we simply cannot continue using power from the prototype generator to maintain the portal’s connection.)"
            c "(With the other generator already being used to keep the hospital afloat, it is crucial that we conserve as much power as we can to try and wait until we find someone qualified enough to help us with all the scrap parts we have in stock. Thus, both the portal generator and the prototype generator will be allocated to the hospital.)"
            c "(Until further notice, you will remain in the dragon’s world until we have the resources to bring you back. We cannot say when this will be. We sincerely apologise for making this decision without consulting you, but we simply have no other choice.)"
            $ renpy.pause (3.5)
            Em normal "Is everything alright? You appear to be fairly bleak." #Yes, I copied my own mod for this part. Creativity is hard when laziness prevails.

            menu:
                "I’m not entirely sure.":
                    $ renpy.pause (0.5)

                    Em frown "Uncertainty is often a blessing in disguise. Uncertainty gives you the freedom to act without knowing whether something will be good or bad. Uncertainty gives you more leniency with your actions as a result."
                    Em "Feeling uncertain, however, is another problem entirely. Many a politician had seen their downfall thanks to feeling uncertain."
                    Em ques "But I digress. I do hope you feel better soon. Perhaps a break from being an ambassador would help."

                "I think so.":
                    $ renpy.pause (0.5)

                    Em frown "\"Thinking\" will get you nowhere. The world of politics has taught me more than enough about that concept. You’re either alright or you’re not."
                    Em ques "And, depending on the answer, you’ll have to take action so that you can be the best you can for not only yourself, but for those around you."

                
                "I received a pretty big shock. How am I supposed to be alright?":
                    $ renpy.pause (0.5)

                    Em frown "Regardless of the shock, it’s crucial to stay calm in a given scenario. Show any sign of distress, and people will pick up on it. If people notice your distress, then they’ll become distressed as well."
                    Em "Trust me when I say that you don’t want an entire population to be distressed."

            $ renpy.pause (1.0)
            Em normal "Now, what exactly does that message of yours say?"
            c "To summarise, humanity has put an end to the trade agreement for the time being while they conserve as much power as they can until they get somebody to use the parts they have. In the meantime, they ended their connection with the portal, leaving me stranded."
            $ renpy.pause (2.0)
            Em mean "..."
            $ renpy.pause (0.5)
            Em frown "This is indeed quite shocking. I will have to inform the rest of the council so that we can figure out what to do."
            Em "For now, we have bigger problems to handle."
            $ renpy.pause (1.0)
            Em "With only a single generator from the underground facility, we will have a very hard time redirecting the comet. I’m not entirely sure our current plan will work, considering we made our plan under the assumption that there would be at least two generators to be used."
            Em "If we use all of our backup reserves, then we might be able to redirect the comet, but just barely. It just hurts me that we don’t have another choice for survival."
            c "Then let’s hope this plan works."
            Em "Indeed. We’ll have to spend today connecting all available energy reserves to the one we made for the comet. Hopefully the extra day wasted won’t be our downfall."
            $ renpy.pause (1.5)
            Em ques "I hate to ask you this, but could you do me a favour, [player_name]?"
            c "Of course, Minister."
            Em normal "I need you to contact Remy and see whether the change of plans is feasible in the first place. Ask him to then submit a report as soon as possible." #Because you clearly aren't capable of doing it yourself...
            c "I will."
            Em "Thank you. You are dismissed."
            c "Good day to you, Minister."

            $ renpy.pause (2.0)

            scene black with fade
            nvl clear
            window show

            n "After my meeting with Emera, I went to Remy to inform him of his new duties. With a distraught face, Remy reluctantly accepted his work. With my help, he managed to send an updated report only a few hours later; enough for the council to make an early decision on an updated approach to the comet."
            n "As tomorrow became today, I was constantly informed about the current status of the comet. After the entire day, I received the news that the comet was able to be redirected, but not without a huge cost. Maverick had been right with his guess in the sense that the entire power grid had been put under a lot of strain, leading to dragonkind having little to no power for a few days. Society plunged into chaos, but was able to eventually recover."
            n "Humanity, however, wasn’t so lucky. Shortly after the comet had been redirected, I received news that my city had completely collapsed, leaving me truly trapped in the dragon’s world. The last scraps of power had been used to inform me of the chaos that now filled the city and its populace."

            window hide
            nvl clear
            window show

            n "Heartbroken by my failure to save humanity, my thoughts turned to the portal. I remembered that I would be able to use the backup coordinates to return to the day of my arrival, effectively giving me another shot to save both humanity and dragonkind. Luckily, the portal seemed to have a backup source of power—just enough for a single use."
            n "However, before activating the portal and saying goodbye to this world, I decided to visit Remy one last time."

            stop music fadeout (3.0)
            window hide
            nvl clear

            $ renpy.pause (1.5)
            scene remyapt at Pan ((0, 80), (0,80), 5.0) with dissolveslow
            $ renpy.pause (3.3)
            show remy look with dissolve
            play music "mx/decay_kol.ogg"
            

            c "Hello, Remy." #This scene. This *bloody* scene. It took me days to write this part and it isn't even good. And trust me, if you think this is bad, the original is *far* worse.
            Ry "Hey, [player_name]. Have you been keeping yourself safe with everything out there?"
            c "I managed, yeah. Luckily I had enough things stocked up so that I didn't have to go out much. I'm just glad that all the chaos finally seems to be over."
            Ry shy "I feel the same way. Despite that, I'm just relieved that the worst is now done, especially considering what the alternative was."
            c "Of course."
            Ry look "At least the comet had been redirected, even if a majority of my original work had been vetoed."
            c "Nothing went to waste, Remy. There's a reason why we finished the updated report so quickly."
            Ry "I know. Still, it feels like a slap to the face, even if external circumstances led to me needing to update the report."
            c "Yeah, I guess so."
            $ renpy.pause (1.5)
            c "Remy, I... {w=0.5}need to tell you something."
            Ry shy "What's wrong?"
            $ renpy.pause (1.0)
            Ry look "Wait. Did you receive some news about humanity?"
            Ry shy "Is everything alright back at home?"
            stop music fadeout (3.0)
            $ renpy.pause (1.5)
            c "From what I've heard, it's complete anarchy back home. The little bit of power that was left had been used to inform me of the chaos on the other side."
            $ renpy.pause (1.0)
            c "{cps=17}Humanity is gone.{/cps}"

            $ renpy.pause (1.5)
            play music "mx/left_behind_2_kol.ogg"
            show remy sad with dissolve
            $ renpy.pause (1.0)

            Ry "I...{w=0.4} didn't think this would happen so soon. It really is horrible what happened, [player_name]. I can’t imagine how it must feel to lose everything you knew just like that." #*cough* Amelia was kind of your everything, Remy. *cough*
            Ry "I can only wish you the best of luck in recovering from that experience."
            c "Thanks, Remy. Honestly, I don’t think I’ll ever fully accept it, but I'll try my best for that to not weigh me down."
            Ry shy "I’m aware of the feeling. Sometimes, however, you just kind of learn how to live with the feeling of loss. It’ll forever be a part of you, sure, but with enough effort and time, you can grow around that pain."
            Ry normal "That’s what I learned from all the times we talked with each other."
            c "Interesting to see how the tables have turned."
            Ry shy "Y-Yes, it is."
            $ renpy.pause (0.5)
            Ry look "So, what now?"
            c "I'm trying again."
            $ renpy.pause (1.0)
            Ry "Excuse me?"
            c "Long story short, the portal is actually a time machine. Humanity and dragonkind live on the same planet, but seperated by many, {i}many{/i} years."
            c "I want to go back to the day of my arrival and try again. Hopefully I can save humanity as well."

            $ renpy.pause (2.0)
            show remy shy with dissolvemed
            $ renpy.pause (1.0)

            Ry "T-This is a lot to take in. All our myths about humans, the way out society had been structured, our history..."
            c "I'm sorry for that, Remy."
            Ry "No, don't be. I understand more than you think, [player_name]. I just need the time to fully grasp the concept, that's all."
            $ renpy.pause (0.5)
            Ry normal "How will you power the portal with no generators?"
            c "There's a small battery of some sorts somewhere. It should be enough for one use."
            $ renpy.pause (1.0)
            Ry look "So this is it? I won't see you again?"
            c "Another version of you will, but not the Remy I'm speaking with right now."
            $ renpy.pause (1.0)
            Ry "I see..."
            $ renpy.pause (0.5)
            Ry shy "It’s fascinating to know what the portal actually does, but I'll admit that it’s so confusing to think about all the possibilities with time travel actually being real." #Yes, this is the part where the new script got sewn together with the old one. That's why there's such a jarring split here.
            Ry "I find it so interesting to see that my original theory of black holes wasn't entirely far off, but then again, it was just a theory made in a time of ignorance."
            $ renpy.pause (0.5)
            Ry sad "Not that we’ll ever find out the full truth after you’re gone, that is."
            c "Well, you could always connect a generator back to the portal once the energy reserves have been fully restored."
            Ry look "There just wouldn’t be a reason for it. At least, not with humanity having severed their connection. Besides, I’m guessing that not even our top scientists will be able to figure out how to get the portal working again, let alone figure out how to reach you."
            c "Well, never say never. For all we know, a human might just pop out from nowhere and fix the portal."
            Ry "Maybe, but you said it yourself: humanity is gone."
            Ry normal "Ah well, I guess we can hope."
            $ renpy.pause (1.0)
            c "Will you be able to manage on your own without me?"
            Ry shy "I should. Remember, I have Adine at my side now. This is far more than what I used to have before I met you. Sure, I’ll be devastated with you gone, but I’m certain that Adine will be able to help me cope with your loss."
            Ry normal "Not only that, but Amely as well. She’ll definitely keep things interesting."
            Ry sad "Though, nothing will be able to compare to you."
            Ry shy "Not because you’re a human, mind you. It’s because of how you treated me and how you helped me recover to the point where I am today."
            Ry normal "Remember that whenever you’re going through a hard time, [player_name]. You were able to change not just my life for the better, but helped save countless lives as well."
            c "You have no idea how much that means to me, Remy."
            Ry shy "No, I don’t. Despite that, I still mean everything that I said."

            $ renpy.pause (0.5)
            hide remy with dissolve
            $ renpy.pause (0.5)
            m "Remy looked at me longingly, as if he wanted to say goodbye but lacked the courage to do so."
            $ renpy.pause (0.5)
            show remy shy with dissolvemed
            $ renpy.pause (0.75)
            Ry "I’ll miss you, [player_name]."
            c "I'll miss you too, Remy."

            $ renpy.pause (0.5)
            hide remy with dissolve
            $ renpy.pause (0.5)
            m "Remy moved closer to me and embraced me with one of his wings, enveloping me in a soft, warm hug. We stood like this for a few moments before Remy parted from me." #Another hug?! Whyyyyyy?!
            $ renpy.pause (1.5)
            scene black with fade
            $ renpy.pause (0.5)
            m "Once my final visit came to an end, I reluctantly made my way to the portal, somberly thinking about how I owe a better future to those I had lost back home."
            $ renpy.pause (1.5)
            m "I booted the portal up so that I could fulfil my original promise to help humanity, keeping Logan’s last wish in mind to do what I could to guarantee everybody's safety."

            $ persistent.kol_tlh_EndingD_done = "D"
            $ kol_tlh_endingD = True

            jump kol_tlh_credits

            

            














        else:
            #ENDING E HERE   

            $ save_name = (_("TLH - Ending E")) #Yep, it's time for E. Sure, it ain't nearly as depressing as TLD's ending E, but this time it hurts in a different way! Best of luck, folks!

            $ renpy.pause (2.0)
            Lg "*sigh*"
            Lg "Let’s see what we can do with the generator. Considering the state of the damn thing, this might take quite a long time."
            c "Well, the sooner we get started, the better."
            Lg "I guess so. We only have so much time, after all."

            stop music fadeout (1.5)
            $ renpy.pause (1.5)
            scene hallway at Pan((0, 0), (0, 150), 3.75) with dissolvemed
            $ renpy.pause (4.0)
            scene kolmorefacility with dissolve
            $ renpy.pause (1.0)

            m "The two of us entered the room housing the unfinished generator once more. Logan immediately got his tools out, while I took the file and opened it to where I left off. After some basic preparations, we got to work."
            $ renpy.pause (1.0)
            m "However, Logan seemed to be struggling somewhat, even with the help I gave him. Time after time, he would lightly swear under his breath while seemingly fighting against some of the parts."
            
            $ renpy.pause (1.0)
            show logan annoyed at Position(xpos = 0.3) with dissolve
            $ renpy.pause (1.0)

            Lg "Bloody hell, this thing just doesn’t want to cooperate. It’s as if some parts grew a brain just to spite me for not being finished with them the other day."
            Lg serious "[player_name], see if you can find anything about a \"T36-xH regulator\" in that file." #I totally didn't make that up in the moment of writing. Nope, totally not...
            c "On it."

            play sound "fx/pages.ogg"
            $ renpy.pause (1.5)
            c "Here we go."
            Lg annoyed "Good. Give the page to me."
            $ renpy.pause (1.5)
            Lg "Damn it, looks like I’ve gotten the connections wrong. Guess that’s why the wires won’t connect."
            c "I’m assuming that the regulator or whatever is interfering with the electrical outputs then?"
            Lg "Among other things."
            Lg serious "I should be able to bypass that pesky connection if I just…{w=1.85}{nw}"

            $ renpy.pause (0.5)
            play sound "fx/highvoltzap_kol.wav"
            show logan surprised with dissolve
            play soundloop "fx/hiss.ogg" fadein 1.0
            $ renpy.pause (1.0)
            play music "mx/ashes_kol.ogg"
            $ renpy.pause (1.0)

            Lg "...shit." #And now the S-bomb?! Damn, what's next, Logan calling Emera a bitch?   EDIT FROM FUTURE KOLS: Actually, why didn't you do that? That would've been amazing!
            c "Logan?!"
            show logan serious with dissolve
            Lg "Run! NOW!" with Shake ((0, 0, 0, 0), 1.0, dist=14) 

            $ renpy.pause (0.5)
            hide logan with dissolvequick
            $ renpy.pause (0.5)
            scene hallway at Pan((0, 150), (0, 150), 3.75) with dissolvemed
            $ renpy.pause (0.5)

            m "Me and Logan both ran away from the generator as fast as we could. I nearly tripped over my own feet several times, but somehow Logan always managed to push me back up as soon as I stumbled."

            stop soundloop fadeout (1.0)
            scene np1n at Pan((100, 0), (100, 0), 6.0) with dissolve
            $ renpy.pause (1.0)
            play sound "fx/explosion.ogg"
            stop music fadeout (1.5)

            m "A massive explosion erupted from the underground facility just as we were about to make out, sending a shockwave that launched me outwards." with Shake ((0, 0, 0, 0), 4, dist=27)
            m "As I landed on the ground, I could feel my consciousness starting to drift away as a loud ringing overcame my ears."

            $ renpy.pause (0.5)
            scene black with dissolvemed
            $ renpy.pause (6.5)
            Lg annoyed "[player_name], wake up…"
            $ renpy.pause (1.5)
            Lg serious "Damn it, wake up already! I don’t have the strength to carry you back, so you better regain your senses!"
            $ renpy.pause (1.5)
            Lg "Screw it..."
            $ renpy.pause (1.0)
            play sound "fx/hit2.ogg"
            $ renpy.pause (1.0)
            scene np1n at Pan((100, 300), (100, 300), 6.0)
            show logan serious dk
            with dissolveslow
            $ renpy.pause (2.0)

            Lg "Ah, looks like that worked. Let me help you up."

            $ renpy.pause (0.5)
            hide logan with dissolve
            $ renpy.pause (1.0)
            scene np1n at Pan((100, 0), (100, 0), 6.0) with ease
            $ renpy.pause (1.0)
            show logan serious dk with dissolve
            $ renpy.pause (0.5)

            Lg "There we go."
            Lg annoyed dk "[player_name], I hate to tell you this, but we messed up. Big time."
            play music "mx/rezatheme.ogg" #Wowie, another unused track! :O
            c "...huh?"
            Lg serious dk "The generators. They exploded. {w}And it's my fault."
            $ renpy.pause (1.0)

            menu:
                "No, it’s our fault.":
                    $ renpy.pause (0.5)

                    Lg "You weren’t the one to screw the upgrade up. All you did was provide me the information I needed while working."
                    Lg "You’re innocent in all of this."

                "Yeah, it totally is.":
                    $ renpy.pause (0.5)

                    Lg "Now, millions—if not more—will die because of me. I don’t see how the dragons are going to be able to redirect the comet now."
                    $ renpy.pause (1.0)
                    Lg "..."
                    $ renpy.pause (1.0)
                    Lg "Isn’t it great how the universe just loves to show me the middle finger at the worst of times?"

                "We couldn’t have expected this, Logan. You shouldn’t blame yourself.":
                    $ renpy.pause (0.5)

                    Lg "That’s the neat part, [player_name]. I could have."
                    Lg "If we never left the generator in the first place, the risk of it exploding would have been drastically lower. It’s due to my negligence and the fact that I didn’t work fast enough the other day that it exploded now."
            
            $ renpy.pause (1.0)
            Lg "As if things weren’t bad enough with us losing the generator that we were working with, we lost the backup one as well. Our shining hope, gone in an instant."
            c "But we still have the generator you made back home, no? We could hold out for now."
            Lg "It’s only a matter of time before that generator fails. Quite frankly, the scraps that we have would only give us so much time."
            Lg "The city is on life support, [player_name]. We’ve failed."
            $ renpy.pause (2.0)
            m "I let the realisation sink in as the dust settled around me. With dragonkind having lost their main weapon against the comet, it’s unlikely they will be able to redirect it in time."
            m "And with the dragons gone, it’s only a matter of time before the city falls as well. Not that we could do much anyway, now that the generators that powered the portal are gone as well."
            m "As I stood in silence with my legs injured, I could hear another set of footsteps approaching us."

            $ renpy.pause (1.0)
            show logan serious dk at Position(xpos = 0.3) with ease
            show logan serious dk flip with dissolve
            $ renpy.pause (1.0)
            show bryce stern b dk at Position (xpos = 0.75) with easeinright
            $ renpy.pause (1.0)

            Br "[player_name]! Logan! You two alright?"
            c "I think so. My legs are pretty beaten up, but I’ll live."
            Br "Do you think you can walk?"
            c "I should be able to."
            Br "Good. Logan?"
            Lg "Yeah, I’m good. Just my torso hurting like hell, that’s all."
            Br brow b dk "That wound on the back of your head begs to differ."
            Lg annoyed dk flip "Trust me; I’m fine. I’ve gone through worse."
            $ renpy.pause (1.0)
            Br stern b dk "Just what happened in the underground facility?"
            $ renpy.pause (2.0)
            stop music fadeout (2.0)
            Br "...wait."
            $ renpy.pause (1.0)
            Br sad b dk "No..." #Bryce really doesn't deserve this treatment...
            Lg "..."
            c "..."
            play music "mx/drowning_kol.ogg"
            $ renpy.pause (0.75)
            Br "You mean…"
            Lg "Yeah. Sorry, Bryce."

            $ renpy.pause (1.0)
            m "Bryce only stared at the ground, not even wanting to look anyone in the eyes. His expression was hollow, as if all sense of hope had died within him."
            $ renpy.pause (1.0)
            Br "There isn’t even a point in arresting you for trespassing. What good would it even do?" #He's gone completely hollow... :(
            $ renpy.pause (2.0)
            Br "..."
            $ renpy.pause (1.0)
            Br stern b dk "Follow me to the office, please. I…{w=0.75} need to take your statements."

            $ renpy.pause (1.0)
            scene black with fade
            $ renpy.pause (2.0)
            nvl clear
            window show

            n "With the three of us at the police station, Bryce took our statements of what happened at the underground facility. Despite our trespassing, Bryce was simply in too bad of a mood to give us a punishment. Instead, he told me and Logan to go to Emera first thing in the morning and try to come up with something new to redirect the comet."
            n "In the meantime, Bryce told us that we should contact either Sebastian or Maverick if we needed any help and that he will be \"off-duty\" for the time being. I could only imagine what Bryce meant by that statement." #Probably drinking himself to death... in a maybe literal sense. Maybe. (Nah, that would've been too depressing and there's no way I'm fitting an entire arc like that in a single ending)
            n "Me and Logan eventually went back to our apartments, too shaken up to discuss what had happened with each other."

            window hide
            nvl clear
            window show

            n "Night eventually turned to day, and I woke up with a feeling of dread as I knew that I had to explain everything to Emera. I tried to delay as much as I could, but in the end, I had to make my way to Emera’s office. When I arrived, I already saw that Logan had been talking with the minister, albeit in an anxious tone."
            
            stop music fadeout (2.0)
            window hide
            nvl clear

            $ renpy.pause (1.0)
            scene emeraroom at Pan ((0, 0), (0, 180), 5.0) with dissolveslow
            $ renpy.pause (2.5)
            show emera frown at Position(xpos = 0.8)
            show logan serious flip at Position(xpos = 0.3)
            with dissolve
            $ renpy.pause (1.0)

            Em "Hello, Ambassador. Please, take a seat. Your associate already explained everything."
            
            $ renpy.pause (1.0)
            play music "mx/advance_kol.ogg"
            $ renpy.pause (1.0)
            Em "Answer me this: why? Why did you think that it was a good idea to risk everything that we had worked for?" #Oh, you can *hear* the seething rage she's trying to hide.

            menu:
                "I simply wanted to ensure the survival of dragonkind.":
                    $ renpy.pause (0.5)

                    Em mean "And that went well, now didn’t it?"
                    Em "By wanting to ensure our survival, you have inexplicably caused our doom instead."

                
                "I wanted the possibility of humanity surviving as well.":
                    $ renpy.pause (0.5)

                    Em mean "So, you’re telling me that you threw the council’s plan away in the volitle hope of alleviating humanity’s struggles?"
                    Em "I’m afraid you’re not better than Reza if that’s the case." #Yep, she just said that. I'm not even kidding.

                "I’m not sure.":
                    $ renpy.pause (0.5)

                    Em mean "You don’t know why you caused so much pain and despair for our kind in the coming days?"
                    Em "Your attempts to play the innocent victim will cause you to carry the weight of millions on your shoulders, [player_name]."


            $ renpy.pause (2.0)
            Em frown "I don’t have time to argue with you about this."
            
            $ renpy.pause (0.5)
            hide emera with dissolve
            $ renpy.pause (0.5)
            m "Emera turned around and went toward her phone. After pressing a few buttons, she picked her phone up and put it on speaker."
            $ renpy.pause (0.5)
            show emera frown at Position(xpos = 0.8) with dissolve
            show logan annoyed flip with dissolve
            $ renpy.pause (1.5)

            Em "Good morning, Remy. You’re on speaker."
            Em "I want you to see whether it’ll be possible to divert the comet without the aid of the underground generators."
            Ry look "Wait, what? Why?"
            Em "It’s a story that we should discuss in private. I’d advise you to come to my office as soon as possible."
            Ry "I see..."
            $ renpy.pause (1.5)
            Ry sad "Unfortunately, I can’t."
            Em mean "Excuse me? What do you mean you can’t?"
            Ry look "I’m not exactly at work. You are calling my private number, after all. To summarise, I’m sick. {i}Very{/i} sick. Both physically…"
            $ renpy.pause (1.0)
            Ry sad "…and mentally."
            Em frown "Remy, you listen to me right now. I don’t care if you’re sick or not. You {i}need{/i} to research the possibility of redirecting the comet without the underground generators. If you don’t, then you will cause the death of us all." #Oooo, guilt-tripping. That'll go lovely with Remy's mental state.
            $ renpy.pause (2.0)
            Ry "..."
            Ry "What happened?"
            Em "Ask [player_name] and Logan. They’re right here with me."

            stop music fadeout (3.0)
            $ renpy.pause (2.0)
            m "The phone went silent for a few moments, as if Remy was hesitating on saying something. Eventually, with what sounded like scorn in his voice, he spoke."
            $ renpy.pause (1.0)
            play music "mx/gravity.ogg"

            Ry "[player_name]..." #...what on earth made me decide to write this part the way I did? Never did Remy as a character show any signs of being this hateful and petty, so why now?
            c "Yes, Remy?"
            $ renpy.pause (1.5)
            Ry angry "Not only did you hurt me when I needed you the most, but you also caused all of this? I thought that, after so long, I had a future. I finally had something—no, {i}someone{/i}—to keep me going."
            Ry cry "But that was just another lie, wasn't it? Was everything that you told me a lie? Was everything simply things that you did and said out of pity?"

            if kol_tlh_4B_played == False:
                Ry "Yes, I know I called you in the middle of the night, and that on its own is excusable."
                Ry "But everything else? Why did you avoid me every time I wanted to spend time with you? {i}Why?{/i}"


            Em "Keep your personal life out of this, Remy. This is too dire a situation to get angry now."
            $ renpy.pause (2.5)
            Ry look "Fine, but let me say this right now, then: we’ll be lucky if we can even delay the comet with what resources we have. Without those generators, we don’t have any hope. Unless we suddenly find some huge supply of energy to use, there’s little chance that we can make it."
            $ renpy.pause (1.0)
            Ry "..."
            Ry "As for you, [player_name], we’ll meet soon. One last time."

            stop music fadeout (2.0)
            $ renpy.pause (2.5)
            show logan serious flip with dissolve
            $ renpy.pause (1.0)
            m "Remy hung up soon after he finished speaking, leaving an ominous silence to fill the office. Logan only looked at me with a mixed expression of raw confusion and concern."
            $ renpy.pause (1.0)

            Lg annoyed flip "What was that all about?"
            Em "No matter. Personal lives are of no importance right now. We need to focus on the upcoming comet."
            Lg "And what about it? You heard it yourself, Minister: there’s not much we can do."
            Em mean "I refuse to stand idly by and wait for a comet to wipe us all out. My people are in danger, ambassador, and if you won’t help, then it’s best that you leave."
            $ renpy.pause (2.0)
            Lg "..."
            $ renpy.pause (1.0)
            Lg serious flip "Alright, what {i}can{/i} we do?"
            play music "mx/judgement.ogg" fadein (3.0)
            Em frown "I suspect that we need to cut into our emergency supplies as well as whatever reserves we have left. Since we ordered the use of all the generators to be connected to our power grid, we might be able to pull something off."
            c "I’m not entirely sure. Remy’s word about us not being able to do much seems trustworthy."
            Em "You heard that he isn’t himself, [player_name]. His emotional state might cause him to not think rationally, causing him to choose the most pessimistic outcome."
            Em ques "Regardless of what he says, the council will try its best to redirect the comet in the few days that we have left."
            Lg "I have an idea, though I’ll need your permission for it, Minister."
            Em normal "Speak."
            Lg "I ask for permission to work on constructing more generators with the parts that are available. I’m far more capable of working on the finer, more intricate parts than most dragons, and at a far quicker pace as well."
            $ renpy.pause (1.0)
            Em frown "As much as I dread letting you anywhere near another generator, we have no other choice. We need all the help we can get."
            $ renpy.pause (1.0)
            Em normal "You have permission, Logan."
            Lg "Thank you, Minister. I will start immediately."

            $ renpy.pause (0.5)
            show logan serious with dissolve
            hide logan with easeoutleft
            $ renpy.pause (1.0)
            show emera at center with ease
            $ renpy.pause (1.5)

            Em frown "As for you, [player_name], I’ll assign you the task of research. A copy of Remy’s research should still remain on his computer back in his office at the library. See if you can find anything that might help us now."
            Em "I’ll also call for a few of our staff to go through the library alongside your review for anything that Remy might have missed."
            Em "Make haste, [player_name]. Time is of the essence."
            c "I’ll try my best, Minister."
            Em "You are dismissed."

            $ renpy.pause (1.0)
            scene black with fade
            stop music fadeout (3.0)
            $ renpy.pause (3.0)

            nvl clear
            window show
            play music "mx/shield_kol.ogg" fadein (1.0)

            n "With my work having been assigned to me, I immediately went to work in an attempt to right my wrong. Every spare moment of time I had was spent researching energy efficient ways of redirecting the comet. Several dragons came to me, giving me extracts from books detailing several possibilities; however, each of them was already documented as implausible by Remy."
            n "It didn’t take long for me to become exhausted from all the research I put in, making me wonder how Remy was even able to do all of this on his own in the first place. Eventually, I had to call it a day and give up. I slept on Remy’s bed in his office, knowing that it would save time for me tomorrow."

            window hide
            nvl clear
            window show

            n "I repeated this process for the next few days, but nothing noteworthy came up in my research. It seemed like Remy had taken notes on every single detail. The more I went on, the more I started to lose hope in ever finding something noteworthy. I could only wish that Logan had more luck in his endeavours."

            window hide
            nvl clear
            $ renpy.pause (2.0)
            window show

            n "On the day that the dragons were supposed to redirect the comet, all available resources were used, but to no avail. Despite the new generators that Logan managed to make and despite all my research, everything was for nothing. Like Remy had said, the comet was only slowed down."
            n "Dragonkind had used all the power they had, but nothing helped. Eventually, they ran out, causing widespread blackouts. Nothing could be done."
            n "Yet, I had a small hope left as I realised that the portal was never damaged in the explosion. It was possible for me to go back to the day of my arrival and try again—to succeed where I had failed. I checked on the portal and saw that, miraculously, it had a small battery that gave the portal enough charge to be used once."
            n "However, before I activated it, I waited. I wanted to see whether anything could be done for this world."

            window hide
            nvl clear
            stop music fadeout (7.0)
            window show

            n "As the comet came closer and closer, the night sky lit up considerably. I estimated that the comet would hit in a few hours at the earliest and tomorrow afternoon at the latest. Not wanting to leave this world without a trace, I called everyone I had met to meet me at my apartment for one final goodbye."

            window hide
            nvl clear

            $ renpy.pause (1.0)
            scene o3 at Pan((0, 250), (0, 250), 5.0)
            show bryce stern at Position(xpos = 0.8)
            show maverick angry at Position(xpos = 0.96)
            show adine disappoint b flip at Position(xpos = 0.2)
            show remy look flip at Position(xpos = 0.04)
            with dissolveslow
            $ renpy.pause (3.0)
            play music "mx/marching_kol.ogg"

            Mv angry "You’re a coward, you know that? At least face your failure with dignity instead of running away." #And now Maverick feels betrayed. That's a nice way to end his whole character development arc, eh?
            c "Maverick, please. I know this is hard, but I need to try again. I hope that, in another timeline, I’ll be able to save you all."
            Br brow "I still can’t wrap my head around this time-travel stuff. It just seems so unreal, as if everything is from a bad sci-fi book or something."
            Ad sad b flip "At least there will be hope for us in another time."
            Ad disappoint b flip "I know I’ll see you again, but it just doesn’t feel right. You’ll meet me again, but I won’t remember anything about it. It's as if you'll see another person like me in another time, complete with my memories and personality."
            Ad sad b flip "It feels so…{w=0.5} fake."
            Ry "I understand, Adine. I understand."
            $ renpy.pause (0.5)
            Ry sad flip "All of this hurts so much. We went through so much together, and then you’ll leave us all to die? Sure, we didn’t have the best exchange over the phone the other day, but still…"
            $ renpy.pause (2.0)
            Ry "..."
            $ renpy.pause (1.0)
            Ry "I’m sorry I acted the way I did, [player_name]. I wasn’t myself."
            c "Don’t worry, Remy. It will all be alright."
            Mv "No, it won’t. Stop tossing euphemisms around. Everybody knows that nothing will be alright."
            Mv "Except for you, the cowardly ambassador running off into the past to try again. Will you succeed? Will you fail again and cause even more pain and suffering?" #If only he knew about the past attempts...
            Br stern "Maverick, stop. You’re not helping."
            Mv "I’m leaving. I’ve had enough talking to a traitor." #Would "betrayer" be a better word instead of traitor? Eh, I'll leave it as is.

            $ renpy.pause (0.5)
            show maverick angry flip with dissolve
            $ renpy.pause (0.5)
            hide maverick with easeoutright
            $ renpy.pause (1.5)
            Br "I should follow him. I don’t want Maverick to cause any more trouble."

            $ renpy.pause (0.5)
            show bryce sad with dissolvemed
            $ renpy.pause (1.0)
            Br "I-It was nice seeing you for one last time, [player_name]. I wish you the best of luck in your next attempt."
            $ renpy.pause (0.5)
            show bryce sad flip with dissolve
            $ renpy.pause (0.5)
            hide bryce with easeoutright
            $ renpy.pause (0.5)
            show remy at Position(xpos = 0.8) with ease
            show remy sad with dissolve
            $ renpy.pause (3.5)

            Ad "This isn’t your first attempt, is it? Just how many times have you gone through all of this, [player_name]?"
            c "I’m not sure. I can’t remember."
            $ renpy.pause (1.0)
            Ad "..."
            $ renpy.pause (0.5)
            show remy lookcry with dissolvemed
            $ renpy.pause (0.5)

            Ry "And how many times have we died in the past? How many times did {i}everyone{/i} die?"
            $ renpy.pause (2.0)
            c "..."
            Ry cry "..."
            Ry "I-I see." #A most terrible realisation.
            $ renpy.pause (1.0)
            Ad disappoint b flip "I can’t help but think of Amely right now. She never had a true home. She will never grow up. She will never know what life is like outside of the orphanage."
            $ renpy.pause (1.0)
            Ad sad b flip "..."
            $ renpy.pause (1.0)
            Ad frustrated b flip "If there’s one last thing I’ll do before the comet hits, it’ll be to spend some time with Amely. There’s no way I’m letting her die alone and afraid." #Why *that* sprite? Hmmm...
            Ry shycry "That’s really kind of you to help her like that, Adine."
            Ad disappoint b flip "But first..."

            $ renpy.pause (1.0)
            hide remy
            hide adine
            with dissolvemed
            $ renpy.pause (1.0)

            m "Adine stretched her wings and wrapped them around Remy, holding him tightly as he silently wept."
            $ renpy.pause (1.0)
            Ad disappoint b flip "I’m so glad that we were able to get together after so many years, Remy. I never said this, but I missed you. With you, I can see a part of Amelia still thriving, being as happy as ever."
            Ry shycry "I..."
            Ad "Shush, Remy. Don’t speak now. I don’t want to remember this moment as one of words."
            $ renpy.pause (1.0)
            m "Adine continued to hold Remy for a few more moments, softly humming as tears fell from Remy’s face. In time, they parted, but not before Adine gave Remy a light kiss on his cheek." #I'd ship that.

            $ renpy.pause (1.0)
            show adine disappoint b flip at Position(xpos = 0.2)
            show remy shycry at Position(xpos = 0.8)
            with dissolvemed
            $ renpy.pause (1.0)

            Ad sad b flip "Goodbye, Remy. I’ll miss you."
            $ renpy.pause (1.0)
            Ad disappoint b flip "..."
            Ad "And you too, [player_name]. Good luck." #You can see that Adine cares far more about Remy now instead of the MC.

            $ renpy.pause (1.0)
            hide adine with easeoutright
            $ renpy.pause (3.0)

            Ry "..."
            c "..."
            $ renpy.pause (0.5)
            Ry "Let’s take a walk to the portal."
            c "Alright."

            $ renpy.pause (0.5)
            hide remy with dissolve
            stop music fadeout (5.0)
            $ renpy.pause (2.0)
            scene np5 dk with dissolve
            play sound "fx/steps/rough_gravel.wav"
            $ renpy.pause (2.5)
            scene np4 with dissolve
            $ renpy.pause (2.0)
            scene np3 with dissolve
            $ renpy.pause (1.0)
            m "We left my apartment and slowly wandered the now abandoned streets to the portal. Even in the middle of the night, it was extraordinarily bright, making it very easy to see where we were going."
            $ renpy.pause (2.0)
            show np2 dk with dissolve
            $ renpy.pause (2.0)
            m "After having walked in silence, Remy spoke up."

            $ renpy.pause (2.0)
            show remy lookcry with dissolvemed
            $ renpy.pause (0.5)
            play music "mx/ruin_kol.ogg"
            $ renpy.pause (2.0)

            Ry "I really am sorry for how I acted, you know."
            c "Don’t be. You had every right to respond the way you did."
            Ry cry "It still doesn’t excuse my behaviour with Emera on the phone. I have to wonder whether if I had listened to Emera instead of letting my emotions get the better of me, we’d be in a different situation."
            $ renpy.pause (1.0)
            Ry "..."
            Ry "This is all my fault, isn’t it?" #Like many a depressed individual, he takes all the blame on himself and twists the narrative to justify his lie. Poor guy.
            c "No. You weren’t the one to cause the generators to explode."
            Ry shycry "But I was the one who refused to come up with a possible solution in response."
            c "You said it yourself, Remy: there wasn’t much that we could do."
            Ry lookcry "Maybe if I wasn’t such a sourpuss, there could’ve been something done."
            $ renpy.pause (1.0)
            Ry cry "But it’s too late now."

            $ renpy.pause (1.0)
            hide remy with dissolve
            $ renpy.pause (0.5)
            scene np1n flip at Pan((100, 0), (500, 150), 6.0) with dissolveslow
            $ renpy.pause (5.5)

            m "We walked for a little while further until we reached the portal, standing ever defiant to the world and its problems."
            $ renpy.pause (1.0)
            m "Yet, as we went closer, we saw another face standing there, waiting."

            $ renpy.pause (1.0)
            show remy cry flip at Position(xpos = 0.2) with dissolve
            $ renpy.pause (0.5)
            show logan serious at right with dissolve
            $ renpy.pause (0.75)

            Lg "Hey. Figured you’d want to try the portal out."
            Ry shycry flip "So, this is the Logan I’ve been hearing so much about. It’s nice to meet you."
            Lg "The feeling is mutual, even if our circumstances aren’t the most ideal."
            Lg annoyed "Especially judging from the fact that you’re crying, Remy."
            $ renpy.pause (0.5)
            Ry lookcry flip "This is embarrassing."
            Lg "Don’t worry about it. From everything that’s going on, it’s hard to not cry."
            $ renpy.pause (1.0)
            Lg serious "So, I’m guessing you’ll want to go on another attempt, [player_name]?"
            c "Yeah."
            Lg "As I expected."
            Lg annoyed "Well, the portal has enough power to send you through to the past. I could use it to go back home, but it’s pointless. Humanity is doomed, and we both know it."
            Lg serious "It’s better to give you another shot instead."
            Ry shycry flip "You know about the portal’s ability to time travel, Logan?"
            Lg "I do. It’s a long story as to how I know."
            Lg "I shouldn’t dawdle, though. The longer we wait, the less time that [player_name] has to escape."
            $ renpy.pause (1.5)
            Lg "..."
            $ renpy.pause (1.0)
            Lg "Take this."

            $ renpy.pause (0.5)
            hide logan with dissolve
            $ renpy.pause (0.5)

            if persistent.kol_tlh_EndingE_done == "E":
                $ renpy.pause (1.0)
                show logan serious at right with dissolvemed
                $ renpy.pause (1.5)

                m "Logan slowly moved over to me and whispered in my ear in such a way that it sent chills down my spine."
                $ renpy.pause (1.5)
                Lg "{size=30}{cps=22}I've changed my mind. You will get nothing from me.{/cps}{/size}" #OH SHIT HE KNOWS!!!
                $ renpy.pause (0.75)
                m "Logan looked over to my pocket and saw something dangling out of it, quickly pulling it out to hold a watch identical to his own."
                $ renpy.pause (1.5)
                Lg annoyed "{size=30}{cps=22}There's only one way you could have gotten {i}this{/i}...{/cps}{/size}"
                $ renpy.pause (2.5)
                Lg "{size=30}{cps=28}I am beyond disappointed in you, [player_name]. I thought that you would learn from your previous attempt, but apparently not.{/cps}{/size}"
                
                $ renpy.pause (1.5)
                show logan serious flip with dissolve
                $ renpy.pause (0.5)
                hide logan with easeoutright
                $ renpy.pause (0.5)

                m "Logan dropped the duplicate watch on the ground and walked away with disdain on his face."
                $ renpy.pause (0.5)
                m "Ashamed, I picked it up and put it back in my pocket." #Turns out the MC did fail again and Logan noticed. What a 4th wall break.
                $ renpy.pause (1.0)



            else:
                m "Logan removed his watch and gave it to me with a faint smile on his face."

                $ renpy.pause (0.5)
                show logan serious b at right with dissolve
                $ renpy.pause (0.5)

                Lg "I want you to remember me if that’s possible. Besides, it’s not like I’ll be using the watch soon anyway."
                Lg "Every time you look at it, I want you to remember us all. Remember that you are our last hope."
                Lg "That watch will serve as a symbol of our goal to save both humanity and dragonkind."
                Lg "Yes, the time travel will probably screw with your memory, but I don’t care anymore. Just…{w=1.15} please. Don’t fail."
                $ renpy.pause (0.5)
                m "Logan’s words drifted slightly as he looked into the distance. It almost seemed as if he was trying to hide his face from me as he tried to spit his words out."
                $ renpy.pause (1.5)
                Lg normal b "May we meet again in another time, friend." #Is this the only time ever that Logan calls the player "friend?" Because, if so, then damn.

                $ renpy.pause (0.5)
                hide logan with dissolvemed
                $ renpy.pause (1.0)
                m "Logan simply left after he finished speaking, slowly stumbling away from the portal. The only ones that were left were me and Remy."
                $ renpy.pause (1.0)

            show remy at center with ease
            $ renpy.pause (0.5)
            show remy shycry with dissolve
            $ renpy.pause (0.5)

            Ry "I guess this is it. I won’t see you anymore, will I?"
            c "Not in this timeline. I’m sorry that I have to leave you alone like this, Remy."
            Ry "But I’m not. I have Adine this time. I can at least guess that in most of those other attempts, I was truly alone."
            Ry cry "{cps=16}Yet, it still hurts to see you leave.{/cps}"
            $ renpy.pause (1.0)
            m "All I could do is stand in front of him with a sense of guilt, watching his tears stream down from his face."

            stop music fadeout (1.5)
            $ renpy.pause (2.0)
            play music "mx/prayer.ogg" fadein (1.5)
            $ renpy.pause (0.5)

            c "I’ll try my best to remember you, Remy. I promise."
            $ renpy.pause (0.5)
            Ry cry "T-Thank you."

            $ renpy.pause (0.5)
            hide remy with dissolve
            $ renpy.pause (0.5)

            m "Remy slowly lifted his head and gave me a small lick with his tongue as he unfurled his wings. He wiped his tears away and stood strongly."

            $ renpy.pause (1.5)
            show remy shy with dissolve
            $ renpy.pause (1.5)

            Ry "I hope you’ll succeed on the other side, [player_name]. Make us all proud."
            c "I will."

            $ renpy.pause (0.5)
            hide remy with dissolveslow
            $ renpy.pause (1.5)

            m "With my time running out, I went to the portal and powered it on. With much hassle, it eventually started its routine of powering on. I stood between the two pillars and stared outward at a bright night sky."
            
            play sound "fx/tel.wav"
            $ renpy.pause (2.0)
            show remy shy b with dissolve
            
            m "The last thing I saw before phasing out of this world was Remy slowly undoing his tie and looking at me with an expression of wistful hope."

            stop sound fadeout (2.0)
            $ persistent.kol_tlh_EndingE_done = "E"
            $ kol_tlh_endingE = True

            jump kol_tlh_credits

            # Soooooo, I just realised something grim. Will Remy be overcome with so much grief and false guilt that he would kill himself before the comet hits?
            # Would he do that in a similar way to Naomi ECK's Naomi mod's ending E? You know, how Naomi didn't want to see all her friends suffer and die a painful death because of her errors?
            # Or, would he stick around with Adine and Amely to try and comfort them in those last few moments?
            # Knowing what happened in the base game (and, if you want to go into non-canon territory, TLD ending E), the former is the most likely.
            # ...
            # This... is a horrific thought.





else:
    #ENDING A

    $ save_name = (_("TLH - Ending A"))

    $ renpy.pause (2.0)
    nvl clear
    window show
    play music "mx/lost_in_a_dream_kol.ogg" fadein (2.0)

    n "As the days passed and nothing new happened, I continued my duties as an ambassador, helping with whatever I could to guarantee the highest chance of redirecting the comet, all while Logan helped humanity back on the other side."
    n "Unfortunately, I never saw Logan after we went our separate ways. Despite that, I had a feeling that Logan was doing everything he could to let humanity hold on as long as possible before the trade agreement could continue as promised."
    n "It did make me wonder what the Sergeant’s reaction was when Logan was found back home, though."
    n "Regardless, I knew that the work that Logan is putting in would be celebrated by everyone in the city."

    window hide
    nvl clear

    $ renpy.pause (3.0)
    scene o at Pan((0, 0), (0, 250), 5.0) with dissolveslow
    $ renpy.pause (3.0)

    $ renpy.pause (1.0)
    play sound "fx/door/doorbell.wav"
    $ renpy.pause (1.5)
    play sound "fx/door/door_open.wav"
    $ renpy.pause (1.5)
    show remy normal with easeinright
    $ renpy.pause (1.0)

    Ry smile "Good evening, [player_name]."
    c "Hey, Remy. What brings you here at this time of day?"
    Ry normal "Official business, I’m afraid. You know how things have gone as of late."
    c "Let me guess, yet {i}another{/i} visit to Emera."
    Ry "The one and only. We’ve got a meeting with her in a bit about the comet."
    c "What an honour."
    Ry "I suppose it is. Was getting a front view seat worth all the hours of exhausting work? I’m not entirely sure. Despite that, I’m happy that I could have been a part of all of this."
    Ry shy "Never in my life have I thought that I would save the world alongside a human."

    menu:
        "The feeling is mutual.":
            $ renpy.pause (0.5)

            Ry "Of course. I imagine that this must feel quite strange to you as well."
            Ry "I guess we can both share a common feeling in this regard."

        "I’m sure you never thought that you would date a human as well, but here we are.": #That's... slightly jarring.
            $ renpy.pause (2.0)

            if kol_tlh_4B_success == False or kol_tlh_datecounter < 2:
                Ry look "Yes, that too..."

            else:
                Ry "I-I suppose so. Life sure is interesting at times…"

        "As if that’s a bad thing to experience.":
            $ renpy.pause (0.5)

            Ry "Well, to start, I can’t say that having the world in danger is a good thing in the first place."

            if kol_tlh_4B_success == False or kol_tlh_datecounter < 2:
                Ry "Though I suppose I can understand where your logic is coming from."

            else:
                Ry "But I guess I can’t really complain if I get to spend some time with someone I care a lot about in the process."
    
    $ renpy.pause (1.5)
    Ry "I just realised that we’ll receive so much attention after everything is done. This...{w=0.75} will make my job at the library much more difficult."
    c "I’m sure Emera would probably protect you from all the potential harassment that you’ll be getting."
    Ry look "Only if it would make her look good in the public eye, otherwise I doubt that she’ll do anything."
    $ renpy.pause (0.5)
    Ry normal "We shouldn’t stay here. We’ve got a meeting to attend, and we might already be running late."
    c "You never told me that we needed to hurry."
    $ renpy.pause (1.5)
    Ry shy "..."
    $ renpy.pause (1.5)

    if kol_tlh_4B_success == False or kol_tlh_datecounter < 2:
        Ry "Let's just go, shall we?"
        c "Sure."

    else:
        Ry "How sore is your body from the other day? Do you think that you’ll be able to walk fast enough?"
        c "I’ve mostly walked the pain off with my constant trips through town, but speed walking is as fast as I can go."
        Ry "W-Well, the option for me to carry you around is still there if you’re up for it."
        c "Do you think you’ll manage?"
        Ry normal "I should be able to. I’ve carried you once before, and I could probably do so again."
        c "In that case, I'll take you up on the offer."
        Ry smile "Then hop aboard. Do watch out for the wings, though."

        $ renpy.pause (0.5)
        hide remy with dissolve
        $ renpy.pause (0.5)

        m "Remy lowered his body for me, and with a bit of a struggle, I managed to get on Remy’s back. Remy suddenly raised himself off of the ground and slightly shook his body so that I could be seated in a better position."
        $ renpy.pause (1.0)
        Ry normal "Hold on tight, please. This might be a bit of a bumpy ride."
        c "There isn’t that much to hold on to, but I’ll try."
        Ry "At least you don’t have to worry about me flying, then. Flying around would probably cause me to throw you off." #I wonder, I wonder...
        Ry shy "Not that I could fly right now. I’d need quite a lot of practise so that I could get strong enough to carry you around while in the air."
        c "Fair enough. {w}Now, let's go."

    $ renpy.pause (1.0)
    scene black with dissolvemed
    $ renpy.pause (1.0)
    play sound "fx/steps/rough_gravel.wav"

    if kol_tlh_4B_success == False or kol_tlh_datecounter < 2:
        m "The two of us hastily left my apartment, hoping to reach Emera's office before long."

        $ renpy.pause (2.0)
        scene buildingoutside at Pan((0, 0), (0, 0), 0.0) with dissolvemed
        $ renpy.pause (0.5)
        show remy normal with dissolve
        $ renpy.pause (0.5)
        Ry "After you, [player_name]."
        c "Thanks."


    else:

        m "The two of us left my apartment, and as Remy closed the door for me, I started to hold on tightly to his neck. Out of nowhere, Remy started to rapidly increase in speed, catching me off guard at first."
        $ renpy.pause (1.0)
        m "With Remy dashing through the streets, I could feel the wind blow through my clothes and my body being soothed by the constant swaying of Remy’s movements."
        $ renpy.pause (1.0)
        m "It wasn’t long before we reached the outside of Emera’s office."

        $ renpy.pause (2.0)
        scene buildingoutside at Pan((0, 0), (0, 0), 0.0) with dissolvemed
        $ renpy.pause (0.5)
        
        Ry smile "And we have arrived at our destination! Now, if you don’t mind, I’d like to have you off my back. I don’t think it would look great if Emera saw me carrying you around."
        c "Of course."

        $ renpy.pause (2.5)
        show remy normal with dissolve
        $ renpy.pause (0.5)
        Ry smile "Ah, that feels far better."

        menu:
            "Are you calling me fat, Remy?": # *cough* TDOMI *cough*
                $ renpy.pause (0.5)

                Ry shy "What, no! I’m just relieved that I can get some deep breaths after running with a weight on my back the whole time."

            "I imagine that running around town would make you quite tired.":
                $ renpy.pause (0.5)

                Ry normal "Even more so with you on my back, but a few deep breaths will help me feel better."

            "Well, that was quite fun.":
                $ renpy.pause (0.5)

                Ry normal "I could imagine so. Still, it’s nowhere near as fun as flying around, even if that requires far more effort to be put into it."
                Ry "Maybe one day we’ll be able to fly together, but for now this will have to do."


        $ renpy.pause (1.5)
        Ry shy "You’re not feeling sore after all that, are you?"
        c "I'm alright, thanks."
        Ry normal "That’s good to hear. Carrying you around would have been pointless if you ended up even more sore instead."
        $ renpy.pause (0.5)
        Ry "But I digress. Emera is waiting for us."

    $ renpy.pause (1.5)
    show corridor with dissolvemed
    $ renpy.pause (1.75)

    m "The two of us went into the office building, hopefully for the last time for a while. As we made our way through the halls, I saw quite a few eyes glance at us before going about their business."
    $ renpy.pause (1.0)
    m "Strangely, when we were at Emera’s office, her door was wide open."
    
    stop music fadeout (2.5)
    $ renpy.pause (1.0)
    scene emeraroom at Pan ((0, 0), (0, 180), 5.0) with dissolveslow
    $ renpy.pause (4.5)
    show emera normal at Position(xpos = 0.8) with dissolve
    $ renpy.pause (1.0)
    show remy normal flip at Position(xpos = 0.2) with easeinleft
    $ renpy.pause (1.0)
    play music "mx/scraps_kol.ogg"

    Em ques "Well you certainly took your time getting [player_name], Remy."
    Ry "My apologies. I do hope we aren’t too late."
    Em "Quite frankly, you’re just on time. If you were even a few minutes later, we would have some problems."
    Em normal "That is not the case, however. Welcome, Remy. Welcome, Ambassador. I believe that Remy already told you about our business here, correct?"
    c "You wanted us to have a meeting about the comet?"
    Em "To an extent. Most of the things that are necessary in terms of redirecting the comet had already been handed over to our scientists involved in the whole ordeal."
    Em ques "I instead wanted to bring you and Remy here to be the first to hear the live updates of the comet’s redirection. After all, with the work that you two put in, it seems only fair that you’d be the first to hear of the comet’s progress."
    Em normal "Though, do not think there won’t be any compensation for your hard work, [player_name]. The same goes to you as well, Remy."

    $ renpy.pause (1.0)
    show remy shy flip with dissolve
    $ renpy.pause (1.0)

    Em "But we shall discuss that after the comet has been redirected. Are there any last-minute things that you need to mention about your research, Remy?"
    Ry normal flip "Nothing noteworthy. I can give you a summary of the plan that I forwarded to the other council members, but I doubt that would change much."
    Em "No need."
    Em ques "And [player_name]? Anything you would like to add or would like to know?"
    c "Just how exactly will we receive these live updates?"
    Em normal "You will be in contact with one of the scientists involved with the comet's redirection."
    $ renpy.pause (1.0)
    Em "Speaking of, it’s time to give this scientist a call. I’m sure that he must be waiting for us."

    $ renpy.pause (0.5)
    hide emera with dissolve
    $ renpy.pause (0.5)

    m "Emera stood up from her desk and walked to the other side of her office with what seemed like pride in her step. She pressed a few buttons and picked up a phone, but not after signalling for me to come over to her. Emera put the phone on speaker while we waited."
    $ renpy.pause (1.0)
    m "A few moments of awkward silence passed before a voice came from the other side."
    $ renpy.pause (1.0)
    show emera normal at Position(xpos = 0.8) with dissolve
    $ renpy.pause (0.5)

    "???" "Hello! Is this Minister Emera on the other end of the line?"
    c "This is [player_name] speaking."
    "???" "Woah, really?! It’s an honour to be able to speak to the legendary human after everything I’ve been hearing about you, ha ha!"
    $ renpy.pause (0.5)
    "???" "Oh, I’m sorry. This isn’t professional of me at all." #Yeah, tried to write a carefree, socially awkward character. That failed horribly.
    $ renpy.pause (0.5)
    Ek "My name is Erika. Nice to meet you!"
    Ek "Is Remy nearby?"
    Ry normal flip "Yes, I'm here."
    Ek "Glad to hear it! I’m sure the Minister already told you two everything ahead of time?"
    c "Of course."
    Ek "Alright then! So, here’s the drill: as we slowly progress in redirecting the comet, I’ll be giving the news as it happens. This will of course lead to some awkward moments of silence in between though, if that’s alright?"
    c "What, will you be playing some low-quality hold music while we wait for the next update?"
    Ek "Pffffft, that’s a good one!"
    $ renpy.pause (1.0)
    Ek "Oh, um, keeping professional. My apologies."
    c "You don’t need to be professional here. I’m guessing that you experience more than enough stress as is, so there’s no need to hide everything under a mask. Just be yourself."
    Ek "Thank you! It helps keep my mind calm to not be as formal."
    show emera frown with dissolve
    Ek "And we’re about to begin. Wish us luck!"

    $ renpy.pause (1.0)
    play sound "fx/answeringmachine.ogg"
    $ renpy.pause (0.5)

    m "A small beep soon followed, leaving an eerie silence in the room. Looking back at Emera, I could see that she was extraordinarily worried despite trying her best to hide it. Remy, however, appeared to have a stoic expression of sorts."
    $ renpy.pause (2.5)
    Ry shy flip "Should all of this fail, I at least want to say this: thank you for doing the best you possibly could have, [player_name]. And, of course, thank you for everything else." #TROPE ALERT! TROPE ALERT!
    c "I’m just happy to be with you right now, Remy."
    Ry "I feel the same way."

    $ renpy.pause (1.0)
    play sound "fx/answeringmachine.ogg"
    $ renpy.pause (1.5)

    Ek "Alright, first update! We have made contact with the comet and will soon be at full power."
    c "Quick question: how exactly will the energy from all the generators be used to redirect the comet?"
    Ry normal flip "I can answer that if you want me to."
    Ek "Oooo, go right ahead! It’s fitting that the architect of the original plan explains what we’re doing over here."
    $ renpy.pause (0.5)
    Ry shy flip "Okay, then. The original plan was to maximise the impact of our efforts to redirect the comet while also using as little power as possible. After much trial and error while researching, I came up with the idea of using ion thrusters to slow the comet down to a near standstill." #Ion thrusters? *What?*
    Ry normal flip "Of course, this wouldn’t be enough on its own. After the comet had slowed down enough, the pulses would then change into a very small, concentrated laser. This should hopefully evaporate the surface of the comet to such a degree that it would create a thruster of sorts, causing it to change its directory."
    Ry "If everything falls into place, this would be enough to make the comet pass the earth safely." #I tried my best to come up with something even slightly realistic, alright? Cut me some slack.
    Ek "I couldn’t have explained it better myself."
    Ry smile flip "Thank you. I did try my best to make it easy to understand when presenting the plan to the council."
    $ renpy.pause (0.5)
    Ek "Well, it’s time for the next period of awkward silence to commence. See you soon!"

    $ renpy.pause (1.0)
    play sound "fx/answeringmachine.ogg"
    $ renpy.pause (2.5)

    Em "I find it so strange that, despite the livelihoods of everybody at risk, you’re so casual. Why is this?"

    menu:
        "It helps to keep spirits high.":

            c "If I only kept a serious tone throughout the conversation, it would bring the mood down. Having everybody in a pit of gloom won’t make the situation better."
            Em ques "A valid point."

        "Is there a reason why I need to be formal?":
            $ renpy.pause (0.5)

            Em "I suppose not. Regardless, it feels uncanny that you seem to be so carefree about our civilization facing such a huge crisis."
            Em ques "Maybe it’s due to you being unfamiliar with how we view life; maybe it’s something akin to a feeling of negligence toward our society."
            Em frown "Or, something else entirely."

        "I felt that I would achieve more with a casual tone instead.":

            c "Did you hear how Erika sounded, Minister? It sounded like a bundle of nerves talking on the other side of the phone instead of a person."
            c "It would’ve been far better if I switched to a casual tone instead."
            Em "Of course. Perhaps a more casual approach would make these updates feel more…{w=0.9} authentic, in a sense. Having a bunch of facts hastily thrown at you isn’t the most helpful."

    $ renpy.pause (0.3)
    Ry normal flip "May I ask you something, Emera?"
    Em normal "You may."
    Ry "Why is it that this was the method you chose to report information to us instead of, say, a live news feed on a screen? This just doesn’t seem efficient to have to wait in silence between each update." # Mostly because I wanted to insert a cameo character tbh.
    Em frown "I'm disappointed in you."  #Okay, why the hell did I write this? Like seriously, *whyyyyyyyyyyy?*
    Ry shy flip "What?"
    Em "I figured that you would know considering you were the person to come up with the suggestion of live updates. Instead, you ask me the questions that you made up with an answer that you already know." #Why so vague? This explains nothing! What kind of drugs were I on when writing this part? NOTHING MAKES SENSE.
    Em mean "I expect you to answer your own question on this matter, Remy, as any assistant of mine should." #Good grief, I'm creating a strawman for literally no other reason but to have a strawman. 11/10 writing, folks! *facepalms*
    c "Stop it."

    $ renpy.pause (0.75)
    stop music fadeout (2.0)

    m "The words leapt out of my mouth without me even considering the consequences of what I had just said. As soon as I realised what had just happened, both Remy and Emera looked me dead in the eyes. I tried to improvise an argument, knowing that I couldn’t back out of this now."

    $ renpy.pause (1.0)
    play music "mx/crypts_kol.ogg"
    $ renpy.pause (1.0)

    c "All Remy did was ask a simple, innocent question. He’s gone through so much stress that the council put on him considering the job that he had to do."
    c "Do you really think that he’d be able to remember every single niche detail of every single paragraph of his report? Do you really think that, after nearly overworking himself, he’d have the energy to remember his entire report as well as carry out his usual tasks at the library?"
    show remy look flip with dissolve
    c "All Remy asked for was a refresher. That’s it. Why do you have to berate him for a small mishap after everything he did for the council? He’s the main reason why we’re all here in the first place, after all. Do you truly think that talking down to a saviour of dragonkind would look well for you, Minister?"
    show remy shy flip with dissolvemed
    $ renpy.pause (1.5)
    Em frown "..."
    $ renpy.pause (1.0)
    c "And I do have to apologise for speaking out like this to you, but I feel that it needs to be said. All I’m asking is for you to give Remy a break and truly value everything he has done."
    $ renpy.pause (2.5)
    Ry "..."
    Em "..."
    c "..." #Like I said: strawman. I have become the very thing I swore to avoid.
    $ renpy.pause (1.5)
    Em normal "Remy, we will have a meeting at eight in the morning. Don’t be late. As for you, [player_name], we need to speak in private at a later date. I’ll arrange a meeting when I’m available."
    $ renpy.pause (1.0)
    show emera frown with dissolvequick
    m "Emera paused slightly to give me an analytical look of sorts, as if she were trying to read my body language."
    $ renpy.pause (1.0)
    Em ques "And no, this talk won’t be of a negative nature. Unless, of course, our plan had failed. Have I made myself clear?"
    c "Yes, Emera."
    Em normal "Good. In the meantime, I will reflect on what you said. I believe that there’s–{w=1.85}{nw}"

    $ renpy.pause (1.0)
    play sound "fx/answeringmachine.ogg"
    $ renpy.pause (1.5)

    Ek "And we’re at full power! The comet has pretty much stopped right now aside from slight rotational movement here and there. We’re slowly shifting to the second phase."
    Ry normal flip "How is the power situation looking so far?"
    Ek "I can check for you real quick…"
    $ renpy.pause (2.5)
    Ek "We’re at seventy-one percent of our total reserves, excluding the emergency reserves."
    Ry smile flip "It looks like there was a miscalculation to our benefit. I thought we would be at around forty percent right now." #That's... one hell of a miscalculation, Remy.
    Ek "Me neither! It does make things much easier to handle if there happens to be a miscalculation for your benefit somewhere."
    Ry normal flip "Indeed."
    c "Anything else that you want to share with us, Erika?"
    $ renpy.pause (0.5)
    Ek "Hmmm, I can’t think of anything noteworthy for now. That is, unless you want a bunch of super complicated maths thrown at your face."
    $ renpy.pause (0.5)
    c "I’ll pass, thanks."
    Ek "Maybe next time, then! For now, I’ll have to leave you on hold for quite some time, as we really need to focus on this part over here. I’ll talk once significant movement had been detected from the comet."

    $ renpy.pause (1.0)
    play sound "fx/answeringmachine.ogg"
    stop music fadeout (4.0)
    $ renpy.pause (2.5)

    m "As silence reigned once more, the three of us only looked at each other nervously. With the first phase of the redirection being a success, I could only hope that the next one would go as smoothly."
    
    $ renpy.pause (0.75)
    play music "fx/clock.ogg"
    $ renpy.pause (4.5)
    show emera normal with dissolve
    m "Seconds turned into moments, which turned into minutes. As the ticking of the clock became the only sound in the office, Remy gave a slight glance at me, seeming far more calm than I had. Emera, on the other hand, looked like she was trying to maintain a stoic facade but failing spectacularly."
    $ renpy.pause (3.5)
    show remy look flip with dissolve
    m "Eventually, almost an entire hour had passed before a voice broke the maddening sounds of clockwork."
    $ renpy.pause (1.0)
    stop music
    $ renpy.pause (1.0)
    play sound "fx/answeringmachine.ogg"
    $ renpy.pause (2.5)
    play music "mx/prophecy.ogg" fadein (2.0)
    show remy normal flip with dissolve

    Ek "I’m so, so sorry that I left everybody hanging for so long!"
    c "It’s alright. You need to focus on the comet first before informing us of the current results."
    Ek "I know, I know. I just hate to leave everybody hanging in dread, you know?" #I'll admit, Erika do be sounding like a hipster of sorts. Quite the dashing one, in fact.
    $ renpy.pause (1.0)
    Ek "Talking about the comet, it’s my honour to inform you that we have managed to create several points where the laser branches off onto different parts of the surface, causing multiple points to evaporate at once."
    Ek "In simpler terms, the comet now has multiple boosters that will redirect it away from us."
    Ek "The team estimates that, within the next half hour, the comet will have moved enough to the point where it will safely pass us."
    Em "That is marvellous to hear. I’m trusting that we still have enough power left?"
    Ek "Yes, Minister. We are currently at thirty-two percent capacity, not including the emergency reserves."
    Ek "According to our calculations, we might still be able to have some energy left after we redirected the comet."
    Em "Excellent."
    $ renpy.pause (0.5)
    m "Despite Emera looking expressionless and sounding just as emotionless, I felt that she had a huge feeling of joy within her." #Because of course the MC has magical senses that could just detect the inner emotes of any dragon.
    $ renpy.pause (0.5)
    Em "I will now leave you to your job, Erika. I wish you and your team the best of luck in this final stretch."
    Ek "Thank you, Minister."

    $ renpy.pause (1.0)
    play sound "fx/answeringmachine.ogg"
    $ renpy.pause (2.0)

    Em frown "I think I need a small break after all of this. I can’t imagine that all this stress is helping me in my age." #Boomer.
    Ry "Of course, Emera."
    Em ques "On the other hand, I suppose another massage is due. It’s been quite some time since I’ve had one." #...why the hell are you saying that in front of the MC? I swear, my writing took one hell of a dip with this ending.

    $ renpy.pause (0.5)
    show remy sad flip with dissolvemed
    $ renpy.pause (1.5)

    Ry "..."
    Em normal "I suppose that it would all be sorted out later. In the meantime, I’d like a coffee, please. Try not to spill it like last time."
    Ry normal flip "I’ll be back soon."

    $ renpy.pause (0.5)
    show remy normal with dissolve
    $ renpy.pause (0.5)
    hide remy with easeoutleft
    $ renpy.pause (1.5)

    Em frown "I know what you’re thinking, and no, we won’t have our talk now. We have far too little time. Instead, let me ask you a question that has been on my mind for a while now."
    Em "What will you do after all of this?"

    if kol_tlh_tld_crossover2 == True:

        menu:
            "I’d like to return home for a while.":
                $ renpy.pause (0.5)
                $ kol_tlh_endingA_variation = True

                Em "Oh? And why is that?"
                c "I imagine that, after being gone for so long, things have been very hard back in my city. With us still waiting to receive a generator, humanity will be on their final few breaths."
                c "I need to go back to try and help wherever I can. Yes, I’d still most likely take part in the trade negotiations from the other side, but at least I can help everyone back home while there."
                Em normal "A noble pursuit; one I can respect quite a lot. I promise you this: after the comet has been redirected, we will send two generators as an apology to humanity for taking so long. I am extremely sure we would be able to afford the loss of two generators while we recover."
                c "Thank you, Minister. It means a lot to me."
                Em ques "You are the last person who needs to show some gratitude, Ambassador."


            "I need to fulfil my duty as an ambassador here.":
                $ renpy.pause (0.5)

                Em "Oh? Why do you feel this way?"
                c "I have been sent by humanity to arrange a trade agreement alongside Reza for our survival. I promised that I would not return until my mission had been completed."
                c "I will continue to serve as an ambassador here to strengthen the relationship between our two societies because, at this point, we have become far too dependent on each other to part ways."
                Em normal "I agree with your logic, [player_name]. Very well, I’ll give you full permission to continue your duties as ambassador. We will also send two generators to humanity as an apology for taking so long to deliver our end of the bargain."
                c "Thank you, Minister. This truly means a lot to me."
                Em ques "You don’t need to be the one to show how thankful you are, Ambassador."


    else:
        c "I need to fulfil my duty as an ambassador here."
        $ renpy.pause (0.5)
        Em "Oh? Why do you feel this way?"
        c "I have been sent by humanity to arrange a trade agreement alongside Reza for our survival. I promised that I would not return until my mission had been completed."
        c "I will continue to serve as an ambassador here to strengthen the relationship between our two societies because, at this point, we have become far too dependent on each other to part ways."
        Em normal "I agree with your logic, [player_name]. Very well, I’ll give you full permission to continue your duties as ambassador. We will also send two generators to humanity as an apology for taking so long to deliver our end of the bargain."
        c "Thank you, Minister. This truly means a lot to me."
        Em ques "You don’t need to be the one to show how thankful you are, Ambassador."

    $ renpy.pause (1.0)
    Em normal "{i}We{/i} are."
    $ renpy.pause (1.0)
    show remy normal flip at Position(xpos = 0.2) with easeinleft
    $ renpy.pause (1.0)

    Ry "Here you go, Emera. Extra hot, as usual."
    Em ques "It’s such a shame that you couldn’t have arrived a bit later. Me and [player_name] had quite an interesting conversation."
    Ry shy flip "My apologies for interrupting."

    stop music fadeout (2.0)
    $ renpy.pause (1.0)
    play sound "fx/answeringmachine.ogg"
    $ renpy.pause (1.0)
    play music "mx/tranquility.ogg" fadein (2.0)
    $ renpy.pause (2.0)

    m "Suddenly, a beep came from the phone, with a loud cheer being audible in the background. During all the clashing voices, I could just barely make out Erika trying to speak."
    $ renpy.pause (1.0)
    Ek "So, I believe that you might have an inkling of an idea of what happened if you can hear the background."
    c "It's official, then?"
    $ renpy.pause (1.0)
    Ek "It is!" with vpunch #...why the vpunch? Eh, whatevs.
    $ renpy.pause (1.0)
    Em normal "That is wonderful to hear! I congratulate you and your team for accomplishing such a monumental task."
    Ek "Thank you, Minister! It means a lot to hear those words!"
    $ renpy.pause (2.5)
    Ek "I’m sorry, but I have to hang up now. I’m afraid that I can barely hear myself speak."
    c "It’s alright. Thank you for your service, Erika."
    Ek "It was a pleasure! And thank you for waiting for so long to hear all the reports! It was truly an honour to be able to talk to you, [player_name]."
    Ek "Godspeed, everyone!"

    $ renpy.pause (3.0)
    play sound "fx/answeringmachine.ogg"
    $ renpy.pause (3.0)

    scene black with fade
    $ renpy.pause (2.0)
    nvl clear
    window show

    n "And with that, the comet had been redirected. With dragonkind now entering a new age of hope, things are starting to truly look up for the first time since the Reza murders."
    n "Remy received a position in the council as a Minister of Human Affairs; the first of its kind. Remy was extremely bewildered by the position, yet he accepted it regardless. He was also offered a statue alongside mine, to which Remy only responded with a lighthearted comment about how he'll think about the offer for a bit."

    window hide
    nvl clear
    $ renpy.pause (3.0)
    window show

    
    if kol_tlh_endingA_variation == False: #Stay in dragonland (base route with no TLD variation)

        n "It has been some time since I’ve last heard of humanity, however. Ever since the dragons sent the generators through, we didn’t hear of any updates from their side. Naturally, I feared the worst, hoping that Logan hadn’t failed to keep the city going while I was here."
        n "Yet my spirits had been rekindled as I received a letter from Logan about a week after we sent the generators. Apparently, humanity is making a slow yet steady recovery. The hospital back home is fully operational, and many of those there have recovered. Infrastructure is being rebuilt, food supplies are stabilising, and dirty water is being purified."
        n "Deciding to share the good news with Remy, I invited him to my apartment as soon as he had the time to visit."

        window hide
        nvl clear

        $ renpy.pause (3.0)
        scene o at Pan((0, 0), (0, 250), 5.0) with dissolveslow
        $ renpy.pause (3.0)

        if kol_tlh_4B_success == False and kol_tlh_datecounter < 2:

            stop music
            m "But he never came. I tried calling him to see if he maybe forgot, but none of my calls went through to him."
            m "Eventually, I decided to give up and wondered if Remy simply didn't want to see me any more."
            $ renpy.pause (1.0)
            m "With nothing else to do for the time being, I decided to write a letter to Logan about how things were on my side of the portal."

            $ kol_tlh_false_endingA_3 = True
            $ persistent.kol_tlh_EndingA_done = "A (False Route 3)" #Yep. You've been so much of an asshole that he just straight-up ghosts you.
            $ kol_tlh_endingA = True
            
            jump kol_tlh_credits



        else:
            show remy normal with dissolve
            $ renpy.pause (2.0)

            Ry smile "I’m really happy that everything is going so well back home, [player_name]. Hearing humanity thrive will be far better for us in the long run."
            c "You’re already starting to sound like a politician, you know that?"
            Ry shy "Really? I do hope that this won’t be a bad thing."
            c "Why would it be? Regardless of your title, you're still the same Remy."
            Ry normal "I suppose you’re right. I’m just afraid that I’ll become like Emera and only care about myself."
            $ renpy.pause (0.5)
            c "Speaking of, how does it feel to work alongside Emera instead of having her boss you around?"
            $ renpy.pause (0.5)
            Ry "Well, it’s definitely an interesting feeling. Never in my wildest dreams did I imagine that the person I'd grown to despise would become my coworker. I suppose that Emera not really bullying me anymore is a good thing."
            c "Really? Just like that?"
            Ry "It wouldn’t look good for her public image if she bullied another minister in the council."
            c "Yeah, that makes sense."
            Ry smile "But why talk about work when we can have a fun time instead?"
            c "What do you have in mind?"
            Ry normal "How would you like to see what Tatsu Park is like at night?"
            c "I’ll admit, it does sound interesting."
            Ry smile "Then I’ll see you at eleven."
            Ry normal "For now, I’ll have to unfortunately leave you. I have to write down the information that you gave me, as it falls under human affairs."
            c "Alright then. Catch you later."
            Ry "Goodbye, [player_name]."

            $ renpy.pause (0.5)
            show remy normal flip with dissolve

            if kol_tlh_4B_success == False or kol_tlh_datecounter < 2:
                $ renpy.pause (0.35)
                show remy look flip with dissolve
            else:
                pass

            $ renpy.pause (0.5)
            hide remy with easeoutright
            $ renpy.pause (1.5)
            play sound "fx/door/doorclose.ogg"
            $ renpy.pause (1.0)

            if kol_tlh_4B_success == False or kol_tlh_datecounter < 2:
                m "As Remy walked outside, I couldn't help but think about how he seemed to be a bit nervous of something. Was there something serious that he wanted to tell me tonight?"
            
            else:
                m "As Remy walked outside, I couldn’t help but think how happy he seemed to be, as if he had finally broken the shackles of his depression. I wondered if this was how Remy had felt back when he was with Amelia."

            $ renpy.pause (1.0)
            stop music fadeout (3.0)
            scene black with fade
            $ renpy.pause (2.0)
            m "I carried on with my duties for the rest of the day until it was time for me to go to Tatsu Park."
            $ renpy.pause (2.0)
            scene kolpark2night with dissolveslow
            $ renpy.pause (1.0)
            m "Upon arriving, I saw Remy looking into the distance, just like how he did back when he first revealed his tragic past to me."
            $ renpy.pause (1.0)
            show remy normal dk with dissolve
            $ renpy.pause (2.0)
            play music "mx/starlight.ogg"

            Ry smile dk "Good night, [player_name]." #Cheesy jokes FTW!
            c "Hello to you too, Remy."
            Ry shy dk "Thank you for coming at such an hour. It means a lot."
            c "After everything we’ve been through, being up late at night is nothing."
            Ry "I suppose that’s fair. Still, it just feels a bit surreal seeing a public space this quiet."
            Ry smile dk "But as a reward, we get to see the moon and stars as they always were, with no star in the sky slowly becoming brighter and brighter with each passing day."

            if kol_tlh_4B_success == False or kol_tlh_datecounter < 2:
                pass

            else:
                Ry normal dk "And the best part? I get to do it with you."
                $ renpy.pause (0.5)

                menu:
                    "It definitely is the best part.":
                        $ renpy.pause (0.5)

                        Ry smile dk "I’m happy you think so too. You have no idea how special this all feels to me."

                    "I suppose the night just makes everything feel more special in a way.":
                        $ renpy.pause (0.5)

                        Ry "Indeed. That’s why I love the night so much; probably even more so than the day."
                        Ry "Seeing everything slowly fall asleep while the moon and stars dot the night sky…"
                        $ renpy.pause (0.5)
                        Ry smile dk "It's beautiful."

                    "How many times have you done this before?":
                        $ renpy.pause (0.5)

                        Ry shy dk "I could have probably flown here from my apartment while closing my eyes."
                        c "Could have?"
                        Ry "I went out at night a lot with Amelia back in the day. We’d often stare at the stars for hours."
                        Ry smile dk "Doing this again after so long feels nostalgic to me, in a sense."
            

            $ renpy.pause (1.5)
            Ry shy dk "May I confess something to you, [player_name]?"
            c "Any time, Remy."
            $ renpy.pause (0.5)
            Ry "I'm lost."
            Ry "Never in my wildest dreams would I ever imagine that I would become a minister. Yet, having a new position created specifically for me? How do you even begin to comprehend that?"
            Ry "Not to even begin with the fact that the council wants to build a statue of me. I mean, all I did was do my job. I did what was expected of me. Why should I be rewarded for following orders?" #The poor guy is bewildered beyond belief...
            c "Because you did more than just follow orders. You went out of your way to give dragonkind the best chance that they could possibly have had. And, to add to that, you helped with the Reza confrontation. That alone deserves an award."
            $ renpy.pause (1.5)
            Ry shy dk "..."
            $ renpy.pause (0.5)
            Ry "I-I suppose you’re right. Still, since nobody held this position before me, I have no clue what to do or how to do it."
            c "That’s why I’m here, Remy. There’s a reason why I’m an ambassador, you know."

            if kol_tlh_4B_success == False or kol_tlh_datecounter < 2:
                #False ending A here

                $ renpy.pause (1.5)
                stop music fadeout (5.0)
                show remy look dk with dissolvemed
                $ renpy.pause (1.5)

                Ry "An ambassador, yes."
                $ renpy.pause (0.5)
                c "Is there something wrong, Remy?"
                $ renpy.pause (1.5)
                show remy sad dk with dissolve
                $ renpy.pause (1.5)
                Ry "I... {w=0.65} guess it's time to tell you why I wanted to be here with you."
                
                if kol_tlh_datecounter <2: #Less severe false ending A here
                    $ renpy.pause (1.0)
                    $ remystatus = "good"

                    Ry look dk "We both know that our work has kept us severely busy as of late. Our work stressed us out to untold levels."
                    Ry "I don't know about you, but I was at a breaking point. You now know this when we talked during the night the other day."
                    $ renpy.pause (0.5)
                    Ry "This is something I wanted to say back then, but couldn't bring myself to. After all, you kept me going through the stress, so how could I be worried about all of this?"
                    $ renpy.pause (1.0)
                    Ry sad dk "I've realised that my fears were justified, however."
                    c "What are you talking about?"

                    $ renpy.pause (1.5)
                    play music "mx/movingon.ogg" fadein (2.0)
                    $ renpy.pause (0.5)

                    Ry "I feel like we just don't have the same bond that we had before the Reza incident. I remember how we used to spend some time whenever our schedules lined up."
                    Ry look dk "But now? The only times we had together were during your visits to the library and the night that I called you for help."
                    Ry sad dk "It's as if I'm slowly losing another person who's close to me."
                    Ry shy dk "Yes, I have Adine to keep me company again like so many years ago, but even then our relationship is only a shadow of what it used to be."
                    Ry sad dk "The reason we're so now close is because of our shared loss of Amelia. If we didn't have that, then I doubt that Adine would even talk to me." #Which is in direct contrast to what Adine tells the MC in her dates, but, as you know, depression makes your head go wack.
                    $ renpy.pause (0.5)
                    Ry "I know that this is harsh, but it needs to be said."
                    $ renpy.pause (0.5)
                    c "I had no idea this what how you felt, Remy. I'm truly sorry that I didn't put as much effort into our relationship as you did."
                    Ry "No, [player_name]. I'm sorry for making us believe that there was something when in reality there wasn't."
                    $ renpy.pause (2.0)
                    c "You said it yourself that our work kept us incredibly busy. Now, we don't have to worry about the comet as much."
                    c "We have far more time available.{w} So, are you willing to forgive me and give us another shot?"
                    
                    $ renpy.pause (3.5)
                    show remy shy dk with dissolvemed
                    $ renpy.pause (1.0)

                    Ry "I will." #This won't backfire at all, right?
                    c "Thank you."

                    $ kol_tlh_false_endingA_1 = True

                    jump kol_tlh_endingA_continued


                else: #More severe false ending A here
                    $ renpy.pause (1.0)
                    $ remystatus = "bad"

                    Ry look dk "I've been thinking about what you said to me the other night when I called for help."
                    Ry shy dk "In such a dark time, I called for advice from the one who helped me with my thoughts the first time. I hoped that after everything, you'd be able to help me again. After all, you care about me, so why wouldn't I believe this?"
                    Ry sad dk "Instead, I found nothing but belittlement from the closest person to my soul that I had in years." #Yeah, he's really laying it on thick for this part.
                    Ry "It made me question everything we had. When I originally wanted to talk to you here, and when you said all those kind things..."
                    
                    $ renpy.pause (1.0)
                    play music "mx/prayer.ogg"
                    $ renpy.pause (0.5)

                    Ry "Were they all lies to try and win me over?" #A false realisation made from ignorance's lies. I feel sorry that you were neglected by the *horrible* player's actions to the point where you believe this, Remy.
                    Ry "Am I something that you could play around with to see how I would react?" #Based off of a line in Remy 3, for those wondering.
                    $ renpy.pause (1.0)
                    Ry look dk "As if this doesn't get worse, Adine talked to me shortly after you left. I told her about all the things that I had felt during our chat."
                    Ry sad dk "I felt so lost and betrayed, [player_name]. I thought that maybe you were just cranky from being woken up in the middle of the night, but after what Adine had said to me..."
                    $ renpy.pause (2.0)
                    Ry "I believe that we shouldn't see each other any more."
                    c "Remy, this-{w=0.95}{nw}"
                    Ry "Don't. Just...{w=0.5} don't."
                    Ry look dk "Adine told me that I should maybe try and distance myself from you, but after what happened...{w=1.8}{nw}"
                    $ renpy.pause (1.0)
                    Ry sad dk "It won't be enough."
                    c "..."
                    Ry "If I stick around with you, I might do something that I will regret. For my own safety, I need to do this."
                    $ renpy.pause (1.0)
                    Ry look dk "..."
                    Ry "I'm sorry that I couldn't have realised all of this sooner. We wouldn't have wasted our time like this."
                    $ renpy.pause (1.0)
                    Ry "Thank you for letting me reconnect with Adine, at least. I'm happy that I've found someone far better." #He finally moved on from a toxic, gaslighting relationship. I'm proud of ya, Remy.
                    Ry sad dk "Goodbye, [player_name]."

                    hide remy with dissolvemed
                    play sound "fx/takeoff.ogg"
                    $ kol_tlh_false_endingA_2 = True
                    $ persistent.kol_tlh_EndingA_done = "A (False Route 2)"
                    $ kol_tlh_endingA = True

                    jump kol_tlh_credits


                

            else:
                Ry "I'm sure that things will go smoother if a human is helping the Minister of Human Affairs with, well, human affairs." #Oh, you awkward loveable dork. <3
                $ renpy.pause (1.0)
                Ry normal dk "Speaking of, you’ve been quite the help to me as of late. I don’t know how I would’ve done my job without you."
                Ry shy dk "Or everything else, for that matter."
                $ renpy.pause (1.0)
                Ry "I have to be blunt here when I say this: You helped me out of depression to the point where I can truly enjoy life again. I can wake up in the morning with a feeling of excitement. I can do my job without feeling the weight of my failures weighing me down." #And now, time to lick the MC's boots in a super wholesome way!
                Ry "I have people to talk to when things go wrong. I have regained a close friend, and found love."

                $ renpy.pause (1.0)
                show remy sad dk with dissolve
                $ renpy.pause (0.5)

                Ry "A-And..."
                $ renpy.pause (1.0)
                c "You don’t have to talk about it if you don’t want to."
                Ry "I must. You deserve to hear it."
                $ renpy.pause (1.0)
                Ry "..."
                $ renpy.pause (1.0)
                Ry "{cps=20}T-Thanks to you… I no longer want to end it all.{/cps}" # *flashbacks to finding remyhan.png*
                $ renpy.pause (1.0)
                Ry shy dk "I’m afraid that grief, regret, and loneliness combined is a very dangerous cocktail. There were so many times where I had been so close, but then? I thought of you. You gave me the strength to go on, and look where we are now."
                Ry "If you never came into my life, then I don’t know what would have happened. So, from the bottom of my soul, I thank you. {w}Dearly."

                $ renpy.pause (0.5)
                hide remy with dissolve
                $ renpy.pause (0.5)

                m "Remy slightly shifted his body and gave me a small lick on the side of my face." # *mlem*

                $ renpy.pause (0.5)
                show remy shy dk with dissolve
                $ renpy.pause (0.5)

                Ry "I will never be able to repay you for what you did."
                $ renpy.pause (1.5)

                menu:
                    "Then don’t. All I wanted was to see you happy.":
                        $ renpy.pause (0.5)

                        Ry smile dk "I don’t think happiness is a suitable form of payment, but if that’s what you want, then consider the debt paid."
                    

                    "I should be the one to repay you, Remy.":
                        $ renpy.pause (0.5)

                        Ry "Excuse me? Why?"
                        c "Without you, I definitely would’ve had a harder time being more comfortable here. Everything would feel more strange, more cold, and more lonely. Who knows what would’ve been different if my attitude had changed to that degree during my stay?"
                        Ry smile dk "It looks like we’re in each other’s debt. Would that make us eligible to cancel each other’s debt?"
                        c "It probably would."
                        Ry "Then so be it."

                    
                    "All in a day’s work.":
                        $ renpy.pause (0.5)

                        Ry "I severely doubt that changing a life to this degree is an average day’s work."
                        c "We humans just do things differently."
                        Ry smile dk "At this point, I might actually believe you."


                $ renpy.pause (2.0) 
                Ry normal dk "I have a lot to still thank you for, like how you made me get in touch with Adine again."
                Ry shy dk "I'm sure that you know all of this by now, but it really doesn't hurt to mention it another time."

                jump kol_tlh_endingA_continued










    else: #Go back home to the human city (TLD variation)

        n "It has been some time since I’ve last heard of humanity, however. Ever since the dragons sent the generators through, we didn’t hear of any updates from their side. Deciding that humanity now needs my help more than dragonkind, I announced to the council that I would temporarily return to my home."
        n "The council, wanting to send an apology, gave me two generators as a parting gift to return  to humanity. With the generators and parts already back home, we should already have enough to power most of the city’s infrastructure by now, granted that Logan actually did his part."
        n "Yet, before I wanted to go back home, I went to Remy’s apartment to say goodbye."

        window hide
        nvl clear
        stop music fadeout (2.0)

        $ renpy.pause (0.5)
        scene remyapt at Pan ((0, 80), (0,80), 5.0) with dissolve 
        $ renpy.pause (2.5)
        play music "mx/finally_home_kol.ogg" fadein (2.0)
        show remy normal with dissolve
        $ renpy.pause (1.0)

        Ry shy "You know, I was afraid that this day would come sooner rather than later."
        c "It’s not like I’m going away permanently. Besides, you could always come and visit once we strengthen the relationship between humans and dragons."
        Ry normal "It’s a possibility, yes, but unlikely. With me being a minister now, it would be extremely hard for me to convince the council to go on vacation, let alone to go through the portal to visit you."
        c "You could just disguise it as a business trip, with you now being responsible for all human affairs."
        Ry "I suppose it’s plausible. Ah, well, I guess we'll just have to wait and see."
        Ry smile "Maybe you’ll come back before I get my leave in."
        c "Hey, anything is possible now. It all depends on what life is like back home, and whether we could somewhat supp–{w=2.5}{nw}" #I can't get the timing of this right for the life of me.

        play sound "fx/door/doorbell.wav"
        $ renpy.pause (1.0)
        c "I didn’t know you were having guests."
        Ry shy "I invited them just before I heard that you’d be coming over."
        $ renpy.pause (0.75)
        play sound "fx/door/door_open.wav"
        $ renpy.pause (1.0)
        show remy at Position(xpos = 0.2) with ease
        show remy shy flip with dissolve
        show remy normal flip with dissolve
        $ renpy.pause (1.0)
        show adine normal b at Position(xpos = 0.8) with easeinright
        $ renpy.pause (1.0)

        Ad "Hey, [player_name]."

        $ renpy.pause (1.0)
        show amely small at Position(xpos = 0.9) with dissolve
        $ renpy.pause (1.0)

        Am "Human!" #Took ya long enough, Amely.
        Ad giggle b "Yes, Amely. [player_name] is a human."
        c "Hello, Adine."
        $ renpy.pause (0.8)
        c "And hello, Amely!"
        Am "Hi!"
        Ad "I’m sorry for Amely being so clingy today. She learned what a human is at the orphanage today and now she’s obsessed with them."
        c "Well maybe I should just take her with me through the portal, then."
        Ad disappoint b "So it’s true. You’re really leaving?"
        c "Only for a bit. I still have to serve as an ambassador, you know."
        Ad normal b "Of course. It wouldn’t make sense if you suddenly stopped being an ambassador after everything you’ve done."
        
        $ renpy.pause (0.5)
        hide amely with easeoutleft
        $ renpy.pause (0.5)

        Ad giggle b "And there she goes. I hope she doesn't make too much of a mess, Remy."
        Ry "Oh, I wouldn't mind at all."
        $ renpy.pause (1.0)
        show adine normal b with dissolve
        Ry "My apologies for diverting the conversation in this manner, but you mentioned that Amely should accompany you to the human world."
        c "Yes?"
        Ry shy flip "I’m afraid that it won’t happen, and not for the reason that you might think."
        Ad giggle b "Remy decided that he’s up for the challenge of adopting Amely."
        Ry look flip "Did you really have to spoil the surprise like that, Adine?" #Now with added Adine content!
        Ad normal b "You would have gone on for several more minutes if I hadn’t."
        $ renpy.pause (0.5)
        Ry shy flip "..."
        c "Remy, I’m so happy to hear that you'll finally start that family that you've always wanted to."
        Ry normal flip "Thank you, [player_name]. If everything goes well, Amely will be officially adopted by the end of next week. It’s just a shame that you won’t be here to see her full reaction."
        c "Wait, she doesn’t know yet?"
        Ad think b "She has trouble understanding big words like \"adoption\" or \"custody.\" She wouldn’t understand us talking even if she tried."
        Ad giggle b "Not that she would want to right now, anyway."

        $ renpy.pause (0.5)
        hide remy
        hide adine
        with dissolve
        show remyapt at Position(xpos=0.0, xanchor='left', ypos=1.0, yanchor='bottom') with ease #Seriously, screw this method of eeasing a background. What a way to overcomplicate things.
        $ renpy.pause (0.5)
        show amely normal at Position(xpos = 0.75) with dissolve
        $ renpy.pause (0.5)

        Am "It tasty!"
        c "That…{w=0.5} doesn’t hurt, does it?"

        $ renpy.pause (0.5)
        hide amely with dissolve
        show remyapt at Position(xpos=0.0, xanchor='left', ypos=0, yanchor='top') with ease
        $ renpy.pause (0.5)
        show remy normal flip at Position(xpos = 0.2)
        show adine giggle b at Position (xpos = 0.8)
        with dissolve
        $ renpy.pause (0.5)

        Ad "Not at all. I’m sure the situation would be different for you, though."
        Ry shy flip "She has really sharp teeth for her age. I found that out the hard way when I played with her recently."
        Ad "Your poor belly must have felt the full force of the bite considering how thin your scales are there." #Uh, you sure you're up for the challenge of "Amely," Remy?
        Ry "It still hurts a little bit."
        c "Well, they say that experience is the best teacher."
        Ry normal flip "It most certainly is, even if the lessons aren’t exactly the kinds of lessons that you’d like to be taught."
        $ renpy.pause (1.0)
        Ad disappoint b "…and it looks like my shift starts soon. I guess I’ll have to take Amely back to the orphanage now if I still want to be on time."
        Ad normal b "It was nice talking to you for one last time, [player_name]. I’ll miss you."

        $ renpy.pause (0.5)
        show amely small at Position(xpos = 0.9) with easeinright
        $ renpy.pause (0.5)

        Ad giggle b "Let me know when you come back, alright? You still have that invitation to view an exclusive stunt flying practice, you know."
        c "I’ll definitely remember this time, I swear."
        Ad "Good! Well, I guess I’ll see you some other time. Say goodbye to [player_name], Amely."
        Am "Bye bye!"
        c "Goodbye, Adine. Bye bye, Amely!"
        Am "Yay! Human said bye bye back!"
        Ry smile flip "Goodbye, you two."

        $ renpy.pause (0.5)
        show adine giggle b flip
        show amely small flip
        with dissolve
        $ renpy.pause (0.5)
        hide adine
        hide amely
        with easeoutright
        $ renpy.pause (0.5)
        play sound "fx/door/doorclose.ogg"
        $ renpy.pause (1.0)
        show remy at center with ease
        show remy smile with dissolve
        $ renpy.pause (0.5)

        Ry shy "I’m guessing that you’d like to go now as well. I’m sure everybody back home is waiting for your return."

        menu:
            "Maybe, maybe not.":
                $ renpy.pause (0.5)

                Ry "Why the uncertainty?"
                c "Well, it’s not that anybody expects me to come back right now. I’m going out of my own free will to help everybody back home."
                Ry normal "I suppose that’s a fair point, considering we haven’t received an official demand from humanity since the whole debacle with Logan."


            "It’ll be for the best.":
                $ renpy.pause (0.5)

                Ry normal "I see. Well, it’s not like I can stop you. Your life is in your own hands, not somebody else’s."


            "I’m not so sure if I’m exactly wanted back home.":
                $ renpy.pause (0.5)

                Ry look "How so?"
                c "Let’s just say that the authorities might be upset if I leave my post as an ambassador."
                Ry normal "But you’re taking two generators with you, are you not? Wouldn’t that alone be more than enough for the officials back in your world to at least welcome you?"
                c "It would. I guess I’ll find out when I cross through the portal."
                Ry "Indeed."

        
        $ renpy.pause (1.5)
        Ry shy "..."
        $ renpy.pause (1.0)
        hide remy with dissolve
        $ renpy.pause (1.0)

        m "Remy slowly inched towards me with an expression mirroring a shy inner confidence on his face."
        $ renpy.pause (0.75)
        Ry shy b "I-I’m not sure when I’ll see you again, so I’d like you to have this." #Oh my goodness gracious it's actually happening! He's finally starting to move on!!!
        $ renpy.pause (0.75)
        m "Remy paused for a brief moment before undoing his tie. He looked at it wistfully, then handed it over to me with a slight smile."

        $ renpy.pause (1.0)
        show remy shy b with dissolvemed
        $ renpy.pause (1.0)

        Ry "Perhaps…{w=0.55} it's time for a change."
        c "Remy, are you sure you want to do this? I know how much that tie means to you, considering it’s one of the few things you still have left of Amelia."
        Ry "I think Amelia would be proud if I gave it to you instead. Her memory now lives on in you, even if you have never met her."
        Ry "You’re far too similar to Amelia for the dots to not align."
        Ry normal b "So please, [player_name]. I insist."
        $ renpy.pause (1.0)
        m "After thinking for a few moments, I took Remy’s tie and held it. On its own, it felt far  softer than I thought it would."
        $ renpy.pause (1.5)
        Ry shy b "Could you please wear it?"
        c "Of course."

        $ renpy.pause (1.0)
        show remy smile b with dissolve
        $ renpy.pause (1.0)

        m "I folded the large tie in a way that it would be able to comfortably fit me. After some struggle, I eventually managed to get it right. As I put the tie on, I could see Remy smiling proudly."
        $ renpy.pause (0.5)
        Ry "It looks really good on you, you know that?"
        c "Thanks, Remy. Honestly, I don’t really feel like I deserve this honour."
        Ry shy b "Trust me, you do. If Amelia was still here, she’d say the same."
        $ renpy.pause (0.85)
        Ry "I-I shouldn’t hold you for much longer, though. Besides, I need to go to a conference in a while anyway."
        $ renpy.pause (1.0)


        if kol_tlh_4B_success == False or kol_tlh_datecounter < 2:
            pass

        else:

            Ry "..."
            $ renpy.pause (1.0)
            Ry "You know how I said that maybe I should keep my tie off if I start to feel more adventurous without it?"

            menu:
                "Of course, Remy.":
                    $ renpy.pause (0.5)

                    Ry "Then..."

                    $ renpy.pause (0.5)
                    hide remy with dissolve
                    $ renpy.pause (0.5)

                    m "Remy slowly looked me in the eyes, as if looking for some sort of signal. As I approached his muzzle, Remy closed his eyes and made his move. Suddenly, I lost all awareness of everything around me as I solely focused on the moment."
                    m "Just like last time, Remy used quite a bit of tongue, but it didn’t matter to me anymore. All I could feel was warmth within my soul." #Still can't write romance for the life of me. Some things never change.
                    $ renpy.pause (0.5)
                    m "Eventually, we parted. Remy gave me a small lick on the nose before giving me a big grin."

                    $ renpy.pause (0.5)
                    show remy smile b with dissolve
                    $ renpy.pause (0.5)

                    Ry "Well, that was lovely."
                    c "It definitely was, that’s for sure."
                    $ renpy.pause (1.5)

                
                "I don’t think we should waste any more time.":
                    $ renpy.pause (0.5)

                    Ry "That’s completely understandable. I’ve probably kept you here long enough as is."
                    c "Unfortunately, yeah."
                    $ renpy.pause (1.5)
            
            
        Ry normal b "I guess this is goodbye, then. I only wish you the best of luck back home."
        Ry "And please, do stay safe. I don’t want to lose you to some kind of crime or accident."
        c "Don’t worry, Remy. Until we meet again."
        Ry "For sure."

        $ renpy.pause (0.5)
        scene black with fade
        stop music fadeout (3.0)
        $ renpy.pause (1.5)

        m "With nothing else to do, I went to the portal, feeling a sense of hope for our future back home and a sense of melancholy, knowing that it might be quite some time until I set foot here again."
        
        $ renpy.pause (1.5)
        scene np1x at Pan ((200,200), (450,100), 6.0) with dissolveslow
        $ renpy.pause (3.5)

        m "When I arrived, I saw that Bryce had been patiently sitting in the grass, guarding the two generators that I was supposed to take with me." #Because of *course* he would.

        $ renpy.pause (1.5)
        show bryce normal b with dissolve
        play music "mx/portal_kol.ogg"
        $ renpy.pause (1.0)

        Br "Hey. Need some help with these?"
        c "Sure. You can pass the second one through while the portal starts up."
        Br "Right."
        Br laugh b "You know, things should get pretty interesting now that you’re going away for a while."
        c "How so?"
        Br smirk b "For starters, Maverick has become a lot more relaxed as of late, even by his standards."
        Br brow b "He even said that you had a role in it."
        c "Interesting..."
        Br smirk b "Not budging that easily, huh? I guess I’ll just have to figure it out some other way." #Good luck. With that.
        Br normal b "Well, I could go on and on, but we both know that we have our own stuff to do. All I can do is wish you the best of luck in whatever you’ll be doing on the other side."
        c "Thanks, Bryce. I appreciate it."
        c "Do try to take it easy with the alcohol while I’m gone, alright?"
        Br stern b "Already making progress. It’s rough, but I’m managing."
        Br laugh b "Maybe I should start with my shipbuilding hobby again."
        c "If it’ll help you out, then please, do."
        Br normal b "Yeah, guess so."
        $ renpy.pause (0.5)
        Br "Now, should I start the portal up, or…"
        c "Thanks, Bryce. As your reward, I’ll try to make it to your next BBQ."
        Br smirk b "Don’t make promises that you know you can’t keep. We could just have one without you."
        Br laugh b "We’ll save some stuff for you this time, though. Don’t want you thinking that we didn’t even consider your absence."
        c "I appreciate your thoughtfulness."
        Br smirk b "You need to think of others to be able to be a police chief, you know."
        Br normal b "Oh, and nice tie. It looks good on you."
        c "Thanks. Remy gave it to me as a gift."
        Br brow b "I don’t think I’ve ever seen that klutz without his tie on. I’m sure it’ll be quite the sight next time I see the guy."
        Br normal b "But whatever. We’ve got work to do."

        $ renpy.pause (0.5)
        hide bryce with dissolve
        $ renpy.pause (0.5)
        play sound "fx/slide.ogg"
        queue sound "fx/tel.wav"
        $ renpy.pause (2.5)

        m "I picked one of the generators up and stood between the two pillars of the portal, hopefully for the last time for the time being. Bryce pushed the other generator alongside me before starting the portal’s routine."
        m "Soon, my sight became dizzy as I was transported back home. The last thing I saw before flashing lights overcame my vision was Bryce's figure giving me a small wave."

        $ renpy.pause (1.5)
        scene black with fade
        $ renpy.pause (9.5)
        stop sound fadeout (4.0)
        $ renpy.pause (1.5)
        scene city at Pan ((0, 360), (0, 0), 4.0) with dissolveslow
        $ renpy.pause (1.5)

        m "After what had felt like an eternity, I emerged from the other side of the portal. A quick glance at a few corners of my vision told me that things were well. Nothing looked as if it had degraded even further since the last time I set foot here."
        stop music fadeout (3.0)
        m "I started to slowly walk with one generator in my arms, hoping to find someone willing to help me with the other one."
        m "Luckily, I didn’t have to walk far before I saw a familiar face."

        $ renpy.pause (1.0)
        show logan surprised with dissolvemed #Coincidences are wacky in the land of writing.
        $ renpy.pause (0.5)
        play music "mx/stride_kol.ogg"

        Lg "Well, uh, this is–{w=0.95}{nw}"
        c "Unexpected?"
        Lg serious "Yeah. I thought you—{i}the ambassador of humanity{/i}—were still supposed to be doing ambassador stuff. Why are you here?"
        Lg "And why the hell do you have two generators with you?"
        c "We diverted the comet, Logan. We did it."

        $ renpy.pause (1.0)
        show logan normal with dissolvemed
        $ renpy.pause (0.5)

        m "Logan only smiled as a response, briefly looking down at the ground as he retreated to his thoughts. When he looked back up, I could see a spark of raw accomplishment behind his eyes."
        $ renpy.pause (0.75)
        Lg "Looks like you did your part like I asked you to. I’m proud of you, [player_name]."
        c "Thanks. Judging from everything that I can see so far, I’d say that you did your part as well."
        Lg smiling "Well, maybe this handy letter that I was supposed to send to you will confirm your suspicions."
        c "How convenient."
        Lg normal "Convenience had truly been revived in these hard times." #I also revived convenience because, well, it's convenient.

        $ renpy.pause (0.5)
        play sound "fx/envelope.wav"
        $ renpy.pause (0.5)
        nvl clear
        window show

        n "Dear [player_name],"
        n "Your contributions to humanity have been a resounding success. Many of our facilities and infrastructure will have a partial or full supply of power by the time you receive this letter. In addition, a large portion of those that were ill have made an astounding recovery, furthering our plans for a complete restoration."
        n "As for our food and water supplies, they are being worked on as well. Our food factory is currently undergoing renovations, and the purifiers at the water treatment plant are being repaired thanks to the valiant efforts of Logan and his crew."
        n "We wish you the best of luck with handling the trade agreement on the dragons’ side. Should you feel that you need anything, feel free to see me personally. I shall welcome you with open arms."
        n "-Sergeant Edmund"

        window hide
        nvl clear
        $ renpy.pause (1.0)

        Lg smiling "And now that you’re done, I can say this: welcome back, [player_name]. I missed you."

        menu:
            "Thanks for the warm welcome, Logan.":
                $ renpy.pause (0.5)

                Lg normal "Any time."

            
            "I wasn’t gone for that long.":
                $ renpy.pause (0.5)

                Lg annoyed "Trust me, when you’re constantly busy with work that may or may not determine the fate of everything you know and love, every second becomes way more noticeable."
                c "I guess I can see that, yeah."


            "What, are you going to give me a hug now?":
                $ renpy.pause (0.5)

                Lg normal "Oh please, I’d find it far more enjoyable to blow an airhorn in your ear to wake you up. Just like how one would get a slacker to start working."
                c "That would only work once, though. Afterwards, you wouldn’t be able to wake me up with the airhorn anymore. I'll learn."
                Lg smiling "Then I’ll just have to hit you on the head with said airhorn."
                $ renpy.pause (1.0)
                c "..."
                Lg normal "Just don’t be a slacker, and you’ll be good."
                c "(Because waking up at the crack of dawn is definitely considered a good time to start your day…)"


        $ renpy.pause (0.5)
        Lg annoyed "I’m guessing that you haven’t suddenly acquired super strength since we last met, have you?"
        c "Unfortunately not."
        Lg serious "Figured. Here, let me help you. We’ll take these back to my place."
        c "Lead the way, oh great leader."
        Lg normal "You know very well that we’re equals here, right? I am by no means your \"leader.\""
        c "If we’re equals, would that make you a slacker?"
        Lg smiling "Only if it makes you actually useful in repairing electronics."
        c "Touché."

        $ renpy.pause (0.5)
        hide logan with dissolve
        $ renpy.pause (0.5)

        m "Logan grabbed the generator at the portal and went ahead of me. I almost had to break into a sprint to catch up."

        $ renpy.pause (1.0)
        scene kolcitycentre at Pan((0,180),(0,180),3.0) with dissolve
        $ renpy.pause (1.5)

        m "While we went through the city, I saw several people looking at us with surprised faces, and several people that simply carried on with their day. Despite all of that, I could see that nobody looked hopeless."
        
        $ renpy.pause (2.25)
        scene kolloganout at Pan ((0, 0), (0, 250), 5.0) with dissolveslow
        stop music fadeout (3.0)
        $ renpy.pause (1.5)
        
        m "We eventually reached Logan’s house, standing as strong as ever."

        $ renpy.pause (0.5)
        play music "mx/couch_kol.ogg"
        show logan serious with dissolve
        $ renpy.pause (1.0)

        Lg "Right, just put these inside next to the others."
        c "Others?"
        Lg normal "Yeah. Others." #Why are you even surprised, MC?
        $ renpy.pause (1.0)
        m "Curious, I carefully went in ahead of Logan, cautious of the possibility of a bunch of valuable electronics laying around on the floor."
        
        $ renpy.pause (1.5)
        scene kolloganhouse at Pan ((0, 220), (0,360), 3.0) with dissolveslow
        $ renpy.pause (1.5)

        m "Surprisingly, everything seemed in order. There were a few piles here and there, sure, but everything looks far more organised since my last visit."
        $ renpy.pause (0.5)
        Lg serious "There, in the corner."
        m "I made my way to where Logan said and saw that there were several rough generators neatly packed together. I could only stare in shock at what I saw."

        $ renpy.pause (0.5)
        show logan normal with dissolve
        $ renpy.pause (0.5)

        Lg "At least put the generator down before gawking at what I’ve been doing as of late, please."
        $ renpy.pause (0.5)
        play sound "fx/metalbox.ogg"
        $ renpy.pause (1.25)
        Lg "Thank you."
        c "I didn’t expect this many, Logan. Do they all work?"
        Lg annoyed "Yes and no. They can generate power, sure, but they’re a bit finicky about it. Sometimes they’d work at full capacity; sometimes I needed to struggle for an hour to get the thing running for a few minutes at half capacity."
        Lg normal "Luckily, with those blueprints you got, things are slowly going better and better by the day."
        "???" "Hey Logan, would it be feasible to substitute this GC part with a combination of our different H-class parts?"
        
        $ renpy.pause (0.3)
        show logan normal flip with dissolve
        $ renpy.pause (0.5)

        Lg serious flip "No, Matthew. That part is unique to the draconic subclass, so we don’t have the resources right now to substitute it. Keep it as is until we either get more parts from the dragons or until we figure out how to reverse-engineer it."
        Lg "You {i}could{/i} send it to Chris, but I doubt that he’d appreciate you pestering him about it now."
        Mw "Got it, thanks. I’ll just leave it as is."

        $ renpy.pause (0.5)
        show logan serious with dissolve
        $ renpy.pause (0.5)

        c "Who was that?"
        Lg normal "A member of my team. Did you {i}really{/i} think I’d be able to do this much work on my own?"
        c "I mean, the letter you gave me did say that you had a team, so…"
        Lg annoyed "Yeah, guess that kinda spoiled it."
        Lg normal "Well, whatever. As you can see and hear, we made stuff, sorted stuff, tested stuff, and fixed stuff."
        Lg "And the best part? We only had a single case of somebody getting electrocuted!"

        menu:
            "That’s… the best part?":
                $ renpy.pause (0.5)

                Lg "Yep. Fun fact: the risk of electrocution is quite high when working with technology you haven't seen in many years, as well as when said technology is directly based on parts you don't even know how they work in the first place."
                c "Well, when you put it that way…"
                Lg "My point exactly."


            "Is the person safe?":
                $ renpy.pause (0.5)

                Lg "I mean, you’re still talking to me, so yeah."
                $ renpy.pause (0.75)
                c "…what happened, and why am I not surprised?"
                Lg smiling "Science happened, [player_name]."
                Lg normal "As for you not being surprised, well, I’m not you. You’ll have to find out for yourself why you’re not surprised. All I’m doing is my job." #Easy: you're a masochist.

            
            "You really need to implement stricter safety precautions.":
                $ renpy.pause (0.5)

                Lg annoyed "But that’s boring and I don’t like it. Sure, when it comes to my team, I make sure that they stay as safe as possible, but me?" #How are you not dead yet?
                Lg smiling "Well, you only live once. Better to live on the edge than to be satisfied with menial accomplishments."


        $ renpy.pause (0.5)
        Lg annoyed "So, since you’ve yet to answer my question, I’ll ask you again: why are you here, and how did you bring two generators with you?"
        c "I felt that I would be of more use here instead. Considering that dragonkind is focusing on recovering from the comet being redirected, they probably won’t be able to continue with the trade for a bit."
        c "It’ll be better for us all if I come back for a short time to work on whatever I can."
        c "Despite the dragons being in recovery, the council felt obligated to send two generators with me as an apology for taking so long to fully contribute to the trade as agreed."
        Lg thinking "Well, that’s really kind of them."
        Lg normal "It almost sounds familiar, to an extent." #*wink*
        c "Trust me, Logan; these are official gifts."
        Lg "Yeah, I'll trust you."
        $ renpy.pause (0.5)
        Lg "Now, how would you like to take a nice, relaxing stroll through the city? I think it’ll be good if we can catch up for a bit instead of chatting here in the middle of a bunch of stuff happening in the background."
        c "Sure."
        Lg "Great! Let’s get going, shall we? No point in wasting time, after all."
        c "That’s…{w=0.65} literally the point of a stroll."

        $ renpy.pause (1.0)
        Lg "..."
        $ renpy.pause (0.5)
        show logan annoyed with dissolve
        $ renpy.pause (1.5)
        Lg "..."
        $ renpy.pause (0.5)
        Lg "Damn, you’re right for once. Huh." #Woah, that, like, never happens.
        $ renpy.pause (0.5)
        hide logan with dissolve
        $ renpy.pause (0.5)
        stop music fadeout (3.0)

        m "Logan trailed off from his words and simply walked out of his house. I tried my best to hide my smug face as I followed after him."

        $ renpy.pause (1.5)
        scene kolloganout at Pan ((0, 360), (0,360), 3.0) with dissolveslow
        $ renpy.pause (1.5)
        play music "mx/exile_kol.ogg"
        $ renpy.pause (0.5)
        show logan normal with dissolve
        $ renpy.pause (0.5)

        Lg "So, where would you like to go?"
        c "I think the plaza should be a good place to hang out. It’s been some time since I’ve seen the hustle and bustle there."
        Lg "Alright, we can do that."

        $ renpy.pause (1.0)
        show kolcitycentre at Pan((0,180),(0,180),3.0) behind logan with dissolve
        $ renpy.pause (0.5)

        Lg "So tell me, how’s everything back in Dragonland?" #Yep, I'm using that name.
        c "Dragonland? Is {i}that{/i} what you’re calling it now?"
        Lg "Well, it’s better than constantly saying \"the land of the dragons\" or \"the dragons’ world.\" Dragonland is short, simple, and gets right to the point."
        c "I guess I can see where you’re coming from."
        $ renpy.pause (0.5)
        c "Well, as you can imagine, things are a bit messy. The grid is recovering, the council gained a new minister, I got a bunch of stuff, and life goes on as normal."
        
        $ renpy.pause (0.5)
        show logan annoyed with dissolve
        $ renpy.pause (2.0)

        Lg serious "…what do you mean you \"got a bunch of stuff?\" I mean, sure, I can see that you have a nerdy tie, but I doubt that’s what you meant."
        c "As a reward for my services, I got full citizenship, ownership of my apartment, a bunch of money, and a statue."
        Lg surprised "{i}Damn,{/i} that’s some nice stuff. I’m actually jealous of you now."
        c "I’m sure the council will be able to reward you as well in some way."
        Lg normal "I doubt they’d want to reward a nuisance. I mean, if you looked at what I did through the council’s eyes, all I did was put unnecessary stress on everyone involved."
        Lg annoyed "And if I made the information about what we did together public, I can’t say that it would look good for the both of us."
        Lg normal "So, I’ll just keep my mouth shut."
        $ renpy.pause (0.5)
        Lg annoyed "Now, what about that new minister?"
        c "The Minister of Human Affairs."
        Lg thinking "Ooo, fancy. Who’s the lucky dragon?"
        c "Remy."
        Lg annoyed "You mean that white dragon you wanted me to meet?"
        c "The one and only."
        Lg "It would make sense considering his involvement with you and, presumably, Reza. Good for him, then."
        $ renpy.pause (0.5)
        Lg "And Bryce? Is he holding up?"
        c "Well, Bryce is being Bryce. Not much else to say there."
        Lg normal "Heh, still chugging the bowls of beer, huh? Glad he still seems to be in such high spirits."
        c "You know, now that I think about it, you seem to always be quite interested in Bryce."

        $ renpy.pause (1.5)
        show logan serious with dissolve
        $ renpy.pause (0.5)

        Lg "How about you keep your mouth shut, alright?"
        c "Looks like I hit a nerve."
        $ renpy.pause (1.5)
        Lg "..." #I ship it.
        $ renpy.pause (0.5)
        Lg "…anyway, as you could clearly tell, things are good here. Not as good as Dragonland at this exact moment, sure, but far better than what it was. Nothing else I can really add, honestly."
        $ renpy.pause (0.5)
        Lg annoyed "No, that’s a lie."
        c "Oh?"
        $ renpy.pause (1.5)
        Lg "Our scouts made yet another interesting discovery. Apparently, a large group of people had been spotted heading towards us. From our reports, they seem to be travelling via broken motorcycles and on foot. The authorities are still deciding what we should do." #Because of course I'd like to shoehorn Martin into all of this.
        $ renpy.pause (0.5)
        Lg normal "We truly are living in a very, {i}very{/i} intriguing time."
        c "This group of people: is it public knowledge that they’re coming?"
        Lg serious "Of course not. All it takes is one person to think that a group of raiders is coming to cause mass hysteria. Trust me when I say that panic is the last thing that we need right now."
        Lg annoyed "Speaking of which, we should stop talking about that. We’re here."

        $ renpy.pause (1.5)
        scene kolcityplaza at Pan ((0, 180), (0, 180), 4.0) with dissolvemed #Not exactly fitting, but this was the closest that I could get.
        $ renpy.pause (2.0)

        m "As we approached the trading plaza, I could see several stalls where goods were being sold for specific resources. I could only stare with my mouth open as I saw just how busy it had been, how many people there were, and how much trading happened. "
        m "It must have been years since I’ve last seen any part of the city this busy."

        $ renpy.pause (0.5)
        show logan normal with dissolve
        $ renpy.pause (0.5)

        Lg "I’m grabbing myself something to eat. You want something?"

        menu:
            "I’ll pass.":
                $ renpy.pause (0.5)

                Lg "Come on, let me treat you! Consider it a celebration of what we did together."
                c "No thanks, Logan. I’m not really in the mood to eat something."
                Lg "Your loss."


            "Sure, I won’t mind.":
                $ renpy.pause (0.5)

                Lg "Nice. There’s a stall over in the corner that has some pretty great food. Definitely a must-try."
                c "And how are you going to pay for it? You don’t look like you have anything to trade with."
                Lg "I have an arrangement with the merchants here. The authorities will be able to provide some compensation in my stead, almost like how our ambassador statuses worked."
                c "I see."

                $ kol_tlh_snack_with_logan = True


        $ renpy.pause (0.5)
        m "Logan went to a nearby stall and stood in line. With nothing else to do, I figured that I might as well wait with him."
        $ renpy.pause (0.5)
        m "We talked about random nonsense as the line grew shorter and shorter. Eventually, our turn arrived."
        $ renpy.pause (1.0)

        Lg "Hey, Zack. One serving of sliced pork chops, please."
        Zk "As usual. Anything else?"

        if kol_tlh_snack_with_logan == True:

            Lg "Do yourself a favour and get the stir fry, [player_name]. The stuff is out of this world."
            c "Alright, I’m trusting you on this."
            Lg "One serving of stir-fry as well. That’ll be all."

        Zk "I’m guessing that this’ll go to the higher-ups like last time, Mr Privileged?"
        Lg "Yeah."

        if kol_tlh_snack_with_logan == True:
            m "The merchant only nodded and started to prepare our food at lightning speed. It hardly felt as if any time had passed before our food was ready."

        else:
            m "The merchant only nodded and started to prepare Logan's food at lightning speed. It hardly felt as if any time had passed before the food was ready."

        $ renpy.pause (0.5)
        Zk "Good day to ya, Logan."
        Lg "Thanks. Same to you."
        $ renpy.pause (1.0)
        Lg "There’s an open seat for us over there. Follow me."

        $ renpy.pause (0.5)
        hide logan with dissolve
        $ renpy.pause (1.5)
        show kolcityplaza at Pan ((0, 360), (0, 360), 4.0) with ease
        $ renpy.pause (0.5)
        show logan normal with dissolve
        $ renpy.pause (1.0)

        if kol_tlh_snack_with_logan == True:

            Lg "There we go. Dig in."
            $ renpy.pause (1.0)
            m "With curiosity, I tried the stir-fry that Logan spoke so highly of. After the first bite, an explosion of savouriness filled the corners of my mouth as the vegetables swirled around in harmony."
            m "The first bite quickly led to the second, and then the third. Somehow, I managed to eat my entire bowl before Logan was halfway done with his meal. In awkward shame, I silently sat, waiting for Logan to finish."
            m "Fortunately, the sense of embarrassment didn’t last long, as Logan stopped eating a few moments after I was done."

        else:

            Lg "There we go. Meal time."
            $ renpy.pause (1.0)
            m "Logan casually started to eat his meal while I sat in awkward silence, staring at how busy the city plaza was today."
            $ renpy.pause (1.0)
            m "Fortunately, the awkward feeling didn't last as Logan stopped eating for a brief moment."


        $ renpy.pause (1.0)
        Lg annoyed "I think I’ll save this for later. Better to have a snack saved for when you’re working."

        if kol_tlh_snack_with_logan == True:
            
            Lg normal "And, by the looks of it, you agree with my statement about that stir-fry."
            c "For sure. It was amazing!"
            Lg smiling "Yeah, I know. That’s why I recommended it in the first place."


        $ renpy.pause (1.5)
        Lg serious "You know, I’m a bit curious about something."
        c "What about?"
        Lg "It’s been obvious that the both of us went through the journey of a lifetime, yet it still feels to me like it’s only just beginning. The thing is, so much can happen between now and who-knows-when."
        Lg "So, to put it in simpler terms, what do you think the universe has in store for us?"

        menu:
            "We’ll almost fully recover from the solar flare with the help of the dragons.":
                $ renpy.pause (0.5)

                Lg annoyed "An optimistic future. Perhaps, even a realistic one. For as long as we can strengthen our relationships, we might very well live the life that we once did."


            "Dragons and humans will live in each other’s worlds.":
                $ renpy.pause (0.5)

                Lg annoyed "Hmmmm..."
                $ renpy.pause (0.5)
                Lg "It could be possible, but unlikely in the near future. We know too little about dragonkind to be able to support them in our current state. The way I see it, cultural exchange programmes are far more likely than full-on immigration programs."

            
            "We’re only delaying our inevitable collapse.":
                $ renpy.pause (0.5)

                Lg annoyed "And what makes you say that?"
                c "All it takes is a large group of raiders or the dragons suddenly turning on us to throw us back to square one. Perhaps, even worse."
                Lg "That’s an extremely pessimistic view, not to mention entirely unrealistic. Why would the dragons turn on us with how their entire society had been founded by human principles, not to mention the entire comet thing?"
                Lg "The worst I can see happening is a wave of dragons coming into our world and our resources being put under severe strain, causing internal fighting between the two civilisations." #Foreshadowing?

            
            "I’m not sure.":
                $ renpy.pause (0.5)

                Lg annoyed "Perhaps it’s better not to think about the future. After all, knowing what’s ahead of you would only ruin the surprise, no?"
                

        c "Why would you ask such a question, Logan?"
        Lg smiling "Just curious. Nothing more, nothing less." #Logan gives a somewhat philosophical answer, then literally just goes "Because yes." Amazing. XD
        $ renpy.pause (0.5)
        Lg normal "And would look at the time. It’s work-o’-clock! Let’s get going, shall we?"
        $ renpy.pause (1.5)
        Lg "You can help me out by going through the documentation that my team wrote and compare it to the blueprints you borrowed from the production facility way back."
        Lg smiling "And don’t you start complaining, you hear me? You wanted to come here to help, so you’ll bloody help."
        $ renpy.pause (0.75)
        c "I was wrong back then. You haven’t changed one bit since we started working together so long ago."
        Lg normal "Perhaps, perhaps not. Who else can say that I changed except for me?"
        c "A fair point."
        Lg "Now, off we go. If you don’t hurry up, I’ll have to drag you all the way back to my place."
        c "And what if my limbs are sore? Will you stop to pick me up again?"

        stop music fadeout (7.5)
        $ renpy.pause (0.5)
        show logan smiling with dissolve
        $ renpy.pause (0.5)
        m "Logan laughed at my response, then looked at me with a wide grin."
        $ renpy.pause (1.0)

        Lg "Oh no, not again. If your muscles don’t want to work anymore, then there’s always the possibility of an ESTIM."
        c "There’s no way you have something that could stimulate my muscles with electricity to the point of forcing me to walk."
        Lg normal "Would you want to find out?" #Y'know, just passive-aggressive things.
        $ renpy.pause (2.5)
        c "...no."
        play music "mx/saviour_kol.ogg" fadein (2.0)
        Lg "Good. Let’s go for real this time. The day is long, and there is much to do."
        c "Alright. Lead the way."

        $ persistent.kol_tlh_alternate_EndingA_done = "A (The Last Dragon Route)"
        $ kol_tlh_endingA_alternate = True

        jump kol_tlh_credits



        







            




label kol_tlh_endingA_continued:

$ renpy.pause (0.5)
stop music fadeout (2.0)
$ renpy.pause (2.5)
play music "mx/hope_kol.ogg" fadein (3.0) #I used it because I wanted to whether it fits or not (it doesn't, not really) 

Ry shy dk "Speaking of, I’ve been meaning to tell you something that you might be interested in hearing."
c "Oh?"
Ry "After quite a long time of thinking about it, I decided to try my best to give Amely a proper home." #IT'S HAPPENING!!!
c "That’s really great to hear, Remy. After everything, it appears that you will be able to fulfil your dream of starting a family!"
Ry normal dk "I suppose you’re right in that regard. I just never thought that this was how everything would turn out."
Ry smile dk "I’m not complaining, though."
Ry normal dk "We’re sorting the adoption papers out in the next few days, and if we’re lucky, Amely will have a proper home by the end of next week."
Ry shy dk "I just hope I don’t mess up my second chance like my first one."
c "I don’t think Adine would even let you think about messing up in the first place."
Ry smile dk "You do have a point there."
Ry normal dk "I’m glad that Adine helped me get used to the children at the orphanage. It taught me a thing or two about how to raise a child and how to make them feel at ease."

if kol_tlh_4B_success == False or kol_tlh_datecounter < 2:
    Ry "But, those are all things that I can worry about when the time officially comes."

else:
    Ry "But, those are all things that I can worry about when the time officially comes. For now…"

    $ renpy.pause (0.5)
    hide remy with dissolve
    $ renpy.pause (0.5)

    m "Remy stretched one of his wings and wrapped it around me, shielding me from the cold wind that started to blow. I felt a surreal sense of calmness, wanting to simply fall asleep in Remy’s embrace."

    $ renpy.pause (0.5)
    show remy shy dk with dissolve
    $ renpy.pause (0.5)

    c "I should be careful not to fall asleep right now. This is pretty comfortable, you know."
    Ry "Is that so?"
    c "Yeah, it is so."
    Ry smile dk "If you fall asleep, I'll have to carry back to your apartment again, though I'm sure you wouldn't mind that."
    c "Not in the slightest."


$ renpy.pause (2.0)
Ry shy dk "I know I must be bothering you with a bunch of questions tonight, but would you mind if I asked another one?"
c "You haven’t bothered me at all so far, so I doubt the next question would do anything to change that fact."
Ry "I see."
Ry "Well…{w=0.45} why did you speak out against Emera like that back when we redirected the comet?"
c "Isn’t it obvious by now?"
Ry "I’m afraid not, assuming that there’s some deeper meaning behind all of this that I’m missing."
c "It’s because I don’t want you to suffer. I’m not letting anybody degrade your spirit in any way if I can help it. After spending so much time with Emera, you’ve gotten used to her sharp words."
c "I want to change that. You’re as much a person as anybody else. Why should you go through so much ridicule for trying to do your job \"in a position you weren’t suited for\" in the first place?"
c "I believe that anyone can do any task if they put their heart and soul into it. Stopping Emera from bullying you is the first step in reigniting that passion within you."
c "Do you understand, Remy?"

$ renpy.pause (0.5)
show remy normal dk with dissolve
$ renpy.pause (0.5)

Ry "I do,{w=0.35} and I thank you for your effort."
$ renpy.pause (1.0)
Ry shy dk "I'm starting to wonder just how many times I've repeated myself by now. I’m sounding like a broken record, aren’t I?"

menu:
    "I’m sounding like a broken record, aren’t I?":
        $ renpy.pause (0.5)

        Ry smile dk "Oh, shush."

    "Not at all. If anything, you’re just emphasising your gratitude.":
        $ renpy.pause (0.5)

        Ry smile dk "I suppose that’s one way of looking at it, even if it could sound irritating to some."

    "Broken records still play music, no?":
        $ renpy.pause (0.5)

        Ry "I-I..."
        $ renpy.pause (1.0)
        Ry smile dk "...I guess they do."


$ renpy.pause (1.5)
Ry normal dk "You look pretty tired, [player_name]. Would you like to take a small nap?"
c "You know, that doesn’t sound like that bad of an idea."
Ry "Well, make yourself comfortable. I’ll just move slightly so that you can have more space."
c "I don’t think I can get more comfortable than I already am. I mean, I have a soft, warm pillow and a blanket. What more do I need?"
Ry smile dk "How about this?"

$ renpy.pause (0.5)
hide remy with dissolve
$ renpy.pause (0.5)

m "Remy lowered his neck and held his muzzle close to my face. With a shy expression, he moved in and gave me a light kiss while squeezing me tighter with his wing."

$ renpy.pause (0.5)
show remy smile dk with dissolve
$ renpy.pause (0.5)

c "You're full of surprises, you know."
Ry shy dk "I just figured that you might want a good night’s kiss before sleeping, that's all."
c "Thanks, Remy."
Ry smile dk "I'm glad to be of service."

$ renpy.pause (0.5)
scene black with dissolvemed
$ renpy.pause (1.0)

m "It wasn’t long before I slowly started to drift off to sleep. As my waking mind slowly faded away, the last thing that I could see was a great smile on Remy’s face, and a gleeful tear rolling down his eye." #Yes, I ended both my mods in pretty much the same way. Whatcha gonna do about it? :)

if kol_tlh_false_endingA_1 == True:
    $ persistent.kol_tlh_EndingA_done = "A (False Route 1)"
else:
    $ persistent.kol_tlh_EndingA_done = "A"

$ kol_tlh_endingA = True

jump kol_tlh_credits









#===========================================================
#-----------------------------------------------------------
#===========================================================




label kol_tlh_credits:

$ renpy.pause (1.0)
scene black with dissolveslow
stop sound fadeout (2.0)
$ renpy.pause (4.0)

$ _game_menu_screen = None
$ renpy.block_rollback()

show extra1 at Pan ((450, 0), (540,0), 25.0)
show koltlhcredits1 at right
with dissolvemed
$ renpy.pause (10.0)
show black2 at right with dissolvemed
show koltlhcredits2 at right
with dissolvemed

$ renpy.pause (15.0) #There, tidied your code for you, MBS.
scene black with dissolvemed

show varadead at Pan((520, 0), (0, 326), 20.0)
show credits1 at left
with dissolvemed
$ renpy.pause (8.0)
show black2 at left with dissolvemed
show credits2 at left with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed

show remysad at Pan ((750, 326), (1430, 0), 25.0)
show credits3 at right
with dissolvemed
$ renpy.pause (8.0)
show black2 at right with dissolvemed
show credits4 at right with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed

show oranged at Pan ((-350, 326), (-850, 100), 20.0)
show credits5 at left
with dissolvemed
$ renpy.pause (8.0)
show black2 at left with dissolvemed
show credits6 at left with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed

show cgspill at Pan((0, 90), (250, 184), 20.0)
show credits7 at right
with dissolvemed
$ renpy.pause (8.0)
show black2 at right with dissolvemed
show credits8 at right with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed

show cg1 at Position(xpos=0.8, xanchor='center')
show credits9 at left
with dissolvemed
$ renpy.pause (8.0)
show black2 at left with dissolvemed
show credits10 at left with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed
scene logo with dissolvemed
$ renpy.pause (8.5)
scene black with dissolvemed

stop sound fadeout 1.0
stop music fadeout (4.0)

$ renpy.pause (4.0)


play sound "fx/system3.wav"

if kol_tlh_endingA == True:
    s "Ending achieved: [[A]ge of Collaboration, or Ending A for short."
    play sound "fx/system.wav"
    s "Congratulations for getting the best possible ending for The Last Hope! Very interesting times lay ahead for you, Ambassador."



elif kol_tlh_endingA_alternate == True:
    s "Ending achieved: [[A]mending Intuition, or the alternate route for Ending A."
    play sound "fx/system.wav"
    s "Congratulations for getting the best possible ending for The Last Hope! I wonder if that large group of people that Logan was talking about would help your city recover..."

elif kol_tlh_endingB == True:
    s "Ending achieved: [[B]lessed by Dragonkind, or Ending B for short."
    play sound "fx/system.wav"
    s "Congratulations for getting the good ending for The Last Hope! You and Remy surely have been spoiled thanks to your contributions, haven't you two?"

elif kol_tlh_endingC == True:
    s "Ending achieved: [[C]hanged with Experimentation, or Ending C for short."
    play sound "fx/system.wav"
    s "Congratulations for getting the neutral ending for The Last Hope! Maybe it's best not to think about what Izumi said."

    if persistent.kol_tld_endingc == True:
        s "Besides, she seemed very serious about her statement about not wanting you to \"find the truth.\""

elif kol_tlh_endingD == True:
    s "Ending achieved: [[D]windling of Humanity, or Ending D for short."
    play sound "fx/system3.wav"
    s "You have now seen The Last Hope's bad ending. At least the dragons are safe."

elif kol_tlh_endingE == True:
    s "Ending achieved: [[E]ra’s End, or Ending E for short."
    play sound "fx/system3.wav"
    s "You have now seen The Last Hope's worst possible ending."
    $ renpy.pause (1.0)
    play sound "fx/system3.wav"
    s "..."
    $ renpy.pause (1.0)
    play sound "fx/system3.wav"
    s "Try not to wonder about the dragons' last moments or how your city crumbled, please. It will only hurt your next attempt."


$ renpy.pause (2.0)
play sound "fx/system3.wav"
s "All mod endings seen so far: [persistent.kol_tlh_EndingA_done], [persistent.kol_tlh_alternate_EndingA_done], [persistent.kol_tlh_EndingB_done], [persistent.kol_tlh_EndingC_done], [persistent.kol_tlh_EndingD_done], [persistent.kol_tlh_EndingE_done]"
$ renpy.pause (0.5)

if persistent.kol_tlh_EndingB_done == "B" and persistent.kol_tlh_EndingC_done == "C" and persistent.kol_tlh_EndingD_done == "D" and persistent.kol_tlh_EndingE_done == "E" and persistent.kol_tlh_EndingA_done == "A" and persistent.kol_tlh_alternate_EndingA_done == "A (The Last Dragon Route)":
    
    play sound "fx/system3.wav"
    s "Interesting. It seems that you have completed all endings of this mod."
    $ renpy.pause (0.5)
    play sound "fx/system3.wav"
    s "Would you like to reset your progress?"

    menu:
        "Yes.":
            $ renpy.pause (0.5)
            play sound "fx/system3.wav"
            s "Very well..."
            $ renpy.pause (1.5)

            $ persistent.kol_tlh_EndingA_done = "..."
            $ persistent.kol_tlh_alternate_EndingA_done = "..."
            $ persistent.kol_tlh_EndingB_done = "..."
            $ persistent.kol_tlh_EndingC_done = "..."
            $ persistent.kol_tlh_EndingD_done = "..."
            $ persistent.kol_tlh_EndingE_done = "..."
            $ persistent.kol_tlh_badendingcheck = False
            $ persistent.kol_tlh_goodendingcheck = False

            $ persistent.kol_tlh_chapter1A_skip = False
            $ persistent.kol_tlh_chapter1B_skip = False
            $ persistent.kol_tlh_chapter2A_skip = False
            $ persistent.kol_tlh_chapter2B_skip = False
            $ persistent.kol_tlh_chapter3A_skip = False
            $ persistent.kol_tlh_chapter3A_5_skip = False
            $ persistent.kol_tlh_chapter3B_skip = False
            $ persistent.kol_tlh_chapter4A_skip = False
            $ persistent.kol_tlh_chapter4A_5_skip = False
            $ persistent.kol_tlh_chapter4B_skip = False

            play sound "fx/system3.wav"
            s "Reset has been successful. Have a good day."

            jump ml_main_menu


        "No.":
            $ renpy.pause (0.5)
            play sound "fx/system3.wav"
            s "Very well."

            jump ml_main_menu


else:

    jump ml_main_menu
