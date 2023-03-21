label tlh_Chapter4A:

$ save_name = (_("TLH - Chapter 4A"))

$ renpy.pause (3.0)
scene o4 at Pan((0, 0), (0, 250), 5.0) with dissolveslow
$ renpy.pause (3.0)

m "A new day, a new opportunity. As I slowly gathered my bearings, my mind started to wander about what was happening back home. I also wondered what had happened to Logan."
m "Since he didn’t come to get me the night of his supposed plan, something must have gone wrong on his end. The warning he gave me about the police being busy should he not knock at my door also concerned me. Just what did he actually do?"

if kol_tlh_endingA_route == True:
    m "The authorities must really be keeping him busy back home with all the parts he brought through. It’s been a few days since I’ve heard any news from the other side. Perhaps the authorities had him assigned to testing all the old parts that Logan told me about."
elif kol_tlh_tld_crossover == True:
    m "The authorities must really be keeping him busy back home with all the parts we brought through. It’s been a few days since I’ve heard any news from the other side. I’m guessing that the energy reserves just haven’t reached a stable enough level for Logan to come back."

if kol_tlh_tld_crossover == True:
    m "Regardless, with him away, I need to do the best that I can to uphold the trade agreement between humanity and dragonkind now that Logan has essentially made humanity’s ultimatum irrelevant, just like how he asked of me."
else:
    m "Regardless, with him away, I need to do the best that I can to uphold the trade agreement between humanity and dragonkind now that Logan has essentially made humanity’s ultimatum irrelevant."

$ renpy.pause (1.0)
play sound "fx/door/doorbell.wav"
$ renpy.pause (1.0)
c "On my way!"
$ renpy.pause (1.0)

if persistent.kol_tlh_chapter4A_skip:
    $ renpy.pause (1.75)
    c "(Wait, haven't I seen this before at some point?)"

    menu:
        s "(Do you want to skip forward?)"

        "Yes.":
            $ renpy.notify("The trial was successful in your favour; Maverick remains a police officer.")
            $ kol_tlh_mavstillofficer = True

            scene black with fade
            jump tlh_Chapter4A_skip

        "No.":
            pass


play music "mx/hollow_kol.ogg" fadein (2.0)
play sound "fx/door/door_open.wav"
$ renpy.pause (2.0)
show remy normal with easeinright
$ renpy.pause (1.5)

c "Remy?"
Ry "Good morning, [player_name]. I’m guessing that you weren’t expecting me to be the one to show up to your apartment."

if kol_tlh_bryce_escort == True:
    c "It’s certainly a surprise, I’ll give you that. Where’s Bryce?"
else:
    c "It’s certainly a surprise, I’ll give you that. Where’s Sebastian?"

Ry shy "I’m afraid that you most likely won’t see any of the police officers today. It’s a bit chaotic at the police station currently."
Ry "Besides, I was sent directly by Emera to come get you as soon as you were available."
c "What’s happening at the police office, then? If everybody has to be present, then I can’t imagine that it would be good."
Ry look "You’re right."
$ renpy.pause (0.5)
Ry "From what I’ve heard, it has something to do with Maverick."
c "Oh..."
Ry "I’m guessing it has to do with Maverick killing Reza back in the underground facility. I can’t think of anything else that it could be about." #If only he knew about the forged report. Now *that* would be a mess for the council.
c "So, Bryce is currently dealing with Maverick?"
Ry "This is just a theory of mine, though. You would have to hear from Bryce himself if you want the full story."
Ry normal "But that’s for another time. Are you ready to go?"
c "Yeah."
Ry "Alright. After you."

$ renpy.pause (0.5)
scene black with fade
play sound "fx/steps/clean2.wav"
$ renpy.pause (0.5)

m "We walked outside my apartment into the all-too-familiar town, hastily making our way to Emera’s office. I looked at Remy occasionally, noticing that he really didn’t seem like his usual self, desperately trying to hide whatever was on his mind."

$ renpy.pause (1.5)
scene buildingoutside at Pan((0, 0), (0, 0), 0.0) with dissolvemed
$ renpy.pause (0.5)

m "It wasn’t long before we arrived at the outside building. Remy led me through the hallways straight to Emera’s office. A feeling of mild curiosity started to rise within me as I wondered what the latest reports from the council were."

$ renpy.pause (1.5)
show corridor with dissolvemed
$ renpy.pause (1.75)
play sound "fx/knocking1.ogg"
$ renpy.pause (2.0)
Em "Come in, please."
$ renpy.pause (1.0)
play sound "fx/door/door_open.wav"
$ renpy.pause (1.0)
scene emeraroom at Pan ((0, 0), (0, 180), 5.0) with dissolveslow
$ renpy.pause (2.5)

m "Emera sat by her desk, slowly filling out heaps and heaps of paperwork. She raised her head when she heard the door open and looked at us with a slight expression of gratitude."

show emera normal at Position(xpos = 0.8) with dissolve
$ renpy.pause (1.0)
show remy normal flip at Position(xpos = 0.2) with easeinleft

Em ques "Ah, the two of you have arrived. I didn’t expect your visit to be so early in the day, [player_name]." #Bruh you asked Remy to get the MC as early as possible.
Em frown "Thank you for making haste, Remy. I'm happy to see you still doing {i}something{/i} right for once."
show remy shy flip with dissolve
Em normal "I’m really not in the mood to fill out paperwork right now, so seeing you two just as I was about to start makes me filled with joy."
Em "But I digress. As you know, there are more important matters to discuss."
Ry look flip "I’ll make my way–{w=0.8}{nw}"
Em frown "No, Remy. You will stay for this meeting, as some of the information that will be discussed here will be relevant to your research."
$ renpy.pause (0.5)
Ry look flip "Yes, Emera."
Em "Now, on to our business. We have reviewed and implemented your idea, [player_name]. It seems that it’s already turning in results, as our power reserves had increased tenfold since we issued the call."
Em ques "If we include any generators from the underground facility, we will be able to successfully redirect the comet should our capacity increase by its current rate."
c "That’s good to hear."
Ry look flip "My apologies for interrupting, Emera. I have a fairly important question to ask."
Em normal "No need to apologise. You are a part of this meeting, after all." #But you are a condescending bastard, so of course Remy had to apologise beforehand. Trauma kinda does that.
Ry "What would happen in the event that our main sources of power fail?"
Em frown "We would then have to resort to the emergency supply."
c "Emergency supply?"
Em "We have stores of power that could help us in the event that the power grid were to fail. It would give us enough time to repair whatever went wrong without society itself being affected too much."
Em "Should the generators fail, we’ll have to resort to that as our backup. The problem with this, however, is that we won’t have any power left in our grid after the comet has been redirected. Chaos would ensue in every city until we'd recovered enough from our energy expenditures."
Em "I severely hope that we won’t have to resort to it." #Foreshadowing!
c "I see. Any further updates on the situation?"
Em "Not necessarily. Remy here will continue with his research on the best approach to redirecting the comet while we charge our power capacity in preparation for the comet."

show remy shy flip with dissolve

Em ques "If you have anything to suggest, then please, go ahead."
c "Not a suggestion, but news."
stop music fadeout (2.0)
Em normal "Oh?"
c "Humanity had reconsidered their ultimatum. Things are far too desperate over there to simply give up the trade. They have extended their deadline."
Em frown "And where have you heard this?"
$ renpy.pause (0.5)
c "(Uh...)"
$ renpy.pause (1.5)
play music "mx/decay_kol.ogg" fadein (1.0)
c "After Logan went away, I received news detailing humanity’s reconsideration."

if kol_tlh_tld_crossover == True:
    c "In addition, Logan will soon be making a return to fill Reza’s place."

Em "I was more referring to a source, Ambassador [player_name]."
$ renpy.pause (3.0)
c "...I received a short letter recently. It’s somewhere in my apartment." #Tell me your sweet little lies~
Em "Forgive me, but I don’t understand. The reason why Ambasador Logan was sent through the portal was to prevent the constant sending of letters to preserve humanity’s power supplies, correct?"

if kol_tlh_tld_crossover == True:
    Em "If Ambassador Logan is making a return, why would humanity waste the energy required to send the letter through?"

Em "On top of that, if humanity really did decide to extend their deadline, then why didn’t they use that deadline instead of the initial one?"

menu:
    "I can’t say how the authorities operate.":
        c "The way our leaders back at home worked was always a mystery to me. I unfortunately cannot give you a straight and easy answer, Minister."
        c "They simply do what they want when they think it’s the correct time to do so."

    "Perhaps everything was staged from the start?":
        c "Maybe the authorities wanted to send a more serious message the first time as a way of intimidating everyone, or maybe as some sort of bluff? After all, if the initial deadline was short, don’t you think that dragonkind would have to act sooner?"
        
        if kol_tlh_tld_crossover == True:
            c "As for Logan being sent through again, maybe it’s to give their initial bluff some sort of legitimacy, with this one being the more serious attempt for humanity to get what they want."

    "The situation simply could have changed.":
        
        if kol_tlh_tld_crossover == True:
            c "The authorities back home always acted in the moment, with only a few of them actually planning for our long-term future. I’m guessing that the situation changed enough back home to warrant extending the ultimatum’s deadline and sending Logan back through again."
        else:
            c "The authorities back home always acted in the moment, with only a few of them actually planning for our long-term future. I’m guessing that the situation changed enough back home to warrant extending the ultimatum’s deadline."

        c "It would certainly explain why humanity decided to use up more of their energy supply."

Em "I see." #So, to counter Emera's excellent arguments, the MC just says "Duh, I dunno." What an ambassador.
$ renpy.pause (1.5)
Em normal "Then I will have to inform the rest of the council in our next meeting that the trade between humanity and dragonkind is still ongoing. By how much is the deadline extended?"
c "Long enough for us to redirect the comet. You can worry about our owed generators after that."
Em "So be it."
Em ques "Remy, how far have you progressed with your research?"
Ry normal flip "I should be able to present my findings tomorrow."
Em "Good. Now, at least try not to ruin your research when you present it to the council tomorrow. I’d rather not have to present torn and scrunched-up scrolls."
Ry shy flip "Yes, Emera."
Em "And on top of that, gather up all of humanity’s PDAs and put them back where they were now that the trade is continuing."
Ry "Of course."
Em normal "Then you are dismissed."

$ renpy.pause (0.5)
show remy normal with dissolve
hide remy with easeoutleft
$ renpy.pause (0.5)
show emera at center with ease
show emera ques with dissolve
$ renpy.pause (0.5)

if kol_tlh_tld_crossover == True:
    Em "Now back to you, ambassador. Since Logan is no longer here, I have ordered that you no longer need to be escorted at all times. Should Logan return, however, this matter will be taken into reconsideration."
else:
    Em "Now back to you, ambassador. Since Logan is no longer here, I have ordered that you no longer need to be escorted at all times."

c "Thank you."
Em normal "If you have anything to say, then do so now."
c "Nothing."
Em "So be it. Have a good day, Ambassador [player_name]."

$ renpy.pause (0.5)
hide emera with dissolve
$ renpy.pause (0.5)

m "Emera went back to her paperwork while I left her office, glad that I now have the rest of the day to look forward to."

$ renpy.pause (1.0)
show corridor with dissolvemed
$ renpy.pause (1.75)
scene buildingoutside at Pan((0, 0), (0, 0), 0.0) with dissolvemed
$ renpy.pause (0.75)

m "I made my way through the halls until I reached the outside world again, taking a deep breath of fresh air."
stop music fadeout (5.0)
m "Yet, my mind didn’t seem to relax as easily as my body had. For some unknown reason, I felt that there was something hiding beneath Emera’s words, remaining unsaid throughout our meeting."
m "Was my mind simply being irrational, or was there truly some valid sense of suspicion? And if so, then at what? Or, who?"

scene black with fade
m "Wishing to distract myself from this feeling of unease, I decided to visit the police station to see what all the fuss was about. Remy would be too busy right now with all of Emera’s orders."
$ renpy.pause (1.5)
scene town1 with dissolve
$ renpy.pause (1.5)
m "Strangely, the streets felt anxious as I made my way through the town. Everybody around me seemed to be more tense, with the occasional eye glancing at me with a feeling of uncertain hope. At least, that’s what I could gather from the several passers-by."
$ renpy.pause (3.0)
scene koloutisdepolice at Pan ((0, 0), (0, 0), 4.0) with dissolve
$ renpy.pause (2.0)
scene office at Pan ((128, 250), (0, 250), 3.0) with dissolveslow

m "Upon entering the police station, I noticed several officers gathered in various locations. Some of them, like Sebastian sitting with his head in his hands, I recognised. Others I did not, such as a blueish grey dragon with pinkish frills looking worryingly out towards the crowd." #ECK Naomi made a cameo?! In this mod?!?!?
m "It didn’t take long for someone to take notice of me."

$ renpy.pause (0.5)
show bryce stern b with dissolvemed
$ renpy.pause (1.5)
play music "mx/dramatic.ogg"

Br "This isn’t the best time for you to be here, [player_name]."
c "Why?"
Mv nice "Why shoo someone who might be of help, Chief?"
Br "Not now, Maverick."
Br "Just…{w=0.4} look, things are a mess right now. You’d have to come back at another time if you want to have a chat."
$ renpy.pause (1.25)

if kol_tlh_endingA_route == True:
    c "This is about Maverick’s actions, isn’t it? Both Reza’s death and the report."
    Br "Yes. I’ve already reported it to Emera, but sadly she is too caught up with other more serious affairs, as you know. She just didn’t have the time to deal with Maverick, even if Reza’s death is technically under her jurisdiction."
    Br "So, she gave me full authority to deal with this situation. I’ve called for the entire force to be here for the purpose of us coming up with a solution for Maverick."
    Br "There’s just no way in hell that I’ll be able to make such an important decision on my own without feeling biassed."
    Br sad b "Never in my entire time as a police officer had I seen corruption among the force, and never as a chief did I have to deal with it. And with Maverick being the culprit like how we found out the other day? It’s rough."
    $ renpy.pause (1.25)
    Br stern b "But...{w=0.5} I shouldn't rely on emotions right now. This is far too crucial for that."
    c "Then why {i}do{/i} you have to deal with it? Aren’t there judges responsible for handling Maverick’s case?"
    Br "Things are a bit different here when it comes to the police force. The council will have to manage a criminal offence by a police officer directly. Usually, the council sends the police officer in question for trial. Sometimes, under extremely specific circumstances, they issue a sentence themselves."
    Br "But in this case, I was given direct authority to deal with Maverick. Something like this almost never happens. I think I've heard of something like this happen around twice in the last century." #Oddly specific. And, uh, how do you know this, Bryce? Why are you telling this to the MC?
    Br sad b "Do you now know why I can’t manage this all on my own? It’s just too much."
    $ renpy.pause (2.0)
    Br stern b "Please leave, [player_name]. I don’t want you of all people to sink into this mess of a situation."

else:
    c "This is about Maverick killing Reza, isn’t it?"
    Br "If only it were as simple as that. We wouldn’t be having a crisis if it was {i}only{/i} about Maverick killing Reza."
    Br "I had a talk with Logan before he went away. Ever since he came to our world and said that a feral dragon killed Reza, I had my suspicions about something being misinterpreted."
    Br "Though, I’ve figured out from Logan that humanity believed that a random feral dragon just showed up and killed Reza. I know you won’t have any reason to lie to humanity despite your relationship with Maverick, so you’re out of the picture."
    Br "Sebastian wouldn’t have been responsible, as he directly oversaw you writing your report. He would have informed me of anything suspicious."
    Br "So, who bloody else could hide Maverick’s actions than Maverick himself? Somehow, he managed to get your report in his hands and forged it to hide his own back."
    Br sad b "Never once had I seen corruption in this force, [player_name]. Not once. And having Maverick be the one to do it, the friend I’ve had for so many years?"
    $ renpy.pause (3.0)
    c "I'm sorry, Bryce."
    Br "I'm sorry for my sake as well." #Yep, he's on the verge of breaking. Poor guy.
    $ renpy.pause (1.25)
    Br stern b "But not now. I have business to attend to."
    Br "Please, [player_name]. Leave."

Sb disapproval b "No."

$ renpy.pause (0.5)
hide bryce with dissolve
$ renpy.pause (0.5)
show office at Pan ((128, 250), (128, 250), 3.0) with ease #TEST
$ renpy.pause (1.0)
show sebastian disapproval b at Position (xpos = 0.85) with dissolve
$ renpy.pause (1.0)
show bryce stern b flip at Position (xpos = 0.15) with dissolve

Br "Sebastian, you too?"
Sb "Let me explain myself, Chief. [player_name] is as involved in this as I am. After all, who else could serve as a better witness to both of Maverick’s actions than someone who directly saw Reza’s death and someone who was involved with the forged report?"
Sb "Sure, I’m an official police officer and thus better suited for this decision regarding official business, but at this point [player_name] might as well be an honorary member."
Sb "Besides, [player_name] could perhaps be able to provide a better understanding of Maverick’s actions."

$ renpy.pause (0.5)
hide bryce with dissolvemed
$ renpy.pause (0.5)

m "The room drowned in silence after Sebastian’s unexpected words. Bryce stood in deep thought for some time before turning around and looking away from both me and the rest of the force."

$ renpy.pause (0.5)
show bryce stern b flip at Position (xpos = 0.15) with dissolvemed
$ renpy.pause (0.85)

Br "Alright, then let’s have a vote, shall we? Who’s in favour of letting [player_name] get involved in this decision?"
$ renpy.pause (1.0)
m "Nearly the entire room responded, whether that be the lifting of hands, claws, or standing up. Only a few sat still in silence."
Br "Then by my authority as Chief of the police force, I allow [player_name] to be a part of our decision-making process."

stop music fadeout (2.0)
show sebastian smile b with dissolve
$ renpy.pause (1.0)

Br smirk b flip "Well, you saw them all. Looks like you’ll have to get yourself involved with official police business one more time."

if kol_tlh_endingA_route == True:
    Br stern b flip "Even if I wished you wouldn’t."

menu:
    "I hope that I’ll be able to help.":
        $ renpy.pause (0.5)
    
        Br smirk b flip "Since when haven’t you? I’ll trust your judgement and advice, whatever that might be."

    "What are my orders, Chief?":
        $ renpy.pause (0.5)

        Br stern b flip "Don't get so excited, [player_name]. This is pretty serious stuff."
        Br smirk b flip "Don’t worry about any orders, though. You’ll be able to manage after everything so far."
    
    "At this point I might as well be a police officer with being an ambassador as a side job.":
        $ renpy.pause (0.5)

        Br smirk b flip "I’m sure it will look good on your resumé if you ever want to apply for a job here."

Br stern b flip "Now, I must ask you to chime in every once in a while when something comes up. Your opinions here will be critical to our decision."
c "Alright."
Br "Everybody, let’s continue where we left off."

$ renpy.pause (0.5)
hide bryce
hide sebastian
with dissolve
$ renpy.pause (0.5)

m "Bryce walked to a nearby desk and grabbed a few papers strewn haphazardly across it. He then came back to me and handed a few sheets of paper to me, letting me read through them quickly."
m "Maverick was accused of the murder of a high-profile guest whom he was supposed to be protecting. There were also mentions of Reza and his actions, but I skipped them due to knowing everything there was to know about the Reza case."

if kol_tlh_endingA_route == True:
    m "I saw a few things about the Reza case and Maverick’s corruption, but I skimmed over it all, doubting that there was anything new that I could have gained from reading them. Bryce started talking again as soon as my eyes left the last page."
else:
    m "He was also charged with corruption for lying to both the council and humanity due to Maverick forging both reports. There was a brief description that went into further detail, but I didn’t have the chance to read it before Bryce started talking again."

$ renpy.pause (0.5)
show office at Pan ((0, 250), (0, 250), 3.0) with ease #TEST
$ renpy.pause (0.5)

m "Maverick gave me a slight glance, indicating some sort of concealed desire, before turning his head away to look at Bryce again."
c "(Alright, Maverick. I’ll try my best to repay the favour for you giving humanity a chance.)"

$ renpy.pause (0.5)
show bryce stern b flip at left with dissolve
$ renpy.pause (1.5)
play music "mx/path.ogg" fadein (0.85)

Br "So, we have agreed that Maverick’s sick leave doesn’t give him a pass for his crimes, correct? Let’s revisit Reza’s death and hear everybody’s opinions."
Br "According to this statement, Reza was killed outside the underground facility on the night of the fireworks due to a bite wound from Reza. Yet, in the official report, it was said that a feral dragon entered an unknown backdoor and killed Reza while [player_name], me, and the librarian working for the council were confronting him."
Br "This official report was written by none other than Maverick, who handed a copy to the council, as well as a report to humanity in some way."
Br "What I don’t understand is how this was managed. I have an idea that Maverick somehow got hold of [player_name]’s report without letting Sebastian notice anything off about it. Any suggestions?"
"???" "I’m saying that there had to be some extra insight to make this possible. Is there a possibility that this was an inside job?"
Br brow b flip "That doesn’t make any sense, though. The only way this could be possible is if there was a relationship between Maverick and [player_name]. Given how the two had gotten along up until now, that would make this very unlikely."

menu: #Prepare for mental gymnastics galore, 'cause this trial is full of 'em.
    "Maverick just wouldn’t have a reason to ask for my help.":
        $ kol_tlh_mav_trial_counter -= 1
        $ renpy.pause (0.5)

        Br stern b flip "Exactly. It just doesn’t seem feasible."

    "An ulterior motive had to be at play here.":
        $ kol_tlh_mav_trial_counter += 1
        
        c "Maverick isn’t the type to do something like this just to avoid punishment, at least from what I know about him. I’m guessing that he had to have a pretty strong reason to even try to do what he did."
        Br stern b flip "A fair point, but I’m afraid that it just raises more questions than answers. Why would Maverick feel this strongly about something to warrant his actions? How would forging the report help him in a meaningful way outside of still being part of the force?"
        Br "We just don’t have enough points."
        Mv normal "I’m right here, Bryce. I’m sure I’ll help you if you just ask nicely."
        Br "Your turn will come later, Maverick."
    
    "A sudden turn of feelings could have changed that.":

        c "Maverick acted the way he did to me because Reza was involved. Now that he’s gone, he doesn’t have a serious reason to be suspicious or even rude to me. Maverick might have well planned to do something involving me."
        Br "So you’re admitting that you might have been involved in all of this."
        c "I’m only highlighting the possibility of Maverick having a change of heart."
        Br stern b flip "Hmph."

$ renpy.pause (1.25)
"???" "I figure that Maverick must have had the original report and forged it at a time and place where nobody would notice. The only point in time where I think that it could have happened was when copies of the report were made."
Br "Damn, you're right."
Br "[player_name] wrote the report while Sebastian kept watch, that’s for certain. Due to us having a few copies of the report ourselves, I’m guessing that someone had the chance to edit it while those copies were made."
Br "It would be the perfect opportunity for Maverick to make any changes he wanted."

