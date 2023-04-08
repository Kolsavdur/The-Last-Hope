label tlh_Chapter2A:

$ save_name = (_("TLH - Chapter 2A"))

$ renpy.pause (3.0)
scene o4 at Pan((0, 0), (0, 250), 5.0) with dissolveslow
$ renpy.pause (3.0)

m "As was routine, the morning sun arose and shone into my apartment, illuminating the darkness of the previous night. Strangely, the daylight had given me the drive to handle whatever would come my way today."
m "Bizarre dreams of what had happened yesterday rushed through my head, with me forgetting them in mere seconds after I stood up from my bed." #Ey, that rhymes!

if persistent.kol_tlh_chapter2A_skip:
    $ renpy.pause (1.75)
    c "(Wait, haven't I seen this before at some point?)"

    menu:
        s "(Do you want to skip forward?)"

        "Yes.":
            scene black with fade
            stop sound fadeout (1.0)
            stop music fadeout (1.0)
            $ kol_tlh_bryce_escort = True
            jump tlh_Chapter2B

        "No.":
            $ renpy.pause (1.0)


play music "mx/forgotten_forest_kol.ogg" fadein (1.0)
$ renpy.pause (1.0)
play sound "fx/door/doorbell.wav"
$ renpy.pause (1.0)
c "Coming!"

$ renpy.pause (0.5)
play sound "fx/door/door_open.wav"
$ renpy.pause (1.5)
show bryce normal b with dissolvemed

c "Bryce? I thought that you’re still in the hospital."
Br laugh b "I got discharged yesterday evening. And about time, as well. Do you have any idea how hard it is to be stuck in bed for a few days against your will?"
c "Sort of, though I’d imagine it must be extra hard for you, for reasons that may or may not vary." #(He misses his booze.)
Br normal b "I guess you could say that. After all, the force does need their chief to help them every once and a while."
Br stern b "But that’s not why I’m here today. I’ve got some serious things to tell you. Maybe we should go on a walk while I inform you about what’s happening."
c "Alright."

if kol_tlh_letter_read == True:
    m "Before I left, I took the message I had received from the humans with me, just in case I needed it for today."

else:
    Br "Before we go though, you should probably read this."
    $ renpy.pause (0.5)
    m "Bryce handed me a small sealed envelope that at first only looked like your average letter. However, upon closer inspection, I recognised the seal that had been stamped on the envelope."
    $ renpy.pause (0.5)
    Br "This recently came in from the portal; supposedly for you. Another one came in shortly afterwards meant for the council. I think that you should read that now before we go."
    m "I opened the letter and started to read, intrigued as to what it might contain."
    play sound "fx/envelope.wav"
    $ renpy.pause (0.5)

    nvl clear
    window show

    n "Ambassador [player_name],"
    n "Not only have you failed so far in bringing us the generators as agreed beforehand, but you have also indirectly caused the death of your partner. Under normal circumstances, you would have been ordered to return to us immediately, with the trade agreement being cancelled at once."
    n "However, our situation has gotten too dire to simply pull out now. Fierce debates are currently happening as to what we should do to continue this trade offer, so expect a reply within the next few days."
    n "We expect you to fulfil your duties as ambassador in full when you receive our next reply. For now, continue as you are and maintain peace on the dragon’s side."
    n "-The Authorities of Humanity"

    window hide
    nvl clear

    $ kol_tlh_letter_read = True
    $ renpy.pause (1.0)
    Br brow b "I’m guessing that the letter doesn't exactly bring the best of news."
    c "I can’t say. I think this is something that I should think over for a bit."
    Br smirk b "Luckily for us, there is more than enough time to think on our walk."
    Br normal b "Let’s go then, shall we?"

m "Me and Bryce left my apartment and went through the streets, similar to how we first did when Bryce told me about Reza’s first murder."

play sound "fx/steps/clean2.wav"

scene black with fade
$ renpy.pause (1.5)
scene town2 with fade
$ renpy.pause (1.5)
show bryce stern b with dissolve
$ renpy.pause (3.0)

c "I’m guessing that this has to do with the messages we received yesterday, right?"
Br "Yeah, and more."
Br "Are you aware of an abnormally bright star in the night sky by any chance?"
c "More than aware."
Br "So you know."
c "Yeah. I was the one that informed the council about it a few days ago so that we could start making plans about it."
Br brow b "Is that so? I only heard from Emera earlier today that we’re at risk of a potential collision and that our top scientists are currently getting a plan put together."
c "Which is probably why we’re going to go to Emera right now, correct?"
Br smirk b "You’re smarter than you look." #Oof, poor MC...
Br normal b "Though, I shouldn’t be so surprised since you’ve done so well with the investigations recently."
Br stern b "But I’m getting off-track here. Emera wanted to see you about the messages we received yesterday. I’m only guessing that the obligatory comet discussion will come after that, too."
Br "And to think all of these things happened while I was stuck in a damn bed this whole time."

menu:
    "Better that than being dead, I suppose.": #Talk about being blunt here.
        $ renpy.pause (0.5)
        Br brow b "I mean, I guess? I would still prefer to not have been shot in the first place, though."
        c "You do make a point."
        Br stern b "But yeah, rather being shot than dead. I don’t think Sebastian or Maverick would take my death very well."
    
    "You still helped, though.":
        c "Despite that, you still guided the rest of the force while you were in the hospital. That on its own is still impressive."
        Br laugh b "I just told them some basic stuff while they visited me. I wouldn’t exactly call that \“guiding the force\”."
        c "But you still helped them."
        Br normal b "I guess so."

    "They would have happened regardless.":
        Br "The thing is, I could have been on the field, like helping with Reza being sent back to the human world."
        Br "And before you say anything, I know that I gave some advice then. It doesn’t change the fact that I could have helped more if I had been more careful when originally dealing with Reza."
        Br "But that’s sadly just part of being a police officer. You just can’t help everybody everywhere all the time."

$ renpy.pause (1.75)
scene park3 at Pan ((100, 0), (0, 0), 3.0) with dissolveslow
$ renpy.pause (0.75)

m "Eventually, we reached the outside of the office building. Bryce turned over to me with an expression hinting at concern, masked by seriousness."

show bryce stern b with dissolve
$ renpy.pause (0.5)

Br "You ready for this, [player_name]?"
c "I don’t have much of a choice, Bryce."
Br "Then you’re better off than I am. Having to deal with Emera right now of all times, especially with what’s going on, makes me a bit uneasy. My earlier visit was more than enough to prove that."
Br "After all, she could decide to send you home again without further notice, however unlikely that is." #Wjat even is your logic here Bryce? Are you still too high on hospital meds to be able to be a realist here or something?
c "That wouldn’t be such a good idea considering the circumstances right now."
Br "Hence me suggesting that it would be extremely unlikely, but still a possibility nonetheless."
$ renpy.pause (0.25)
Br "Let’s just get this over with."

scene buildingoutside at Pan((0, 0), (0, 0), 0.0) with dissolvemed
$ renpy.pause (0.5)
m "Me and Bryce entered the office building. We slowly went through the halls in silent anticipation, wondering what Emera had to say."
$ renpy.pause (0.5)
show corridor with dissolvemed
$ renpy.pause (0.75)

show bryce stern b flip at Position(xpos = 0.15) with dissolve
play sound "fx/door/door_open.wav"
$ renpy.pause (1.5)
show sebastian drop b at Position(xpos = 0.85) with easeinright
$ renpy.pause (1.0)
hide sebastian with easeoutleft

m "However, just as I was about to open the door, Sebastian left Emera’s office with a distraught face. He looked at Bryce for a short while and left at a rapid pace."
c "(What happened with Sebastian just now?)"

stop music fadeout(10.0)
play sound "fx/knocking1.ogg"
$ renpy.pause (2.0)
Em normal "Come in."
$ renpy.pause (1.0)
play sound "fx/door/door_open.wav"
$ renpy.pause (1.0)
scene emeraroom at Pan ((0, 0), (0, 180), 5.0) with dissolveslow
$ renpy.pause (2.5)

m "Upon entering, Emera shot a glance at both me and Bryce. She seemed to be mildly concerned, as if she had come to a terrible realisation."

show emera frown at Position(xpos = 0.85) with dissolve
$ renpy.pause (1.0)
show bryce stern b flip at Position(xpos = 0.2) with easeinleft

play music "mx/clocks.ogg"
$ renpy.pause (1.0)
Em "Good morning, Ambassador and Chief."
c "Good morning, Minister. I believe that you wanted to see me, correct?"
Em "That is correct, but not for the reason you might think. It seems that we have more...{w=0.8}current matters to discuss."
Br "In what regard, if I may ask?"
Em normal "[player_name], you received a letter from the human world recently, as did we. Do you have that letter here with you?"
c "Yes, I do."
m "I handed the letter to Emera. While she read through it, I started to feel more unrestful, waiting for what her response would be."
$ renpy.pause (1.0)
Em frown "..."
c "Is something wrong?"
Em "Your supposed \“response\” that this message mentioned came earlier today. An officer who was on patrol at the portal saw this and immediately came to report it to me, since he believed that this response would be part of my responsibilities."
Br brow b flip "We did manage to catch Sebastian just before we entered your office, Minister."
Br stern b flip "Though, he seemed to be in too much of a hurry to inform us what was happening."
Em "Because I asked for him to make haste, Chief."
c "Why?"
$ renpy.pause (1.0)

Em "The humans’ response wasn’t just any old thing like you might expect, it seems."

$ renpy.music.set_pause(True, channel="music") #Oh, how I yearn for a simple fade-to-pause. Curse you, Ren'py.
$ renpy.pause (0.5)

Em "Your \"response\", [player_name], seems to be another human."
show bryce brow b flip with dissolvequick

$ renpy.music.set_pause(False, channel="music") 
$ renpy.pause (1.0)