menu:
    "Maverick couldn’t have had enough time to edit the report.":
        $ kol_tlh_mav_trial_counter += 1

        c "There would have to be a lot of changes made to the report to have Maverick adequately cover himself. It just doesn’t make sense that there would be enough time for him to make the edits and copy the reports without taking too long."
        c "In addition to that, the edited handwriting would have been too messy for someone like Maverick if he had been in a rush."
        Br "You’ll be surprised just how quick Maverick can write while also not making it look like a disaster. He’s almost on the level of a runner in that regard."
        Br "Still, perhaps even this is a bit of a stretch..."

    "Then what about the report for the council?":
        $ renpy.pause (0.5)

        Br brow b flip "That was done before your report, remember? Maverick could have said what he wanted in that and edited yours to give him an alibi."
        c "Do you really think that he’d remember everything that he wrote in the council’s report word for word, all just to make accurate edits?"
        Br stern b flip "Yeah. I've known him far longer than you do, [player_name]. He has always proven himself to be the one with the most vivid memories."
        $ renpy.pause (0.5)
        Br "…for better, or for worse."

    "It’s the only time I hadn’t seen Maverick when I wrote the report.":
        $ kol_tlh_mav_trial_counter -= 1
        $ renpy.pause (0.5)

        Br "So, that theory has now been confirmed."
        Mv scared "..."
        Br smirk b flip "That’s one thing to check off of the list of questions."

$ renpy.pause (1.0)
Br stern b flip "Next section. It should at this point be fairly clear that Maverick has used dishonest methods to try and prevent being found out. The question that I have is: \"why?\""
Br "Sure, you could assume that he still wanted to work as an officer of the law after Reza’s death, but that would directly contradict the point of being an officer in the first place."
Br "We are here to uphold the law and protect those who need us. Yes, Maverick protected me and [player_name] from Reza, but by killing him, he has severely damaged diplomatic relations with humanity."
c "Speaking of which, I’ve got some news about the trade. Humanity has reconsidered their ultimatum and is willing to extend the deadline that we have."
Br brow b flip "Is that so? I wasn’t expecting to hear news of the trade at this time."
Br stern b flip "Especially considering that everything about it seems sketchy. Why would humanity suddenly extend their ultimatum when they seemed pretty serious last time about having the council reply in a given time frame?"
c "It’s a long story. I’m sure Emera will fill you in eventually."
Br "Not something that I’m looking out for, but alright."
"???" "Permission to speak, Chief?"
Br "Go ahead."
"???" "I believe that Reza’s death was something that happened in the moment, like the incident with Miles a few years back." #Uh-oh, the M-word dropped again. Yikes.
"???" "What are the odds that Maverick forged that report to try and fix his mistakes after the situation died down?"

$ renpy.pause (0.5)
stop music fadeout (1.0)
hide bryce with dissolvemed
$ renpy.pause (2.5)

m "The room grew eerily silent, creating a sense of concealed intensity. Eyes darted around the room, trying to find some sort of signal that someone might speak up. "
m "Maverick, looking almost melancholic in a sense, stood up and raised his voice slightly, stuttering as he thought about what to say."

show bryce stern b flip at Position(xpos = 0.15) with dissolve
$ renpy.pause (0.85)
show maverick sad at Position(xpos = 0.85) with dissolvemed
play music "mx/markday10.ogg"
$ renpy.pause (4.0)

Mv "I-I took a personal pledge after my brother’s passing. For as long as I’m still an officer, I won’t {i}ever{/i} let anybody else die on my watch. Especially not Bryce."
Mv angry "My brother died so that Bryce could live. If I had let Bryce die by Reza's hands, Miles’ death would have been for nothing. Did any of you think that I would just stand idly by while hoping that Bryce wouldn’t get killed by that pathetic excuse of an ambassador?" #That must've hurt to say...
Mv irritated "Draw whatever conclusions you want from these words. I don’t care. I did what I had to do to protect those closest to me."

$ renpy.pause (0.5)
hide maverick with dissolvemed
$ renpy.pause (0.5)

m "Maverick sat back down, leaving a feeling of mild surprise and wonder hanging in the air. Nobody dared to speak for some time as the police force pondered Maverick’s words."
m "But, of course, it couldn’t have been silent forever. Bryce resumed his talking, although with a hint of sympathy betraying his otherwise professional presentation."
$ renpy.pause (0.5)
Br "I didn’t think that this was how you felt, Maverick. I know how touchy a subject this is for you, and for you to reveal this to us all at this time…"
Br "Even if it might go against you—and chances are, it will—I thank you for telling us this."
Mv sad "Just go on where you left off, Chief. I’d rather not linger on this."
Br "Right."
stop music fadeout (4.0)
$ renpy.pause (0.75)
Br "Am I correct in deducing that Maverick killed Reza in the defence of others?"
m "Everybody in the room nodded their heads, except for Maverick, who silently sat and stared at Bryce."
Br "[player_name], what do you say? Maverick confessed why he killed Reza, but why do you think he forged the report?"

play music "mx/vines_kol.ogg" fadein (2.0)

menu:
    "To continue his job as an officer.":

        c "Maverick revealed just now that he doesn’t want anybody to die on his watch. It’s very possible that he forged the report so that he could continue to uphold his pledge."
        c "He was afraid that, should humanity hear about Maverick being involved, he would get discharged."
        Br brow b flip "A fair point if it wasn’t for the fact that Maverick would know that he would put the trade with humanity at extreme risk by lying."
        Br stern b flip "It would have been better if Maverick had just come clean from the start instead of letting all this happen."

    "To confuse anybody that might want to dig deeper.": #Just *how* sleep deprived was I when I wrote this option? Dear me, this is *horrible.*
        $ kol_tlh_mav_trial_counter -= 1
        $ renpy.pause (0.5)

        Br brow b flip "What do you mean?"
        c "You just said that Maverick doesn’t like to talk about his brother, right? Perhaps he could have forged the report to keep people from learning more about his brother’s death."
        Br stern b flip "What kind of mental gymnastics are you performing here, [player_name]? What you proposed makes absolutely no sense. Why would anyone want to investigate Maverick's past, especially if it's already on record?"
        Br "And {i}why{/i} would the forged report be involved?"
        c "..."
        c "Yeah, I guess that was kind of a stretch."
    
    "To thank me.":
        $ kol_tlh_mav_trial_counter += 1
        $ renpy.pause (0.5)

        Br brow b flip "Excuse me?"
        c "Hear me out, Bryce."
        c "Remember back in the underground facility when I stalled for time for Remy to get help?"
        Br "What about it?"
        c "After you’ve been shot, I followed Reza’s instructions and went outside, where Maverick leapt on Reza. For all I know, this could be Maverick’s way of thanking me for not letting Reza kill you while you were stuck down there."
        Br stern b flip "I’m not sure I follow. How would you benefit from Maverick forging the report?"
        c "If humanity knew that Reza’s escort was the one that killed him, humanity might have cut contact there and then. By lying, Maverick could have potentially saved our diplomatic relationship."
        $ renpy.pause (1.0)
        Br "..."
        c "..."
        Br "Maverick?"
        Mv normal "A pretty good deduction, I’ll admit. Interesting that [player_name] managed to figure that much out so quickly."
        Mv nice "Better watch out, Chief. You have competition."
        Br "..."

$ renpy.pause (2.0)
Sb drop b "Well, what do we do now? Are we going to inform everybody of what actually happened at the night of the fireworks?"
"???" "Doing so would cause the trade to be in danger, though."
Br stern b flip "Yes, but-{w=0.6}{nw}"
"???" "Won’t the Maverick case divert attention away from focussing on more important things like the comet?"
Br "Probably, though that’s–{w=0.8}{nw}"
"???" "Maverick can’t just be left unpunished. He committed serious crimes. What would that make us look like if we let him go with just a simple slap on the maw?"
Br "Maverick will-{w=0.75}{nw}"
"???" "And the humans? Surely they want justice for–{w=1.0}{nw}"

show bryce angry b flip with dissolve
Br "QUIET!" with Shake ((0, 0, 0, 0), 2.5, dist=17) #Is this a bit too close to Bryce snapping like in Bryce4? Hmmm...
$ renpy.pause (1.5)
show bryce stern b flip with dissolve
$ renpy.pause (1.0)
Br "Give me some time to think, please. I’ll return shortly."
hide bryce with dissolve

m "A loud burst of voices oozed into the air, sounds of arguments and agreements blending together into one incoherent mess. Having enough of this, I walked to where Bryce just stood."
$ renpy.pause (1.0)
stop music fadeout (2.0)
c "EVERYBODY, LISTEN TO ME!" with vpunch #An ambassador delivering a speech? Damn, what's next, supermarkets selling food?
$ renpy.pause (1.0)
m "The conversation abruptly came to a halt, and several curious glances were cast my way. I had a brief moment of self-awareness, but I quickly regained my composure and spoke."

play music "mx/forge.ogg" fadein (1.0)
$ renpy.pause (0.5)

c "Thank you. During this meeting, I have come to a few conclusions of my own that I need to share to help everybody come to a final decision."
c "Some of you might be bound by the law, always following orders as loyally as you can. After all, the laws kept your civilization going for as long as anyone can remember."
c "Yet, sometimes those laws need to be bent. Not every case can fit the law perfectly. That’s why judges and juries exist to fill that gap. Right now, even more so. If anything were to happen that might put the trade in danger, both our civilizations would suffer."
c "I ask you this: don’t let old traditions impact new decisions. How else are we to progress into a better future if we’re all stuck with the customs of the past?"
"???" "Are you asking us to simply ignore Maverick’s crimes entirely for the sake of maybe having a better future? For all we know, letting him go might cause more damage than just dealing with him now!"

menu:
    "He must be dealt with, but not now.":

        c "What Maverick did was bad, yes, but if we focus on what he has done now, then how much time will we have to focus about the bigger problems that we are facing soon?"
        c "We can all deal with Maverick at a later date; after the comet has passed and the trade has been completed."

    "How much trouble would Maverick really cause?":
        $ kol_tlh_mav_trial_counter += 1
        
        c "From what I’ve heard, crime is almost non-existent here. Ever since me and Reza came here, that has changed. Tell me, will letting Maverick—an experienced police officer—free truly cause more trouble than dealing with him right now?"

    "You’re blowing this out of proportion.": #"You're totally making this worse than it actually is lmao" bro Mav literally nearly caused utter chaos of course the officer had the right to make it sound as bad as it is
        $ kol_tlh_mav_trial_counter -= 1

        c "This isn’t a \"maybe\" here. Generators have already been set up to start storing energy for the comet. Dealing with Maverick is a hassle that will waste time."
        c "What I’m trying to say is that the comet {i}will{/i} be redirected. This isn’t as bad as you make it out to be."

$ renpy.pause (0.5)
m "Murmurs started to emanate after I finished speaking. I turned my head to Maverick, who only looked at me with an expression of concern, making me feel a bit uneasy. Did I really make the impact I wanted to make?"
m "Sebastian silently took notes of my advice, looking over what I had said with suppressed confusion and doubt, as if two conflicting viewpoints were having a duel in his mind to determine which viewpoint he'll believe in."
m "Bryce entered the room, looking far more calm than a few minutes ago. By the looks of things, he had come to terms with whatever thoughts were brewing within his mind."

stop music fadeout (1.0)
$ renpy.pause (0.5)
show bryce stern b flip at Position (xpos = 0.2) with easeinleft
$ renpy.pause (2.5)

Br "I’ve come to a final decision about what to do with Maverick. With [player_name]’s thoughts, as well as some things that arose from everybody currently here, I feel that this decision is unbiased enough to make."
Br "Naturally, should anybody disagree, then please speak your mind."

play music "mx/judgement.ogg" fadein (1.0)
$ renpy.pause (3.5)

if kol_tlh_mav_trial_counter >= 2:
    Br "Maverick will stay as a police officer for the sake of keeping the trade going. We already narrowly avoided the trade ending, so I don’t want to stretch our luck even thinner than it already is."
    Br "However, Maverick won’t go unpunished. He will be suspended for a month while making use of our counselling services so that Maverick won’t ever do what he did again. This will start as soon as the trade has been completed."
    Br "We will also not make any information about Maverick’s involvement public outside of the council. In the eyes of humanity, a feral dragon bit Reza to death, as stupid as that sounds."
    $ renpy.pause (0.5)
    m "The police force burst into chatter once more, all uniting with sounds of agreement and welcoming Bryce’s decision to keep a valuable member of the force. Maverick shot a glance over at me, showing a stoic expression of what I assumed to be gratitude."
    $ renpy.pause (0.5)
    Br "Are there any objections to my decision?"
    $ renpy.pause (2.0)
    Br "None?"
    $ renpy.pause (1.0)
    Br "Then my decision is final. Sebastian, I want you to go to Emera and announce the news."

    $ renpy.pause (0.5)
    show sebastian drop b at Position(xpos = 0.8) with dissolve
    $ renpy.pause (0.5)
    Sb "Sure, Chief."
    $ renpy.pause (0.5)
    show sebastian drop b flip with dissolve
    hide sebastian with easeoutright
    $ renpy.pause (0.5)

    Br "As for you, Maverick, go to the production facility and help with whatever they need. I’m sure the extra help would be appreciated so that more time could be spent generating power for the comet."
    Br "Everyone is dismissed."
    $ renpy.pause (1.0)
    Br smirk b flip "Except for you, [player_name]."
    c "Yes?"

    $ renpy.pause (0.5)
    stop music fadeout (3.5)
    show bryce at center with ease
    show bryce smirk b with dissolve
    $ renpy.pause (0.5)

    Br normal b "I wanted to thank you for giving your opinions. You have no idea how stressful this whole ordeal has been for me in the past few days."
    Br stern b "Reza’s death was on my conscience for quite some time, and after I found out about the forged reports as well?"
    Br sad b "I was on the verge of cracking."
    c "I’m just glad that I could have helped you to make your decision, Bryce."
    Br normal b "It’s appreciated. I guess that things would have been a lot more hectic if I had been successful in chasing you away."
    Br smirk b "And to add to that, Maverick didn’t have to get discharged while still serving a punishment; a compromise that both sides are happy with."
    c "Yeah."

    $ renpy.pause (1.0)
    show bryce normal b with dissolve
    play music "mx/clouds.ogg" fadein (1.5)
    $ renpy.pause (0.5)

    Br smirk b "Say, how about we go to the bar this evening to celebrate?" # O h  d e a r
    c "So soon? I mean, it wasn’t that long ago since we’ve been at the bar."
    Br normal b "C’mon, it’s a celebration for goodness sake! I’m planning to bring Sebastian and Maverick as well, so this isn’t something to miss!"
    c "I’ll have to think about it. Anything can pop up between now and later."
    Br "I guess, yeah. Still, feel free to head to the bar at sundown if you’re able to."
    c "Got it, Bryce."
    Br "But for now, I have to get back to work. After all, I've got to do quite a lot of paperwork. I dunno if you’ve heard, but you’re able to go around town without an escort anymore."
    c "Yeah, I've heard."
    Br "Great. Well, see you around."
    c "Goodbye, Bryce. Good luck with your work."

    hide bryce with dissolve

    $ kol_tlh_mavstillofficer = True

else:
    Br "Maverick will have to be discharged. Not only has he been guilty of killing Reza and forging the reports to hide himself, but he also put the trade with humanity at monumental risk."
    Br "However, sending him to prison for rehabilitation doesn’t seem necessary. Maverick did what he did to help others. Unfortunately, by doing so, he has caused more harm than good. Regardless, his intentions were in the right place, so prison will just waste our resources."
    Br "I am not planning on making this information public outside of informing the council. Things are already shaky with humanity, so we don’t need to inform them that an enforcer of the law was the one who killed their ambassador."
    
    $ renpy.pause (0.5)
    m "The police force erupted in voices of chaos, with several thoughts and opinions showering Bryce left, right, and centre. I looked over to Maverick, who only returned a blank stare."
    $ renpy.pause (0.5)

    Br "Everybody, calm down!" with hpunch
    $ renpy.pause (0.5)
    Br "It’s clear that some of you might be unhappy with my decision, while others agree with it. Unfortunately, my decision is final."
    Br "I’ve thought about both possibilities while in my office, and I believe that this is the best outcome for us all. Those that disagree with me will have to make an appointment at some point during the day or send me a letter."
    Br "For now, I see this case as having been dealt with. Sebastian, I need you to inform Emera of my decision. As for everybody else, please return to your work."
    Br "Maverick, meet me in my office while we sort the paperwork out. Remember to bring your necklace."

    stop music fadeout(2.0)
    $ renpy.pause (0.5)
    Mv shocked "..."
    $ renpy.pause (0.85)
    Mv sad "Yes, Chief."
    $ renpy.pause (0.5)
    hide bryce with dissolve
    $ renpy.pause (0.5)
    
    m "I started to walk out of the police office, but I got stopped just as I was about to exit the door."

    $ renpy.pause (0.5)
    Br stern b "Wait."
    $ renpy.pause (0.5)
    show bryce stern b with dissolve
    $ renpy.pause (0.5)

    Br "Thanks for being a part of this, [player_name]. Your judgement was valuable. I can’t say that I liked making this decision, but there wasn’t another idealistic choice."
    c "Happy to help, Bryce."
    play music "mx/loss_kol.ogg" fadein (2.5)
    Br sad b "If only this was a happy result."
    Br "These past few days have been rough. I was constantly worrying about what to do with Maverick since the day he killed Reza. And with it being revealed that he forged those reports as well?"
    Br "..."
    $ renpy.pause (1.0)
    Br "I’ve lost a close friend today."
    c "You could always hang out outside of work, you know."
    Br "I doubt that Maverick would want to anymore."
    $ renpy.pause (1.5)
    c "..."
    Br "..."
    $ renpy.pause (0.5)
    Br stern b "E-Excuse me, but I have to get back to doing that paperwork. Thanks for the small chat."
    c "Goodbye, Bryce."

    hide bryce with dissolvemed #Bryce is gonna drink himself to death, isn't he?

stop music fadeout (2.0)
$ renpy.pause (1.0)
m "I made my way out of the police office, feeling mentally exhausted after what had just transpired."
scene black with fade
$ renpy.pause (1.0)
m "Deciding to take a breather, I went to Tatsu Park to rest and gather my thoughts."
$ renpy.pause (2.0)
scene park2 with dissolveslow
$ renpy.pause (2.0)

m "I arrived at the park and looked around for a bit. It seemed to be unusually quiet, with only a few dragons occasionally passing by the blooming trees. I felt a sense of calm within myself as everyone went about their business, wondering how things were back home."

if kol_tlh_tld_crossover == True:
    m "Yet, within that same sense of tranquillity, anxiety started brewing deep within my soul. Will the generators from the underground facility truly be enough to redirect the comet? Will humanity be able to survive long enough? Will Logan be alright? Did the things we brought through the portal actually help humanity?"
else:
    m "Yet, within that same sense of tranquillity, anxiety started brewing deep within my soul. Will the generators from the underground facility truly be enough to redirect the comet? Will humanity be able to survive long enough? Will Logan be alright?"

$ renpy.pause (0.5)
c "(Perhaps I just need to take a small nap to clear my mind.)"
$ renpy.pause (0.5)
m "I sat down on a nearby bench under a tree and made myself comfortable. It wasn’t long before I dozed off into the realm of dreams."

scene black with fade
$ renpy.pause (5.0)
Ry "[player_name]?"
$ renpy.pause (2.0)
Ry shy "[player_name], are you listening?"
$ renpy.pause (2.0)
Ry look "[player_name]!"
$ renpy.pause (2.0)

scene park2
show remy look
with dissolveslow
$ renpy.pause (2.0)

play music "mx/dusk_kol.ogg" fadein (1.5)
c "Remy?"
Ry shy "Thank goodness you’re okay. I was worried that you wouldn’t wake up."
Ry "You must have been exhausted to have slept that deep. I’ve been trying to get you awake for some time now."

menu:
    "How long, exactly?":
        $ renpy.pause (0.5)

        Ry "If I had to guess, probably the last five minutes or so." #Wouldn't a rational person call an ambulance at that point?
        c "That must have been terrifying for you, then."
        Ry look "It was."

    "Did you think that I was dead or something?":

        Ry "No, not at all. I could still see you breathing, and your heart didn’t stop beating."
        Ry look "I assumed you had passed out or that something worse had happened to you. People don't usually sleep like that, you know."

    "It’s alright, Remy. I just wanted to get some rest, that's all.":
        $ renpy.pause (0.5)

        Ry "Well, I’m just glad that it wasn’t something else."
        Ry look "With the way you slept, you almost seemed as if you had completely passed out on the bench."

Ry "Did something happen that made you so exhausted?"
c "All I did today was go to Emera, as you know."
$ renpy.pause (1.0)
c "Oh, and I went to the police office as well to see what was going on there."
Ry "And now I see why you took a nap. I can’t imagine the chaos that had to be dealt with there."
c "It wasn't that bad, Remy." # *ahem*
Ry "Perhaps, perhaps not."
$ renpy.pause (0.75)
Ry shy "Mind if I sit next to you?"
c "Please, go ahead."

hide remy with dissolve
m "Remy gently sat next to me on the park bench. Instead of giving me space, he squeezed himself against my side, sighing lightly."
show remy shy with dissolve
$ renpy.pause (0.5)

c "So Remy, could I ask you a question?"
Ry normal "Of course."
c "What were you doing here in the first place?"
Ry shy "I needed to take a break from work. I usually go to Tatsu park when I need to get away from Emera for a bit, even if I know that she likes to be here as well."
Ry "Things have been so rough at work recently. With all the research I have to do in such a finite amount of time while also putting up with Emera every single day, it takes its toll."
Ry sad "I don’t know how I’m even pulling through. I love doing research, but this? Every single day, I need to analyse as much information as I can for the council. There’s no passion in it whatsoever."
Ry "Yet, that’s not the worst part."
Ry "It’s the fact that, if I don’t do this, then everybody might die."
c "Remy."
$ renpy.pause (0.5)
Ry "I’m stuck, [player_name]. It’s like I have to sacrifice myself for the survival of others. It’s just that…"
$ renpy.pause (0.5)
Ry "I don’t think there is anything left to sacrifice."
c "Remy, listen to me here."
c "You’re burning yourself out due to all your work, that much is obvious. Please, take it easy for a bit. From what I can gather, you’ve already done a ton of research."
c "I’m sure the council will be able to make a good decision with the resources you’ve provided them already."
c "Don’t.{w} Overwork.{w} Yourself.{w} Nobody will benefit from it."

$ renpy.pause (1.5)
Ry "..."
$ renpy.pause (1.0)
m "Remy stared blankly at me, showing an emotionless expression. His seemingly hollow eyes glistened at me exhausted, devoid of any will to continue talking or to think."

$ renpy.music.set_pause(True, channel="music") #Unnecessary, but whatevs
$ renpy.pause (0.5)

c "Remy?"
Ry "No, I will not overwork myself. That simply would not do, would it?" #How many Amelia references have I made so far? I've lost track in counting. (It's probably more than 3 or something.)
Ry "{cps=15}I cannot lose myself now. Not when everyone is depending on me.{/cps}" #Wait, why did I put the slow text here again? Eh, I'll just leave it as is. EDIT FROM FUTURE KOLS: Because Remy realised that if he overworked himself to death like Amelia, he'd cause everyone he knows and doesn't know to suffer like him, if not worse.

$ renpy.pause (1.0)
$ renpy.music.set_pause(False, channel="music") 
$ renpy.pause (1.0)

Ry shy "…M-My apologies. I don’t know what came over me there. I wasn’t myself."
c "It’s alright, Remy. Are you feeling better now?"
Ry "I guess I am, though I can’t point out why."
Ry "It’s strange that I always seem to feel better after I spend some time with you. Despite these last few days being some of the most stressful in my life, having you around makes that weight far easier to bear."
c "I’m just happy that I can be there for you when you need it the most."
Ry "And I truly thank you for it."
$ renpy.pause (2.0)
Ry "I just realised something."
c "What is it?"
Ry look "It was really immature of me to suddenly burst out like that at you. I really shouldn’t have dumped all my feelings on you without at least asking if it was okay to do so."

menu:
    "Don’t feel guilty about it.": #"Just don't be sad!" is the MC's logic here. *sigh*
        
        c "I told you that you can talk to me about anything, Remy. That extends to any time as well. Don’t worry too much about it."

        $ renpy.pause (0.5)
        show remy shy with dissolve
        $ renpy.pause (0.5)

        Ry "Alright. I’ll try not to."

    "Yeah, you really should’ve asked first.":
        $ renpy.pause (0.5)

        Ry "I know, and I’m sorry. I just can’t seem to have control over myself as of late."
        Ry shy "It won’t happen again. I promise."

    "At least you’re not keeping it all inside.":
        $ renpy.pause (1.0)

        Ry "..."
        $ renpy.pause (0.5)
        Ry sad "...at least, yes."

$ renpy.pause (3.5)
Ry shy "Oh, but this isn’t the time nor the place. I’m just happy that you at least listened."
$ renpy.pause (0.5)
m "Remy unexpectedly wrapped his wing around my body like a blanket, gently holding me closer to his warm, soft scales. We sat like this for a while, not making any moves nor speaking to each other." # <3
$ renpy.pause (2.0)
m "It was only natural, however, that the silence would eventually be broken."
$ renpy.pause (1.0)

Ry shy "I really should get to work, but I don’t want to go back just yet. I don’t like to say this, but I need this moment. It feels…{w=1.0} calming."
c "Then take as long as you need."
Ry "I wish I could."

$ renpy.pause (0.5)
hide remy with dissolve
$ renpy.pause (0.5)
m "Remy unwrapped his wing and stood up from the bench. He looked back at me and gave a slight smile before stretching like a cat."
$ renpy.pause (0.5)
show remy normal with dissolve
$ renpy.pause (0.5)

Ry "Goodbye, [player_name]. I’ll see you some other time."
Ry shy "And thanks."
c "Don’t mention it, Remy. Good luck with your work."
Ry normal "I wish you the same."

hide remy with dissolve
$ renpy.pause (1.0)
m "Instead of taking off like I expected Remy to, he somberly marched his way to the edge of the park on his way to the library."
c "(And there he goes. I do hope that he takes his health seriously.)"
m "Feeling mentally recharged enough from spending a brief amount of time with Remy, I decided to head out once more."
$ renpy.pause (1.0)

scene park3 with dissolve
$ renpy.pause (1.0)
scene town7 with dissolve
$ renpy.pause (1.0)

m "I looked around me as I walked through the town with a sense of hope, knowing that, with my and Remy’s efforts, this world will be saved. I realised that, despite everyone’s hardships, nothing would be in vain."

$ renpy.pause (1.0)
scene kolmoretown2 at Pan ((0, 0), (0, 180), 5.0) with dissolve
stop music fadeout (2.5)
play sound "fx/steps/steps.ogg"
$ renpy.pause (3.0)
m "However, any further thoughts that I might’ve had were cut short as I heard footsteps approaching from behind me."
$ renpy.pause (1.0)
c "Maverick, I swear that–{w=1.0}{nw}" #The MC is learning! :O
stop sound

Lg tnormal "Oh, please, I haven’t gotten {i}that{/i} fat since I’ve last seen you. I’d have to eat quite a lot to match Maverick in weight." #...maybe not.
c "Logan?!"

show logan tnormal with dissolve #The tired Logan from TLD returns to make a cameo once more!
play music "mx/couch_kol.ogg"
$ renpy.pause (1.0)

if kol_tlh_tld_crossover == True:
    Lg "Are you surprised? Didn’t I tell you that I’ll be back within the next few days?"
    c "I didn’t expect you to be back this soon, though."
    Lg "Life is full of surprises if you work hard enough."
    $ renpy.pause (0.5)

else:
    Lg "Surprised?"

c "Judging from your eyes, I’m guessing that you didn’t sleep.{w} As usual."
Lg tannoyed "What a wonderful and insightful observation that you have just made, [player_name]. It would have taken decades for our greatest innovators to figure out what you just did in mere seconds."
Lg tserious "Of {i}course{/i} I didn’t get any sleep. It was for a reason, though."
Lg "I wanted to come back and help things out here as fast as I could. Luckily, the contributions I made warranted my return."
$ renpy.pause (1.0)

if kol_tlh_endingA_route == True:
    Lg "With all the stuff I brought, I’ve managed to create a prototype generator as a base for humanity, while the authorities used the generator I brought to power the hospital. Supposedly, somebody will be healed soon enough to be able to use my base to try and mass produce some generators."
    Lg tannoyed "I’ve also toyed with some of the scrap parts, but I couldn’t get too far with them. A lot of that stuff is outside my skill level."
    Lg tsmiling "But that didn’t mean I was completely useless. There should be enough repaired parts to keep humanity going for more than long enough until the comet is redirected."

    if kol_tlh_tld_crossover == True:
        c "I thought you were ordered to keep the energy reserves stable enough until somebody more qualified takes your place."
        Lg tnormal "That’s exactly what I did. The base generator I constructed was used to build up the energy reserves as a demonstration. Even if it was slow, it was sufficient enough to warrant my return."
        Lg "All that needs to be done is for somebody more qualified to get revived."
        Lg tsmiling "Heh, that rhymed. Nice."

    else:
        c "Then why did the authorities decide to send you back here instead of working to, I don’t know, keep power levels stable?"
        Lg tannoyed "Apparently I’m more needed over here, so that’s good."

else:
    Lg "With the spare parts and blueprints I brought, I’ve managed to reconstruct a kinda stable generator that should keep humanity going for about a week. Granted, it’s only strong enough to partially power the hospital, but it was apparently enough for the authorities."
    Lg "With some persuading, I managed to go back here."
    c "What about all the parts that you told me about that needed to be repaired?"
    Lg tannoyed "So, the generator I made will supposedly provide enough power for somebody more qualified to be healed, which will then be responsible for the scrap. With my blueprints, they’d be able to construct some sort of hybrid generator from both humanity’s and dragonkind’s parts."
    Lg "At least, that’s what I think. All I did was test which parts were responsive to make a generator and, you know, made that generator."

if kol_tlh_tld_crossover == True:
    Lg tserious "Oh, and just to remind you: you {i}still{/i} haven’t sent your PDA to humanity yet."
    c "Damn, I completely forgot about that. The Sergeant won’t be happy with me, will he?"
    Lg "Not in the slightest."
    $ renpy.pause (0.5)

else:
    Lg tnormal "Oh, and before I forget: you need to send your PDA to humanity. They desperately need it to repair most of the scrap."

c "My PDA should be back at my apartment. Mind doing me a favour and get it?"
Lg tnormal "I can go to your apartment, sure. I’ll just take a nice long nap before I bring it to you."
c "Right..."
$ renpy.pause (0.5)
c "Speaking of, why are you so tired? You could have just taken a nap before coming here."
Lg tannoyed "I almost forgot, but all those things I've told you about? I've also worked on them through many nights in order to finish them as soon as possible. The authorities gave me the opportunity to return, which I took as fast as I could before they reconsidered. So, here we are."
Lg "Just gotta take the chance before it gets taken away, after all. Me sleeping probably would've been the cause of that."
c "Well, now that you’re here, you’d have to make a visit to Emera first."
Lg tserious "Hell no. Not now. I’m gonna take a nice long nap first before I visit that bureaucratic hag."
c "Be careful what you say, Logan. We don’t want to risk everything we’ve worked on up until now. Besides, an ambassador isn’t supposed to act like that; something you should know by now."
Lg "Yeah, yeah. I just can’t think straight now, so forgive me for that. Still, I’d much rather crash at your place for a while until I’ve gotten enough rest to visit her."

if kol_tlh_bryce_escort == True:
    Lg tannoyed "By the way, why are you without Bryce? Are we free to go where we want without an escort?"
else:
    Lg tannoyed "By the way, why are you without Sebastian? Are we free to go where we want without an escort?"

c "With you here, the answer is a definite {i}maybe.{/i} It’s a long story."
Lg "Then save it for later. You can fill me in on all the details then. For now, I’m going to sleep on your couch, and there’s nothing you can do about it."
c "Go knock yourself out, Logan."
$ renpy.pause (1.25)
Lg "*sigh*"
Lg "Did you {i}really{/i} have to make a pun now, [player_name]?" #A bit of a stretch for a pun tbh, but whatevs. Past me is an enigma I'll never understand.

menu:
    "I didn’t even notice until you pointed it out.":
        $ renpy.pause (1.5)

        Lg "Then screw me."

    "Puns always lighten the mood.":
        $ renpy.pause (0.5)

        Lg "Never had for me, and never will. Keep your puns for yourself."

    "What? I thought it was your dream to enjoy some good puns every once in a while.":
        $ renpy.pause (2.5)

        play sound "fx/slap1.wav"
        c "OW!" with vpunch
        Lg "Do. Not." #Amazing.

$ renpy.pause (0.5)
Lg "Now, see you later. Sleep calls, and I must obey."
$ renpy.pause (0.5)
hide logan with dissolve
$ renpy.pause (0.5)

m "Logan walked off into the distance towards my apartment. Despite being tired, I could see that Logan took the longer road towards my apartment, away from any potential prying eyes."
m "I decided to follow him to see whether he’ll fall asleep on his way home."

scene black with fade
$ renpy.pause (0.5)
stop music fadeout (2.5)
$ renpy.pause (2.0)
scene kolapartmentnoon with dissolve
$ renpy.pause (2.0)

m "I eventually arrived at the outside of my apartment, where I saw Logan sleeping on the doorstep." #Logan hobo real?!
c "(Oh, right. I’ve locked the door, so he wouldn’t have been able to get in.)" #The MC is evil confirmed.

$ renpy.pause (1.0)
play sound "fx/door/handle.wav"
$ renpy.pause(1.0)

m "I unlocked the door and tried to shake Logan awake, but he kept on sleeping. Eventually, I gave up on trying to wake him up."
m "However, not wanting Logan to wake up even crankier with a sore neck, I got a spare pillow from my apartment and put it on the ground. I gently moved Logan so that his head rested comfortably on the pillow."
$ renpy.pause (1.5)
c "(Sleep well, Logan.)" #Or not. Maybe this is a suitable form of an apology.
m "While here, I decided that I might as well grab my PDA and send it through the portal. No need to keep humanity waiting for something that might give me more time here. If my estimations were correct, then humanity’s portal should still be active for me right now to send the PDA through."

$ renpy.pause(1.0)
play sound "fx/door/creaky.wav"
$ renpy.pause(3.5)

c "(There we go.)"
m "I walked back out of my apartment, leaving the door unlocked in case Logan decided to wake up. As a cool wind popped up from nowhere, a strong sense of duty overcame me. I realised just how intricately weaved Logan’s plan was, keeping both sides as happy as possible while everything was balancing on an unstable lie."

$ renpy.pause (0.5)
scene black with fade
$ renpy.pause (3.0)
m "As was tradition, I made my way to the portal on top of the hill."
$ renpy.pause (1.5)
scene np1x at Pan  ((200,200), (450,100), 6.0) with dissolveslow
$ renpy.pause (0.5)

m "The two pillars stood as grand as ever, defying the natural scenery of the surrounding areas."
play sound "fx/telstart.ogg"
$ renpy.pause (0.5)
m "I powered the portal up and put the PDA on the floor. I had to wait for a while as the portal continued its routine before the PDA could be sent through. Luckily, I didn’t need to wait long for that to happen. The PDA slowly vanished, presumably ending up right on the other side."
$ renpy.pause (2.0)
stop sound fadeout (1.5)
$ renpy.pause (0.5)
m "As the portal powered down, an eerie silence enveloped me, its call striking at the depths of my mind. Something about all of this felt off to me, yet I couldn’t point out why."
m "Was something unexpected going to happen now that I’ve sent my PDA through to humanity? Perhaps my mind was simply playing tricks on me due to the stress I’ve been going through as of late, yet I can’t feel certain about it."
m "I turned around to walk back to my apartment, only to unexpectedly bump into somebody instead."
$ renpy.pause (1.0)
c "I’ll give you credit where credit is due. I didn’t even hear you this time around."

if kol_tlh_mavstillofficer == True:
    show maverick normal b with dissolve
else:
    show maverick normal with dissolve

$ renpy.pause (0.5)
play music "mx/dream_catcher_kol.ogg"
$ renpy.pause (0.5)

Mv "Mostly because you were using the portal when I snuck up on you." #This is probably the closest I'll get to writing a pre-Miles incident Maverick. Enjoy, folks.
Mv "I’m guessing that whatever you sent through was going to help maintain diplomatic relations from the humans’ side."
c "I guess you could say that."
Mv "Then at least you’re still doing your part in not causing both our civilisations to collapse."

menu:
    "It’s only because of you that I’m even able to do this.":
        $ renpy.pause (0.5)

        Mv "I only threw humanity off. You did all the hard work, so you deserve the credit."
        Mv "Besides, even if I was the catalyst for this reaction, you were the spark that got it going."

    "Well, Logan did have a part in it.":
        $ renpy.pause (0.5)

        Mv "Maybe, maybe not; it doesn't matter right now. The point is that the trade is relatively stable, and that’s what’s important."
        Mv "Even if those who were the most suspicious of us played their role as well."

    "There’s still a lot of work left to do, though.":
        $ renpy.pause (0.5)

        Mv "Certainly. Yet through your efforts, I believe that the trade will continue despite the hardships that both our civilisations face."

$ renpy.pause (0.5)
c "You seem awfully relaxed, Maverick."
$ renpy.pause (1.0)
c "…especially for what happened back in the office."

if kol_tlh_mavstillofficer == True:
    Mv nice b "Yeah, you can say that."
    Mv "I expected to get a far worse punishment, yet here I am, still a member of the force. Normally, the punishment for corruption and murder isn’t this lax."
    Mv "And to think that it was all your doing. I appreciate it, [player_name]."
    c "Don’t mention it, Maverick. I simply wanted to return the favour."
    Mv "So it seems."
    Mv normal b "You know, I was wrong to have automatically assumed that you were just like Reza, always scheming, always hiding something from me."
    c "I mean, I can’t blame you. The only perception of a human you had before I came here was Reza, so it was only natural for you to have assumed that Reza represented how every human acted."
    Mv "And now you see why I was initially so suspicious of you."
    c "Yeah."
    $ renpy.pause (0.5)
    Mv "..."
    Mv "Thanks for looking out for me, [player_name]. Without you, I probably would have experienced far worse things than I otherwise would have."
    $ renpy.pause (1.5)
    Mv nice b "Friends?"
    $ renpy.pause (1.0)
    c "Friends."
    m "I raised my hand and pointed it toward Maverick while signalling for a handshake. Maverick, not knowing what to do, decided to grab my hand with one of his claws and follow my motions."

else:
    Mv "Well, now that I won’t be part of the police force anymore, I don’t really have much to worry about. Whatever will happen is outside of my control, so why bother fighting it?"
    c "I didn’t expect something like that to come from you, Maverick."
    Mv nice "Me neither, yet here we are."
    Mv normal "Still, I want to thank you for at least trying to cover for me back at the office, even if some of the things you said weren’t exactly helping me out."
    c "Sorry about that."
    Mv "It’s alright. Nothing that can be changed now. Sure, I can sulk about it all I want, but it won’t do anything to change my situation."
    c "I see."
    Mv "At least I can say that I tried my best. Everything else is up to you."
    c "Yeah, I guess it is."

$ renpy.pause (1.0)
c "So, what even brought you here in the first place?"

if kol_tlh_mavstillofficer == True:
    Mv normal b "I’m supposed to be the portal guard for the rest of the day. Usually Sebastian would take this shift, but I volunteered to take it instead."
    c "How kind of you."
    Mv "No, not kindness. I needed a breather from everyone else."

else:
    Mv normal "I wanted to go to the portal because I knew that nobody would be here for the time being. Sebastian's guard shift is supposed to start in an hour or whatever, so now would be a good time."
    Mv "To be blunt, I need a breather from everyone. Of course, I didn't expect to see you here, but things happen."

c "Oh, how come?"

if kol_tlh_mavstillofficer == True:
    Mv angry b "Everyone has been treating me differently since Bryce informed the force about what I did. Not only was I shunned by Bryce during the Reza case, but I'm now being shunned by everyone I thought was my friend."
    Mv normal b "Hence, the break. I’m sure it’ll pass eventually, but for now I’d rather keep my distance."
    c "Should I give you some personal space, then?"
    Mv nice b "Only if you want to. At this point I don’t even mind you being here."
    $ renpy.pause (1.0)
    c "…thanks? I’ll, uh, take it as a compliment."

else:
    Mv angry "Everyone has been treating me differently since Bryce informed the force about what I did. Not only was I shunned by Bryce during the Reza case, but I'm now being shunned by everyone I thought was my friend."
    Mv normal "Hence, the break. I’m sure it’ll pass eventually, but for now I’d rather keep my distance."
    c "Should I give you some personal space, then?"
    Mv nice "Only if you want to. At this point I don’t even mind you being here."
    c "…thanks? I’ll, uh, take it as a compliment."

Mv "Take a seat. I’m sure you don’t want to constantly stand."

$ renpy.pause (0.5)
hide maverick with dissolve
$ renpy.pause (1.0)
scene np1x at Pan  ((450,300), (450,300), 1.0) with ease
$ renpy.pause (0.5)

m "I gently sat down on the soft, lush grass surrounding the portal. Not entirely comfortable around Maverick, I still maintained my distance from him."

$ renpy.pause (1.0)

if kol_tlh_mavstillofficer == True:

    show maverick normal b with dissolve
    $ renpy.pause (0.5)

    Mv nice b "You know, Bryce is going to have a celebration at the bar later. I’m guessing I’m involved somehow."
    c "Yeah. Bryce already invited me. He said he wanted to celebrate the fact that he didn’t have to have you discharged."
    Mv normal b "I should’ve guessed. It wouldn’t have been easy for Bryce to let me go. Especially not with all the hell that’s been going on recently."
    Mv "I don’t know if you’ve picked this up, but Bryce has been drinking heavily as of late."

    if kol_tlh_seb_ask_nobooze == True:
        c "I do. Sebastian told me all about it."
        Mv "So, he’s also concerned. I’ve been wondering about that, actually."
        Mv "If Sebastian already told you about Bryce’s worsening habits, then you already know why I’m concerned about him."
        Mv "This is too much, even for Bryce."

    else:
        c "I’ve noticed, yeah."
        Mv "Well, it’s been getting worse, so much so that Bryce is ending up late for work due to being unconscious from an alcohol overdose. Of course, it goes deeper than that, but it would be unnecessary to give you every single detail."
        c "That bad, huh?"
        Mv "Yep. I’m just guessing that the imminent threat of extinction doesn’t do wonders for his mental health."
        $ renpy.pause (0.5)
        Mv scared b "Nor my actions, for that matter."
    
    $ renpy.pause (0.5)
    Mv normal b "That’s why I’m hesitant about going to the party. Not only would I subconsciously cause him to drink more due to all of his pent-up stress about me, but the added social aspect of drinking with friends tends to cause one to consume far more alcohol than one otherwise would."
    Mv "Based on my theories, I doubt that Sebastian would want to come along either for much of the same reasons."
    c "Leaving Bryce to have yet another lonely time at the bar with Zhong to take care of him after he passes out."
    Mv "Precisely. It’s a case of Bryce being damned either way."
    Mv "And it’s not as if I can cut him off easily, either. Bryce can get irrationally angry if you take his beer away, whether directly or indirectly."
    Mv "But enough about Bryce. I’m assuming that you’ve been keeping up with the council’s orders?"
    c "I have, yeah."
    Mv nice b "Good. Like I said, all our lives are depending on your actions now. Screw up, and you’ll get to experience what Reza felt just before dying."
    $ renpy.pause (1.0)
    c "..."
    $ renpy.pause (0.5)
    Mv normal b "It’s a joke."
    c "Humour isn’t really your strong point, is it?"
    Mv nice b "Get me drunk and then ask again." #Maybe this could be a reference to that one AwBH scene? Like I said, the past version of me was on all sorts of wacky brainwaves that I'll never understand.
    c "Perhaps I don’t need to. It’s been interesting seeing you be so kind and open as of late."
    Mv "Don’t get used to it. I’m just in a good mood, that’s all."
    $ renpy.pause (2.0)
    c "Well, I think I need to be going."
    Mv normal b "See you around, [player_name]. It was nice talking to you."
    c "The feeling is mutual, Maverick."