Br "Why would the humans want to send another person through the portal?"
c "Because, despite Reza being dead, everybody is too desperate to give up. My message made that clear enough. The authorities probably sent another ambassador to try and replace Reza in hopes of still getting the generators."
Em ques "I thought of exactly the same thing. After all, judging from your letter and the story of how your world came to be the way it is today, I highly doubt they would want to give up hope so easily."
Em normal "Still, I do wonder why they decided for you to stay here and not return to your world momentarily for a revised plan."
c "I guess we’ll find out shortly."
$ renpy.pause (1.5)
m "We all waited for a short moment until Bryce looked at Emera, as if he wanted to silently ask permission to speak."
$ renpy.pause (0.5)
Br stern b flip "Minister, is there any chance that I could be dismissed from my duties as being your personal escort? Since Reza is no longer a threat, do you not think that it would be better if I could work more closely with [player_name] and this new ambassador?"
Em "I’m afraid that such a matter will take time to consider, as we don’t know whether this new ambassador is better than Reza."

menu:
    "Which is exactly why Bryce needs to be dismissed.":
        c "If Bryce could continue with his regular duties at the office, he’d be more involved with me and whoever came through the portal. Don’t you think that this could indirectly lead to you being safer, Minister?"
        c "On top of that, if the new person {i}does{/i} turn out to be as bad as Reza, then that would create a pretty bad public image for everyone involved. Having Bryce be more available as the Chief of Police would minimise that risk."

        $ renpy.pause (0.5)
        show emera mean with dissolvequick
        $ renpy.pause (0.5)

        m "Emera seemed to flinch after I finished talking. My theory that I had proposed to Remy back in Tatsu Park had been proven correct; if I could use Emera’s fear of public backlash against her, then I could have an easier time convincing her of anything." #Why did you have to spell it out to the player? They're not that dumb as to remember the reference to Remy 3.
        Em frown "I can see your logic here, [player_name]."
        $ renpy.pause (1.0)
        Em "Very well. Chief, you are formally dismissed from your duties."

        $ kol_tlh_bryce_escort = True

        Br "Thank you, Minister."

    "[[Remain silent.]":
        Br "I understand."

m "Bryce grew silent once more, as did the room in eager anticipation."
m "We continued to wait for what seemed like hours, with everybody patiently waiting in stoic anxiety."

$ renpy.pause (1.0)
play sound "fx/knocking1.ogg"
$ renpy.pause (0.5)
m "Eventually, the door to the office received a loud knock."
stop music fadeout (1.0)

Em normal "Come in."
$ renpy.pause (0.5)
play sound "fx/door/door_open.wav"
$ renpy.pause (1.0)

m "The door immediately opened, revealing a very nervous Sebastian and a human face with an expression of slight contempt."
$ renpy.pause (0.3)
Em "Officer, I think that it would be best if you were to leave us alone for now."
Sb drop b "Alright."
$ renpy.pause (0.3)
m "Sebastian left the office, sighing a small sigh of relief as he handed his duties over to Emera."

Em "Welcome to our world. Please, take a seat."
m "The human entered the office, taking the open seat next to me. He looked at me for a short while, smirked, and looked back at Emera."

show logan serious flip at Position(xpos = 0.15) with easeinleft #Dear me, Logan looks so damn cursed here without a thick border around him.
play music "mx/confrontation.ogg" fadein(1.0) #This is such a poor choice of music for this scene, but screw it. I don't like overusing the same tracks.
$ renpy.pause (0.5)

Em "I’m terribly sorry that we have to meet under such circumstances, but since we received a very short notice, we could not prepare your arrival as we did for Reza and [player_name]."
Em ques "Speaking of, might I ask who it is that decided to visit us on such a wonderful day?"
Lg "The name’s Logan. You’re Emera, right?"
Em normal "That is correct. It is truly pleasant to meet you, Ambassador Logan."
Lg "I believe that it would be more pleasant if the circumstances are more favourable."
Lg "First off, I do apologise that humanity couldn’t arrange something before my sudden arrival. The current state of civilization and our ever depleting resources prevented us from wasting more power than we could afford."
Lg normal flip "That’s why I’ve been sent instead. After all, it's better to arrange something in person than sending a bunch of letters back and forth."
Lg serious flip "And now for the reason I’ve been sent here."
Lg "Humanity has issued an ultimatum. We demand that either [player_name] be sent back to us or we receive the generators that are now overdue."
Lg "Refuse these terms, and humanity will cut contact with you and your kind, thus cancelling the trade agreement immediately." #Yikes, sounds quite harsh, though I suppose that it's good leverage considering that humanity might be able to make their own generators soon as revealed by Logan later on...

$ renpy.pause (0.5)
play sound "fx/writing.ogg"

m "Emera went silent for some time, pondering about the situation that had now befallen her. She took some paper, wrote something down, and put it aside. Afterwards, she looked back up in a way that hinted at concealed fear." #Dear me, why does everyone drift off into thought? Reality isn't *that* bad, so you don't need to disassociate so damn hard!

stop sound fadeout (1.0)
$ renpy.pause (1.5)

Em frown "How long do we have to make a decision?"
Lg "Humanity has ordered a response in three days, with a two-day grace period in case efforts had to be made in finding [player_name]."
$ renpy.pause (1.0)
Em mean "And tell me: why exactly did humanity decide to make this ultimatum?"
Lg "As the one responsible for Reza’s and [player_name]’s visits, you should very well know why." #Damn, Logan means business.

show emera frown with dissolvequick

Lg "With Reza being killed by a feral dragon, we believe that it’s no longer safe for us to continue doing business. However, considering our desperate situation, we had no choice but to still follow through with our original agreement."

show bryce brow b flip with dissolvequick #Bryce do be pretty damn suspicious, huh?

Lg "That being said, [player_name] has suddenly become of value to us; more so than Reza, in fact. So, the authorities decided to make this ultimatum."
Lg "Which brings us to the present."
c "Why do the authorities want me all of a sudden? I thought that I didn’t matter too much when I first stepped through the portal."
Lg normal flip "Things change, [player_name]. I’ll fill you in later."
Em frown "I’m afraid that I will have to consult with the rest of the council about this matter, so I will not be able to provide an immediate answer."
Lg serious flip "That’s… why we gave you time to decide."
Em "Ah, yes, my apologies."
Em "For now, you’ll have to have an escort with you during your stay. We unfortunately haven’t arranged a place of your own yet, so you’ll have to temporarily stay with [player_name] until we have sorted things out. Do you find that acceptable?"
Lg normal flip "It’ll do for now."
Em normal "Chief, please arrange an escort for our newly arrived guest."

if kol_tlh_bryce_escort == True:
    Br stern b flip "I’ll arrange for Sebastian to be his new escort. Considering the sudden circumstances of another human being here, I feel that it isn’t safe for [player_name] to be alone anymore."
    Br "That is why I ask–{w=0.6}{nw}"
    Em "Yes, yes, Chief. You may be [player_name]’s escort."
    Br smirk b flip "Thank you, Minister."

else:
    Br stern b flip "I will personally take the position of being the new ambassador’s escort if that pleases you, Minister."
    Em "So be it. Do take note that this still doesn’t exempt you of your duties from me just yet."
    Br "I understand. Thank you, Minister."

$ renpy.pause (1.0)
Em "Now, Ambassador Logan, are there any more things that you need to inform me about?"
Lg serious flip "That should be just about everything."
Em frown "Very well. Now, if you’ll excuse me, I need to inform the rest of the council of humanity’s ultimatum. I shall contact you within the following few days."
Lg "Alright, then."

play sound "fx/chair.wav"
$ renpy.pause (0.8)
hide emera with easeoutleft
$ renpy.pause (0.3)

m "Emera got up from her desk and walked outside her office at a hurried pace, leaving me, Logan and Bryce all alone. An atmosphere of tension started to form."

$ renpy.pause (1.0)
show logan at Position(xpos = 0.65) with ease
show logan serious with dissolve
$ renpy.pause (0.3)
stop music fadeout (8.0)

Br stern b flip "I’ll have to go back to the station to change the schedules for the patrols real quick. Do you think that you’ll be able to take Logan to your home while I’m gone?" #Wow, ditching his duties immediately. Proud of ya, Chief...
c "Yeah. I’ve actually known him for quite a long time at this point, so he shouldn’t be too much trouble."
Lg annoyed "I’m {i}right{/i} here, [player_name]."
Br laugh b flip "Actually, I can definitely see that now."
Br normal b flip "I’ll come to your place after I’m done at the office. From there we’ll be able to manage the entire escort situation."
c "Didn’t you just handle that, Bryce? After all, doesn’t any order from Emera immediately take effect?"
Br stern b flip "Not with deciding an escort for a high-profile guest, as simply deciding who the escort will be on the spot isn’t really possible due to how complex the process actually is. All I could do now was accept the order to arrange an escort."
Br "We went through quite the process just to assign Maverick to Reza and Sebastian to you. This will likely be the same."
Lg normal "Then you better get on that."
$ renpy.pause (0.4)
Br stern b flip "I guess I should. Goodbye, [player_name] and Logan."

show bryce stern b with dissolve
hide bryce with easeoutleft
$ renpy.pause (0.3)
show logan normal at center with ease

m "Bryce slowly left the office in a slightly tired manner, leaving only me and Logan left. Logan sighed, relieved to no longer be the messenger of humanity."

play music "mx/stride_kol.ogg" fadein (3.0)
$ renpy.pause (1.3)

Lg serious "Damn, that was hard. I guess I finally understand why people are afraid of talking to people in power." #It was hard because you were playing the most vicious of vipers during that talk, Logan. Politeness and respect goes a long way.
Lg annoyed "I wonder how you managed to cope with being an ambassador to literal dragons for like… what, two weeks?"
Lg normal "Eh, whatever. It’s great to see you again, [player_name]."
c "Same here Logan, even if our meeting would be better under more favourable circumstances." #And now the MC is copying logan. Wow, how creative.
Lg serious "Heh, you’re telling me. Here I hoped that we would hopefully see each other again in a street filled with functional lights and human electronics, but as you can see, that is clearly not the case."
c "Well, we {i}could{/i} go on a walk in a street with functional street lights, if that’s what you really want."
Lg normal "Anything to get me the hell away from bureaucracy for a few moments. The lifestyle just doesn’t suit me."
c "Then why did you become an ambassador?"
Lg serious "I’ll explain everything when we’re in private. Some things just aren’t meant for prying ears."

hide logan with dissolve
$ renpy.pause (0.3)
show corridor with dissolvemed
$ renpy.pause (1.0)