else:

    show maverick normal with dissolve
    $ renpy.pause (0.5)

    Mv "You know, I’m kind of lost as to what to do now."
    c "How so?"
    Mv scared "I don’t think that I’m able to find a job to sustain myself now. Even if this information is kept private, I suspect it will be leaked to the press."
    Mv normal "Despite Bryce’s reactions about wanting me gone, I can imagine that the possible leak would make him far more upset than he already is."
    Mv "We both knew what had to be done, even if we didn't like it."
    c "I can’t imagine that somebody would want to leak this information, though."
    Mv angry "Are you this oblivious to your surroundings, [player_name]? Did you not notice the reactions of the police force when Bryce delivered my sentence?"
    Mv "Someone out there hates me or Bryce enough to leak my actions to the public. It might be their way of damning me one last time or getting back at Bryce for letting me go."
    Mv "I can see that the urge for revenge is strong in the police force."
    $ renpy.pause (0.8)
    Mv normal "Not that it matters. I knew what the results would be if I had been caught forging your report. It’s my responsibility to accept those consequences."
    c "Where will you go after you’ve been fully discharged? Since you still seem to have some idea of what's happening in the force right now, I imagine that you still have connections there."
    Mv "Remember, I was already fully dischardged. I gave up my necklace and title."
    Mv sad "All I have left are damaged connections."
    $ renpy.pause (0.5)
    Mv normal "That wasn't what you asked, though. To answer you, I can’t say. I’ll probably have to move somewhere where I’m not as well known. Though, if anything gets leaked, even that would be pointless."
    
    if annasurvives == True:
        Mv nice "Maybe Anna would have something for me."
        c "Why Anna?"
        Mv normal "We have…{w=0.7} a history, so to speak."
        Mv "I’m sure she’d be able to find an opportunity for me to work at the production facility. If not, then I’ll figure out what to do from there."
        c "I wish you good luck with that, then."
        Mv nice "Thanks."

    $ renpy.pause (1.0)
    Mv normal "Before I go, I need to ask you a favour."
    c "I’m happy to help, Mav."
    Mv nice "\“Mav\”, huh? Heh. It’s been ages since someone called me that."
    $ renpy.pause (0.5)
    Mv normal "I want you to keep an eye on Bryce, especially when it comes to his drinking." #Ties back to Mav's argument of wanting to protect Bryce.
    Mv "I imagine that the threat of imminent extinction can’t do wonders for his mental health, nor can the fact that he had to discharge one of his best friends. He's already in a bad situation by being late for work due to his blackout the other day."
    Mv scared "Just…{w=0.65} don’t let it go out of control. Try to reason with him, alright? I know that we haven’t been kind in the past, but if there’s anything I need to ask you to do, it’s this."
    Mv "Forget about the comet, or the report, or humanity. I don’t want my friend to lose his job."
    $ renpy.pause (0.5)
    show maverick sad with dissolve
    $ renpy.pause (0.5)
    Mv "Or...{w=0.4} worse."
    c "I’ll try my best, Maverick."

    show maverick normal with dissolve
    $ renpy.pause (0.5)
    m "Maverick only nodded in response."
    $ renpy.pause (0.5)
    Mv "I should be going now. I remembered that there was still something that I needed to do at the police station before fully leaving it all behind."
    Mv nice "I’ll leave you to your nosy ambassador duties. You know what to do."
    Mv "Goodbye, [player_name]."
    c "Bye, Maverick. It was nice talking to you."

    $ renpy.pause (0.5)
    hide maverick with dissolve
    $ renpy.pause (0.35)
    play sound "fx/takeoff.ogg"
    $ renpy.pause (0.5)

    m "Maverick stood up from the ground and stretched slightly. He then looked back at the portal briefly and took off into the skies, leaving me alone close to the portal."


$ renpy.pause (0.5)
m "I got up and brushed the blades of grass off of my pants. With the rest of my day ahead of me, I struggled to come up with something to spend it on."

$ renpy.pause (1.5)
play soundloop "fx/steps/steps.ogg" fadein 1.0
stop music fadeout (7.0)
scene np2x at Pan((0, 150), (0, 150), 0.0) with dissolve
$ renpy.pause (1.5)
scene np3x at Pan((0, 220), (0, 220), 0.0) with dissolve
$ renpy.pause (1.5)
scene town1 with dissolve
$ renpy.pause (1.5)

m "As I walked through town, my mind lit up as I remembered the conversion with Remy I had earlier. I started to grow concerned about the way he acted, especially in regards to how he stared blankly at me when I told him not to overwork himself."
m "Perhaps I had to make a trip to the library once more."

stop soundloop fadeout 4.0
$ renpy.pause (0.5)
scene black with fade
$ renpy.pause (3.5)
scene library at Pan ((640, 228), (0,228), 10.0) with dissolveslow
$ renpy.pause (3.0)

m "Upon arriving, I noticed that the library was the busiest that I'd ever seen it. There were dragons in practically every hallway that had bookcases. Despite the fact that it was busy, there were few sounds made, with the exception of a few children speaking slightly loudly with their parents, only to be followed with shushes."
m "Figuring Remy would most likely be in his office, I went there to look for him first before checking the other parts of the library."

$ renpy.pause (0.5)
scene kollibraryhall at Pan ((0, 250), (0, 250), 3.0) with dissolve
$ renpy.pause (1.5)
play sound "fx/knocking1.ogg"
$ renpy.pause (3.5)

c "(Huh, no response. Maybe he didn't hear me?)"
c "(I'm sure a small peek wouldn't hurt...)"

play sound "fx/door/door_open.wav"
$ renpy.pause (1.5)
scene office2 at Pan ((0, 228), (128,228), 3.0) with dissolveslow
$ renpy.pause (3.0)

m "I silently opened the door, finding Remy asleep on the bed in his office while surrounded by many open books."
$ renpy.pause (0.5)
m "I lightly touched Remy’s head, causing him to jolt awake in response."

show remy shy with dissolvequick
$ renpy.pause (1.0)
play music "mx/bubbles.ogg" fadein(2.0) #Yooooooo, that one unused track is finally being used!!! :O

Ry look "[player_name]? What are you doing here?"
c "Looks like it was my turn to wake you up."
Ry shy "I-I was just resting my eyes."
c "You rest your eyes with several books around you?"
$ renpy.pause (1.0)
Ry look "Alright, I fell asleep while trying to research some information. It's so boring going through the same sources over and over again, trying to figure out what the authors could and could not be implying."
c "That can’t be the only reason why you fell asleep, though."
Ry shy "I’m just tired, [player_name]. That's all."
$ renpy.pause (1.5)
Ry normal "I’m also guessing that you didn’t exactly come here just to wake me up."


menu:
    "I wanted to check up on you.":
        $ renpy.pause (0.5)

        Ry shy "Oh?"
        c "The conversation we had earlier made me a bit concerned about you, Remy. I decided to come here and see if you were okay."
        
        show remy look with dissolve
        $ renpy.pause (1.0)
        show remy shy with dissolve
        $ renpy.pause (0.5)

        Ry "Thank you, [player_name]."

    "No, the sole purpose of my visit was to see whether you were sleeping.":

        c "Considering the conversation we had earlier, I had a feeling you’d probably want to sleep from being overworked."
        c "So, I came here to wake you up, should that have been the case."
        Ry look "Oh..."
        Ry "Well, thanks, then."

    "I wanted to see the progress of your work so far.":
        $ renpy.pause (0.5)

        Ry look "Did Emera send you?"
        c "I came out of my own curiosity and interest."
        Ry "I see."

$ renpy.pause (0.75)
Ry normal "In any case, I better get back to work now that you’ve woken me up. That report won’t finish itself, I’m afraid."
c "No."

stop music fadeout (1.0)
$ renpy.pause (2.0)
play music "mx/fragments.ogg"
$ renpy.pause (0.5)

Ry look "No?"
c "I told you to take it easy, Remy. The fact that you fell asleep on the job is more than enough evidence that you’ve overworked yourself."
Ry "Please, [player_name]. Let me work this one time. I’m almost finished with the finer details of my report. It won’t take long."
$ renpy.pause (2.0)
c "…you’re trying to work so much to distract yourself from something, aren’t you?"
Ry shy "What?"

if kol_tlh_chapter1B_done == True and kol_tlh_2Bplayed == True and kol_tlh_3B_played == True:
    c "The way you’ve been acting recently: how you’ve shifted your mood during our time at the café before Adine came, how you seemed bleak after we baked that cake together, and how devoid you sounded after Adine went to the orphanage with Amely."
    c "With all of that, I’m guessing that you’re working yourself to the point where you can only think about work and not whatever is bothering you."

elif kol_tlh_chapter1B_done == True and kol_tlh_2Bplayed == True:
    c "The way you’ve been acting recently: how you’ve shifted your mood during our time at the café before Adine came and how you seemed bleak after we baked that cake together."
    c "With that, I’m guessing that you’re working yourself to the point where you can only think about work and not whatever is bothering you."

elif kol_tlh_chapter1B_done == True and kol_tlh_3B_played == True:
    c "The way you’ve been acting recently: how you’ve shifted your mood during our time at the café before Adine came and how devoid you sounded after Adine went to the orphanage with Amely."
    c "With that, I’m guessing that you’re working yourself to the point where you can only think about work and not whatever is bothering you."

elif kol_tlh_2Bplayed == True and kol_tlh_3B_played == True:
    c "The way you’ve been acting recently: how you seemed bleak after we baked that cake together, and how devoid you sounded after Adine went to the orphanage with Amely."
    c "With that, I’m guessing that you’re working yourself to the point where you can only think about work and not whatever is bothering you."

elif kol_tlh_chapter1B_done == True:
    c "I can't shake the feeling off ever since you shifted your mood during our time at the café before Adine came. You didn't seem like yourself when we talked about Amely, you know."
    c "With that, I can only guess that you're working yourself so much to avoid thinking about what's been bothering you. Whether it had something to do with Amely or not I'm not entirely sure, but that's besides the point."
    c "Something is bothering you, and I want to help with it."

elif kol_tlh_2Bplayed == True:
    c "I can't shake the feeling off ever since your sudden mood change after we baked that cake together. Besides, wanting to go to that dinner with Adine when there was still a lot of time left?"
    c "I'm sorry, but something didn't feel right. I'm thinking that you must be working yourself so much so that you can forget about whatever is on your mind."
    c "All I want to do is help you, Remy. Nothing less."

elif kol_tlh_3B_played == True:
    c "I'm still thinking a lot about how you felt the other day after Adine took Amely back to the orphanage. It was as if you were living in another world of your own or something."
    c "Is this why you're working so hard, Remy? To fill your mind with thoughts to hide whatever is bothering you, just like that daydream about raising children the other day?"
    c "Please, Remy. This isn't the way to deal with whatever is bothering you. Just give me the chance to help you."

else:
    c "You’re working yourself to the point where you can only think about work and not whatever is bothering you. At least, that's what I think right now."

$ renpy.pause (1.0)
Ry look "..."
$ renpy.pause (0.5)

c "Forgive me for sounding so harsh to you Remy, but I don’t want you to suffer like this."
Ry sad "I know, [player_name]. I know."
$ renpy.pause (0.5)
m "Remy trailed off in thought, leaving an eerie silence in his office. His eyes darted from left to right, as if trying to come up with a proper response to my accusations."

$ renpy.pause (1.5)
show remy shy with dissolvemed
$ renpy.pause (1.0)
stop music fadeout (2.0)

Ry "If you’re really afraid of my condition, then maybe you could help me with my research."
Ry "That is, assuming you don’t mind."
$ renpy.pause (0.5)
play music "mx/campfire.ogg"

c "Anything to help you not feel as if you’re carrying all the world’s burdens on your back."
Ry look "In a way, I kind of am."
c "Remy."
Ry shy "Okay, okay..."
$ renpy.pause (0.5)
Ry normal "Do you know how to make spreadsheets?"
c "It’s been a long time, but I think that I should be able to."
Ry smile "Well, this isn’t too complicated. You would just need to import and insert some data from my computer, as I’ve already made the spreadsheet."
Ry normal "Here, let me show you an example of what to do."

$ renpy.pause (0.5)
hide remy with dissolve
$ renpy.pause (0.5)

m "Remy booted his computer, and with a relatively soft fan spinning in the background, it showed the computer’s interface. On its background, I saw a red dragon that I didn’t recognise, though it looked similar to the one I saw in the photographs back in Remy’s apartment."
$ renpy.pause (0.5)
c "(Wait...{w=0.75} is that Amelia?{w=0.35} Her picture here does look similar to the pictures in Remy's apartment...)"
$ renpy.pause (1.0)
c "(Oh Remy, I'm so sorry...)"
$ renpy.pause (0.5)
m "Remy quickly opened a program and started to instruct me on what I should be doing. I was confused at first, but with Remy’s guidance, I quickly got the hang of the program."

$ renpy.pause (0.5)
show remy smile with dissolve
$ renpy.pause (0.5)

Ry "You’re quite the fast learner."
c "Only because I learned from a wonderful teacher."
Ry shy "Is that so? I can’t imagine myself being really good at teaching."
$ renpy.pause (0.5)
Ry normal "Well, in any case, I’ll be going through the library halls and gathering some additional things to verify the information that I’ll be presenting to the council. If you need anything, don’t hesitate to come and find me."
Ry shy "I already owe you enough as it is."
c "Don’t worry about paying me back, Remy. I’m happy to help you out."

$ renpy.pause (1.75)
show remy shy flip with dissolve
$ renpy.pause (0.5)
hide remy with easeoutright
$ renpy.pause (0.5)

m "Remy only shyly nodded and left the office, leaving me alone with his computer in front of me."
$ renpy.pause (0.5)
c "(And now, every office worker’s favourite thing to do. Praise be to spreadsheets, the foundations of the entire global economy before the solar flare.)"

scene black with fade
$ renpy.pause (5.0)
scene office2 at Pan ((128, 228), (128,228), 3.0) with dissolve
$ renpy.pause (3.0)

c "(Alright, that should be enough. My fingers are really going to hurt the next day after all this typing, aren’t they?)"
m "I sat and looked at the computer screen, staring at the work that I had managed to do. Everything was organised in a pristine manner, sure to appeal to even the most perfectionistic of dragons."
$ renpy.pause (0.5)
m "Deciding to give my body a break from all the sitting that I had done, I stood up from Remy’s chair and stretched. Just as I had finished stretching, I heard a knock on the door."
$ renpy.pause (0.5)
Ry look "[player_name], can you open the door for me, please?"

$ renpy.pause (0.5)
play sound "fx/door/door_open.wav"
$ renpy.pause (2.5)
show remy look with dissolvemed
$ renpy.pause (1.5)
show remy normal with dissolve
$ renpy.pause (0.5)
Ry "Thanks. It’s a bit hard to open the door when you’re carrying so much stuff."

menu:
    "Did you carry half the library with you?":
        $ renpy.pause (0.5)

        Ry look "How would I even begin with carrying so much in a single trip? I doubt that I’d even be able to carry an entire shelf’s worth of books."
        c "It was a joke, Remy."
        Ry shy "Oh..."
        Ry "Now I just feel dumb for not getting it earlier."

    "You really like to gather as much information as you can, huh?":
        $ renpy.pause (0.5)

        Ry look "When your entire civilization is on the line, you have to be as thorough as possible. If a minor error is made, such as something that cannot be verified using your primary sources..."
        c "Yeah, I get what you mean."
        Ry shy "So, better to do everything correctly the first time instead of having to do everything over again."

    "You could have just asked me to help you carry everything.":
        $ renpy.pause (0.5)

        Ry "I wouldn’t want to have you work on the spreadsheet and help me carry all of this."
        Ry smile "Otherwise, you might as well be an employee here at the library."
        c "You wouldn’t mind that in the slightest, would you?"
        Ry shy "It would certainly make things a bit easier."

$ renpy.pause (1.0)
Ry smile "And it looks like you’ve gotten the entire spreadsheet done. I’m honestly impressed at how fast you managed to complete it."
Ry shy "You’d definitely be a better candidate to work in my position than me should the position ever open up."
c "Like I said, I learned from a wonderful teacher."
$ renpy.pause (0.35)
m "Remy avoided my eyes, turning his head to try and hide his flustered appearance."
$ renpy.pause (0.25)
Ry "Well, thank you for getting it done nonetheless. I might be able to finish everything I need later today while still being relatively early for my due date."
Ry "Now, if you’ll excuse me, I need to get back to work."
c "Or you can take a short break first. You even said it yourself: you have enough time."
Ry "I…{w=0.5} suppose so.{w} Thank you, [player_name]."
Ry smile "Actually, how about I show you some gameplay of the video game on my computer?" #Video game time! Now with less interactivty!
c "The one that caused your computer to crash?"
Ry normal "Yes, that one."
c "I'd love to."

hide remy with dissolve
$ renpy.pause (0.5)

m "Remy loaded the game on his computer and sat down in front of his desk. After pressing some buttons, the game started. Remy started to explain some basic mechanics of the game, the story up until the point he had been playing, and many more details while I watched and listened with interest."
Ry smile "You see, in Marmoa, there’s this one person called Aaliyah the Ascended who serves as a tyrannical ruler of sorts. What makes him so powerful is that he has a human with magical divine abilities, as well as a massive army to enforce his position. So, to overthrow him…"

scene black with fade
$ renpy.pause (3.5)
scene office2 at Pan ((128, 228), (128,228), 3.0) with dissolve
$ renpy.pause (2.0)

c "You’re really good at this game, you know."
show remy shy with dissolve
$ renpy.pause (0.5)

Ry "Please, it’s just because of all the hours I’ve spent grinding."
Ry normal "Now, I’d love to show you more, but I really need to get back to work. I kind of lost track of the time."
c "No worries. I’m just glad that you got a chance to catch a breather."
Ry smile "And I’m happy that you were here to come visit me."
Ry normal "I'll let you know if anything comes up with the council or if there's anything I can do for you."
c "Noted."
c "Well, good luck getting everything done, Remy. It’s the final stretch, after all."
Ry "Indeed. Goodbye, [player_name]."
c "Have a nice day."
Ry smile "The same to you."

$ renpy.pause (1.0)
stop music fadeout (2.0)
scene black with fade
$ renpy.pause (0.5)

m "Satisfied with my check-up on Remy, I decided to go home and take the rest of the day off."
$ renpy.pause (0.5)
play sound "fx/steps/clean.wav"
$ renpy.pause (6.5)
scene kolapartmentnoon with dissolvemed
$ renpy.pause (2.0)

m "When I reached my apartment, I saw that Logan wasn’t sleeping outside any more."
$ renpy.pause(1.0)
play sound "fx/door/creaky.wav"
$ renpy.pause(4.5)
scene o at Pan((0, 0), (0, 250), 5.0) with dissolveslow
$ renpy.pause (3.0)

m "As I opened the door, I saw that Logan was sitting in front of a pile of sketches and notes while drinking a cup of coffee."

$ renpy.pause (1.0)
play music "mx/portal_kol.ogg"
show logan serious with dissolve
$ renpy.pause (0.85)

Lg "You could have told me that your apartment was locked, you know." #(Seething)
c "Hello to you too, Logan. I’m guessing that you slept well on the doorstep, no?"
Lg annoyed "Like a baby."
c "Judging from all the stuff you have laid out in front of you, I’m guessing that you didn’t sleep very long either."
Lg normal "You know how I am with sleep, [player_name]. I can get by with an absolutely minimal amount of sleep. Add that to a strong cup of Joe, and a sleep schedule becomes a sleep recommendation."
c "As if you had a sleep schedule to begin with."
Lg "If I did, I wouldn’t have done all of this."
m "Logan gestured to all the pieces of paper in front of him, showing a sense of accomplishment with his smile."
$ renpy.pause (0.5)
c "What are you up to now, Logan?" #What do you *think*, MC?

if kol_tlh_endingA_route == True:
    Lg "Well, I had a thought pop into my head recently. What if something goes wrong back home and shortens the time that we have here to redirect the comet?"
    Lg annoyed "I mean, Murphy’s Law has proven itself to be quite the bastard to me throughout the years, so it’s a safe assumption to make."

    if kol_tlh_tld_crossover == True:
        Lg serious "So, what if I take the information that you have in your PDA, as well as some parts from the dragons, and upgrade the generator we brought through the portal? It would be able to power a significant portion of the city while also being pretty damn stable."

    else:
        Lg serious "So, what if I take the information that you have in your PDA, as well as some parts from the dragons, to upgrade the generator I took with me the other day? It would be able to power a significant portion of the city while also being pretty damn stable."

    c "But what if that doesn’t work out? Should the generator back home break due to your tampering, we’d essentially throw all our work away."
    Lg "I’m willing to take that risk. Double or nothing, as they say."
    $ renpy.pause (0.5)
    Lg "I know that we have taken a hell of a lot of risks as of late, but I have a gut feeling that we need to go through with this one as well. As we stand right now, should the energy demand ramp up back home, that generator won’t be enough."
    Lg "Besides, there’s still the base generator that I made for humanity to rely on should something seriously wrong happen."
    c "Are you sure of this, Logan?"
    Lg annoyed "If this doesn’t work, then the prototype generator with all the extra parts should keep humanity going long enough for the comet to be redirected."

    $ renpy.pause (0.5)
    show logan serious with dissolvemed
    $ renpy.pause (0.5)

    Lg "So yes, I’m sure."
    c "And what about the authoroties? I don’t think they’d approve of you going back to upgrade the generator."
    Lg "The dragon council most definitely wouldn’t have approved of what we’ve done, yet here we are. Besides, I’m sure they'll agree to more stability for the city."
    Lg annoyed "Even if I’m disobeying his orders for me to stay here."
    $ renpy.pause (0.5)
    c "Everything you’ve done so far has worked out…"
    $ renpy.pause (1.5)
    c "Alright, Logan. I’m in."
    Lg normal "Right. Thanks for believing in this, [player_name]."
    Lg annoyed "So, I believe that the underground facility that you mentioned might have some parts worth checking out. If what you told me about the generators in there is correct, then surely there would have to be parts for them as well."
    c "Just be careful, though. The underground facility is extremely dangerous, with several water pockets around it that might cause the entire building to flood."
    Lg serious "I'll be careful."
    $ renpy.pause (0.5)
    Lg "You know, perhaps it’ll be better if I check it out right now. The faster I scout the area, the sooner we can upgrade the generator back home and the more time we’ll have."
    Lg "I’ll just leave my notes here for me to finish later. There's no point continuing if the part you need to theorise about doesn’t even exist."
    Lg "You coming along, [player_name]?"
    c "I’ll have to pass. I need to get some sleep myself. It’s been a pretty busy day."
    Lg annoyed "I can imagine."
    Lg normal "Well, enjoy your nap. I’ll do some exploring and then make a visit to that pesky politician."
    c "Good luck."

    $ renpy.pause (0.5)
    show logan normal flip with dissolve
    hide logan with easeoutright
    $ renpy.pause (0.5)

    m "Logan started to walk out of my apartment, but as I suddenly remembered something, I called out to him."
    c "Wait."

    $ renpy.pause (0.5)
    show logan annoyed at Position (xpos = 0.85) with easeinright
    $ renpy.pause (0.5)

    Lg "Yeah?"
    c "There will be police on guard at the underground facility. You know, to prevent people from entering due to how dangerous it is."
    Lg normal "Noted. I’ll find a way around them."

    $ renpy.pause (0.5)
    show logan annoyed flip with dissolve
    hide logan with easeoutright
    $ renpy.pause (1.0)
    play sound "fx/door/doorclose.ogg"
    $ renpy.pause (1.0)

    m "With nothing else to do, I decided to rest my tired mind in preparation for whatever Logan might come up with for his master plan."

    jump tlh_Chapter4A_skip