m "We both left Emera’s office, excited to see the outside world once more. Suddenly, I felt far more free than I was just a few moments ago, having not just the ability to move around as I wished but also not feeling the tension that had formed during Emera and Logan’s conversation anymore."

$ renpy.pause (1.0)
scene park3 at Pan ((100, 0), (100, 0), 3.0) with dissolve
$ renpy.pause (1.0)

m "It wasn’t long before we both left the office building altogether, finally breathing fresh air once again."
$ renpy.pause (1.0)
scene park3 at Pan ((100, 0), (100, 0), 3.0) with dissolve
$ renpy.pause (1.0)
m "We walked for a bit in the streets, taking the longer yet isolated paths to my apartment. As soon as there wasn’t anybody that could eavesdrop on us, Logan started to talk."

stop music fadeout (2.5)
scene kolmoretown2 with dissolve
$ renpy.pause (1.0)
show logan normal with dissolve
$ renpy.pause (1.5)
play music "mx/colossal_forest_kol.ogg" fadein (1.0)

Lg serious "I didn’t exactly want to be the bearer of bad news, [player_name]. I had my hands tied behind my back."
c "What exactly do you mean?"
Lg "The authorities back home essentially ordered me to be the one to deliver the news since they knew that I was somebody who you had a lot of contact with considering that we used to work together at some point."
Lg "They put me through some basic training as to what I should and shouldn’t do as an ambassador, filling my head as if I was in elementary school all over again."
c "So that’s why you sounded so harsh when you talked with Emera. You’ve changed." #AKA, my excuse if Logan seems way different in terms of character to his TLD counterpart. >:)
Lg "No, [player_name].{w} {i}Everything{/i} has changed."
Lg "You have to understand: when the authorities got Reza’s body, as well as the report stating that he was killed by a feral dragon that nobody had any apparent control over, they were enraged, to say the least."
Lg "Trust and goodwill has been shattered back home. Hell, there’s rumours going around that one of the authorities even suggested a full-scale invasion as recompense. It’s a miracle that they even decided to send another ambassador through." #Oooo, a reference to Remy's bad ending. I guess this is a poor attempt to tie in with TLD again, huh?
c "A lot of chaos has been going on here as well. I’m guessing that you managed to read the report yourself before coming here, right?"
Lg "Yeah. What about it?"
c "Then you’re aware of Reza’s crime spree."

$ renpy.pause (0.3)
m "Logan winced." #Why?
$ renpy.pause (0.2)

Lg "Best we don’t talk about that. The belief back home ranges from outright lies made up by the dragons to justify their, and I quote, \“senseless massacre of humanity’s future hope\”, to outright sympathy for the dragons." #But what does that have anything to do with you wincing?!
Lg "But since arguments didn’t bring results, they decided to make a plan that involved getting said results."
c "The ultimatum."
Lg "Exactly. And who else to use to send it than somebody who knew a lot about one of their ambassadors?"
Lg normal "I bet that they’re regretting that decision right now."
$ renpy.pause (1.5)
show town1 behind logan with dissolve
$ renpy.pause (1.5)
scene kolapartmentnoon with dissolve

m "We eventually reached my apartment after quite some time of walking and talking. I opened the door and let Logan walk in first. He stood at the entrance for some time and glared at everything my home away from home had to offer before taking a seat on my couch."

$ renpy.pause (0.5)
play sound "fx/door/door_open.wav"
$ renpy.pause (2.25)
scene o at Pan((0, 0), (0, 150), 3.0) with dissolvemed
$ renpy.pause (2.0)

show logan normal with easeinright
$ renpy.pause (1.5)
Lg smiling "Damn, this feels almost nostalgic in a way."
Lg normal "I never thought that I’d say that a working light bulb and a proper couch would ever be nostalgic, but I guess here we are." #You... literally have a proper couch of sorts back at your place. Is it also so hard to assume that you have a working lightbulb in your stashes somewhere as well, Logan?

menu:
    "My reaction was quite similar to when I arrived here.":
        Lg "And for good reason. Who would’ve guessed that such simple everyday things would end up being such luxuries?"
        Lg serious "It just shows us that everybody wants life to return to the way it was."
        c "Yeah."

    "You’ll get used to it.":
        $ renpy.pause (0.5)
        Lg serious "I hope I don’t. It would just make going back so much harder if I got used to the pleasantries that dragons have over here."
        $ renpy.pause (0.5) #Awkward silence or something? Eh, whatevs.

    "Let’s just hope that we can have such pleasantries again soon enough.":
        $ renpy.pause (0.5)
        Lg serious "Only if we can actually get the generators we’re owed."
        c "I suppose that's fair."


$ renpy.pause (1.0)
c "You mentioned that I suddenly became of value back home and that you think that the authorities regret sending you through. Any explanation to that?"
Lg "Yeah. Recently, there was–{w=0.6}{nw}"
stop music fadeout (2.0)

play sound "fx/knocking1.ogg"
$ renpy.pause (1.0)
play sound "fx/door/door_open.wav"
$ renpy.pause (1.0)

show logan at Position (xpos = 0.25) with ease
show logan serious flip with dissolve
$ renpy.pause (0.5)
show bryce smirk b at Position (xpos = 0.85) with easeinright
$ renpy.pause (0.5)
play music "mx/clouds.ogg" fadein (1.0)

Br "Hey, [player_name]. Long time no see." #So Bryce is making dad jokes now, huh? Hmmmmmmmmmmmm...
c "I didn’t think that an hour would be considered a long time for you, Bryce."
Br laugh b "Yeah, you got me."
Br normal b "Anyway, the escorts have now been arranged."

if kol_tlh_bryce_escort == True:
    Br smirk b "Sebastian will now be transferred to Logan, while you get to be escorted by yours truly."
    Br normal b "I figured that Logan might want a quick tour around town, so I’ve asked Sebsatian to handle that."
    c "Speaking of, where is Sebastian?"
    Sb drop b "Right here, [player_name]."

    show sebastian drop b at Position (xpos = 0.95) with easeinright
    $ renpy.pause (0.5)
    m "Sebastian looked at Logan with a slightly annoyed face while speaking in a petty tone."
    $ renpy.pause (0.25)
    Sb "So, do you want me to show you around town?"
    Lg normal flip "But of course. How else am I supposed to learn about dragonkind?"
    Sb "Then please follow me."
    $ renpy.pause (0.5)

    show sebastian drop b flip with dissolve

    hide sebastian
    hide logan
    with easeoutright
    $ renpy.pause (0.5)
    show bryce normal b with dissolve
    show bryce at center with ease

    m "Sebastian left my apartment with Logan following right behind him. After they left, I could hear a soft chuckle coming from Bryce."
    c "What’s so funny?"
    Br smirk b "Apparently Sebastian wasn’t entirely prepared to see another human pop out of the portal while on patrol."
    Br laugh b "So, when Logan came through, all he could do was stand awkwardly in shock and tell him to wait until he went to Emera first." #Please elaborate, past me. What sleep-deprived brainwave made you think that this would create a perfectly clear image?
    Br "I don’t think that Sebastian will forget that awkward encounter any time soon."
    c "I guess so."
    Br stern b "Now, let’s get back to business. Even if you know the town pretty well at this point, I’ll have to accompany you to any areas that might be unsafe. I’m pretty sure you get the drill."
    c "If I didn’t get it by now, then I’d probably have a lot more problems to deal with."
    Br "Yeah. Just a small problem though: I still have a lot of work to catch up since my trip to the hospital, and I don’t think that being your escort for the day would help with my work. Would it be possible if I were to leave you on your own for now?" #Yeah, I know I'm supposed to guard you and whatevs, but I kinda don't wanna. Don't tell Emera pls and thx
    c "What if Emera realises that I’ve been walking around town without an escort?"
    Br "Then I might lose my job. Thing is, if I don’t keep up with my work, then I’ll {i}definitely{/i} lose my job. I have to choose the lesser evil."
    c "I see. In that case, I’ll stay undercover when I’m going out. I don’t want to give you any extra stuff to deal with."
    Br smirk b "Thanks. I appreciate it. I’ll be at the police office if you’re looking for me."
    Br "Have a great day, [player_name]."
    c "You too, Bryce."

    show bryce smirk b flip with dissolve
    hide bryce with easeoutright
    $ renpy.pause (0.5)
    m "Bryce left my apartment, leaving me to embrace the foreign serenity I was so used to nowadays."
    m "I wondered for some time as to what I should spend the rest of my day on, and I eventually concluded that I should visit Remy and see how he is doing."

else:
    Br "I’m here to pick Logan up so that I could show him around town. After all, what’s an ambassador if they don’t even know where they are?"
    Lg normal flip "Well, luckily for you, I just so happened to be here."
    Br smirk b "As is expected."
    Br normal b "So, are you up for my offer?"
    Lg annoyed flip "Well, I don’t really have much else to do except for educating [player_name] over here about what's happening back home."
    $ renpy.pause (0.5)
    Lg normal flip "Sure, why not?"
    Br "Then please, follow me."
    Br "As for you [player_name], I know that Sebastian is supposed to look out for you, but he's held up at the police office thanks to some paperwork."
    c "What if Emera realises that I’ve been walking around town without an escort?"
    Br stern b "Then I might lose my job. Thing is, if Sebastian doesn't keep up with his work, then he'll {i}definitely{/i} lose his job whether I like it or not. I have to choose the lesser evil." #Carin' about the homies; that's what Bryce does.
    c "I see. In that case, I’ll stay undercover when I’m going out. I don’t want to give you any extra stuff to deal with."
    Br "Thanks a lot."
    Br normal b "Come on, Logan. We have things to do."
    Lg "Yeah, yeah."

    show bryce normal b flip with dissolve

    hide bryce
    hide logan
    with easeoutright
    $ renpy.pause (0.5)
    m "Logan followed soon after Bryce left my apartment, leaving me behind. I contemplated what I should do for the rest of the day, eventually deciding to pay Remy a visit."

stop music fadeout (1.0)
$ renpy.pause (0.5)