else:
    Lg "Well, I’ve had a thought that goes something like this: what if the generator I had made suddenly broke, leaving everyone back home at square one? I mean, nobody would be able to repair it if something went wrong."
    Lg serious "And it’s not like I had the chance to make a second one, either. It was too great a risk without knowing if the first one would actually work."
    Lg "You said that there should be two generators in the underground facility and not one, right? A main one, and one to serve as a backup, correct?"
    c "Yeah, but we need both if the dragons are to be able to deflect the comet."
    Lg normal "What if I told you that having both generators might not be necessary?"
    c "Excuse me?"
    Lg serious "I’ve been theorising for most of the day at this point that the generators in the underground facility are able to be overcharged, increasing their generating capacity by at least threefold."
    Lg annoyed "With the blueprints I analysed from the production facility, your notes that you made during your research at the library, and what we have back home, I could probably rig something together that would be able to combine the best of everything."
    Lg serious "This of course carries a huge risk, but if we succeed, then we might be able to secure humanity for months if your description is anything to go by. All the while, dragonkind can get their asteroid deflected."

    menu:
        "How would you even go about this?":
            $ renpy.pause (0.5)

            Lg annoyed "I’m still thinking about that. I’ll obviously have to get parts, which I’m assuming I might find in the underground facility. It wouldn’t make sense that spare stuff wouldn’t lie around there."
            Lg "I, uh, still need to think everything through. This plan is still in its infancy, after all."

        "Why do you always come up with such elaborate schemes?":
            $ renpy.pause (0.5)

            Lg "Because I want the best chance of survival for humanity. Simple as that."
            Lg thinking "Though, the dragons have started to grow on me as well."
            Lg normal "Anyway, screwing around with complicated stuff is way more fun than just following a generic step-by-step plan that everybody else does. So, why not come up with something more interesting and hopefully more effective?"

        "And you came up with all of this while I was gone?":
            $ renpy.pause (0.5)

            Lg smiling "A sleep-deprived brain with coffee pumping through it does wonders for your creativity in a short amount of time."
            c "I... {w=0.5}doubt that."
            Lg normal "Feel free to be as jealous as you want."

    $ renpy.pause (1.0)
    c "So, when will your next master plan take place?"
    Lg annoyed "So far?{w} Tonight."
    c "Wait, what?!" with hpunch
    Lg "The comet is supposed to hit very soon, no? Why would you want to waste time by just being a sitting duck?"
    c "But you {i}just{/i} came up with the plan. Shouldn’t it be necessary to test it first?"
    Lg normal "I’ve pulled off crazier stuff with less time. You just need to ask my university professors."
    Lg serious "That was, if they were still alive."
    Lg annoyed "But I digress. The sooner we get this done, the better. I want to finish my notes here and then take a look at the underground facility shortly. Mind coming along?"
    c "I think I need some rest myself. It’s been a really busy day for me."
    Lg normal "Figured. Maybe I should lock you out so that you can sleep outside while I’m gone."
    c "You’re not going to let this go, are you?"
    Lg "Nope."
    $ renpy.pause (0.5)
    Lg serious "Any advice you can give me about the underground facility beforehand?"
    c "Only that it’s near the portal. It’s also surrounded by water pockets, so it’s unsafe to explore. The police are supposed to prevent anyone from entering."
    Lg annoyed "I have my ways of getting past that. Though the pockets of water do concern me a bit, as anything that might go wrong underground–{w=4.0}{nw}"
    c "–will cause the building to flood due to an explosion from the generators, causing us to be stuck here with no way to power the portal."
    stop music fadeout (1.0)
    $ renpy.pause (3.0)
    Lg serious "You'd either have to know some intense theory for that conclusion, or you need to have personal experience of such an event happening." #Ooooooo, MC done messed up.
    Lg "Anything you want to tell me, [player_name]?"
    $ renpy.pause (1.0)
    c "Sorry. I don’t know what came over me for a second."
    $ renpy.pause (0.5)
    c "(Why is my head aching all of a sudden? This doesn't feel right in the slightest.{w} Wait, is \“right\” even the correct word?)"
    $ renpy.pause (0.5)
    Lg "..."
    $ renpy.pause (0.5)
    Lg annoyed "For now, I’m off to the underground facility, and then I’ll properly announce my return to Emera. I’ll leave my notes here for now." #Just carry on like you saw nothing, Logan.
    c "I think I need to sleep {i}right now.{/i} I’m not feeling well all of a sudden."
    Lg serious "Alright. Take care of yourself, [player_name]. See you when I’m back."
    c "Bye."

    $ renpy.pause (0.5)
    show logan annoyed flip with dissolve
    hide logan with easeoutright
    $ renpy.pause (1.0)
    play sound "fx/door/doorclose.ogg"
    $ renpy.pause (1.0)

    m "Logan left the living room and went outside, stopping momentarily before closing the door. With my sudden headache making complex thoughts hard, I decided to climb in bed and rest, hoping that the headache would soon pass."

    jump tlh_Chapter4A_skip



label tlh_Chapter4A_skip:

$ renpy.pause (1.0)
scene black with fade
stop music fadeout (2.0)
$ renpy.pause (4.0) 
scene o2 at Pan((0, 250), (0, 250), 4.0) with dissolveslow
$ renpy.pause (1.0)

m "I slowly woke up, feeling awake but not rested. As I looked around me, I was surprised to see that it was already dark outside."
$ renpy.pause (0.5)
c "(Was I really {i}that{/i} exhausted?)"

if kol_tlh_endingA_route == False:
    $ renpy.pause (1.0)
    c "(Well, at least my headache is gone now.)"

m "I slowly made my way to the living room, where I saw Logan hunched over the table with more notes than before. He looked up at me with a grin as soon as he heard my footsteps."

$ renpy.pause (0.5)
show logan normal with dissolve
play music "mx/bolt_kol.ogg"
$ renpy.pause (0.5)

Lg "Welcome to the world of the living. Did you enjoy your several hour \"nap?\""

menu:
    "Could have been better.":
        Lg "Let me guess: you slept poorly but also well enough that you feel awake?"
        c "Something like that, yes."
        Lg "Then that’s good enough for what we’re going to do."

    "I didn’t expect to have been out for this long.":
        $ renpy.pause (0.5)

        Lg annoyed "Neither did I. You must have had quite the day to have slept for as long as you did."
        Lg normal "At least you should be well rested enough for what we’ll be doing now."

    "You could have woken me up sooner, you know.":
        $ renpy.pause (0.5)

        Lg "See, that would have been rude of me to wake you up when you slept like a cosy toddler after having spent an entire day in a ball pit."
        c "That’s… an interesting comparison."
        Lg annoyed "Yeah, it kinda is. At least it gets the point across."
        Lg normal "But I digress. You’ve gotten more than enough rest for what's in store tonight."

$ renpy.pause (0.75)
Lg annoyed "Unsurprisingly, the underground facility did yield some interesting results."

if kol_tlh_endingA_route == True:
    Lg "I found some spare parts that might be pretty damn useful. Hell, they were even neatly labelled for me. It’s just a shame that most of them have faded to the point where they’re barely legible."

else:
    Lg "I found the two generators as well as some spare parts. Hell, the parts were even labelled, believe it or not. Sure, they’re faded, but they’re still legible, even if I need to strain my eyesight to read them."

Lg "I took some notes of the stuff I found, worked on a few things here and there, and came up with a plan. Let’s just hope that everything goes smoothly."
c "What a time to be having second thoughts."
Lg serious "Please, [player_name]. Do you really think that I can do anything and everything without being remotely concerned? I’m still human, you know." #Woah, Logan showing vulnerability for once? Damn, that's rare.

$ renpy.pause (0.75)
show logan annoyed with dissolve
$ renpy.pause (0.75)

Lg "*sigh*"
Lg "Let’s just go through the plan, shall we?"

$ renpy.pause (1.5)
if kol_tlh_endingA_route == True:
    Lg serious "We’re lucky enough that I already gathered all the parts that I need, so this is just a simple in-and-out mission."
    Lg "Problem is, the parts are damn heavy, so I’ll need help carrying them to the portal quick enough before our grace period ends."

    if kol_tlh_tld_crossover == True:
        Lg normal "And if you’re willing, I’d want to have you along while I upgrade the generator back home. The faster we get that over with, the better."

        menu:
            "I’ll gladly help.":
                $ renpy.pause (0.5)

                Lg normal "That’s what I counted on."
                $ kol_tlh_tld_crossover2 = True

            "I’d rather not.":
                c "We’re already risking far too much on this. If I went with you again, it would only increase the risk of somebody finding out what’s really going on."
                Lg annoyed "Fair, I suppose. I guess you’ll just have to help me carry the stuff through instead of coming with me."

    else:
        c "Of course."
        Lg normal "Thanks."



else:
    Lg "If I’m correct, there will be a few minutes that we have to enter the underground facility while the shifts for the police officers change. This change should happen in about ten minutes."
    Lg serious "We’d then have to do as much as we can in about an hour, as I’m sure that the officers would probably want to patrol the inside of the facility as well."
    c "But why an hour?"
    Lg annoyed "It’s more of an educated guess, if anything. Might be more, might be less. An hour just seems good enough of an estimation to make."
    Lg serious "I’ve also gathered all the parts I could in one place to avoid wasting time."
    Lg normal "If everything goes according to plan, we’d be able to successfully overdrive a generator while also scoring humanity a suitable backup in case things go south."
    Lg annoyed "…which might actually be more likely than you might think. Surprisingly, generators made from parts that were on the brink of death are pretty unstable. Who would’ve thought?"


$ renpy.pause (1.0)
Lg serious "Well, I’ve talked enough. We need to get going."
c "Lead the way."

$ renpy.pause (0.5)
hide logan with dissolve
$ renpy.pause (0.5)
m "Logan stood up and stretched slightly before opening the door to my apartment. As nervousness started to rise within me about the possibilities of what might soon happen, I slowly followed after Logan into the cold night."
$ renpy.pause (1.5)

scene np5 dk with dissolve
play sound "fx/steps/rough_gravel.wav"
$ renpy.pause (2.5)
scene np4 with dissolve
$ renpy.pause (2.0)
scene np3 with dissolve
$ renpy.pause (2.0)
show np2 dk with dissolve
$ renpy.pause (2.0)

m "I couldn't help but be concerned as we pushed through the dark roads. Will Logan's plan succeed and ensure humanity's survival, or will we break dragonkind’s last limb?"
$ renpy.pause (1.0)
stop music fadeout (2.0)
show logan serious dk with dissolve
$ renpy.pause (0.5)

Lg "[player_name]?"
c "Yes?"

play music "mx/ghost_town_kol.ogg" fadein (1.0)

Lg "I’ve come to realise something. {w}Should I fail, then you can just use the portal to try again, right? That means that I don’t really have to worry about failure too much." #There we go. He figured it out.
Lg normal dk "Because you’d just be able to try again and again until you got the perfect result."
c "How do you know all of this, Logan?"
Lg "Because you just told me." #I wonder if you can get this reference. :)
$ renpy.pause (2.0)
c "..."
$ renpy.pause (1.0)
Lg serious dk "In all seriousness, I had a hunch that the dragon’s world just had to be related to ours in some way considering all the similarities like the moon, the plants, the fact that dragons can speak English..."
Lg "The list honestly goes on and on."
Lg "All I needed was your confirmation. I figured that I might as well try the classic \"travelling back in time\" approach to get the most unlikely possibility out of the way." #Can't forget MC's slip of the tongue earlier.
Lg normal dk "Turns out that time travel was our reality, as weird as that might have been."
c "I see."
c "In that case, to make a long story short, yes, I can try again. The reason why it can only be me is complicated, though."
$ renpy.pause (1.0)
Lg annoyed dk "…{w=0.8}wait."
Lg "This isn’t the first time you’ve done this, is it? You know, the whole thing with Reza and whatnot." #See: my previous comment.

menu:
    "I… don’t know.":
        $ renpy.pause (0.5)

        Lg "Hmmm..."
        Lg serious dk "Ah.{w} Well, let’s hope that this attempt is the last one."

    "Probably not.":
        $ renpy.pause (0.5)

        Lg serious dk "I’m assuming that you can’t remember any of your previous attempts then?"
        c "Yes and no. It’s complicated."
        Lg "I expected as much. I mean, why would time travel ever be simple?"
        Lg normal dk "Well, maybe you don’t have to do all of this again. Maybe this will be your perfect result, whatever that is."

    "It’s better if you don’t know.":
        $ renpy.pause (0.5)

        Lg serious dk "Perhaps you’re right. Regardless, let’s hope that you don’t have to go back in time."

$ renpy.pause (1.0)
if kol_tlh_endingA_route == True:
    Lg annoyed dk "I do hope that I can pull the upgrade off back home. Sure, I might have a ton of resources at my disposal, but there’s a feeling of uncertainty that drags me down."
    Lg "Perhaps it’s because of all the stakes, or perhaps the desire to help humanity is influencing me so much that I'm getting anxious about failing everyone back home."
    c "You’ll be able to do it, Logan. After all, you’re basically a mad genius with a strong set of values and morals."
    Lg "…thanks? I wouldn’t exactly call myself a mad genius, but perhaps you’re on to something."
    $ renpy.pause (0.5)
    Lg serious dk "I'm not going to fail. For humanity’s sake."
    $ renpy.pause(1.0)
    Lg normal dk "…and dragonkind’s."
    $ renpy.pause (0.5)

else:
    Lg annoyed dk "In the meantime, I’ll try my best with this. After all, dragonkind—and, by extension, humanity—is depending on us. I can’t screw up here by messing with the generator."
    c "You’ll be able to do it, Logan. After all, you've come this far, so why doubt yourself now?"
    Lg "I guess you do have a point."

$ renpy.pause (0.5)
scene np1o at Pan((100, 0), (500, 150), 6.0) with dissolveslow
$ renpy.pause (5.5)
show logan serious dk with dissolve
$ renpy.pause (0.5)
stop sound

Lg "And we’re here. Looks like we made it just on time. Look."
m "As I stared at the portal in the distance, I saw a dragon I didn’t recognise walk away from the portal. They stopped, took a few steps back, and flew into the skies."
Lg "Are you ready, [player_name]?"
c "My body is ready."
Lg "Then let's go."

$ renpy.pause (0.5)
hide logan with dissolve
$ renpy.pause (0.5)
m "We approached the portal, which stood tall underneath a canvas of a deep, dark blue. Logan wasted no time, going immediately towards the entrance of the underground facility. I followed suit, not wanting to waste more of our precious time."
$ renpy.pause (1.5)
scene hallway at Pan((0, 0), (0, 150), 3.75) with dissolvemed
$ renpy.pause (2.0)
m "The familiar, cold fluorescent lights greeted me just as they did when I first came to the underground facility. Memories of what had happened here—memories that I tried to avoid—came flooding back to me."
stop music fadeout (2.0)

if kol_tlh_endingA_route == True:
    jump tlh_Chapter4_EndingA


else:
    $ renpy.pause (0.5)
    show logan serious with dissolve
    $ renpy.pause (0.5)

    Lg "So...{w=0.75} remind me:{w} this is where the whole Reza thing happened?"
    c "That's correct."
    Lg annoyed "I find it eerie that this place is strikingly similar to what the city had pre-solar flare, yet also seems… different. As if the technology here was reserved for something."
    
    $ renpy.pause (1.5)
    show logan serious with dissolve
    $ renpy.pause (2.5)

    Lg "Tell me, [player_name]. Did Maverick kill Reza here, or somewhere else?"
    Lg serious "And don’t try to lie to me by saying that Maverick didn’t kill Reza."
    c "What is it with you and suddenly figuring a bunch of stuff out?" #Because I was probably running out of ideas when I originally wrote this and decided to make Logan becomme omniscient or something idk.
    Lg "My question first."
    $ renpy.pause (1.5)
    c "Yes, he killed Reza, but outside next to the portal. Not within the building itself."
    Lg "I see."
    $ renpy.pause (1.5)
    Lg "Now, for your answer: I thought that it was finally time to reveal what I had been thinking for some time. Hence, the time travel discussion we had just now."
    Lg "Did you really think that I would believe that a feral dragon would somehow find its way inside here to kill Reza?"
    Lg "And besides, if Reza {i}had{/i} died outside, did you think that just {i}anybody{/i} would randomly show up? Did you forget how remote the portal actually is? Even the forest is quite a way from the portal itself."
    $ renpy.pause (0.5)
    Lg "There were gaps in your report right from the start. I somehow figured that something had to be off, as if you were hiding something."
    Lg "Sure, I kept my suspicions to myself just to see where this would go, but you really have to work on your lying in the future. Just be lucky that the authorities were too angry to have noticed the gaps."
    c "That doesn’t explain how you pointed it to Maverick, though."
    Lg " I thought that whoever killed Reza must have been important enough to be worth hiding from humanity. All I did was a bit of careful listening and a few mental deductions."
    Lg normal "Remember when I said that you could expect chaos at the police office before I originally went away? That conversation I had with Bryce was the final point I needed to figure out who Reza’s killer was."
    c "Leading you to tell Bryce about a fake report, giving yourself enough time to transport the parts and blueprints through the portal."
    Lg "Exactly. One thing then led to another, and now we’re here."
    Lg annoyed "Honestly, I’m thankful in a way that Maverick did what he did. If it was revealed that a police officer killed Reza, the trade would have been stopped right then and there, if not worse."
    c "He had the same logic that you have right now."
    Lg "Really now? Interesting…"

    if kol_tlh_mavstillofficer == False:
        $ renpy.pause (0.5)

        c "Regardless, Maverick lost his job because of you, Logan."
        Lg serious "But it was a sacrifice he was willing to make, no? It was either that, or humanity wouldn’t have gotten those extra resources. Besides, Maverick seems like the type who knew what the repercussions would be for his actions should he go through with it."
        $ renpy.pause (0.5)
        Lg annoyed "And he did. Despite knowing he’d be fired, he still continued to hide everything for the sake of the trade. I have nothing but respect for him."
    
    $ renpy.pause (0.5)
    Lg serious "Enough talking, though. We’re wasting time. Follow me to the generator room."
    c "Sure."

    $ renpy.pause (0.5)
    scene kolmorefacility with dissolve
    $ renpy.pause (1.5)
    show logan annoyed with dissolve
    $ renpy.pause (0.5)
    play music "mx/down_the_well_kol.ogg" fadein (1.0)
    $ renpy.pause (0.5)

    Lg "Now, at first glance, that generator over there seems to be the main one. The backup is hidden behind a metal plate next to the main one. I’m guessing that both of them work side by side if they converge to one power output."
    Lg "What intrigues me more, however, is the fact that the backup generator is still completely intact, while the main one has a few loose wires around it. I’m guessing this was the one that Reza ripped out, right?"
    c "Seems like it. I don’t know why Reza would decide to take the main one instead of the backup generator, though."
    Lg serious "Because…{w=0.4} it gives more power. Why would you take the weaker one when you have to provide an energy source for your dying home?"
    Lg "I thought that this would be common sense, but apparently not."

    menu:
        "Yeah, I didn’t think through what I said.":
            $ renpy.pause (0.5)

            Lg annoyed "A common issue among many, believe it or not. I don’t blame you for it, either. Sometimes you can just be in the moment and blurt something out, or overthink something to such a degree that the most reasonable conclusion eludes you."

        "Maybe I shouldn’t help out if this is what comes out of me.":
            $ renpy.pause (0.5)

            Lg "Eh, don’t blame yourself. We all have slips of the tongue like that."
            Lg normal "Besides, you’re still useful in the form of labour."
            c "How fun."

        "Well, they do say that common sense is a blessing.":
            $ renpy.pause (0.5)

            Lg "Not when you have to use common sense against something or someone senseless."
            Lg annoyed "Well, I’m sure that your mishap was a one-time thing."
    
    $ renpy.pause (0.85)
    Lg serious "I’ve already arranged some tools that I found around here in a neat little pile, so we don’t need to waste more time getting some stuff."
    Lg annoyed "…unless something unforeseen happens, but those are problems for later."
    c "So, how can I help you out?"
    Lg "See that dusty file there? That file contains documented information about these generators. How those have survived or why they’re here baffles me, but I guess it’s cool that they exist for our convenience."
    Lg serious "I’ll need you to go through it while I start the process of upgrading the main generator. From what I’ve skimmed through, there will be a bunch of things that need to be monitored while working on this."
    Lg "This would have been much better if we had a specialised engineer of sorts to help us out, but I guess that we can’t be that lucky."
    c "(Wait, wouldn’t the Administrator be able to help?)"
    $ renpy.pause (1.5)
    c "(Now that I think about it, where {i}is{/i} the Administrator? I haven’t seen her in quite a long time…)"
    $ renpy.pause (0.5)
    c "(Her? How do I even know the Administrator is a {i}her?{/i})" #Timeline memory stuff being wack, that's how.
    Lg "Hey, [player_name], are you still here? You look like you just left your body or something."
    c "Yeah, I'm alright."
    Lg annoyed "Sure..."
    $ renpy.pause (0.5)
    Lg serious "Anyway, you’ll have to monitor the temperatures, electrical outputs, and anything else that might cause a spark or two. Of course, general stability levels are necessary, considering that these are some pretty advanced generators, even by our standards."
    c "Alright, I’ll go through the file while you start working on the generator."

    $ renpy.pause (0.5)
    hide logan with dissolve
    $ renpy.pause (0.5)

    m "Logan only nodded in response. I thought I saw what appeared to be a glimpse of a faltering confidence, but whether that was just my mind playing tricks on me, I couldn’t tell."
    $ renpy.pause (1.5)
    m "I went to the file and slowly picked it up, afraid that I might accidentally damage it. Almost every page seemed to have some coat of dust, with some pages being more visible than others. Trying to understand what the file contained, I read through the pages as thoroughly as I could."

    scene black with fade
    $ renpy.pause (3.5)
    scene kolmorefacility with dissolve
    $ renpy.pause (0.5)

    c "(So, if what I read is correct, then I need to guide Logan on the current temperatures by telling him to work on the heat sinks. Electrical outputs should be checked if something seems to be buzzing ever so slightly.)"
    c "(In addition, I need to have my eyes open for any open wires that might cause a spark. All while keeping the average stability in check by letting Logan know that he’s about to risk something important.)"
    c "(Apparently there's a meter on the generator that should show me the chance of something failing for each part I need to check.)"
    c "(If anything on that meter goes into a critical state and isn’t fixed {i}immediately,{/i} then…)"
    $ renpy.pause (0.5)
    c "(I don’t want to think of what might happen.)" #Kaboom.
    $ renpy.pause (1.0)
    c "(I think I’m ready to monitor Logan’s progress. Let’s hope that we’re successful.)"
    stop music fadeout (2.0)
    $ renpy.pause (2.5)
    play music "mx/plan_b_kol.ogg" fadein (1.0)

    jump kol_tlh_boosting_generator #This is totally not inspired by a certain minigame in another mod that people totally don't despise. Nope, not at all.



label tlh_Chapter4A_continued:

$ renpy.pause (2.5)
stop music fadeout (4.0)

m "As we continued to work on the generator, I could hear a noise coming from afar. My attention perked up almost instantaneously as anxiety and panic filled my veins."
c "Logan."
Lg serious "Not now. I need to concentrate."
c "I think somebody is coming."
$ renpy.pause (0.5)
show logan surprised with dissolve
Lg "I can’t stop now! I need to at least finish the part I’m currently busy with for me to actually be able to step away from this damn thing safely!" with vpunch
Lg serious "You’ll have to stall as long as you can. As soon as I’m done, I’ll find somewhere to hide in the facility."
Lg "Now go!" with vpunch