m "Still, there were several unanswered questions that I still had. Why are the humans supposedly regretting sending Logan through? Why am I needed back home? What’s going to happen with the comet now that humanity has demanded to receive the generators that they’re owed? Why did Logan say that a feral dragon killed Reza?"
c "(I’ll have to talk with Emera about the ultimatum in private. She’ll be able to come up with a far better plan than I could.)" #Debatable, as her plan would probably be filled with bias to keep dragon culture intact or something.
m "In spite of those intrusive questions that I asked myself, I pushed my thoughts aside as I left my apartment on my way to the library."

scene black with fade
play sound "fx/steps/clean2.wav"
$ renpy.pause (4.0)
scene library at Pan ((640, 228), (0,228), 10.0) with dissolveslow
$ renpy.pause (1.0)

m "The library appeared to be much quieter than usual, almost desolate, if Remy hadn't been moving between the bookcases so smoothly. I barely had to move before he noticed me." #Remy be zooming!

play music "mx/choices.ogg" fadein (0.5)
$ renpy.pause (0.5)

show remy normal with easeinright
$ renpy.pause (0.5)
show remy shy with dissolve

Ry "Oh, good afternoon, [player_name]. Please forgive me if I can’t talk for long. I received a very important task from the council that I have to hand in this evening, with it proving to be quite a challenge to manage."
c "I’m guessing that it has something to do with the comet, right?"

show remy look with dissolvemed
$ renpy.pause (0.85)
Ry "Yes."
Ry "I need to gather all of the resources we have on asteroid redirection techniques and present them to the council in such a way that they can come up with a plan."

menu:
    "Do you need any help?":
        $ renpy.pause (0.5)

        Ry "If I could get help, then yes. Sadly, due to the confidential nature of a potential…"
        $ renpy.pause (0.35)
        m "Remy looked around to see if anybody was nearby. After no-one was found, he continued talking in a softer tone."
        $ renpy.pause (0.25)
        Ry "…extinction event, this is all work that I need to keep between me and the council, even if you’re directly involved with this."
        Ry "I'm sorry."
        c "It's alright."
    
    "Are you sure you’ll be able to manage that amount of work alone?":
        $ renpy.pause (0.5)

        Ry shy "I don’t really have a choice here, [player_name]. Whether or not I’m able to do this is irrelevant; all that matters is that I must finish before this evening."

    "Aren’t there others that are supposed to help with this project?":
        $ renpy.pause (0.5)

        Ry shy "There are, but they aren't here right now. I mean, how is a single dragon supposed to gather all of our knowledge on a single topic and present it to our top scientists?"
        Ry look "All the teamwork sadly doesn’t make my job much easier, though."

$ renpy.pause (0.5)
Ry normal "In any case, is there anything I can help you with considering that you’re here?"
c "Not really. I just wanted to check up on you, that’s all. How are your injuries today?"
Ry smile "They're all healed now."
c "That’s good to hear. I can imagine that going from bookshelf to bookshelf would be substantially more difficult if you’re constantly limping."
Ry normal "I guess so."
$ renpy.pause (0.5)
Ry shy "I’m sorry, but I really do need to get back to work. I’ll let you know when I find an opportunity for us to do something."
c "I shall eagerly wait for your response, then."
Ry smile "So be it."

hide remy with easeoutleft

m "Remy dashed back into the library's narrow corridors. I could see how he gathered several books and stacked them to form a small pillar, peering around the sides of the books as he carried them to see where he was going. Remy eventually set the books on a nearby table, sat down, and began reading them."
c "(I’m proud of you, Remy. That could have been quite nasty if you accidentally tripped.)"
m "Deciding that I have nothing left to do at the library anymore, I left the building to wander the streets of the town."
stop music fadeout (3.0)
play sound "fx/steps/clean2.wav"
$ renpy.pause (2.5)

scene koloutsidelibrary at Pan ((0, 180), (0, 180), 2.0) with dissolve
$ renpy.pause (1.5)
scene town3 with dissolve
$ renpy.pause (1.5)
scene kolmoretown3 with dissolve
$ renpy.pause (1.5)

m "I strolled through town, hoping that I could have the clarity I needed to organise my thoughts."
$ renpy.pause (1.5)
scene town1 with dissolve
$ renpy.pause (1.5)
m "Suddenly, I heard a footstep behind me. An ominous presence started to surround the area as intrigue took over me."
$ renpy.pause (0.5)
c "What are you doing here, Maverick?"

show maverick normal with dissolve
#Oh dear, how I detest this scene just because of how it absolutely violates Mav's character. Damn you me for never learning how to write Mav properly.
Mv "I am simply taking a nice pleasant stroll through the town and enjoying the sunlight, that’s all."
c "I don’t believe you for a second. Since when did you randomly appear out of nowhere by chance?"
Mv "I see that the investigations with Bryce have taught you much. Good."
c "Spit it out already, Maverick. I already know that you’re here for an ulterior motive."
Mv annoyed "So impatient of you."

$ renpy.pause (0.5)
play music "mx/forge.ogg" fadein (2.0)
$ renpy.pause (0.5)

Mv normal "I wanted to apologise to you."
c "For what?"
Mv angry "Are you this naive, despite everything that has happened?"
Mv normal "I wanted to apologise for the way I treated you. I was wrong to assume you wanted to help Reza, despite everything you've done so far proving otherwise."
Mv nice "Do understand that from my position, I had no other choice than to be sceptical of you. After all, everything that your so-called colleague has done painted humanity in a bad light."
Mv "It was only reasonable to suspect you had something to do with Reza’s plan."
Mv angry "But don't think for a second that I'm letting you off the hook just because humanity's new toy has arrived."
Mv "I’ll have to watch you and your partner closely to try and prevent another potential incident occurring."

menu:
    "I understand.":
        $ renpy.pause (0.5)
        Mv nice "Glad we’re on the same page."

    "Why not just keep your eyes on Logan?":
        $ renpy.pause (0.5)

        Mv "That would be like asking me to ignore a potential building that might collapse just because a single support beam isn’t faulty."
        Mv normal "You of all people should understand this by now."

    "You’ll only waste your time.":
        Mv "And put everyone in danger again by not stopping another potential serial killer?"
        Mv "I’m not going to be thrown around again by Bryce. I will act should the need arise."

show maverick normal with dissolve
$ renpy.pause (1.5)

Mv "I should be going now."

hide maverick with dissolve
$ renpy.pause (1.5)

c "Wait!"

$ renpy.pause (1.0)
show maverick normal with dissolve

Mv "What do you want?"
stop music fadeout (0.5)
c "Why did you say that a feral dragon killed Reza?" #And it gets worse, because of course it does. Bloody hell, this is so out of character for Mav it's unreal.

show maverick scared with dissolve

$ renpy.pause (0.5)
m "Maverick seemed to be slightly taken back by the question. He thought about his response for quite some time before answering me."

show maverick normal with dissolve
$ renpy.pause (1.5)

play music "mx/intrigue.ogg" fadein (3.5)
$ renpy.pause (0.95)
Mv "You made me realise just how fragile our trade agreement truly was."
Mv angry "Because of you, Bryce got shot by Reza several times and had to stay in the hospital."
Mv normal "However, if it weren’t for you, Bryce might have died if I had gone through with my original plan of storming the facility head-on."
Mv "Do you not realise that should Bryce have died, dragonkind would most likely have stopped the trade agreement right then and there? The council wouldn’t take the death of a police chief at the hands of an ambassador too lightly."
Mv "Even then, the fact that Bryce did get shot doesn’t exactly help to make relations more stable."
Mv "That's why, while making copies, I changed the report you wrote for the humans so that when they read what happened, they didn't immediately close the portal from their side thanks to the loss of one of their ambassadors."
Mv "I also edited reports that were sent to the council to help ease the pains, one of which I personally delivered to Emera."
Mv sad "Yes, I know this is blatant corruption, but I still tried my best with what I could to make the trade just a little bit more stable."
Mv scared "That was before the news about the comet or the new ambassador, however."
c "Do you have any idea of the consequences of what you have done, Maverick? If Bryce were to figure out that you forged the report, then-{w=2.8}{nw}"
#wut did you even say, mav? just... *wut*.
show maverick angry with dissolve

Mv "I know damn well what will happen, [player_name]. I don’t need you of all people to remind me." with hpunch
Mv "Besides, it’s only a matter of time before Bryce finds out. I’m asking you to play along for now so that both our civilisations won’t crumble."
Mv normal "You need our generators to continue living, and we need your PDAs for the comet."
Mv annoyed "As an officer, I despise the fact that I considered doing this in the first place, but this will benefit everyone. I had no choice but to choose the lesser evil."
Mv normal "[player_name], everyone's lives are in your hands. Don't mess this up."

hide maverick with dissolve
play sound "fx/takeoff.ogg"

m "Maverick turned around and took off before I could say anything. Several other questions lingered in my mind, with no hope of receiving answers. Maverick appeared to have another reason for committing a crime in order to cover his tracks, but what does that entail?"
m "I fear that I’m missing a crucial part of the puzzle, but I can’t exactly say what that piece is, nor where it would fit in."

stop music fadeout (1.0)

c "(I should probably just go home. I think I’ve had more than enough confusion for today.)"
m "I slowly collected all my stray thoughts as best as I could and slowly strolled back home."

scene black with fade
$ renpy.pause (2.0)
scene o at Pan((0, 0), (0, 250), 5.0) with dissolvemed
$ renpy.pause (2.0)

m "In the evening, I arrived at my apartment. The sun was slowly setting on the horizon, bathing the distant portal in divine rays of light."
m "My mind, however, is not at ease. There is simply far too much going on that would affect the lives of millions of people. These thoughts eventually gave way to doubt, and doubt gave way to insecurities. After all, a single blunder could wipe out an entire civilization."

$ renpy.pause (1.0)
play sound "fx/door/doorbell.wav"
$ renpy.pause (0.85)
play sound "fx/door/door_open.wav"
$ renpy.pause (2.0)

show logan normal with easeinright
$ renpy.pause (1.0)
play music "mx/barren.ogg" fadein (3.0)

Lg "Good evening, \"Ambassador\" [player_name]."
c "Hey, Logan. So, I’m guessing that you hopefully learned about some things about the town?"
Lg smiling "Yeah, I did. I even got my official ambassador status while I was on my little tour. I honestly didn’t think that I’d get my status today, but it seems that I was wrong."
c "That’s only because of the circumstances that led to your arrival."
Lg serious "Well, what would you even expect? I mean, I literally came here, demanded some stuff on behalf of humanity and just went on my way."
Lg annoyed "I’m surprised the dragons didn’t immediately send me back."

menu:
    "They almost did send me back a while ago.":
        $ renpy.pause (0.5)

        Lg serious "Is that so?"
        c "Yeah. Emera wanted to send me home for safety during Reza's murders. I couldn't let her, for obvious reasons. Regardless, she chose to send me home despite my objections."
        Lg annoyed "But something happened preventing you from going back."
        c "The portal was broken."

        show logan surprised with dissolve

        Lg "Excuse me, {i}what?!{/i}" with hpunch
        c "We were able to fix it though, but that came a bit later."

        $ renpy.pause (1.0)
        show logan annoyed with dissolve
        $ renpy.pause (1.0)

        Lg normal "You know, I’d like to record your experiences here at some point. It would be very interesting to go through all of that and just see what you went through."
        c "You'd be surprised."
        Lg "How ominous."

    "That wouldn’t have been a very good choice on their side.":
        $ renpy.pause (1.0)

        Lg annoyed "I suppose that’s true. From what I understand, the dragons really need those PDAs for some reason. Sending humanity’s messenger back probably isn’t a good way of getting those PDAs."
        Lg serious "And with how desperate everybody is getting back home, I fear that the authorities will go through drastic measures if they don’t get what they want."

    "It’s all because of how kind the dragons actually are to us.":
        $ renpy.pause (1.0)

        Lg thinking "From what I’ve seen here so far, I have to agree with you."
        Lg annoyed "If you were to ask me a few days ago, then I’d heavily disagree."
        c "Due to Reza, I presume."
        Lg serious "Among other things. Like I said, dragons have been getting a bad reputation back home, and things are probably going to get even worse if they refuse the ultimatum."
        Lg "Consider this: the dragons don't have much to lose, whereas the humans are throwing away all hope by taking such a big risk."
        Lg annoyed "And you know how the authorities are."
        c "I do. They always get what they want in the end."
        Lg "And what do you think will happen if the dragons refuse?"
        $ renpy.pause (1.0) #Invasion time, baby!
        c "I see."
        Lg "Precisely."

$ renpy.pause (1.0)
m "Logan seemed to drift off for a moment, causing an eerie silence to grow between the two of us."
$ renpy.pause (1.0)
c "I just remembered something. You never got the chance to answer my question."
Lg annoyed "Question?"
$ renpy.pause (0.75)
Lg serious "Oh, that."
m "Logan sighed heavily while making himself comfortable on the couch."
Lg "This… is going to be a long answer. Make yourself comfortable, as I don’t want your attention to drift here, especially on something as stupid as a cramp or whatever." #Heh, it's a reference!
c "Got it."
Lg "Alright. I’ll start from just a few hours before I left."

stop music fadeout (2.0)

scene black with dissolveslow
$ renpy.pause (2.0)
nvl clear
window show

play music "mx/flashback.ogg" fadein 0.5 #Because you gotta call back to the original Logan infodump, eh? Huzzah for recycled lore! :D

n "For a long time after Reza's body was sent through, humanity debated what to do. The report was read by the authorities, and they were not pleased. I already mentioned that everyone had their own ideas about what we should do, so it took a long time for them to decide to send me through."
n "A scout had appeared while they were making preparations for me to venture into the unknown. Apparently, a monumental discovery was made; one that was far too significant to ignore."
n "I should clarify that shortly after you left, humanity began to develop a backup plan in case your mission failed. Scouts were dispatched further and further from the city and into the desert, hoping to find something that we could use to extend the lifespan of the city for a little bit while we impatiently waited for your return."

window hide
nvl clear
window show

n "One of those scouting missions was a huge success. According to the report, this scout discovered an abandoned copper mine a few miles northeast of the city, complete with primitive smelting equipment. The mine also didn't appear to be completely dry, as it still contained some copper ore that could be smelted."
n "As if it weren't stunning enough, mountains of electronic scrap were discovered farther inside the mine, just... lying there. Forgotten. A few samples were tested, and the findings were remarkable. Even after all these years, some components were still basically functional."
n "The authorities freaked out when they heard the news—so much so that they almost forgot about their original plan to try and get you back. Of course, as you might expect, more bickering followed. I can’t even blame them there; after all, what would you think would happen if you were to show something like a functional lightbulb to someone that hasn’t experienced the luxury of a house with electricity for several years?"

window hide
nvl clear
window show

n "Now, to actually answer your question: I think that the authorities now regret choosing me for the mission to deliver the ultimatum because I’m the best bet they have of making something useful out of those electronics. I could theoretically repair something thanks to my experience working with electronics as well as my master's degree in electromagnetism from back in the day, but only if I had some old blueprints."
n "I believe why the authorities suddenly want you back is because of the PDA you have, as it has a lot of specialised knowledge of electronic equipment among other things, if I remember correctly. Of course, these are only my theories and not an official reason. As far as I know, the authorities want you specifically and not your PDA, even if all the evidence points against that."
n "Unfortunately for them, everything had already been arranged at that point, so there was no turning back. I stepped through the portal, and the rest is history."

window hide
nvl clear

scene o at Pan((0, 250), (0, 250), 5.0) with dissolve
show logan annoyed with dissolvemed
$ renpy.pause (2.0)

Lg normal "Ironic to think that in both scenarios I was the authorities’ best bet in getting what they want, don’t you think?"
Lg serious "I just hope that I can help everybody back home. Sure, if I had undergone the full ambassador training that you and Reza went through, I’d probably be in a better position for negotiation, but that’s obviously not the case."
c "Aren’t there other people back home that could help with the electronics? I’m pretty sure that there’s a skilled electrician somewhere that would be able to help."
Lg "That’s the thing: only some former associates of mine remain to do the task. Everybody that actually has the proper skill needed has fallen seriously ill, which means that they’re all on life support and passively draining our energy reserves."
Lg "Do you see the problem here?"
c "I… {w=0.6}didn’t think things would be that bad back home."
Lg "And that’s why I’m here. I want to do everything in my power to help that which I deeply care about."
$ renpy.pause (1.5)
c "I’m afraid that getting the generators any time soon isn’t going to happen."
Lg "The dragons don’t have a choice. If they–{w=1.3}{nw}"
c "No, you don’t understand. They’re going to need every generator they can get."
Lg annoyed "I’m confused. They should have already made the generators that they’ll be sending us, correct?"
c "I think that it’s my turn to inform you on what’s going on."

show black with fade
$ renpy.pause (3.0)
show logan surprised
stop music fadeout (4.0)
$ renpy.pause (0.5)
hide black with dissolve

Lg "..."
Lg "{i}A comet?{/i}"
$ renpy.pause (0.75)
show logan serious with dissolve
$ renpy.pause (0.5)
play music "mx/judgement.ogg" fadein (1.5)

Lg "How is it that you always get yourself into the strangest of situations, [player_name]? First with all the work we did together, then you getting selected as an ambassador to a dragon-infested world, and now you’re responsible for saving said world from a potential extinction event."

show logan annoyed with dissolveslow

Lg "It seems that we’re on a crossroad here. Choose one route, and neglect the other."
Lg "You know that I’m not letting humanity down, and from what I understand of your little story, you aren’t going too either."
Lg "Yet, you also want to try and save the dragons, correct?"
c "That's my goal."
Lg "How did you even figure out that a comet was on its way?"
c "I...{w=0.5}{nw}"
$ renpy.pause (1.5)
c "I pointed my PDA at the sky, which allowed it to determine that an extinction-level comet was on its way."
Lg "Interesting. I didn’t think that the PDAs’ feature to determine astrological events would work in an alien world."
c "Me neither. Now, is there anything that we can do to try and resolve this problem?"
Lg serious "Not that I can think of right now. It will take some serious idea-testing and brainstorming to solve this. I'll probably have to let you know later."
Lg "Though, there’s still something you need to keep in mind: Humanity is still my top priority. I don’t want to spark hope in everybody back home just to abandon them all. Everything I do is for the benefit of humanity first. Got that?"

stop music fadeout (1.5)

c "I guess."
Lg "Good."

$ renpy.pause (0.5)
play music "mx/clouds.ogg" fadein (4.0) #Because everybody likes a tonal whiplash, no?
$ renpy.pause (0.5)

Lg normal "For now, I’m taking the rest of this day off. Today has been pretty exhausting. Sadly, I didn't get my own place during my trip yet, so I’ll still have to stay with you for the night until something gets arranged for me."
c "I don’t mind. Anything in particular you wanted to do?"
Lg "I wanted to hang out with somebody."
Lg thinking "What was his name again? {w}You know, big guy? {w}Scars on his neck and muzzle?"
c "Bryce?"
Lg normal "Yeah, that’s the one. He invited me to a little event later, to which I might be gone for some time."
c "Let me guess, he invited you to the bar for some drinking?"
Lg annoyed "How did you–{w=0.75}{nw}"
$ renpy.pause (0.4)
Lg normal "Ah.{w=0.4} Any advice, then?"

if nodrinks == True:
    c "None. You won’t stand a chance, {i}especially{/i} if he starts challenging you to a competition according to any bystanders that happened to be near Bryce when he starts drinking."

else:
    c "None. You won’t stand a chance, {i}especially{/i} if he starts challenging you to a competition."

Lg "Competitions, huh? It’s been a while since I’ve been seriously drunk, but I think I’ll manage."
c "I significantly doubt that."
Lg smiling "And I significantly don’t doubt that."
c "Then prepare to spend the night sleeping on the floor."
Lg normal "How comforting."
$ renpy.pause (0.35)
Lg "Anyway, for now, I’m going to go to the library to read up on some stuff. It’ll probably be better if I can immerse myself in some dragon culture when, you know, I’m actually taking part in the effort to negotiate with said culture."
c "Do you think that you’ll be able to find your way?"
Lg smiling "Nope!"
Lg normal "The plan is to just wander around until I recognise where the library actually is." #Nope, not allowed. Bad Logan. You can't be a rebel here! Look where that took Reza to!
Lg annoyed "Or if I happen to find my escort somewhere."