hide logan with dissolve
$ renpy.pause (0.5)
m "Logan went back to working on the generator at a notably increased speed, softly swearing under his muffled breath as I walked outside of the room and into the hallway."

$ renpy.pause (0.5)
scene hallway at Pan((0, 150), (0, 150), 3.75) with dissolvemed
$ renpy.pause (1.5)

m "I walked down the corridor, hoping to see what had caused the noise that I had heard. I was starting to think that whoever had entered had left, until a door at the end of the hallway opened up."

$ renpy.pause (1.5)
show remy look with dissolvemed #Why the hell did Remy even decide to go in the building itself when he knows that it's supposed to be under constant surveilance? Hmmmm...
$ renpy.pause (0.5)
play music "mx/soul.ogg" fadein (2.0)
$ renpy.pause (1.75)

Ry "..."
$ renpy.pause (0.5)
c "..."
$ renpy.pause (0.5)
Ry "I...{w=0.5} didn’t expect to see you here, [player_name]."
c "Neither did I."

if kol_tlh_3B_played == False:
    Ry "And to think we'd meet again like this after such a long time since we had the chance to properly talk to each other."

$ renpy.pause (1.5)
Ry "Might I ask what exactly you’re doing here?"

menu:
    "I was going on a trip down memory lane.":
        $ renpy.pause (0.5)
        show remy sad with dissolvemed
        $ renpy.pause (0.5)

        Ry "I see."
    
    "I was inspecting the underground facility.":
        $ renpy.pause (0.5)

        Ry "But why?"
        c "I wanted to see if anything had flooded since the Reza incident or if anything had been damaged that might prevent the portal from being used."
        Ry "I see."

    "I wanted to see if Logan was here.":
        $ renpy.pause (0.5)

        Ry "Wait, Logan is back?"
        c "Yeah. He announced his return earlier today to Emera."
        $ renpy.pause (1.5)
        Ry "I’m guessing that he isn’t here, then?"
        c "I haven’t found him yet."
        Ry "I should have expected it."

$ renpy.pause (1.0)
c "And why are you here, Remy? Aren’t you supposed to be working tomorrow? It seems strange that you’d be up so late on a workday."
Ry shy "I wanted to see if anything had changed since we confronted Reza. It doesn’t seem that way, though." #Excuses.
c "How come?"

$ renpy.pause (0.5)
show remy look with dissolvemed
$ renpy.pause (0.85)

Ry "I... {w=0.6}have my reasons."
c "Alright then. Anything that I can do for you?"
Ry "Not now, I’m afraid. I just needed some alone time in the middle of the night to get my mind off of things. Ideally, I’d like to keep it that way."
Ry normal "Though, I’m sure we could spend some time together outside. The fresh air would do us good."
c "Sure."

$ renpy.pause (2.5)
scene np1r flip at Pan((100, 100), (100, 100), 6.0) with dissolvemed
$ renpy.pause (2.0)
show remy normal dk with dissolve
$ renpy.pause (1.0)

Ry "You know, I don’t think that we ever spent a night together before except on the night of the fireworks. I’ve been wanting to arrange something like this for quite some time, but with our busy schedules, it just won’t be wise."
Ry smile dk "Besides, I’ve always been a fan of the night more than the day. The tranquillity one could experience when the world was sleeping is almost cathartic, in a way."
Ry normal dk "If only it could be like this during the day as well."
c "If the day were as peaceful as the night, then nothing would ever get done."
Ry "I suppose that's fair."
$ renpy.pause (1.0)
Ry "May I ask you a question?"
c "I'm all ears."
Ry smile dk "I thought that you were a human, not a bunch of ears." # :D

menu:
    "Nice one.":
        $ renpy.pause (0.5)

        Ry "Thanks."

    "You got me. I’m secretly a bunch of ears disguised as a human.":
        $ renpy.pause (0.5)

        Ry normal dk "Now {i}that{/i} I want to see."
        c "Maybe some other day. It’s a bit of a hassle to show my true form."
        Ry smile dk "Then I’ll patiently wait for the opportunity."

    "What’s next? Something about noses?":
        $ renpy.pause (0.5)

        Ry smile dk "Who nose?"
        c "I set myself up for that, didn’t I?"
        Ry "You did."

$ renpy.pause (1.0)
Ry normal dk "Now, my question: what would you do if you couldn’t go back to your world?"
c "I’m not entirely sure. If something were to happen to the portal, then I guess I would stay here until the portal gets fixed."
c "Though, I’m sure you’d like it if I stayed here."
Ry smile dk "I just have an interest towards humans, that's all."
Ry look dk "I do hope that losing the connection to the portal on the other side doesn’t happen, though. I know how much you care about humanity, so if it turned out that you couldn’t go back home, then I’m sure you’d be heartbroken."
c "Yeah, let’s hope that it doesn’t happen. We already both put so much effort into keeping everyone safe. It would be horrible if all of that went to waste."
Ry "Indeed."
$ renpy.pause (0.5)
show remy sad dk with dissolve
$ renpy.pause (0.5)
m "Remy stayed silent for a moment, looking skyward to the waning moon in the sky. As I stood next to Remy, I noticed a small tear falling from Remy’s cheek."
$ renpy.pause (0.5)

menu:
    "[[Hug Remy.]": #Damn, I have a lot of moments in this mod where I hug Remy, huh? Not that it's a bad thing, of course...
        $ renpy.pause (0.5)
        hide remy with dissolve
        $ renpy.pause (0.5)

        m "Not wishing to see Remy sad, I suddenly threw my arms around his neck and hugged him softly. Remy was visibly taken aback by my gesture, looking away for just a brief moment before resting his chin on my shoulder."
        $ renpy.pause (0.5)
        Ry shy dk "I wasn’t expecting this all of a sudden."
        c "I figured that it was a good time to give you a hug, that’s all."
        Ry shy dk "Thank you, [player_name]."
        $ renpy.pause (0.5)
        m "We stood there in silence for a while longer, embracing the warmth of our bodies in the midst of the cold night. The warmth started to spread deep within my soul, calming whatever troubles I may have had seconds prior."
        $ renpy.pause (0.5)
        m "However, as all things must come to an end, we eventually separated, standing in isolation once more."

        $ renpy.pause (0.5)
        show remy shy dk with dissolveslow
        $ renpy.pause (0.5)

        Ry "Perhaps we should meet each other more at night if this is what happens."
        c "We can meet anytime we want, though."
        Ry "But I suppose something like this would make an already wonderful time of day simply more wonderful."
        c "True."

    "[[Watch in silence.]":
        $ renpy.pause (0.5)

        m "Deciding to let Remy have this moment to himself, I stood silently and watched him. He only seemed to have shed another single tear before stopping to look away from the moon and into the distance."
        $ renpy.pause (0.5)
        m "Remy almost immediately looked away again, as if he were trying to look away from something. A few moments had passed before he looked at me again."
        $ renpy.pause (0.5)
        Ry "My apologies. I just remembered something, that’s all. No need to worry."


$ renpy.pause (1.0)
Ry look dk "You know, I should probably go back home and try to get a relatively decent night’s sleep. I’m sure you can figure out why."
c "I understand. Well, it was nice talking to you regardless."
Ry normal dk "The feeling is mutual. Good night, [player_name]."
c "Night, Remy."

$ renpy.pause (0.5)
hide remy with dissolvemed
stop music fadeout (4.0)
$ renpy.pause (1.0)

m "Remy slowly walked into the distance instead of taking off like how I thought he would."
$ renpy.pause (0.5)
m "My short time with Remy had made me completely forget about the generator, however. Hoping that nothing bad had happened while I was away, I cautiously walked back into the underground facility."

$ renpy.pause (0.5)
scene hallway at Pan((0, 150), (0, 150), 3.75) with dissolvemed
$ renpy.pause (1.5)
c "(Nothing looks or sounds damaged, so that’s good so far.)"
$ renpy.pause (1.0)
show logan serious with dissolve
$ renpy.pause (1.0)

Lg "Welcome back. Considering that you were away for so long, I’m guessing that it was quite a serious matter." #Yes. Hugs are a very serious matter.
c "Not really, but that’s besides the point. Are you finished?"

if kol_tlh_chapter4_minigame_win == True:
    $ renpy.pause (0.5)

    Lg smiling "Pretty much. I’ll still check up on a few things whenever, but the core upgrades should be functional. I'm confident that the generator is powerful enough to compensate for the loss of the backup generator, so that's neat."

else:
    $ renpy.pause (0.5)

    Lg "I’m afraid not. Considering that you had to leave me while the generator was in a critical state, I had to redirect my attention to fixing that instead. Thing is, I don’t think that I’m able to do the rest tonight, especially considering the possibility that the cops should be back any time soon."
    Lg annoyed "Who would have guessed that the files documenting all of this seem extra convoluted when you were in a hurry?"
    c "Sorry about that."
    Lg serious "Don’t stress it. I mean, if we were caught, then that would have been far worse. I wouldn’t have had the chance to stabilise the generator, and then…{w=2.5}{nw}"
    $ renpy.pause (1.5)
    Lg annoyed "I’ll finish the last few stuff tomorrow when everything is safe enough for me to work. Chances are, you’ll probably have to come with me. You know, to prevent this from happening again."

$ renpy.pause (0.5)
Lg serious "Though, let’s get outta here. I’m pretty sure the cops are due to come any minute now." #That... doesn't sound right. XD
c "Alright."
$ renpy.pause (0.5)
hide logan with dissolve

if kol_tlh_chapter4_minigame_win == True:
    m "With a feeling of accomplishment, me and Logan left the underground facility and walked towards my apartment in silence. I could see that Logan was so tired from working so intensely that he occasionally stopped and closed his eyes while taking a deep breath."

else:
    m "With a feeling of uncertainty, me and Logan left the underground facility and walked towards my apartment in silence. I could see that Logan was so tired from working so intensely that he occasionally stopped and closed his eyes while taking a deep breath."

$ renpy.pause (0.5)
scene black with fade
$ renpy.pause (0.5)

m "Eventually we parted ways, leaving me to walk the gravel roads in the middle of the night back to my apartment."
$ renpy.pause (1.5)



$ renpy.pause(0.5)
scene black with fade
$ renpy.pause(0.5)
stop music fadeout (2.0)
$ renpy.pause(0.5)
$ persistent.kol_tlh_chapter4A_skip = True

jump tlh_Chapter4B
# ===========================================
# END OF CHAPTER 4A
# ===========================================




label tlh_Chapter4_EndingA: 

$ save_name = (_("TLH - Chapter 4A.5"))
    
$ renpy.pause (0.5)
show logan serious with dissolve
$ renpy.pause (0.5)

Lg "Now, let’s not waste any more time. We’d have to hurry to haul all the parts before our time is up."

if persistent.kol_tlh_chapter4A_5_skip:
    $ renpy.pause (1.75)
    c "(Wait, haven't I seen this before at some point?)"

    menu:
        s "(Do you want to skip forward?)"

        "Yes.":
            $ renpy.pause (1.5)
            if kol_tlh_tld_crossover2 == True:
                menu:
                    s "(It seems that you are currently on the bonus content route. Do you wish to enable the crossover content while skipping?)"

                    "Yes.":

                        stop sound fadeout (1.0)
                        stop music fadeout (1.0)
                        scene black with fade
                        $ kol_tlh_tld_crossover2_skip = True #Kinda redundant since the player already chooses whether they continue with the TLD content considering the skip places the player before that choice, but I'm paranoid so I'll add this *just in case.*
                        $ renpy.pause(4.5)
                        jump tlh_Chapter4B

                    "No.":
                        pass


            stop sound fadeout (1.0)
            stop music fadeout (1.0)
            scene black with fade
            $ renpy.pause(4.5)
            jump tlh_Chapter4B

        "No.":
            pass


Lg "Follow me."

$ renpy.pause (0.5)
hide logan with dissolve
$ renpy.pause (0.5)
scene kolmorefacility2 with dissolve #Can't forget the random can of soda in the BG that's probably in the underground facility for who-knows how many years.
$ renpy.pause (1.0)
show logan serious with dissolve
$ renpy.pause (0.5)

Lg "Here’s the stuff we need to carry."
c "Those look extremely heavy."
Lg annoyed "That’s because they are. Those things are packed to the brim with complex electronics that I could spend weeks analysing if I had the opportunity to do so."
Lg serious "Oh, and before I forget, can you grab the file from over there? That contains all the documentation for the parts."
c "Sure."
$ renpy.pause (0.5)
m "I took the file that Logan pointed towards and carried it under my arm. However, considering how old it must have been, I decided that it wasn’t a good idea to be so reckless with it."
$ renpy.pause (0.5)
c "Uh..."
Lg annoyed "Just put it on top of the box."
c "Right..."
$ renpy.pause (0.5)
Lg "On the count of three, we’ll pick this up. Just make sure that the file doesn’t fall off, alright?"
c "Will do."
Lg serious "Three.{w} Two.{w} One.{w} LIFT!"

hide logan with dissolve
$ renpy.pause (0.5)
play sound "fx/box2.wav"
m "I used every ounce of strength I had to lift the box. With much struggle, I managed to lift the box up. I could see that Logan was struggling as much as I had on his side."
$ renpy.pause (1.5)
scene hallway at Pan((0, 150), (0, 150), 3.75) with dissolve
$ renpy.pause (2.5)
scene np1r flip at Pan((100, 100), (100, 100), 6.0) with dissolve
play music "mx/amb/night.ogg" fadein (1.0)

m "We carefully walked through the hallway, with Logan guiding me as I walked backwards. With even more struggle, we made it outside the underground facility and to the portal. Strangely, the night seemed slightly different than how it was just a few minutes ago."
m "Was it my senses that had been muddled by the dust? Did something change that I wasn’t aware of? Or, could the stress from this mission impact the way I’m thinking?"
m "As I got lost in these thoughts, I hadn’t realised that Logan had already started the portal’s starting routine."

$ renpy.pause (0.5)
play sound "fx/telbuttons.ogg"
show logan normal dk with dissolve
$ renpy.pause (0.5)

Lg "And now, we push this through the portal on the other side and we’re done."
c "Let's do this."

$ renpy.pause (0.5)
hide logan with dissolve
$ renpy.pause (0.5)
play sound "fx/slide.ogg"
m "Once again, I used every ounce of strength remaining in my body to push the box of parts through the portal alongside Logan. Slowly, the box faded away as we pushed it through, signalling the completion of yet another stage in our mission."

$ renpy.pause (0.5)
show logan normal dk with dissolve
$ renpy.pause (0.5)

Lg "And there we go. Nice job, [player_name]."