if kol_tlh_bryce_escort == True:
    c "Well, Sebastian shouldn't be far. You can just call him on the phone if you want."

else:
    c "Well, Bryce shouldn't be far. You can just call him on the phone if you want."

Lg serious "Fine. Do you know the police office's number? That is, assuming they're even at the station in the first place."
c "It’s on a piece of paper next to the phone."

if kol_tlh_bryce_escort == True:

    hide logan with dissolve
    $ renpy.pause (0.5)
    m "Logan went to the phone and started to called the police office for Sebastian. After a short while, he hung up and sighed."
    $ renpy.pause (0.5)
    show logan serious with dissolve
    $ renpy.pause (0.5)
    Lg "And that’s done. I’ll just wait outside for that one dragon that looks like a raptor."
    c "Sebastian."
    Lg "Yeah, yeah. Still need to learn everybody’s names."

else:
    hide logan with dissolve
    $ renpy.pause (0.5)
    m "Logan went to the phone and started to called the police office for Bryce. After a short while, he hung up and sighed."
    $ renpy.pause (0.5)
    show logan serious with dissolve
    $ renpy.pause (0.5)
    Lg "And that’s done. I’ll just wait for Bryce outside."

c "In that case, I'll catch you later. {w}Hopefully."
Lg smiling "As usual, you’re underestimating me, [player_name]."
Lg normal "But enough of that. See you later." #"Later" being whenever Logan and Bryce return to consciousness, that is.

show logan normal flip with dissolve
hide logan with easeoutright
$ renpy.pause (0.5)
play sound "fx/door/doorclose.ogg"
$ renpy.pause (1.0)

m "Logan left my apartment and waited outside. I thought over the new information that I had received from him as well as how that could influence the trade agreement. After all, if humanity manages to repair our broken generators or even create a new one from scratch, there wouldn't be a real benefit in continuing our deal with the dragons."

$ renpy.pause (0.5)
scene black with fade
$ renpy.pause (0.5)
stop music fadeout (2.5)

m "I let my thoughts wander in my mind as the day slowly came to an end."

$ persistent.kol_tlh_chapter2A_skip = True
$ renpy.pause (4.5)

# ===========================================
# END OF CHAPTER 2A
# ===========================================

label tlh_Chapter2B:

$ save_name = (_("TLH - Chapter 2B"))

$ renpy.pause (2.5)
scene o at Pan((0, 0), (0, 250), 5.0) with dissolveslow
$ renpy.pause (7.0)

play sound "fx/answeringmachine.ogg"
$ renpy.pause (0.5)

Ry normal "Hello, this is Remy. I was wondering if you have some time available today."
Ry shy "I need a little bit of help with something. Of course, if you aren’t available, then I’ll manage. Do let me know if you have the time today."
Ry normal "Have a good day."

play sound "fx/answeringmachine.ogg"
$ renpy.pause (0.5)

menu:
    "Meet with Remy.":
        $ renpy.pause (0.5)
        play sound "fx/steps/clean2.wav"
        scene black with fade
        $ renpy.pause (3.0)
        play sound "fx/knocking1.ogg"
        $ renpy.pause (1.0)
        Ry "Come in, please."
        $ renpy.pause (0.5)
        play sound "fx/door/door_open.wav"
        $ renpy.pause (1.5)

        scene remyapt at Pan ((300, 80), (0,80), 5.0) with dissolveslow
        $ renpy.pause (3.3)
        m "I entered Remy's apartment. Remy was nowhere to be found upon first inspection, though emerged from the kitchen a moment later, holding a small spoon."
        
        if persistent.kol_tlh_chapter2B_skip:
            $ renpy.pause (1.75)
            c "(Wait, haven't I seen this before at some point?)"

            menu:
                s "(Do you want to skip forward?)"

                "Yes.":

                    $ renpy.notify("You successfully baked a cake with Remy.")
                    $ kol_tlh_chapter2B_mood = 4
                    $ kol_tlh_2Bplayed = True
                    stop sound fadeout (1.0)
                    stop music fadeout (1.0)

                    scene black with fade
                    $ renpy.pause (4.5)
                    jump tlh_Chapter3A

                "No.":
                    $ renpy.pause (1.0)


        $ renpy.pause (1.0)
        play music "mx/soul.ogg" fadein (0.5)
        show remy normal with dissolve

        Ry smile "Hello, [player_name]."
        c "Hello, Remy. I hope that I’m not interrupting something."
        Ry shy "I know that it’s not really a good idea to keep you away from your work, especially with what’s going on, but I just thought that it would be a good idea to work on this together."
        c "It’s okay. So, what exactly are you working on?"
        Ry "Well, considering what happened last time with our dinner, I wanted to make it up to you."
        Ry smile "So, I’m baking a cake."
        Ry shy "Or, at least I’m trying to. This is the first time I’m trying to bake something, so I was hoping you might maybe help with a few things."

        menu:
            "Of course.":
                $ renpy.pause (0.5)

                Ry normal "Thank you, [player_name]. I appreciate it. I’m a bit afraid of getting the recipe wrong due to how hard it is for me to get all the measurements right, but I’m sure that you’ll be able to help me out."
            
            "Is {i}this{/i} the reason as to why you called me?":
                $ kol_tlh_chapter2B_mood -= 1

                Ry "I’m sorry, [player_name]. I was just afraid that I’ll get the measurements wrong due to how hard it is for me to be precise."
                Ry look "The fact that I accidentally slipped last time should be enough evidence of that."
                $ renpy.pause (1.5)

            "I thought you made the previous dessert yourself.":
                $ renpy.pause (0.5)

                Ry "I just so happened to have some leftover dessert that I bought from the store last time. I don’t really have any baking skills."
                c "Then this will be a learning experience for the both of us."
                Ry normal "I guess so."

        $ renpy.pause (1.0)
        Ry normal "Please wait for a bit."

        show remy normal flip with dissolve
        hide remy with easeoutright
        $ renpy.pause (0.5)

        m "Remy returned to the kitchen for a brief moment and took something from a kitchen cabinet. He then opened a cooking book on the counters and casually turned page after page until he was satisfied."

        $ renpy.pause (0.5)
        scene remyapt at Pan ((300, 80), (300,80), 5.0) with ease
        $ renpy.pause (0.5)

        show remy normal with easeinright

        Ry "Alright. Here’s the recipe I had in mind. I was doing some minor preparations beforehand while I waited for you to come." #You know, like turning the oven on and getting the ingredients out
        Ry shy "This is why you saw me with a small spoon when you arrived."
        c "So, I’m guessing that I’ll be helping you actually mix the ingredients together?"
        Ry "Yes. It’s going to be a bit hard for me to get everything mixed well enough to actually make a proper cake, considering the size of my hands."
        c "Why don’t you just use a mixer, then?"
        Ry normal "I don’t own one. After all, this is my first time doing anything that would normally need a mixer."
        c "Makes sense to me."
        Ry shy "I do want to do some more baking one day, so I should probably get one. That is, if I don't mess up this cake."
        Ry normal "Now, let’s get to that recipe, shall we?"
        c "Right. What kind of cake are we making?"
        Ry "We’ll just be making a simple chocolate cake."
        Ry shy "I do hope that you like chocolate, though."

        menu:
            "\“Liking chocolate\” is an understatement.":
                $ renpy.pause (0.5)

                Ry "Oh, really? If I knew, I would have gotten some chocolate dessert for you last time."
                c "It’s alright, Remy. Treating me to an entire dinner was already more than enough."
                Ry "If you say so, [player_name]."

            "Chocolate is just… meh.": #Absolute criminal.
                $ renpy.pause (0.5)
                $ kol_tlh_chapter2B_mood -= 1

                Ry "Well, if you’d rather have something else, then I’d be happy to make some other cake."
                c "I don’t mind, Remy. You just bake what you like the most."
                Ry "Alright, then."

            "I guess you could say that.":
                $ renpy.pause (0.5)
                $ kol_tlh_chapter2B_mood += 1

                Ry smile "Then I’m glad for that."
                Ry shy "I was a bit nervous that you wouldn’t like chocolate at all. Maybe I should have just asked you what you wanted beforehand."
                c "I’m pretty sure that I’d like anything you make considering how good your cooking is."
                Ry "I suppose that's true."

        
        $ renpy.pause (0.5)
        Ry normal "According to the recipe, we'll have to combine all the dry components, then do the same with the wet ingredients. After that, we'll need to combine everything and bake the mixture."
        Ry "I already pre-heated the oven, though I haven’t had the time to mix all the ingredients yet. While I make the icing, do you think that you can mix the wet ingredients together?"
        c "Only if you tell me what needs to be mixed."
        Ry "You should mix two eggs, half a cup of vegetable oil and one cup of milk together. Remember to add a cup of boiling water and two teaspoons of vanilla essence as well. Be sure to mix everything fairly quickly." #For those that are wondering, yes, this is an actual cake recipe that will work. Uh, you just need to guess the temperature of the oven and for how long it needs to bake, though.
        c "For how long should I mix it?"
        Ry shy "The recipe doesn’t say. I’m guessing until it’s all relatively mixed together, but not too much."
        c "Alright, I should hopefully manage. After the mixing, I’d have to mix it with the dry ingredients, correct?"
        Ry normal "Yes. You'll need two cups of sugar, a teaspoon of salt, one and a half teaspoons of baking soda and just as much baking powder."
        c "And the flour?"
        Ry "One and three-quarters. Oh, and don't forget the cocoa powder. You'll need three-quarters of that as well."
        c "I thought that you needed help with the measurements."

        show remy shy with dissolve
        $ renpy.pause (1.5)
        show remy shy with dissolve
        stop music fadeout (8.0)

        Ry "I-I do, but specifically with the wet ingredients. It's hard for me to measure things like oil without making a mess everywhere, and don't even get me started on eggs." #Sure, Remy. Sure...
        Ry "Let me know if I need to repeat the recipe again."
        c "Will do."

        show remy shy flip with dissolve
        hide remy with easeoutright
        
        $ renpy.pause (2.0)
        play music "mx/submerged_forest_kol.ogg" fadein (2.5)
        $ renpy.pause (1.5)

        jump kol_tlh_makingcake #Welcome to Memory Games: AwSW Edition!


    "Work on plans.":
        $ renpy.pause (1.0)

        m "With Logan having arrived out of nowhere, I decided that it would be better if I didn’t spend the day with Remy and instead tried to develop a more thorough plan to accommodate both the oncoming comet and humanity’s demands." #Because you can *totally* do everything by yourself...
        $ renpy.pause (1.5)
        scene o2 at Pan((0, 250), (0, 250), 3.0) with dissolve
        $ renpy.pause (1.5)
        m "However, despite spending my entire day making such a plan, everything I came up with always had some crucial flaw that I overlooked. Regret started to fill me as I realised that I should have spent my day with Remy instead."

        scene black with fade
        $ persistent.kol_tlh_chapter2B_skip = True
        $ renpy.pause (4.5)
        jump tlh_Chapter3A

        #----------------------------------------------------------------------------
        #END OF CHAPTER 2
        #----------------------------------------------------------------------------