if kol_tlh_tld_crossover2 == True:
    stop music fadeout (1.0)
    $ renpy.pause (1.0)
    $ save_name = (_("TLH - TLD Crossover 2"))
    play music "mx/crossing_over_kol.ogg" fadein (1.0)
    $ renpy.pause (1.5)

    Lg "Welp, the portal won’t stay on forever. Let’s go."
    c "Again? Do I have to?"
    Lg annoyed dk "There’s no way in hell I’m dragging that box alone, so you bet you’re coming along."
    Lg normal dk "Besides, you already agreed to come along, remember?"
    $ renpy.pause (1.0)
    c "Yeah, I remember."
    $ renpy.pause (0.5)
    c "Speaking of that box, won’t the parts just be in the way of our entrance?"
    $ renpy.pause (0.5)
    Lg thinking dk "..."
    $ renpy.pause (0.5)
    Lg smiling dk "Probably not."

    $ renpy.pause (0.5)
    hide logan with dissolve
    play sound "fx/tel.wav"
    $ renpy.pause (1.5)
    m "Before I could say anything, Logan had already gone through the portal. Deciding to toss all caution to the wind, I followed suit."
    
    $ renpy.pause (1.5)
    scene black with fade
    $ renpy.pause (9.5)
    stop sound fadeout (4.0)
    $ renpy.pause (1.5)
    scene kolcitynight at Pan ((0, 360), (0, 0), 8.0) with dissolve
    $ renpy.pause (3.0)
    show logan normal dk with dissolvemed
    $ renpy.pause (1.5)

    Lg normal dk "Nope; they weren’t in the way. How convenient."
    $ renpy.pause (0.5)
    m "As I reoriented myself, I could say that the box filled with Logan’s parts had ended up just an arm’s reach in front of us."
    $ renpy.pause (0.5)
    c "How on earth do you not feel sick from using the portal?"
    Lg annoyed dk "You’re supposed to feel sick?"
    c "{w=0.65}...never mind."
    Lg serious dk "Whatever, then. Let’s get back to carrying."
    c "Can I at least gather my bearings for a second?"
    Lg "No." #Wow, that's blunt, even by Logan's standards. Damn.
    c "(Well then. Screw me, I guess.)"

    $ renpy.pause (0.5)
    hide logan with dissolve
    $ renpy.pause (0.5)

    m "Logan grabbed one side of the box, expecting me to do the same on the other side. Despite my head spinning, I tried to pick the box up and simply follow Logan’s lead. Luckily, it wasn’t long before my head cleared up."

    $ renpy.pause (0.5)
    show logan serious dk with dissolve
    $ renpy.pause (0.5)

    c "Wait, so where are we–{w=0.8}{nw}"
    Lg "My place. I’ve essentially made my home a hub for the generator projects, so it’ll make sense to take it there. Besides, nobody will just barge in to see my work, so…"
    c "But that doesn’t make any sense. I mean, if the Sergeant is keeping track of your progress, why wouldn’t he visit your home?"
    Lg annoyed dk "Because the generators that are {i}used{/i} aren’t at my home; the parts are. The Sergeant doesn’t have any interest in the parts themselves, and until more qualified people are available, the parts stay at my place for me to create more generators."
    Lg normal dk "All the while, the ones currently running are slowly reviving the city."
    $ renpy.pause (0.5)
    Lg annoyed dk "Uh, I’m guessing that you didn’t magically obtain any generator-making skills, correct?"
    
    $ renpy.pause (0.5)
    show kolcitycentrenight at Pan((0,110),(0,110),3.0) behind logan with dissolve
    $ renpy.pause (0.5)

    c "How did you know?"
    Lg "Just a hunch."
    Lg serious dk "And you don’t have enough time to learn anything meaningful, damn it all. Sure, you could read through the file, but by the time you’ve learned anything useful, you’ll probably be considered missing back in the dragon world."
    $ renpy.pause (0.5)
    Lg annoyed dk "Wait."
    Lg normal dk "You sent your PDA through, right?"
    c "Yeah, what about–{w=0.65}{nw}"
    $ renpy.pause (0.5)
    c "{i}Oh.{/i}" #Realisation.
    Lg "Guess you figured out what your little task will be while you’re making your second visit to us."
    Lg "The Sergeant’s house, if you’re wondering where to look. Let’s drop this off first, though."

    $ renpy.pause (0.5)
    hide logan with dissolve
    $ renpy.pause (0.5)

    m "We continued to walk through the desolate streets of the night, hauling the immense weight to Logan’s house. Despite my arms starting to go numb, I still carried the box with as much strength as I could muster."

    $ renpy.pause (0.5)
    scene kolloganoutnight at Pan ((0, 0), (0, 250), 5.0) with dissolvemed
    $ renpy.pause (0.5)

    m "After what felt like hours of agony, we arrived at what I assumed was Logan’s house. Figuring that Logan would want to unlock his door first, I motioned for the box to be put down."
    $ renpy.pause (0.5)
    play sound "fx/kickdoor_kol.mp3" #What a lame sound for kicking a door open.
    $ renpy.pause (0.75)
    m "That was, until Logan suddenly kicked his door open."
    $ renpy.pause (0.5)
    show logan annoyed dk with dissolve
    $ renpy.pause (0.5)

    Lg "I should really replace that lock at some point. Oh well."
    $ renpy.pause (0.5)
    scene kolloganhousenight at Pan ((0, 220), (0,360), 3.0) with dissolveslow
    $ renpy.pause (0.5)

    m "A few steps later, we were inside. I promptly let go of the box, experiencing the rush of feeling my arms again, and with the sensation of being able to feel once more, came pain."
    m "I tried to hide my discomfort as best as I could, but Logan seemed to pick up on my pain almost immediately."
    
    $ renpy.pause (0.5)
    show logan normal dk with dissolve
    $ renpy.pause (0.5)

    Lg "See, if you weren’t as much of a slacker, I’m sure you wouldn’t have to deal with that pain of yours."
    m "I only groaned in response."
    $ renpy.pause (0.5)
    Lg annoyed dk "Well, I suppose not everybody is fit for physical labour. I mean, I definitely wasn’t before the flare hit, but with new times came new adaptations."
    Lg serious dk "But enough wasting time. Like last time, you’re on a tight schedule. Unlike last time, this trip is far more risky considering that nobody knows we’re here."
    Lg "I’ll start organising the parts while you get the PDA. Let’s see if that thing has anything that I could use alongside the documentation for the parts."
    c "Is the Sergeant’s house unlocked?"

    $ renpy.pause (0.5)
    show logan annoyed dk with dissolveslow
    $ renpy.pause (0.75)
    c "Logan."       
    $ renpy.pause (0.5)
    Lg "…probably.{w} Maybe.{w} Hopefully."
    Lg normal dk "Eh, I’m sure you’ll figure something out."
    Lg serious dk "Now, off you go. And do be quiet, please."

    $ renpy.pause (0.5)
    hide logan with dissolve
    stop music fadeout (1.0)
    $ renpy.pause (0.5)
    m "I wanted to give voice to my displeasure, but I figured that Logan was right: I had wasted enough time. I left his house and let the night sky guide my darkened path."
    $ renpy.pause (0.5)
    play sound "fx/steps/rough_gravel.wav"
    scene kolloganoutnight at Pan ((0, 220), (0, 220), 5.0) with dissolve
    $ renpy.pause (2.0)
    show kolcitycentrenight at Pan((0,110),(0,110),3.0) with dissolve
    $ renpy.pause (0.5)
    play music "mx/terrace_kol.ogg"
    $ renpy.pause (1.5)

    m "Running down the streets, I made turn after turn until I exactly recognised where I was and made my way to the Sergeant’s house."
    $ renpy.pause (1.0)
    scene kolsergeanthouse at Pan ((0, 0), (0, 250), 5.0) with dissolveslow
    $ renpy.pause (3.5)
    stop sound fadeout (1.0)

    m "Out of breath, I made it without getting lost along the way."
    $ renpy.pause (0.5)
    c "(Alright, let’s see…)"
    play sound "fx/door/lock.ogg"
    $ renpy.pause (2.0)
    c "(Why did I get my hopes up that this would be easy?)"
    m "Just as I started to worry about how I'd get my PDA back, I spotted an open window barely large enough for me to possibly squeeze through."
    $ renpy.pause (0.5)
    c "(This is going to be one hell of a tight fit, but I can’t see another way in without making too much noise.)"
    m "I lifted myself up onto the window ledge and put my head through. I slowly wiggled my way through until my body seemed to be stuck at my waist."
    $ renpy.pause (1.0)
    m "With enough effort and struggle, I drove my elbows through the window frame and pushed myself through. Careful not to make too much noise, I stretched my now-dead arms in front of me and landed softly."
    
    $ renpy.pause (2.0)
    scene kolinsidesergeanthouse at Pan ((0, 220), (0,360), 3.0) with dissolveslow
    $ renpy.pause (2.0)

    c "(I’ll be really surprised if I can actually use my arms after all of this…)" #Pain is comedy, right?
    $ renpy.pause (1.0)
    m "I started the search for my PDA, slowly sneaking around on the floor. I searched desks, tables, and shelves, but couldn't find anything."
    $ renpy.pause (1.5)
    m "Yet, after enough searching, I found what seemed to be my PDA in a box close to the back of the room."
    c "(So much for securing this in a safe place.)"
    m "I put the PDA in my pocket and went back to the window. Luckily, climbing out wasn’t as hard as climbing in, though the edges of the window ledge almost pushed the PDA out of my pocket."
    
    $ renpy.pause (4.0)
    scene kolsergeanthouse at Pan ((0, 350), (0, 350), 5.0) with dissolve
    play sound "fx/dirtfall_kol.mp3"
    $ renpy.pause (0.5)
    
    m "Yet, my disregard for care had caused me to fall face-first onto the dirt road. Fortunately, the dirt seemed to muffle any noise that might have been made from my impact." #PAIN IS COMEDY, RIGHT?!
    $ renpy.pause (0.5)
    m "Now with both of my arms and my face in pain, I dashed through the streets once more, tracing my steps back to Logan’s home."

    $ renpy.pause (2.0)
    show kolcitycentrenight at Pan((0,110),(0,110),3.0) with dissolve
    $ renpy.pause (2.5)
    scene kolloganoutnight at Pan ((0, 220), (0, 220), 5.0) with dissolve
    $ renpy.pause (1.0)

    m "Upon arrival, I felt as if I was on the brink of collapsing from exhaustion. Before entering Logan’s house, I simply took a seat on the gravel road to rest my body."
    c "(Arms, face, and now legs. I just can’t get a break tonight, can I?)"

    $ renpy.pause (1.5)
    show logan normal dk with dissolve
    $ renpy.pause (0.5)

    Lg "Impressive. I didn’t think that you would be this quick with your trip. Just a shame that I could hear your senseless panting as soon as you arrived outside."
    Lg annoyed dk "Let's hope that you kept your mouth shut while coming here."

    $ renpy.pause (0.5)
    hide logan with dissolve
    show kolloganoutnight at Pan ((0, 0), (0, 0), 5.0) with ease
    $ renpy.pause (0.5)

    m "Not wanting to hear anything, I simply fell on my back and lied on the coarse gravel, gazing at the stars."
    $ renpy.pause (0.5)
    Lg serious dk "Damn, you must be really bloody exhausted. You want a moment?"
    c "Yes, please."
    $ renpy.pause (0.5)
    Lg "Unfortunately, you don’t really have a moment. You got the PDA?" #Hah.
    c "In my right pocket."
    Lg "I'll just go get that for you."
    $ renpy.pause (0.5)
    m "Logan went to my side and dove into my right pocket to retrieve the PDA. I could see him smile as he held his hand out in awe."
    $ renpy.pause (0.5)
    Lg smiling dk "Nice job, [player_name]. I knew I could count on you."
    c "Who… {w=0.4}else could you…{w=0.4} have counted on?"
    Lg annoyed dk "Fair, fair."
    Lg normal dk "Well, you have my gratitude regardless."
    Lg serious dk "Now, if you’ll excuse me, I have to prepare to modify a generator. It looks like we’ll part ways for now. I can’t imagine that the Sergeant would let me go too easily if I brought him an opportunity like this one."
    $ renpy.pause (1.0)
    Lg normal dk "Here, let me help you up."
    $ renpy.pause (0.5)
    m "I tried to reach for his arm, but I simply didn’t have the strength left to grab it after carrying the box and wiggling through the window."
    $ renpy.pause (0.5)
    Lg serious dk "Screw it."

    $ renpy.pause (2.0)
    show kolloganoutnight at Pan ((0, 220), (0, 220), 5.0) with ease
    $ renpy.pause (1.0)

    m "Logan directly picked me up by the waist and placed me on my feet. After trying to stand for a bit, I managed to slightly recover." #Total bro move ngl.

    $ renpy.pause (0.5)
    show logan normal dk with dissolve
    $ renpy.pause (0.5)

    Lg "There. Quick and easy."
    Lg "Now, off you go. I don’t want you to be slacking here when you can be slacking in a better world."
    Lg "Stay safe, [player_name]. We’re in the final stretch now."
    c "Same to you, Logan. Let’s hope our paths cross again soon."

    $ renpy.pause (0.5)
    stop music fadeout (2.0)
    hide logan with dissolve
    $ renpy.pause (0.5)

    m "Logan nodded. I turned around and went my way, trying to keep myself upright as I went through street after street."

    play music "mx/amb/night.ogg"
    play sound "fx/steps/rough_gravel.wav"
    $ renpy.pause (1.5)
    scene kolcitycentrenight at Pan((0,110),(0,110),3.0) with dissolve
    $ renpy.pause (1.5)
    c "(A motorcycle or something like that would definitely come in handy right now. Oh well.)" #Reference to TLD, of course. :)
    $ renpy.pause (1.5)
    scene kolcitynight at Pan ((0, 360), (0, 0), 6.5) with dissolve
    $ renpy.pause (3.0)
    stop sound fadeout (1.0)

    m "In due time, I made my way back to the portal, standing mightily in the light of the moon. As was ritual at this point, I activated the portal, waited for it to do its starting routine, and went through."
    
    $ renpy.pause (0.5)
    play sound "fx/telstart.ogg"
    $ renpy.pause (0.5)
    stop music fadeout (1.0)
    scene black with fade
    $ renpy.pause (6.5)
    stop sound fadeout (1.0)
    scene np1r flip at Pan((100, 100), (100, 100), 5.0) with dissolveslow
    $ renpy.pause (1.5)

    m "As I emerged, I saw a dragon in the distance. Panic overcame me as I thought that I had taken too long and the police officer on duty had arrived."
    $ renpy.pause (1.0)
    m "Yet, as the dragon approached, I noticed that it wasn’t one of the officers."

    $ renpy.pause (0.5)
    show remy look dk with dissolvemed
    play music "mx/dream_catcher_kol.ogg"
    $ renpy.pause (1.5)

    Ry "[player_name]? Did you just come out of the portal?" #...oh shoot.

    menu:
        "What are you doing here, Remy?":

            Ry "I asked you first, so please, answer me."

        "I wanted to test something.":

            Ry "I’m afraid that that doesn’t answer the question."

        "Why should you know?":

            Ry "Because whatever you’re about to say might cause some serious discussion among council members if anything were to be revealed."

    $ renpy.pause (1.5)
    c "Yes,{w=0.3} I came from the portal. I wanted to see if I could find anything back home that could help redirect the comet."
    Ry sad dk "Forgive me, but I don’t believe it. Humanity is in a very dire state, no? Why would they have something lying around to help us if they would just be using that thing themselves?"
    Ry "Instead, you wasted some of humanity’s power supplies by using their portal."
    $ renpy.pause (2.5)
    c "..."
    Ry "..."
    $ renpy.pause (0.5)
    c "Alright, then I’ll say this: I’m trying to strengthen the trade agreement. The trade was almost cancelled after Reza died. I've been working hard to get it back to a point where relations aren't in jeopardy while we work on redirecting the comet."
    Ry look dk "I see..."
    Ry "It’s a really big risk you’ve taken, [player_name]. If the energy supplies for humanity drain too much from your and Logan’s constant back and forth..."
    c "{w=0.35}…let’s not think about it."
    $ renpy.pause (1.0)
    c "And now, your turn. Why are you here?"
    Ry shy dk "I wanted to go on a walk to try and clear my mind. Nothing too interesting. The night does wonders for your mental state."
    $ renpy.pause (0.3)
    Ry sad dk "Wonders…{w=0.5} and horrors."
    c "Do you want to talk about it?"
    Ry shy dk "No, I’d rather not. I need to keep my mind clear for a bit."
    Ry sad dk "You look exhausted, though. It looks like you’re about to fall over at any second."
    c "It’s complicated."
    Ry normal dk "Well, do you want to ride on my back while I take you back to your apartment?" #*Another* reference to TDOMI. Damn, this mod is filled with references, huh?
    c "An interesting offer, I'll admit. {w} Go ahead, Remy."

    $ renpy.pause (0.5)
    hide remy with dissolve
    $ renpy.pause (0.5)
    
    m "Remy lowered his body for me to climb onto, and, with much struggle, I managed to get to a comfortable area and lay down on his back."
    
    $ renpy.pause (1.0)
    play sound "fx/steps/rough_gravel.wav"
    scene black with fade
    $ renpy.pause (1.5)

    m "Remy picked up speed and went away from the portal, his movements slowly lulling me to sleep."
    $ renpy.pause (3.5)
    stop sound fadeout (1.0)
    Ry shy dk "We’re here. It's time to wake up, [player_name]."
    $ renpy.pause (1.0)
    scene np5 dk with dissolvemed
    $ renpy.pause (1.0)
    c "Ugh..."
    $ renpy.pause (0.5)

    m "Remy lowered himself to the floor and gently nudged me off. My legs hurt a bit as I shifted my weight to my feet, but I could stand alright."

    $ renpy.pause (0.5)
    show remy normal dk with dissolve
    $ renpy.pause (0.5)

    Ry "Well, I’ll be off now. I guess I’ll see you some other time."
    $ renpy.pause (0.5)
    c "Wait."
    $ renpy.pause (0.5)
    Ry "Yes?"
    c "You could stay with me for the night."
    Ry "Forgive me, but I don’t think that your couch is big enough."

    menu:
        "I could sleep on the couch instead.":
            $ renpy.pause (0.5)

            Ry shy dk "You would?"
            c "Of course! You wouldn’t burden me in the slightest by making me sleep on the couch."
            Ry "I suppose I could stay the night in that case. Hopefully I don’t bother you too much."
            c "You don’t bother me in the slightest, Remy."

        "We could share the bed.":

            c "My bed should be big enough for the both of us."
            Ry shy dk "O-Oh, well..."
            $ renpy.pause (1.0)
            Ry "If you insist, then I suppose I can stay the night."
            c "After you, Remy."
            Ry normal dk "So be it."

    $ renpy.pause(2.5)
    scene black with fade
    $ renpy.pause(0.5)
    stop music fadeout (2.0)
    $ renpy.pause(3.5)
    $ persistent.kol_tlh_chapter4A_5_skip = True

    jump tlh_Chapter4B

    

    # ===========================================
    # END OF CHAPTER 4A
    # ===========================================






    

else:
    Lg "Well, I suppose this is goodbye for now. I honestly don’t know when I’ll be back, considering I’m breaking direct orders from the Sergeant here. Knowing him, I’d probably not get sent back unless this plan of mine actually works better than I thought it would."
    Lg serious dk "Thanks for everything, though. It was nice seeing you again."
    Lg normal dk "And with how hardworking you are with keeping the dragons safe, I’m sure that you’ll be able to redirect the comet without any hassle."
    Lg "Now, I’ll try my best to not screw up my part of the plan. Stay safe, alright?"
    c "I will, Logan."
    
    $ renpy.pause (0.5)
    show logan smiling dk with dissolve
    $ renpy.pause (0.5)

    m "Logan stretched his hand towards me and gave me a sly smile. Returning the gesture, I gripped Logan’s hand and shook it."
    $ renpy.pause (0.5)
    Lg "See you when this is all over."
    c "See ya."

    $ renpy.pause (0.5)
    hide logan with dissolveslow
    play sound "fx/telstart.ogg"
    $ renpy.pause (3.5)
    m "Logan entered the portal and slowly faded away. Silence fell upon me as the portal turned off again, leaving me alone in the night."

    $ renpy.pause (0.5)
    stop sound fadeout (1.0)
    scene black with fade
    $ renpy.pause (1.5)

    m "With nothing else to do, I returned to my apartment to get some extra sleep for tomorrow."
    $ renpy.pause (1.0)

    $ renpy.pause(0.5)
    scene black with fade
    $ renpy.pause(0.5)
    stop music fadeout (2.0)
    $ renpy.pause(3.5)
    $ persistent.kol_tlh_chapter4A_5_skip = True

    jump tlh_Chapter4B

    # ===========================================
    # END OF CHAPTER 4A
    # ===========================================
    




label tlh_Chapter4B:

$ save_name = (_("TLH - Chapter 4B"))
$ renpy.pause (1.0)

nvl clear
window show

n "I slept remarkably well that night, letting my dreams transport me to another world of half-false memories and distortions of reality."
n "The following day was unremarkable as well. Just the typical duties that I had to do in order for the dragon council to minimise the impact of redirecting the comet."
n "That day was exhausting, yes, but strangely, I couldn’t seem to fall asleep when the rainy night came. Insomnia struck out of nowhere; whether that was from stress or something else entirely, I do not know. In due time, I managed to return to the blissful realm of dream-reality."

$ renpy.pause (1.0)
play sound "fx/phonering.ogg"
$ renpy.pause (0.5)

n "The answering machine had started to ring, waking me up in the middle of the night."

window hide
nvl clear

$ renpy.pause (1.0)
scene o3 at Pan((0, 250), (0, 250), 4.0) with dissolveslow
$ renpy.pause (2.0)
play soundloop "fx/rainloop_kol.ogg" fadein (1.0) #Rain? In a Kolsavdür mod? Oh you know that this means! Iiiiiiiit's trauma-dumpin' time!

c "(Ugh, who calls people this late at night?)"
$ renpy.pause (1.0)
c "(It’s Logan, isn’t it?)" #Logan's the type of guy to brage into your house at night instead of calling, MC.
$ renpy.pause (1.0)