label tlh_Chapter2B_continued:

hide screen kol_extrainfo
stop music fadeout (2.0)
$ renpy.pause (2.5)

c "Done!"
$ renpy.pause (1.5)
show remy normal with easeinright
$ renpy.pause (1.5)
play music "mx/soul.ogg" fadein (1.0)

Ry smile "Alright, let me pour the batter in the cake tins and put them in the oven."

hide remy with dissolve
m "Remy poured the batter into the cake tins and put them in the oven while clumsily setting a timer. Afterwards, he looked at me with an expression of accomplishment."
show remy normal with dissolve
$ renpy.pause (1.0)

Ry smile "I don’t know about you [player_name], but I feel pretty proud of myself."

menu:
    "I hope that the cake doesn’t turn out horrible.":
        $ kol_tlh_chapter2B_mood -= 1
        $ renpy.pause (0.5)

        Ry look "Why would you say that? I mean, we did follow the recipe, so I can’t see why the cake would turn out bad."
        Ry normal "Though, I suppose the recipe could just produce a bad cake. I found that recipes don’t automatically result in good food, so you’ll just have to figure it out as you go."
        Ry "Perhaps the same applies for baking as well."

    "Me too, Remy.":
        c "Considering that it’s my first time baking, I must say that we didn’t do too bad of a job."
        Ry "Oh, for sure."
        Ry normal "I suppose we’ll find out how we did when the cake is finished."

    "Maybe we should open a bakery at some point.": #I wonder if this is referring to something. Perhaps another game with cake and dragons, mayhaps? :)
        $ kol_tlh_chapter2B_mood += 2
        $ renpy.pause (0.5)
        c "Considering how well we did, we might be able to open a bakery together once everything between humanity and dragonkind has calmed down a bit."
        c "Just imagine a bakery where both humans and dragons could eat some cake together. Wouldn’t that be nice?"
        Ry normal "Well, it’s definitely an interesting idea, to be sure. Such a business would probably also help to establish harmony between humans and dragons."
        Ry shy "Maybe I should send that idea to the council during our next meeting. After all, somebody might just actually follow through with it."
        Ry normal "But for now, let’s just focus on this cake first."

$ renpy.pause (1.5)
Ry "And now, we wait."
c "Yeah."
$ renpy.pause (1.5)
c "Remy, I’ve actually wanted to ask you something."
Ry smile "Feel free to ask me anything, [player_name]."
c "What do you think of Logan?"
Ry look "The new human, correct? I can’t say I know enough about him to form an opinion. All I hope is that he doesn’t turn out like Reza."
c "Look, I’ve known him for quite a long time at this point. I highly doubt that he’ll even be half as bad as Reza."
c "Thing is, it does look like he is torn. He has humanity as the focus of his goal, but given the comet's impending threat, I doubt he would want to ignore dragonkind as well."
c "Especially considering that without the generators offered in the trade, we won’t last for too long back home."
Ry "I suppose you’re right. Still, I just feel a bit uncertain of what he’s capable of."
c "I don’t think that he brought a weapon with him, if you were wondering."
Ry sad "You think?"

menu:
    "You’re worrying too much, Remy.":
        $ kol_tlh_chapter2B_mood -= 1

        Ry "But how can I not after all that had happened?"
        Ry shy "You’re the only human that I know of so far that didn’t want to go on a crime spree."
        Ry sad "What if he has other intentions that he’s trying to hide?"

    "Logan isn’t one who would want to do anything like what Reza did.": #(Flashbacks to TLD where he refused to let Martin into the human city.)
        $ kol_tlh_chapter2B_mood += 1

        c "Logan wouldn’t want to resort to such drastic measures. The only time where he’d even consider bringing a gun is if whatever he cared about is in danger."
        c "Since his goal was to either get me back or to bring a few generators, such a situation wouldn’t call for a weapon."
        c "What I’m trying to say is that I can almost guarantee you that he’s friendly."
        Ry look "I still don’t think that I trust him completely."

    "Yeah, maybe you’re right.":
        c "Maybe Logan has brought a gun considering that he didn’t know what had happened when he came searching for me."
        Ry "..."
        c "Still, I highly doubt that he’d actually use it unless he was in a life-threatening situation."
        Ry "You’re not really helping to put my doubts at ease, [player_name]."

c "Maybe you should try to find an opportunity to actually meet Logan."
Ry look "I’m not so sure…"

if kol_tlh_bryce_escort == False:
    c "If you’re really uncertain, then maybe I could accompany you. Besides, Logan is already constantly escorted by Bryce, so it’s not as if he can do anything sketchy."

else:
    c "If you’re really uncertain, then maybe I could accompany you. Besides, Logan is already constantly escorted by Sebastian, so it’s not as if he can do anything sketchy."

$ renpy.pause (2.0)
show remy shy with dissolve
$ renpy.pause (3.0)

Ry "Alright. I’ll try to meet up with Logan for your sake. If anything, maybe I can learn a few things that I could document for the council."

play sound "fx/oventimer_kol.wav"
$ renpy.pause (1.0)
show remy normal with dissolve
$ renpy.pause (0.5)

Ry "Please wait a moment."

show remy normal flip with dissolve
hide remy with easeoutright

m "Remy entered the kitchen once more. As he carefully removed the baking tins from the oven and set them on the kitchen counters, I excitedly awaited the outcome of our baking."
$ renpy.pause (1.0)
Ry shy "[player_name], could you perhaps come?"
c "Okay."
$ renpy.pause (2.0)

if kol_tlh_strikes == 0:
    show remy smile with dissolve
    $ kol_tlh_chapter2B_mood += 3
    $ renpy.pause (1.5)

    m "I looked at the cake that we had made. The cake rose perfectly and had a smooth exterior. Remy took a knife and sliced the cake, revealing a moist and spongy interior."
    $ renpy.pause (1.0)
    c "Talk about decadence. I don’t think I can say that I ever saw a cake that good before."
    Ry "Oh, for sure! Looks like the recipe I had worked wonders."
    Ry shy "Of course, I probably couldn’t have made it without you."
    c "Don't worry, Remy. I’m just happy to help you out."
    Ry smile "So, would you like some cake?"
    c "No, I just wanted to stare at its marvellous presence."
    Ry shy "..."
    c "I’m just pulling your leg, Remy. Here, let me help you cut it."
    Ry "At least let me put the icing on."
    c "Yeah, I guess that it’s kinda important. Of course, we'll have to wait some time for the cake to cool before we can put the icing on first."
    Ry "Oh? I thought you would just put the icing on the cake once it's out the oven."
    c "Only if you want your icing to melt and make a total mess."
    Ry "I see. In that case, we'll wait a bit for the cake to cool down."

    show black with fade
    $ renpy.pause (2.0)
    show remy normal with dissolve
    hide black with dissolve
    $ renpy.pause (1.0)

    m "After quite a long time of waiting for the cake to cool down and for the icing to be spread, the cake was finally ready for us to enjoy."
    $ renpy.pause (0.5)

    hide remy with dissolve
    $ renpy.pause (0.5)
    m "With the both of us smiling, we sliced the cake into several easy-to-serve slices. After we both took a slice for ourselves, we sat down in the living room and started to eat. Flavours of an ever rich chocolate swarmed my mouth, with the spongy cake comforting my tastebuds and the icing bringing everything together."
    show remy smile with dissolve
    play sound "fx/eating.wav" fadein (2.0)
    $ renpy.pause (0.5)

    Ry "I don’t think I ever had a cake that tasted this good before."
    c "Definitely. This is most likely on par with what some of the professional bakers used to make back home before the flare hit. And to think we could make something like this in a typical kitchen."
    Ry normal "Indeed."

    hide remy with dissolve
    $ renpy.pause (0.5)
    m "We continued to enjoy our slices of cake in absolute silence, taking pleasure in the harmonious combination of flavours. It was only a few moments before both of our plates were licked clean."
    $ renpy.pause (0.5)
    stop sound fadeout (1.0)

    show remy shy with dissolvemed
    $ renpy.pause (0.5)
    Ry "You know, I’m almost tempted to get another slice."
    c "Well, what’s stopping you?"
    Ry "A dinner with Adine. I don’t think that I would be able to stop if I ate another slice."

    menu:
        "Perhaps you could just bring the cake along for dessert.": #I don't think the restaurant would even allow that. Just another case of the MC being an absolute idiot.
            $ renpy.pause (0.5)
            Ry normal "Oh, that won’t be necessary. We’ll be having some dessert after our dinner."
            Ry shy "Yet, I don’t think that I’ll be able to finish the cake on my own before it starts to become stale, either."
            Ry normal "I’ll just have to save it for another time."

        "Consequences be damned!":
            $ renpy.pause (0.5)

            Ry look "I don’t think that stuffing my mouth with cake right now is going to be good for me, [player_name]. I’d rather not have a stomach ache of some sort when I have a large dinner later."
            Ry smile "Tomorrow’s breakfast, on the other hand…"
            c "Have at it, Remy. Go and treat yourself."
            Ry normal "Oh, I will."

        "Then mind if I steal another slice?":
            $ renpy.pause (0.5)

            Ry normal "An interesting way to handle the situation, but sure."
            $ renpy.pause (2.5)
            c "And what about another slice as a takeaway?" #Just take the entire damn cake already.
            Ry look "Are you sure that a third slice is healthy?"
            c "But it’s a really good cake…"
            Ry smile "Then maybe I should just give you the recipe so that you can make the cake whenever you want."
            c "With my baking skills, I highly doubt that I’d make a good cake."
            Ry normal "Today’s baking has proven otherwise. I’m sure you’ll be able to make a competent cake on your own."



elif kol_tlh_strikes <= 3:
    show remy normal with dissolve
    $ renpy.pause (1.5)

    m "I looked at the cake that we had made. The cake had a few imperfections here and there, but it still resembled an edible cake. Upon closer inspection, the cake seemed to be slightly off, yet I can’t put my finger on how."
    $ renpy.pause (1.0)

    c "Well, it’s a cake alright."
    Ry look "It definitely is. I hoped that it wouldn’t be so…"
    $ renpy.pause (2.0)

    Ry normal "Oh, but it doesn't matter what it looks like. The cake should still be more than edible. Not too bad for a first try if I say so myself."
    c "Agreed. So, shall we do the honours and cut the cake?"
    Ry "I suppose we should."
    
    hide remy with dissolve
    $ renpy.pause (0.5)
    m "I took the knife and sliced through the cake, revealing the supposed results of my and Remy’s work. The interior resembled the exterior, showing a far too crumbly middle. I served both me and Remy a slice, with the cake crumbling upon impact with the plate."
    $ renpy.pause (0.5)

    c "Wait. {w}We forgot to add the icing."
    show remy shy with dissolve
    Ry "..."
    $ renpy.pause (0.5)
    Ry "I suppose we could get it now if you want. Judging by the cake, I do think that the icing would be needed."
    c "Agreed."

    show remy shy flip with dissolve
    hide remy with easeoutright
    $ renpy.pause (1.5)
    show remy shy with easeinright

    m "Remy went to get the icing he had made. He spread it as evenly as he could across the cake, then spread a thin layer of icing on our slices."
    Ry normal "It’s not the best, but at least the icing is there."
    c "Wait, shouldn't the cake cool down first?"
    Ry shy "Well, it doesn’t really matter if we already cut a few slices, now does it?" #YES, REMY. DO YOU WANT MELTED ICING ALL OVER YOUR KITCHEN COUNTERS?
    c "I suppose..."

    hide remy with dissolve
    $ renpy.pause (0.5)
    m "Both me and Remy then went to the living room and took our seats. I slowly took a piece of the cake and ate it, anxious of what it might taste like."
    play sound "fx/eating.wav" fadein (1.5)
    $ renpy.pause (1.5)
    m "Although not entirely good, it definitely was better than I expected the cake to be, though I started to wonder whether it was due to the cake itself or the icing that covered its flaws."
    m "We ate our slices in silence, with only the occasional glance between us that interrupted our attempt to enjoy a mediocre dessert."
    $ renpy.pause (1.5)
    stop sound fadeout (1.0)

    show remy normal with dissolve
    $ renpy.pause (1.5)

    c "Well, that was a cake alright."
    Ry normal "Indeed. Honestly, I’m a bit thankful that it didn’t taste as bad as I thought it would. For a first try at baking, we definitely could have done worse."
    Ry look "That doesn’t mean that I couldn’t have done better."
    c "Hey, you did a really good job with the icing. Besides, it was my fault for not getting the cake right."
    Ry "…or mine for not helping you out, or not giving you the job of making the icing."
    c "Or perhaps it’s the recipe’s fault for not doing a good job at explaining things."

    show remy smile with dissolve
    m "Remy gave a small chuckle."
    Ry "Perhaps."

else:
    show remy look with dissolve
    $ kol_tlh_chapter2B_mood -=3
    $ renpy.pause (1.5)

    m "I took a look at the cake we had made, or what was supposed to be the cake. It didn’t seem like anything edible, much less like a classic dessert."
    c "..."
    Ry "..."
    c "That..." #...is a thing.
    $ renpy.pause (1.0)
    Ry "Let’s just cut it open and hope that it looks better on the inside."

    hide remy with dissolve
    $ renpy.pause (1.0)

    m "Remy proceeded to cut the cake that we had made. Not only was the cake extremely dry and crumbly on the inside, but certain parts were still raw."
    $ renpy.pause (1.0)
    c " I don’t think that the cake looks edible."

    show remy sad with dissolve
    Ry "What a sad attempt to try and do something nice. All I wanted to do was to try and bake something to make up for last time’s accident."
    Ry "And despite that, I {i}still{/i} couldn’t make up for it."
    c "Remy, you really shouldn’t be so hard on yourself. After all, this was your first time baking a cake. If anything, this could serve as a learning experience for you to try and make something better next time."
    Ry look "I suppose, though I still can’t help feeling that I messed up and ruined everything."
    Ry sad "{size=20}Again.{/size}{w=0.65}{nw}" #Gee, I wonder what this is referring to...
    c "What was that, Remy? I’m afraid that I missed what you said."
    $ renpy.pause (0.5)
    Ry "I-It was nothing."
    Ry look "I’ll throw the cake away later. For now, let’s just take it a bit easy."

    $ renpy.pause (0.5)
    hide remy with dissolve
    $ renpy.pause (0.5)

    m "Remy went to take a seat, with me following him soon after. Remy seemed to be a bit down, though he also seemed to try and hide his true thoughts. We sat for some time until Remy broke the silence."

$ renpy.pause (1.5)
show remy normal with dissolve
$ renpy.pause (0.5)

Ry "Well, in any case, it was great having to spend some time with you, [player_name]. With the way some things are right now, I wouldn’t be surprised if you got sent back through the portal soon."
c "Let us not hold our breath. I'd rather finish the mission I was sent here to complete while also focussing on deflecting the comet."
Ry look "An ever present reminder of these being the darkest days that we as a species have ever seen."
Ry shy "Let’s not think about such things while we’re supposed to have the day for ourselves."

menu:
    "…baking a cake was a setup, wasn’t it?": #What... logic is that even...?
        $ renpy.pause (0.5)
        $ kol_tlh_chapter2B_mood -= 1

        c "Wait, inviting me to help you with baking a cake was all a setup to try and spend the day with me, wasn’t it?"
        Ry "What on earth makes you think that?"
        c "I find it odd that you’d be able to cook a good meal the last time I had dinner with you if you weren’t able to make the correct measurements. You just wanted an excuse for me to come and \“help\” you."
        Ry look "You do realise that cooking isn’t the same as baking, right? Cooking doesn’t really need exact measurements, so you can use as much of a specific ingredient as you want. Baking requires precision."
        $ renpy.pause (0.5)
        c "...never mind."

    "What are we even going to do now?":
        $ renpy.pause (0.5)
        $ kol_tlh_chapter2B_mood += 1

        Ry "We could play a board game, but I don’t think that we’d be able to finish before I need to get going."
        c "What kind of board games do you play, Remy?"
        Ry normal "I always used to play a board game known as Bolliver’s Bane several years ago. I also liked to play Monarchs and Mercenaries. You could even be a human in that one." #Ey, reference to AwBH!
        c "I’m guessing that those humans aren’t really accurate to actual humans."
        Ry smile "Surprisingly, they are. Of course, traits like horns or wings are present, but the overall physique is nearly spot on."
        c "Interesting."
        Ry "I’d probably even say that they’re some of the most accurate renditions of humans that there are."
        c "Now you’ve got to show me how they look."
        Ry shy "I would if I remembered where the board games actually were. I think I’ve misplaced them somewhere."
        c "Oh well."

    "I suppose that it would be better.":
        c "Yeah. Maybe it would be a good idea to stop bringing the mood down every time we get reminded of what’s happening out there. I mean, this is our day to spend, so why bother trying to ruin that time?"
        Ry normal "Indeed. Few often seem to recognise how important it is to not influence positive times with negative thoughts, as they only sour the situation for everyone involved."

        $ renpy.pause (1.5)
        show remy look with dissolve #Yep, Remy just became self-aware for a second. Whoops.
        $ renpy.pause (1.5)

        c "Is something wrong, Remy?"
        Ry "No, I’m alright. I just had a random thought, that’s all."
        Ry shy "In any case, let’s talk about something else."
        c "Okay."

$ renpy.pause (0.5)
m "Remy drifted into thought for a bit after I finished speaking, but soon came back to reality. Somehow, he looked a bit more sombre than he did just a moment ago. I wasn’t sure whether he had been reminded of a stray thought or whether this had any deeper intentions."
$ renpy.pause (2.5)
Ry look "I think I should go now, as I might be a bit late for my scheduled dinner. I hate to sound rude to you of all people, but I think that you should probably leave as well."
c "Remy, there’s still a few hours left before it could be considered evening. There’s more than enough time."

stop music fadeout (1.5)
$ renpy.pause (2.3)

Ry sad "Is there really enough, [player_name]?" #Yes, there is enough time until the comet hits, Remy. Go and focus on your dinner with Adine first.

$ renpy.pause (1.5)
show remy sad flip with dissolve
$ renpy.pause (0.75)
hide remy with easeoutright
$ renpy.pause (0.5)

m "Remy went into his bedroom before I could say anything, leaving me completely alone. Thinking that I probably won’t see Remy any time soon, I decided to take my leave like Remy asked of me."

scene black with dissolve
$ renpy.pause (2.0)
nvl clear
window show

n "Yet, I couldn’t help but wonder why Remy suddenly decided to shoo me away. Nothing like this has ever happened with him, so Remy deciding to ask me to leave despite having several hours left before evening raised some red flags for me."
n "Considering Remy’s strange behaviour recently, something definitely seemed more suspicious than usual. Was Remy trying to hide something from me? And if so, just what was he hiding?"
n "As I walked back home, I started to make some theories, yet none of them seemed likely enough to give it more than a few seconds’ worth of thought. Was there something that I had been missing?"

window hide
nvl clear

$ persistent.kol_tlh_chapter2B_skip = True
$ kol_tlh_2Bplayed = True
$ renpy.pause (4.5)

jump tlh_Chapter3A

#----------------------------------------------------------------------------
#END OF CHAPTER 2
#----------------------------------------------------------------------------


#MAX MOOD VALUE OF 2B IS 8
#MIN MOOD VALUE IS -8
#GET 4 TO PASS (MAKE CAKE PERFECT + ONE KIND THING BASICALLY)