menu:
    "[[Do not answer the call.]":
        $ renpy.pause (0.5)

        m "Figuring that whoever wanted to call me so late at night could safely assume that I was still sleeping, I decided to let the answering machine ring for a few moments until the ringing had stopped." #A fair response tbh.
        stop sound
        m "I let the soothing sounds of rain crashing on the earth lull me to sleep, and, with closed eyes, let my consciousness drift once more."

        $ renpy.pause(0.5)
        scene black with fade
        stop soundloop fadeout (2.0)
        $ persistent.kol_tlh_chapter4B_skip = True
        $ renpy.pause(4.0)

        jump tlh_Chapter5

        # ===========================================
        # END OF CHAPTER 4
        # ===========================================

    "[[Answer the call.]":
        $ renpy.pause (0.5)

        m "Figuring that whoever decided to call me at this hour must have a good reason to do so, I reluctantly got out of my bed and went to the answering machine."

        stop sound
        $ renpy.pause (0.5)
        play sound "fx/phonepickup.ogg"
        $ renpy.pause (1.75)
    
        c "Hello?"
        Ry look "Hello, [player_name]."

        if persistent.kol_tlh_chapter4B_skip:
            $ renpy.pause (1.75)
            c "(Wait, haven't I seen this before at some point?)"

            menu:
                s "(Do you want to skip forward?)"

                "Yes.":
                    $ renpy.notify("You successfully helped Remy with his troubles.")
                    $ kol_tlh_remytherapywin = True
                    $ kol_tlh_remytherapycounter = 4

                    stop sound fadeout (1.0)
                    stop music fadeout (1.0)
                    stop soundloop fadeout (1.0)

                    scene black with fade
                    $ renpy.pause (3.0)
                    $ kol_tlh_4B_played = True
                    jump tlh_Chapter5

                "No.":
                    $ renpy.pause (1.0)


        c "Wait, Remy?"
        Ry "I’m so sorry if I woke you up at this hour, but this is really important."
        Ry "Do you think that you could come over? I…{w=0.8}{nw}"
        $ renpy.pause (1.0)
        Ry sad "...need your help.{w}{size=22} Desperately.{/size}{w=0.5}{nw}"
        c "Sure. I’ll be at your place as soon as I can. Hopefully I won’t get too soaked from the rain."
        Ry "I...{w=0.65} didn’t consider that possibility. Perhaps it’s–{w=0.85}{nw}"
        c "No, I’ll come. I’ll just have to deal with the rain."
        Ry look "Then so be it. I’ll see you soon.{w} And thank you."
        $ renpy.pause (2.5)
        m "My mind started to wonder what Remy exactly meant by \"help.\" I first thought that it might have been some sort of injury, but I soon realised that Remy wouldn’t be so reckless at night." #It's Remy. I'm pretty sure you can make an educated guess with the kind of help Remy needs.
        m "I also tried to think about what Remy had whispered under his breath while on the phone, but since I didn't fully hear what he had said, I had no idea."
        $ renpy.pause (0.5)
        c "(I guess I’ll find out soon enough.)"

        $ renpy.pause (0.5)
        scene black with fade
        $ renpy.pause (1.5)
        play sound "fx/steps/clean2.wav"
        $ renpy.pause (2.5)

        m "Breathing in deeply, I gathered myself and darted into the rain. As I felt the heavy raindrops being soaked into my clothes, I could start to feel myself being weighed down. Despite that, I tried to find a route that would help me stay as dry as possible."
        m "After several breaks to try and let my body recover from the semi-sprints I did, I reached Remy’s apartment. As I wanted to knock, I could hear a voice coming from inside."

        play music "mx/martyr.ogg"
        $ renpy.pause (2.5)
        Ry sad "I know, but I’ve already called [player_name]. I don’t want to drag you into this as well. You’ve already done quite a lot for me as of late."
        $ renpy.pause (2.5)
        Ry "Just…{w=0.5} please. Having you on the phone is enough as is. You don’t need to come."
        $ renpy.pause (2.5)
        Ry "No, of course I won’t do anything rash. It hasn’t gotten that bad yet. Besides, both you and [player_name] are here for support. I didn’t have that until recently."
        Ry "Now please, go back to sleep."
        $ renpy.pause (2.5)
        Ry "Yes, I know that I should be going to bed as well considering the time, but I just can’t. I’m so sorry."
        m "Not wanting to eavesdrop on this conversation any further, I knocked on Remy’s door. I then heard what seemed to be a light gasp of surprise, followed by something that suddenly got slammed. Remy’s muffled voice soon emanated through the walls, but I couldn’t make out what he had said."
        $ renpy.pause (1.5)
        Ry look "Please, come in."

        $ renpy.pause (0.5)
        play sound "fx/door/door_open.wav"
        $ renpy.pause (2.0)
        scene remyapt at Pan ((300, 80), (0,80), 5.0) with dissolveslow
        $ renpy.pause (3.0)
        show remy look with dissolvemed
        $ renpy.pause (0.5)

        Ry "Please forgive me for dragging you all the way out here so late at night."
        Ry sad "And for making you go through the rain as well."
        c "Please, Remy. It’s alright. Now, how can I help you?"
        Ry "I wanted to talk to you. In person.{w=0.85} What I wanted to say just won’t work well over a call."
        Ry "But the thing is, I was going to tell you after the comet was redirected, but it has just burst open to the point where I can't keep it to myself any longer. "
        Ry shy "I'm well aware of how you realised that I hadn't exactly been like myself as of late, especially at work."

        if kol_tlh_chapter1B_done == True: #This scene flows *so* weird but I genuinely can't be bothered to fix it, so, uh, embrace the wonk.
            $ renpy.pause (1.5)
            Ry "Of course, you can't forget how suddenly my mood changed when you arrived while we were at the café with Adine the other day. I suppose that was the first warning sign."

        if kol_tlh_2Bplayed == True:
            $ renpy.pause (1.5)
            Ry look "With that cake we made and how I acted so grim just before I shut myself in my bedroom? Looking back at it now, it was such a stupid thing for me to do, even if all I wanted in that moment was to cry my heart out in my room. Alone."

        if kol_tlh_3B_played == True:
            $ renpy.pause (1.5)
            Ry "Remember how I daydreamed when Adine took Amely back to the orphanage at the end of our day at the beach? I just couldn't feel anything else put grief in that moment, knowing that I'll probably never get to experience the kind of bond that those two have for myself."

            if kol_tlh_3B_remyasked == True:
                $ renpy.pause (1.0)
                Ry sad "Not to mention that you asked me what exactly was wrong and how willing you were to help. I told you that it’s nothing to worry about, but… well… now we’re here."
        
        $ renpy.pause (0.5)
        

        menu:
            "Yeah, I picked it all up. That's exactly why I was so concerned.":
                $ renpy.pause (0.5)
                $ kol_tlh_remytherapycounter += 1

                Ry shy "I see. Maybe I shouldn’t have made it so obvious."
                c "Keeping everything to yourself isn’t a good thing, Remy. You know this."
                Ry "That I do."

            "Wait, {i}these{/i} were the things you were hinting at?":
                $ renpy.pause (0.5)
                $ kol_tlh_remytherapycounter -= 1

                Ry look "\"Hinting\" may not be the right word to use. I think it’s more like \"a small cry for help.\""
                Ry sad "But it seems that they were too small to be picked up." #...ouch.

            "Some things were more obvious than others, I’ll admit.":
                $ renpy.pause (0.5)

                Ry look "Then maybe I should’ve simply asked for help sooner instead of being vague about everything."
                c "One needs to ask for help when they’re ready for it to be the most effective that it can be."
                Ry shy "I suppose you do have a point."
        
        $ renpy.pause (0.75)
        Ry look "But, I digress. This isn’t why I called you for. How do I put this?"

        $ renpy.pause (0.5)
        stop music fadeout (2.0)
        show remy sad with dissolve
        $ renpy.pause (0.5)

        Ry "It’s...{w=0.4} about Vara." #There we go. Finally, the reveal had been made.

        menu:
            "How so?":
                pass

            "I think I know where this is going...":
                pass

            "Is this about how you couldn’t protect her from Reza?": #Damn, MC, that's extremely blunt.
                $ renpy.pause (1.5)
                $ kol_tlh_remytherapycounter -= 1

                Ry "..."
                $ renpy.pause (0.5)
                Ry "It’s more complicated than that, I’m afraid."
                $ renpy.pause (0.5)


        Ry "I know that we barely had the chance to know each other, but I grew very close to her in such a short time."
        Ry shy "In a way, she reminded me of you and Amelia. If it weren't for you, then I would’ve never considered going to the orphanage to take care of Vara or rebuild my friendship with Adine."
        Ry "And with Amelia? Well…{w=0.8} after the six months would have passed and we would both move in together here, we had talks of becoming parents. We wanted to raise a hatchling to the best of our abilities and teach them about the world." #I do hope this matches up with the reveal about Amelia being pregnant in the true ending...
        Ry "With Vara, I could almost see that desire come to life once more, even if I was only helping out at the orphanage."
        
        $ renpy.pause (0.5)
        show remy cry with dissolvemed
        $ renpy.pause (0.5)

        Ry "But just as everything likes to play out in my miserable life, even that had to be taken away from me."

        $ renpy.pause (0.5)
        play music "mx/gravity.ogg"
        $ renpy.pause (0.5)

        menu:
            "Fate really is interesting in that regard, isn’t it?":
                $ renpy.pause (0.5)
                $ kol_tlh_remytherapycounter -= 1

                Ry "Indeed."

            "Yet you're on the road of recovery.":
                $ kol_tlh_remytherapycounter += 1

                c "Think about it like this: with all the support you have right now, you’re slowly recovering from that dark pit you were in just recently."
                c "Sure, this is another bump in that road, but it can be overcome if we all cross over it."
                Ry "But what if I can’t?"
                c "You’ve made it this far on your own, so who’s to say that you won’t be able to with friends?"
                Ry lookcry "It makes sense. I think."

            "What life takes, life returns.": #A poor attempt at being philosophical tbh.
                $ renpy.pause (0.5)

                Ry "What do you mean?"
                c "With what life took away from you, it has also given it back to you in another form. You’ve lost people who were important to you, yes, but you've also gained new friends as well."
                Ry "That’s…{w=0.5} an interesting way to look at things, but not entirely helpful right now, I'm afraid."

        $ renpy.pause (0.5)
        Ry lookcry "I honestly wish that it just stopped there, but no. It gets worse."
        Ry cry "{i}So{/i} much worse."
        c "Then please, if you’re comfortable sharing, do so. I want to help you as best as I can."
        Ry lookcry "O-Okay."
        $ renpy.pause (0.5)
        Ry "Losing Amelia was rough; because of my desire to keep our relationship a secret, I couldn’t have protected her from overworking herself. Now think about Vara."
        Ry "She escaped the orphanage and went to the portal to come and look for me, where she got shot by Reza."
        Ry cry "Just with Amelia, I couldn’t have protected Vara. I couldn’t have kept her away from the portal."
        Ry "{i}{cps=15}I didn’t keep her safe.{/cps}{/i}" #Much better use of slow-down text than the previous attempt. Cheers for doing something right, Kols.
        Ry "And now?{w} She’s gone.{w} Just like Amelia."

        menu:
            "Why are you blaming yourself when it wasn’t your fault?":
                $ renpy.pause (0.5)

                Ry "But it is. Had I not been so careless and made sure that she was well protected in the orphanage, then she would still be here. It was my neglect that caused her to escape."

            "How ironic.":
                $ renpy.pause (0.5)
                $ kol_tlh_remytherapycounter -= 1

                Ry lookcry "How so?"
                c "You said that Vara reminded you of Amelia in a way, right? The fact that she died in a similar fashion to Amelia makes it ironic."
                Ry cry "Yes. I…{w=0.65} suppose it is."

            "You did the best that you could have. We both couldn’t have expected this.":
                $ kol_tlh_remytherapycounter += 1

                c "Don’t beat yourself up for it, Remy. Nobody could have expected this in the slightest. Blaming yourself for uncontrollable and unpredictable events will cause more harm than good."
                Ry "But-{w=0.4}{nw}"
                c "No buts. Hindsight is a bastard, yes, but it shouldn’t be the reason why you can’t look forward."
                $ renpy.pause (0.85)
                Ry shycry "Thank you."


        $ renpy.pause (0.5)
        Ry lookcry "Still, losing Vara was a painful strike for me. Look at Adine and Amely, for example. Those two are practically bound to each other. They spend so much time together it’s unreal."
        Ry cry "And then, here’s me. I tried my best with Vara, and when we started to get close, she was gone. Perhaps it’s better that I never became a parent if this is what happens when I get involved with children."

        menu:
            "Don’t compare yourself with Adine.":
                $ kol_tlh_remytherapycounter += 1

                c "Everybody has their own way of raising a child. Comparing yourself to Adine when she already has far more experience than you is silly. You barely had any time to get used to children and you were already on Adine’s level."
                c "Don’t think that just because you lost Vara means that you’re unfit to become a parent one day."
                c "We even have a saying for comparing yourself with others: \"Comparison is the thief of joy.\""
                Ry shycry "Am I really that good?"
                c "Ask Adine if you’re unsure. She’d be happy to agree with how good of a parent you could become."
                Ry "I-I think I will have to."

            "This was a new experience for you, so don’t feel bad.": #"Don't feel bad about a loved one dying because it's the first time a loved one died for you."   EDIT from future Kols: This analogy, uh... yeeeeaaaahhh...
                $ renpy.pause (0.5)
                $ kol_tlh_remytherapycounter -= 1

                Ry "If my first experiences always end up like this, then maybe I should just stop trying. That way, I can’t be hurt by anything new."
                c "You’ll never experience new things that are good, though."
                Ry "I think that it’s a sacrifice I’m willing to make."

            "What prevents you from trying again?":
                $ renpy.pause (2.0)

                Ry "The fear of losing someone close to me for the third time."
                c "Being stuck in fear of something hinders improvement. If you want to become better, then you need to break free from that fear."
                Ry "I just wish that it was as easy as that."

        $ renpy.pause (0.5)
        Ry shycry "Unfortunately, Vara’s passing isn’t all that bothers me."
        c "I’m taking a shot in the dark and say that it’s your work, correct?"
        Ry "Indeed."
        Ry lookcry "I don’t think that I’ve ever experienced this much pressure in my life. I have this feeling that if I don’t do everything perfectly as fast as possible, then the comet {i}will{/i} hit and kill us all."
        Ry cry "It’s as if all of dragonkind is hoping for me to save them all. But…{w=0.8} what if I don’t? What if I fail and cause millions of lives to be lost in an instant?"
        Ry "Their future curses, their disappointments, their sadness—it all weighs me down."

        menu:
            "This isn’t only in your hands.":

                c "Remember, the council is the one who will use your research. I’m sure they’ll be able to adapt to anything that might not work out so well."
                Ry "Making some of my research meaningless."
                c "I doubt it. Maybe some of that unused research could help in other ways."
                Ry lookcry "I suppose time will tell."

            "The amount of effort you’ve put won’t cause something to go wrong.":
                $ renpy.pause (0.5)
                $ kol_tlh_remytherapycounter += 1

                Ry shycry "Well, if the council doesn’t use my research correctly, then something will still go wrong regardless."
                c "But then it’s the council’s fault, not yours. You did your part to the best of your ability, and for that, I’m proud of you."
                Ry "You compliment me too much, [player_name]."
                c "In all honesty, I don’t compliment you nearly enough." #I'd fix that if I wasn't a lazy prick.
                $ renpy.pause (2.0)
                Ry "..."
                c "..."
                Ry "A-Anyway..."

            "Are you afraid of loosing Adine?":
                $ renpy.pause (0.5)
                $ kol_tlh_remytherapycounter -= 1

                Ry lookcry "What makes you think that?"
                c "Well, you’ve obviously lost some people you deeply cared about in the past. Who’s to say that with your potential failure, you'll probably lose Adine as well?"
                
                $ renpy.pause (0.5)
                show remy cry with dissolve
                $ renpy.pause (0.5)
                
                Ry "I-I haven’t thought about that."
                c "So, this just means that you need to work to the point where you won’t disappoint Adine, right?"
                Ry "I can't say anymore."

        $ renpy.pause (0.5)
        Ry cry "This opens up a new dilemma. I just realised the possibility of hurting Adine by overworking myself."
        Ry "Both you and Adine had told me several times now not to overwork myself by now, but I still do because I want to help as much as I can."
        c "Like how you told me after you left the hospital."
        Ry lookcry "Precisely. Yet, here’s the issue: I’m becoming like Amelia in a way. I’m working myself to death while trying to get something done on time. Adine had already told me about how she felt about Amelia’s death and how it affected her."
        Ry "I guess this is why I blanked out the other day as well, while we were in Tatsu Park. I realised that if I’m not careful, I will follow in Amelia’s footsteps."
        Ry cry "I can't do that to Adine again. If my experience is anything to judge by, then Adine would be broken beyond belief if something happened to me."

        menu:
            "Then stop working. Easy as that.": #"Don't be sad. Just be happy!" I am going to strangle the MC. Uh, no, wait, I wrote this. Uhhhhhhhhh...
                $ renpy.pause (0.5)
                $ kol_tlh_remytherapycounter -= 1

                Ry lookcry "You know that it isn’t as easy as that, [player_name]. Not only wouldn’t I be able to leave due to the dire situation we’re all facing, but a position like this has term limits. Leave now, and it won’t look good, to put it lightly."
                Ry cry "All I can do is work and hope that the supplements I’m taking will carry me through all of this."

            "You’re in the final stretch.":
                $ renpy.pause (0.5)

                Ry "I suppose I am, but it’s usually the final stretch that proves to be the hardest. Those last few weeks, days, hours…"
                $ renpy.pause (0.5)
                Ry "It’s then that everything gets chaotic."
                c "Then we’ll face this chaos together. I’ll make sure that, whatever happens at work, you won’t work yourself to the bone."
                Ry lookcry "How?"
                c "I'll find a way."
                Ry shycry "I suppose you always do."

            "Let me and Adine stay at your side while you’re finishing the last pieces of work left.":
                $ kol_tlh_remytherapycounter += 1

                c "Think about it like this: if both Adine and I could be there for you while you worked—whether that was at home or at the library—then you wouldn’t leave our sight. If you feel really exhausted, then we can take care of you until you feel better."
                Ry shycry "I don’t want to be dependent on you or Adine, though. I don’t want that kind of burden to be placed on your or Adine’s shoulders."
                c "Since when have you ever been a burden?"
                $ renpy.pause (0.5)
                Ry "..."
                c "Remy, this will allow us to prevent repeating the mistakes of the past. You need to believe in us."
                Ry "I’ll think about it. I just don’t want to hurt you or Adine in any way if I can help it."
                c "You won't. I promise."
                Ry "I see."


        $ renpy.pause (1.5)
        Ry lookcry "You know, sometimes I have to wonder what Amelia would think of me. Would she be happy that I’m working for the council and doing research? Would she approve of who I’ve become? Would she even still like me anymore?"
        c "Remy..."
        Ry cry "Or, would she be disappointed with me? How I’m overworking myself and not learning from her mistakes? How I grew distant from Adine due to being stuck in an endless mental cycle of self-pity and guilt?"
        Ry "How I couldn’t have protected Vara?" #This section is heavy, even by my standards. Yikes.
        c "I’ll have to shut you down right there, Remy. This isn’t your rational mind speaking, and you know it."
        Ry "Why? Why should I when I know that I’ll never get the chance to have answers to my questions?"

        menu:
            "Because Amelia would have been proud of you no matter what.": #Wait, I wrote that? How the hell was I capable of writing such a good response?! Is this my magnum opus of responses or something?!
                $ renpy.pause (0.5)
                $ kol_tlh_remytherapycounter += 1

                c "Despite being stuck on a slippery slope, you’ve accomplished so much. Despite depression making your life a living hell every day, you managed to get a position to work for the council. You've finally landed your dream job, even if Emera makes it difficult for you."
                c "On top of that, you’re helping to save the world alongside an actual human. All while suffering from such mental anguish that getting out of bed in the morning seems pointless."
                c "Amelia would be so proud to see how far you’ve come while carrying such a heavy burden, and she would be so proud to see you getting the help that you deserve."

                $ renpy.pause (0.5)
                show remy shycry with dissolvemed
                $ renpy.pause (0.5)

                c "Look, it’s clear that you and Amelia cared about each other a lot. Do you really think that she would hate you for a few mishaps that could happen to basically anybody?"
                Ry "I suppose she wouldn’t. She would have stayed by my side regardless of what I went through. In fact, she’d probably have helped me with my research as well."
                Ry "Thanks, [player_name]. I needed that much more than you might think."


            "Because you’re ruining all the help that you’ve gotten as of late with those thoughts.":
                $ kol_tlh_remytherapycounter -= 1

                c "By allowing those thoughts to run rampant, you’re undoing all the help you’ve gotten recently and allowing yourself to be more vulnerable to those thoughts."
                c "Do you really think that Amelia would want to care for somebody who can’t even care for their own mental state?"
                $ renpy.pause (0.5)
                Ry "..."
                $ renpy.pause (0.5)
                Ry "I think I have an answer to at least one of my questions now. Thanks for that."

            "Holding tightly to Amelia won’t help you get better.":
                
                c "The way I see it, Amelia sounded like the type who wouldn’t have wanted to be a burden in death. Do you think that she would be happy if you held on to her instead of letting go and being the best person that you could potentially be?"
                c "I know this is hard, especially since you’ve held on to her memory for so long that you feel like you can’t let go, but the time has come to do so. You have enough people around you to be able to afford it."
                Ry lookcry "I know, [player_name]. I know. I’m…{w=0.75} afraid that, if I let go, then her memory will die out, that she’d be completely forgotten."
                Ry "I’ve become so intertwined with her being gone that I can’t imagine a life where I just leave her like that."
                c "If you remember those that have passed, they will forever live on. Just because you can move on doesn’t mean that you’ll forget Amelia entirely."
                Ry "Perhaps, perhaps not."

        $ renpy.pause (2.0)
        m "Remy seemed to have drifted in thought, leaving streams of tears across the edges of his muzzle. He wanted to say something, but held his breath and slowly shook his head."
        
        $ renpy.pause (0.5)
        play sound "fx/knocking2.ogg"
        $ renpy.pause (1.0)
        
        m "Suddenly, a loud knock at the door echoed throughout the dark room. Remy seemed to be spooked, yet surprise quickly turned to anxiety as he seemed to realise what had just happened."
        $ renpy.pause (0.5)
        Ry shycry "[player_name], could you answer the door for me? I…{w=0.65} need to get something real quick."

        $ renpy.pause (0.5)
        show remy shycry flip with dissolve
        $ renpy.pause (0.5)
        hide remy with easeoutright
        $ renpy.pause (0.5)

        m "Remy quickly went past me and into another room; presumably his bedroom. Deciding that I didn’t have another choice, I answered the door."

        $ renpy.pause (1.5)
        play sound "fx/door/door_open.wav"
        stop music fadeout (3.5)
        $ renpy.pause (1.5)
        show adine frustrated b with easeinright #This must've been a terrifying sight to see if Remy was still in the living room.
        $ renpy.pause (1.5)

        Ad "Where’s Remy?"
        c "He told me that he wanted to go and get something. I think he went into his bedroom, but I’m not certain."
        Ad annoyed b "Did he really just run off as soon as I knocked on the door?"
        c "Is something wrong?"

        $ renpy.pause (0.5)
        show adine disappoint b with dissolvemed
        $ renpy.pause (1.0)

        Ad "It’s a complicated story, [player_name]. Let’s just check up on Remy first."
        c "Alright."

        $ renpy.pause (0.5)
        hide adine with dissolve
        $ renpy.pause (0.5)

        m "Me and Adine went through Remy’s house and knocked on Remy’s bedroom door. After no response, Adine decided to open the door after waiting for a few moments."

        $ renpy.pause (1.5)
        scene kolremybedroom at Pan ((0, 0), (0, 180), 5.0) with dissolveslow
        $ renpy.pause (3.5)
        show adine sad b flip with dissolve
        play music "mx/black_rose_kol.ogg"
        $ renpy.pause (0.5)
        Ad "Remy!"
        $ renpy.pause (0.5)
        hide adine with dissolve
        $ renpy.pause (0.5)
        m "Adine rushed towards Remy while he sat at his window and looked outwards into the rainy night. Remy, in response, looked away in shame while tears fell onto the ground."
        
        $ renpy.pause (1.5)
        show remy shycry at Position(xpos = 0.85)
        show adine sad b flip at Position (xpos = 0.15)
        with dissolvemed
        $ renpy.pause (1.0)
        #This scene. This upcoming scene. I genuinely think that this might be one of the best things I've ever written, even if it's oh so short. Welp, enjoy, weird code stalker!
        Ry "I didn’t want you to see me like this, Adine. I’m sorry."
        Ad disappoint b flip "I don’t care, Remy. After you suddenly hung up like that, I was concerned for the worst. I flew as fast as I could through the rain to see if you were okay."
        Ad sad b flip "I don’t want to lose yet another close friend."
        $ renpy.pause (2.0)
        Ry "I-I’m sorry to have made you worried."
        Ad "Don’t be. I’m just happy that you’re safe."

        $ renpy.pause (0.5)
        hide remy
        hide adine
        with dissolve
        $ renpy.pause (0.5)

        m "Adine’s voice softened as she spoke those last words. She opened her arms and enveloped Remy in her wings, comforting him as Adine gently wiped Remy’s tears away. I also heard the soft sounds of humming coming from the cocoon of dragon wings in front of me."
        $ renpy.pause (1.0)
        Ad normal b "Shush now, Remy. Everything will be alright. I promise."
        $ renpy.pause (2.0)
        m "Several moments had passed before Adine slowly unfolded one of her wings, revealing a less heartbroken Remy."
        $ renpy.pause (0.5)
        Ad "What are you waiting for, [player_name]?"
        $ renpy.pause (0.5)
        m "I moved towards Remy as indicated by Adine, and soon got enveloped by her wings as well. I moved my arms slightly so that I could be able to hold Remy alongside Adine, providing as much comfort as I could to a broken soul."
        $ renpy.pause (2.0)
        m "We held this position for several minutes as the sound of soft rain spread throughout the silent bedroom. Soon, it became too hot inside the group hug for me, so I gently moved out. Taking this as a signal, Adine stopped as well."
        
        $ renpy.pause (1.0)
        show remy shy at Position(xpos = 0.85)
        show adine normal b flip at Position (xpos = 0.15)
        with dissolvemed
        $ renpy.pause (1.0)

        Ry "That was…{w=0.35} something."
        Ad giggle b flip "Was that something enough to comfort you?"
        Ry "I suppose it was, yes."
        Ad normal b flip "Then the first part of my job is done."
        c "The first part?"
        Ad "I’d like to have a nice, long talk with Remy now. I’m guessing that since you’re here, you already had the chance."
        c "Yeah, we did."
        Ry "It was just some lighthearted chatting, that’s all."
        Ad think b flip "With the amount that you cried, I think that it was anything but lighthearted."
        Ry look "Did I really cry that much?"
        Ad "Like I said, we’ll have a nice, long talk."
        Ad normal b flip "Thank you for coming to help Remy, [player_name]. It means a lot to me that you came at such a late hour to try and comfort him when he needed it the most. I was afraid of what he might have done if you never showed up."
        c "It’s no problem, really."
        Ad "In any case, I’d like to talk with Remy privately on some matters, if that’s okay with the both of you."
        Ry normal "If [player_name] is okay with it, then I am as well."
        c "It’s all fine by me."
        
        $ renpy.pause (0.5)
        hide remy
        hide adine
        with dissolve
        $ renpy.pause (1.0)
        m "Respecting Adine’s wishes, I left Remy’s room, leaving Adine and Remy in solitary privacy."
        $ renpy.pause (0.5)
        scene remyapt at Pan ((0, 80), (0,80), 5.0) with dissolve 
        $ renpy.pause (2.5)
        m "Yet, as I started to leave the house, I could overhear the two dragons talking."

        $ renpy.pause (1.5)

        if kol_tlh_remytherapycounter >= 4:
            $ kol_tlh_remytherapywin = True

            Ry normal "Oh, I had more than enough company until you came."
            Ad disappoint b "Did [player_name] hurt you in any way? I can’t see a reason why you would suddenly want to hide the way you did."
            Ry shy "Not in the slightest. You know how things are between us. I call for help, and [player_name] delivers. Not only that, but I received some really good advice for…{w=1.0} some thoughts, shall we say."
            Ad normal b "Then I’m glad to hear it. We don’t want you to feel hurt, Remy. If we can help you in any way, then we will."
            Ad think b "Though, by the sounds of it, [player_name] helped you far more than I ever could."
            Ry "Don’t say that, Adine. You know it’s not true. The fact that you’re here as well disproves that."
            Ad "I suppose you do have a point."
            Ry smile "Besides, maybe you could help me with some things that [player_name] said. I think that, together, we’ll be able to overcome this hurdle."
            Ad giggle b "Definitely."

            $ renpy.pause (1.0)
            stop music fadeout (4.0)
            scene black with fade
            stop soundloop fadeout (3.5)
            $ renpy.pause (1.0)

            m "There was something else that had been said, but by that point I couldn’t hear clearly enough for me to make it out. As I made my way outside, I noticed that the rain had mostly stopped, allowing me to make my way home without getting even more soaked than I already was."
        
        else:

            Ry look "I just don’t understand…"
            $ renpy.pause (0.5)
            Ad disappoint b "I’m afraid I don’t either, Remy. I would’ve never expected this at all."
            Ry sad "[player_name] has helped me through {i}so{/i} much recently. I just can’t fathom why all of it would suddenly be turned upside down."
            Ry "I mean, without the talks that we had, I would’ve never reconnected with you.{w} I would’ve never gone to the orphanage.{w} I would’ve never even gotten help."
            Ry cry "Why would [player_name] turn on me now when I need help the most?"
            Ad sad b "Maybe it was just too late in the night?"
            Ry "I don’t think it’s that. Something changed between us—that’s for certain. I just can’t pinpoint what…"
            $ renpy.pause (1.0)
            Ad disappoint b "We’ll figure it out in the morning, okay? For now, I recommend staying away from [player_name] for a bit. Don’t cut off contact entirely, though. Just…{w=1.0} distance yourself." #This will be crucial later on in a very speccific scenario. Just you wait.
            $ renpy.pause (0.5)
            Ry "But...{w=0.5}{nw}"
            Ad "This is for your own good, Remy. At least, minimise contact until you’re in a better mental state, alright? Just in case [player_name] says something that might send you into another spiral."
            $ renpy.pause (2.0)
            Ry lookcry "Okay."

            $ renpy.pause (1.0)
            stop music fadeout (2.0)
            scene black with fade
            $ renpy.pause (1.0)

            m "I could hear more words being spoken, but they were too muffled to make out. As I made my way outside, I could still see that it was raining heavily."
            $ renpy.pause (1.0)
            c "(Looks like I’ll have to make a run for it again. Hopefully I can arrive relatively dry back home…)"
            stop soundloop fadeout (2.0)
            $ renpy.pause (1.0)

        $ renpy.pause(0.5)
        $ persistent.kol_tlh_chapter4B_skip = True
        $ kol_tlh_4B_played = True
        $ renpy.pause(3.5)

        jump tlh_Chapter5

        # ===========================================
        # END OF CHAPTER 4
        # ===========================================

        


        


        
#MAX MOOD VALUE FOR 4B IS 7
#THE MINIMUM IS -8
#GET 4 TO PASS (unclear choices, maybe bring down depending on testing)

