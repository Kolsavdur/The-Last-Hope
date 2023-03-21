label tlh_Chapter1A:

$ save_name = (_("TLH - Chapter 1A"))

$ renpy.pause (3.0)
scene o4 at Pan((0, 0), (0, 250), 5.0) with dissolveslow
$ renpy.pause (3.0)

m "I woke up fairly early in the morning, still tired from an uneasy night’s rest. I wanted to sleep for a bit longer, however I knew that there were several important matters to take care of today. Deciding not to delay any further, I prepared myself for all the possible tasks ahead of me for the day."

if persistent.kol_tlh_chapter1A_skip: #Because skips are nice
    $ renpy.pause (1.75)
    c "(Wait, haven't I seen this before at some point?)"

    menu:
        s "(Do you want to skip forward?)"

        "Yes.":
            stop sound fadeout (1.0)
            stop music fadeout (1.0)
            scene black with fade
            jump tlh_Chapter1B

        "No.":
            $ renpy.pause (1.0)

play sound "fx/door/doorbell.wav"
$ renpy.pause (3.0)

c "(Who could be here this early in the morning?)"
$ renpy.pause (0.5)
play sound "fx/door/door_open.wav"
$ renpy.pause (1.5)
m "I went to the door and unlocked it, finding a very urgent Sebastian."

play music "mx/chronos.ogg" fadein (1.0)
show sebastian drop b with easeinright
$ renpy.pause (0.5)

Sb "Hey. Sorry for waking you up this early in the morning, [player_name], but this is important."
c "Don’t worry. I was already awake."
Sb " I see."
Sb disapproval b "Well, to make a long story short, Bryce is currently in the hospital, and as you know, we’re already severely understaffed. Having the Chief of Police out of commission for a while could cause some problems for the police force, as you might assume."
c "Reza isn’t causing any more problems, though. Don’t you think that things would be a bit easier now with him gone?"
Sb drop b "That’s… where the real problem lies."
Sb disapproval b "You see, from what I’ve heard, Bryce wanted to sort Maverick out over the fact that he killed Reza."
Sb drop b "Maybe I shouldn’t have watched the fireworks. If I was still on guard, Reza would probably still be alive. Then we wouldn’t be in this mess." #Wait, why does Seb doubt himself and worry like this? Isn't it exactly the opposite of what he says to the MC?'

menu:
    "I don’t think that it would have been a good idea.":
        $ renpy.pause (0.5)
        c "If you were there with the portal, Reza could have shot you. By watching the fireworks, you might have saved yourself."
        $ renpy.pause (1.5)
        Sb "You're right. And to think that you suggested that idea…"
        Sb smile b "Thanks, [player_name]. You might have saved my life."
        c "Don’t worry about it. Let’s just focus on more important matters now."

    "Anything could have happened.":
        Sb "And anything could still happen. I don’t think that Bryce would be particularly happy about me abandoning my post, you know."
        Sb disapproval b "And yet, I wonder if I {i}could{/i} have even made a difference. I suppose that nothing can be done about it now; wondering will only waste time and energy."
        c "Yeah, we should probably get back to the matter at hand first, then."

    "Chances are, it wouldn’t have mattered if Reza was still alive.":
        Sb "How so?"
        c "I don’t think that Reza would have co-operated regardless of whether he was surrounded or not. I mean, do you really think that a few police officers would be able to stop Reza when he had already killed so many?"
        $ renpy.pause (1.0)
        Sb disapproval b "Maybe if he was surrounded, then yes."
        Sb drop b "Though, judging by the fact that Bryce—who is our most armoured individual in the force, mind you—is recovering in the hospital, I’d say that you have a point."
        c "Well, no use in dwelling on what could have been. Let’s get back to business."

Sb normal b "Right. Now as I’ve said, Bryce wanted to talk about Maverick’s actions. With him being in the hospital for the time being, I don’t think that would happen any time soon."
Sb disapproval b "To add to the dilemma, Maverick doesn’t want to listen to anybody right now, making Bryce and you the only options we have left, and since Bryce is…"
Sb drop b "I’m getting tired of repeating myself. You get the point." #Yes yes, we get the point of you being a broken record, Seb.
Sb disapproval b "Though, Maverick also seemed pretty upset after he went to see Bryce earlier today. I’m guessing that it must have been something else than the discussion about Reza, since discussing the entire ordeal would require all the police officers present. I’m sure you know by now how Maverick can be when he’s upset."
c "Yeah, I understand that."
c "Speaking of the hospital, any news on Remy?"
Sb normal b "His injuries weren’t as severe as Bryce. After a few hours, the doctors decided that his condition was stable enough to be discharged. Somehow."
Sb disapproval b "He’ll be having trouble walking for some time as he recovers due to him being shot near the joint in his leg. The doctors recommended that he stay at home, but from what I heard, he refused, saying that he’d, and I quote, \“feel better at work\”." #Hmmm, I wonder why Remy would feel better? I swear this is totally not foreshadowing or anything.
c "I see. I’ll try to see if Remy is okay when I get the chance. In the meantime, I’m assuming you want me to try and talk with Maverick?"
Sb drop b "Yeah, I hope that you can find out what’s bothering him so much. If the police force were to lose another member…"
$ renpy.pause (0.8)
Sb disapproval b "Look, I know that you and Maverick don’t get along very well, but there isn’t any harm in trying."
c " I’ll try my best. Where can I find him?"
Sb normal b "He should still be in the police office where I last saw him working on paperwork and whatnot."
c "Wait, isn’t he still on mandatory sick leave? Why would he be at the police station?"
Sb disapproval b "He isn’t officially back, though he decided that while Bryce is recovering, he should try and help out back at the station." #but y tho
c "How nice of him."
Sb normal b "He isn’t always like how he was with you and Reza, if you can believe it. Still, maybe it’s best if you just see him for yourself. Who knows, maybe you can succeed where everybody else failed."
c "Alright, I’ll go and check up on him. In the meantime, could you try and schedule an appointment with the hospital for later today? I’d like to visit Bryce."
Sb smile b "Sure."
c "Great. See you later."
Sb normal b "See you later as well."

show sebastian flip with dissolve
hide sebastian with easeoutright
$ renpy.pause (0.5)
play sound "fx/door/doorclose.ogg"
$ renpy.pause (1.0)

m "As Sebastian left my apartment, my mind started to arrange my schedule for today. I wondered how I’m supposed to try and find out what’s wrong with Maverick, as he hadn’t been co-operative during my entire mission in the dragon’s world."
m "However, things might change now that Reza is out of the picture. In the end, I decided that it would be best not to overthink too much and simply try my luck with Maverick."

stop music fadeout (1.5)
scene black with dissolve
play sound "fx/steps/clean.wav"
$ renpy.pause (3.0)
scene koloutisdepolice at Pan ((0, 360), (0, 0), 6.0) with dissolve
$ renpy.pause (1.0)

m "After a while of walking through the town, I eventually reached the police office. It was eerily quiet, almost invoking a sense of abandonment within me. Feeling a little disturbed from the silence, I entered."

$ renpy.pause (1.0)
scene office at Pan ((128, 250), (0, 250), 3.0) with dissolveslow

m "I looked around for a bit, seeing if I can find anybody that could help me. Instead, I stumbled upon Maverick himself looking through some records."
m "As I approached him, his head shot up and looked me dead in the eyes, sending a cold shiver throughout my body."

play music "mx/mysteryambience.ogg" fadein (2.0)
show maverick angry at center with dissolve

Mv "What do you want?"
c "I wanted to talk with you. It sounds like you haven’t been acting like your usual self recently."
Mv "You too, huh? Tell me, {i}ambassador{/i}. Why do you always poke your nose in things that it doesn’t belong in?"

menu:
    "It’s because it’s my job.":
        $ renpy.pause (1.0)
        Mv normal "So, you make a habit of doing things that you’re not supposed to do while disguising it as part of your job."
        c "That’s not what I–{w=0.5}{nw}"
        Mv angry "You’d be a horrible police officer, you know that? You’d probably want to abuse your power for your own personal gain, wouldn’t you?"
        Mv normal "I wouldn’t expect anything less from Reza’s former partner."

    "I just want to do the right thing and help everybody.":
        $ renpy.pause (0.5)
        Mv normal "And why is that? Sure, you might actually have wanted to stop Reza, but that doesn’t hide the fact that my own colleagues tossed me aside like rubble for the exciting and the new."
        Mv "Do you really think that what you’re doing has a positive effect on everybody with no consequences whatsoever?"
        c "The fact that we’re having this conversation disproves that theory."
        $ renpy.pause (0.75)
        Mv "So it seems."

    "Tell me, why do you always have to be so grumpy all the damn time?":
        Mv "So, we’re pointing fingers to each other now? How childish. And here I thought that the legendary human ambassador had some maturity."
        Mv "Ironic to think that the only humans I’ve met are a serial killer and a child pretending to be all grown up." #And how exactly is this ironic? Why didn't past me make a note of this during one of those past brainwaves? Eh, I'm sure it's fine.'
        Mv "I can’t believe that my colleagues threw me away for {i}you{/i}."

$ renpy.pause (1.0)
Mv normal "I suggest you take your leave."
Mv annoyed "Now."
c "Shooing me away won’t put an end to whatever is bothering you. If anything, it will only delay the mental crash you’ll experience."

show maverick rage with dissolve

Mv "AND WHY SHOULD I TELL YOU ANYTHING?!" with Shake ((0, 0, 0, 0), 3, dist=18)
Mv "If you’re so damn interested, why won’t you ask Bryce? I’m {i}sure{/i} he’ll tell you everything that you’re so eager to find out."
Mv angry "Oh, wait. He’s in the hospital. And it's all…{w=1.15}{nw}"

stop music fadeout (1.5)
$ renpy.pause (1.5)
m "Maverick slowly trailed off from his words as he delved into his thoughts. A few moments passed before he spoke again with an almost kind face. His change of facial expression felt jarring to such a degree that it unnerved me more than his outburst."
$ renpy.pause (1.5)
Mv normal "..." #And Mav realised that, yes, it's the MC's fault that Bryce is in the hospital, but if it wasn't for the MC, then Bryce would probably be dead a la Bryce bad ending.

play music "mx/detective.ogg" fadein (4.5)

Mv nice "I’ll say it again. I recommend you leave."
Mv "I have some documents that I still need to check. Perhaps we’ll have to speak again soon."
c "What documents are you looking through, anyway?"
Mv normal "That’s classified information." #Why does Mav hide documents like this from the MC? Hmmm...
c "I see. If there's nothing left for me to do, I’ll go now. There’s still quite a number of things that I need to do today."
Mv "Then I suggest that you go do whatever it is you still need to do."
Mv nice "Until we meet again, [player_name]."

hide maverick with dissolvemed

m "Maverick lifted the records he was busy with and continued to read through them. Deciding that there’s nothing left for me at the police station, I decided to take my leave."
$ renpy.pause (1.5)
scene koloutisdepolice at Pan ((0, 0), (0, 0), 4.0) with dissolve
$ renpy.pause (4.0)
scene town1 with dissolve

$ renpy.pause (1.5)
m "With some time for myself, I continued my journey through the town, hoping to soon finish another task for the day."
$ renpy.pause (1.5)

scene town3 with dissolve
$ renpy.pause (3.5)

scene koloutsidelibrary at Pan ((0, 180), (0, 90), 5.0) with dissolve
$ renpy.pause (1.0)
m "I walked until I eventually reached the library, where I was hoping to find Remy."
stop music fadeout (1.5)

$ renpy.pause (1.0)
scene library at Pan ((640, 228), (220,228), 5.5) with dissolveslow
m "However, upon entering, I found someone unexpected wandering aimlessly through its silent halls."
$ renpy.pause (3.0)

play music "mx/hollow_kol.ogg" fadein (1.5)
show adine normal b with dissolve

c "Adine? What are you doing here?"
Ad think b "[player_name]? I didn’t expect to see you here so early in the morning." #As if the MC never woke up aerly during a normal run of the game...
Ad giggle b "Are your ambassador duties at fault again?"

menu:
    "As they usually are.":
        $ renpy.pause (0.5)
        Ad disappoint b "I expected as much. With everything that’s been going on recently, I figured that you’d be especially busy these past few days."
        c "I guess you could say that."
        Ad "Still, it would be nice to have more time off, especially considering the part you play with the police."
        c "Yeah."

    "I just like to take a nice walk early in the morning, that’s all.":
        $ renpy.pause (0.5)
        Ad think b "I didn’t take you for a morning person. I guess you do learn something new every day."
        c "It’s just a routine I had developed before I came here. Gotta make the most out of the few hours in every day and all that."
        Ad "I suppose that makes sense."

    "Not necessarily. I just needed to do some other things first.":
        c "Well, almost. I had to make an early trip to the police office to sort some things out."
        Ad disappoint b "Oh, did something bad happen?"
        c "I don’t think that I’m allowed to openly talk about the police force’s stuff."
        Ad "I understand. I hope that everything is alright."

$ renpy.pause (0.5)
c "Now that I think about it, I’m sorry I didn’t visit you during your stunt practice. There were a bunch of other things happening and I completely forgot."

$ adinestatus = "neutral"

Ad giggle b "Don’t worry about it. You weren’t obligated to go or anything."
Ad disappoint b "I did hurt my wing, though. It’s all better now, but I decided to not enter the competition because of that."
Ad "I even got my entry confirmation letter before my practice, but I didn’t think that it would be a good idea to take part with an injured wing."
Ad think b "I had some very strange dreams before the day of the competition, actually. Maybe they influenced my decision to not fly?" #Insert "strange dreams" AwSW cliché here
Ad normal b "Oh well, there’s always next year, I hope." #Uh... yes, of course. Definitely. (Hopefully)
c "I’m sorry to hear that you cancelled your application. Having your dreams suddenly vanish like that must be pretty heartbreaking."
Ad think b "I actually got over it pretty quickly. I think that it had to do with having a sense of purpose; that is, to help the children at the orphanage and to be there for Remy."
Ad sad b "Hearing his struggles and how he had dealt with them alone for so long…"
$ renpy.pause (0.5)
Ad disappoint b "I can’t imagine all the pain he has gone through. Leaving him alone when he finally has a spark of hope would be an extremely cruel thing for me to do."

show adine think b with dissolve
$ renpy.pause (3.0)

Ad "We’re both here to visit Remy, aren’t we?"
c "I guess we are."
Ad "It only makes sense. The library only {i}just{/i} opened, and seeing you here this early only tells me that you want to check if Remy is doing okay."
c "Wait, you know what happened to Remy?"
Ad annoyed b "Of course I do! He’s my friend as much as he is yours, you know."
Ad disappoint b "After I got a call from Remy late at night saying that he was in the hospital, I could barely sleep. I told him that I wanted to see him immediately, but he let me know that the hospital didn’t take any visitors so late at night." #How was he able to contact Adine? Weird.
Ad annoyed b "And then he told me that he planned to go to work tomorrow, since he apparently made a quick recovery from Reza’s bullets. Couldn’t he see that he needed to rest and heal?"
c "Well, I guess we have the chance to tell him all of that now."
Ad disappoint b "Yeah. Let’s just go and find him."

scene kollibraryhall at Pan ((0, 250), (0, 250), 3.0) with dissolvemed
m "Me and Adine wandered through the library in our search for Remy, but we couldn’t find him."

show adine normal b with dissolve

c "Maybe he’s in his office?"
Ad think b "It’s a possibility, though I don’t think that we’re allowed back there."
c "Well, nobody is going to call us out for it right now. Since it’s so early, I don’t think that there would be that many people who would see us go into the staff-only areas."
Ad "I hope you’re right, [player_name]."

$ renpy.pause (1.5)
play sound "fx/knocking1.ogg"
$ renpy.pause (1.5)

m "Me and Adine arrived at Remy’s office with the help of my instructions. We knocked on the door, hoping to hear a response. Fortunately, it didn’t take long for a voice to be heard from the other side."
Ry normal "Please enter."

play sound "fx/door/door_open.wav"

$ renpy.pause (1.5)
scene office2 at Pan ((0, 228), (128,228), 3.0) with dissolveslow
$ renpy.pause (3.0)

m "We opened the door and entered Remy’s office. Strangely, it felt far more unwelcoming since the last time I was here."

show remy normal flip at left with dissolve
$ renpy.pause (0.5)
show adine think b at right with easeinright

Ry shy flip "Oh, good morning, Adine and [player_name]. I didn’t expect you two to visit me today."
Ry "Please forgive the mess here. I haven’t had the chance to tidy up yet." #Why isn't your office tidy, Remy? Aren't you supposed to keep your workspace clean or something?
Ad normal b "Hey, Remy. Glad to see that you’re alright. How are you holding up?"
Ry normal flip "I’m perfectly fine. I’ll admit that I’m struggling a little bit to walk every now and again, but the doctors patched me up quite thoroughly."
c "Shouldn’t you be taking it easy back at your home, then? Going to work doesn’t sound like the best idea to me."
Ry shy flip "I just wanted something to do, that’s all. Working here in my office helps to keep my mind off of things."  #You could also have done stuff at home though. I heared that "taking it easy" counts as doing a thing.
Ry "Besides, there’s always something that needs to be done here, especially if we’re going to collect all the information stored on the PDAs you and Reza brought from the trade."

if c4libraryavailable == False:
    Ry "Since you brought me your PDA the other day, I’ve been trying to find a way to present all the data stored on it for the council."
    Ry look flip "It’s tireless work trying to make all our current data formats match with those in the PDA, sure, but at least it can be accessed."
    Ry smile flip "Besides, seeing what humans know and what they have figured out is fascinating stuff."

else:
    Ry "I’ve been prepping some data formats to find a way to efficiently present all the data stored within the PDAs to the council."
    Ry look flip "Honestly, this would have been much harder if I didn’t have access to one of your PDAs, but luckily I don’t have to worry about that too much."
    Ry normal flip "Not that I really mind, that is. I’ve found that researching human knowledge is quite an efficient way of passing the time."
    Ry smile flip "Doing so for my job is an extra bonus."

Ad annoyed b "That still doesn’t excuse you being at work, and you know that. I don’t want you to overwork yourself when you need to get some rest."
Ad sad b "I don’t want to lose you too." #And the first Amelia reference had been made! How many more are there left to be made before the trauma dump of TLH? Find out next time... on Dragon Ball Z!

$ renpy.pause (0.5)
show remy sad flip with dissolve
$ renpy.pause (0.5)

m "A silence lingered in the room for some time as Remy thought about what Adine had said. Soon, Remy spoke up."
$ renpy.pause (1.0)
Ry "Alright, I’ll take it a bit easier from now on."
Ry look flip "I’ll still have to continue with what I’m busy with, but I won’t work as hard as I normally do."
Ad normal b "Thanks, Remy. I know you want to work hard for what you want to do, but sometimes you just need to wait for a better time."
Ad disappoint b "I learned that the hard way recently."
Ry "Is it due to you hurting your wing the other day? It must feel horrible not to fly at the competition when you’ve been practising for so long…"
Ad normal b "It's fine."
$ renpy.pause (1.5)
Ad think b "I guess that I should be going now. It’s almost time for my shift at the café, and I kind of lost track of the time while visiting you."
Ry normal flip "No worries, Adine. Do you think that you’ll be able to go out for a walk later today?"
Ad annoyed b "Remy! What did I just tell you about resting?"
$ renpy.pause (0.5)
Ry shy flip "I’m sorry. My mind is just focussed on other things right now, that’s all."
Ry "Maybe we could talk later over a nice cup of coffee instead?"
Ad normal b "Sure thing. I’ll call you later to let you know when I’m available."
Ad giggle b "And as for you, [player_name], we need to catch up as well. Maybe you can join us for some coffee?"
c "Sounds like a great idea. I can’t promise that I’ll have the time, but I’ll certainly try to make it up to you for not being there for your stunt practice."
Ad normal b "Only if you’re able to, [player_name]."
c "That’s fine by me."
Ad "Alright. See you two around!"
Ry normal flip "See you later, Adine."
c "Goodbye, Adine!"

show adine normal b flip with dissolve
hide adine with easeoutright
play sound "fx/door/doorclose.ogg"
$ renpy.pause (1.0)
show remy normal flip at center with ease
show remy normal with dissolve

m "Adine left Remy’s office and gently closed the door behind her. As her footsteps grew more and more silent, Remy turned his head my way and gave a slight smile. Afterwards, he slowly walked to his bed and sat down comfortably, making sure not to cause himself too much pain."
$ renpy.pause (1.5)
Ry "Please, [player_name]. Take a seat."

menu:
    "[[Sit on the floor.]":
        $ renpy.pause (0.5)
        m "I slowly sat down on the hard floor and tried to make myself comfortable. Remy looked at me with a confused expression in his eyes."
        Ry look "Are you sure you want to sit on the floor? It seems strange to me that you would choose to relax on the carpet when you could relax at my desk instead."
        c "I'll be fine."
        Ry "I see."

    "[[Sit next to Remy.]": #<3
        $ renpy.pause (1.0)
        "I took my seat next to Remy on his bed. As I sat down, I could see Remy starting to blush slightly."
        Ry shy "I thought you’d want to sit at my desk."
        c "Why would I want to sit on a boring office chair when I could sit next to you?"
        Ry "Fair enough, I suppose."

    "[[Sit at Remy’s desk.]":
        m "I made my way over to Remy’s desk and sat on his office chair. Despite being made with a dragon like Remy in mind, the office chair was surprisingly comfortable."
        m "For an office chair, at least."
        Ry "I hope that you aren’t too uncomfortable."
        c "Actually, no. Your chair is surprisingly comfy."
        Ry "Well, I did get a chair specifically suited for dragons like me, as the chair that was already in the office was more suited for runners."
        Ry "I guess that it doesn’t really matter for a human, does it?"

$ renpy.pause (0.8)
m "Remy wandered back into thought for a few moments, however seemed to come crashing back to reality once I spoke."
c "I’ve been noticing that you’ve been acting slightly unusual, Remy. Is there something wrong?" #"Yeah. The child I was taking care of at the orphanage got fucking murdered. That could count as something wrong, no?"
Ry "What makes you think that?"
c "You seemed to have a lot on your mind, judging by the way you talk and how you drift off into your mind."
c "You even seemed to not want to talk to Adine just now, as if you wanted to avoid some things that she had said."
$renpy.pause (1.3)
Ry sad "I don’t want to talk about it right now. Especially not at work."
$ renpy.pause (0.5)
Ry "Speaking of, I want to apologise for what happened during my outburst yesterday. I shouldn’t have shouted at you of all people."
Ry "I don’t even know what overcame me at that moment. Everything now just feels like a blur of some sorts."
c "It’s fine, Remy. Really."
Ry "Is it, though? Why would I react so harshly to someone who has shown nothing but kindness and sympathy to me?" #Idk, because you were having a mental breakdown and couldn't think straight?
c "You’re being too hard on yourself. We both know what happened was something that you weren’t ready to see. An outburst of emotions is only natural."
Ry look "..."
Ry "I suggest we change the topic."
c "Okay."
c "Do you know where Emera might be, by any chance?"
Ry shy "Emera? Why would you want to know where she is?"
c "There’s something crucial that I need to tell her, and the sooner I give her that information, the better it would be."
Ry look "I see. If I had to guess, she should usually be here somewhere in the library right now, as she’s one of the few members of the council that always arrives at work early." #Gotta keep her good appearance up, even among the council.
Ry normal "Or she could be in her office filling in some paperwork. I’d imagine that she wouldn’t leave her office once she learned that Reza has died."
c "Wait, you haven’t told Emera about what happened yesterday?"
Ry shy "I didn’t have the chance yet, and even if I did, I don’t think that she would have been too happy to hear my account." #You had the chance to tell your friend, but not your boss? Seems sketchy to me, Remy...
c "I see. Speaking of, what are the police going to do now?"
Ry "I don’t know. There aren’t any reports that have been released to the council yet, so I’m as clueless as you are."
Ry normal "If I had to guess, Reza’s body was most likely sent to a morgue while a report for the council is being written."
Ry "I don’t think that I’ll get to know any time soon, either. With Bryce recovering in the hospital, the police office is probably more concerned about the ever decreasing amount of officers on duty."
Ry look "And then there’s Maverick."
Ry normal "But I digress. You'll probably have to talk with Bryce or someone else if you want to know anything more than simple speculations."

menu:
    "Luckily, I already have.":
        $ renpy.pause (0.5)
        Ry shy "Wait, you have?"
        c "Yeah. I already talked with Sebastian and Maverick before I came here, and you’re right; they are definitely more concerned about the amount of staff than Reza’s death."
        c "At least, Sebastian is. Maverick, on the other hand…"
        Ry "I think I can make my own conclusions there."

    "I already made plans to talk with Bryce later today.":
        $ renpy.pause (0.5)
        Ry shy "Is that so? I thought that you’d have to schedule an appointment beforehand to visit somebody in the hospital."
        c "That part has already been sorted out."
        Ry "Today really is a busy day for you then, isn't it?"

    "In that case, I’ll let you know if I learn anything new.":
        Ry shy "There’s no need for that, [player_name]. I’ll just read the reports when they eventually come out."
        Ry look "After all, somebody has to organise said reports for Emera when they do get released."

play sound "fx/knocking1.ogg"
$ renpy.pause (1.5)

Ry normal "Please enter."
play sound "fx/door/door_open.wav"
$ renpy.pause (1.0)

show remy normal at left with ease
show remy normal flip at left with dissolve
show emera normal at right with easeinright

Em "Good morning, Remy." #Speak of the devil...
Em ques "…and [player_name], as it turns out. How strange it is to find you here, of all places."
c "Good morning, Minister."
Ry "Hello, Emera. Is there something that I can help you with?"
Em frown "Yes, there is. Normally I’d discuss the following in private, but since [player_name] is involved in the situation, I will speak with the both of you here."
Em "I’d like to know why you didn’t tell me that you were hospitalised yesterday. I’d also like to know why, despite that, you still came to work in apparent secrecy."
Ry shy flip "How did you find out?"
Em normal "Officer Maverick came in a while ago with a report of what happened yesterday night. According to the report, both you and the Chief of Police had been shot by Reza, with the Chief still being in the hospital as we speak."
Em "On top of that, Reza died due to bite wounds on his torso."
Em frown "Do you have any idea what the consequences are of this? Our trade agreement with the humans is now more fragile than ever." #Irrational of you to blame Remy for this when he had literally nothing to do with it, but you do you, I guess...
Em "If you had simply let me know what had happened, then the council could have already come up with a plan on how we are to deal with this situation." #It was *literally* yesterday night. Most of the council would have been asleep by then. Once again, you are irrational and, dare I say, delusional.
c "I’m afraid there are bigger concerns for dragonkind right now, Minister."

stop music fadeout (2.0)
$ renpy.pause (1.0)
m "Suddenly, both Emera and Remy’s attention flocked to me. I thought for a second on how I should try to explain what I had just said, soon letting my thoughts flow naturally."
Em "Then do enlighten me, [player_name]. What bigger concerns are there than the death of Reza and the trade agreement between humanity and dragonkind?"
c "Are you aware of a comet that will pass the earth?"

play music "mx/politics.ogg" fadein (1.0)

Em ques "If that’s what you’re concerned about, then I’m afraid there’s nothing to support your argument. Our top scientists have already concluded that the comet will pass by safely without any risk of endangering us."
c "Forgive my candour, Minister, but I’m afraid there’s far more to that. According to my PDA, that same comet is predicted to collide with the earth, causing a mass extinction event the likes of which your kind has never seen before."
c "If you aren’t doing anything about it, then I’m afraid the comet {i}will{/i} hit the earth."

show remy sad flip with dissolve

$ renpy.pause (1.5)
Em frown "And how are we supposed to stop such an event from occuring?" #Love the fact that you don't even try to fight back, prick.
c "We will need to get as many generators as possible from wherever we can, including the underground building near the portal, somehow combine them and use the energy generated to try and redirect the comet."
Em "I will have to inform the rest of the council so that we can start to formulate a plan."
Em normal "I will also need your PDA so that we could back up your claims. If what you say is true, then we will need every piece of evidence to confirm it."
c "Alright."
m "I gave Emera my PDA, as well as some basic instructions on how to operate it so that she can find the proof that the council will need to verify my claims."
$ renpy.pause (1.0)
Em "I see..."
Em ques "Well, I thank you for bringing this situation to my attention. I will make sure to carry this information over with the utmost haste." #...yet still sticks around for a bit for some questions.
Ry shy flip "May I ask [player_name] a question, Emera?"
Em normal "If that is what you want, then go ahead."
Ry "How did you even figure out that we’re all in danger? To suddenly come to such a revelation from seemingly out of nowhere seems a bit… strange."

menu:
    "Something in the sky didn’t seem right.":
        c "I found that there was a certain star-looking object in the night sky that seemed strange. I also noticed that it seemed to grow in size as the days went by."
        c "All I did was point my PDA towards it, which provided me with all the answers I shared right now."
        Ry "I didn’t think that the PDAs were that powerful. I guess I’ll have to put in the extra time to research them after all."
        Em "Indeed. It seems that your PDAs are far more valuable than we initially thought, especially considering the current circumstances we now find ourselves in. This simply provides more evidence as to why this trade agreement is crucial to us."

    "That’s something I need to keep to myself for now.":
        Ry look flip "Why do you need to keep it a secret? Surely there must–{w=0.85}{nw}"

        show emera frown with dissolvequick
        m "Emera shot Remy a silencing look, causing Remy to slowly trail off from his words." #Why the look, hm? What are you hiding, Minister?
        show emera normal with dissolvequick

        $ renpy.pause (0.5)
        Em ques "It is of no importance as to how [player_name] figured this information out. All that is currently relevant to us is that the information was discovered in the first place."

    "It’s a long story.":
        c "I don’t think that I have the time to explain the full story of how I figured this out, and chances are, you’ll probably find it a bit hard to believe."
        c "Besides, I wouldn’t want to keep Emera too busy by telling a long-winded story that won’t solve our predicament."
        Ry "I see."
        Em ques "Perhaps you do need to share your story at some point in the near future, [player_name]. It would help us to keep things on record should we ever need it."
        Em normal "But for now, you are correct. My time here is very limited."

$ renpy.pause (1.0)
Em normal "Now, if you’ll excuse me, I need to inform the council of this information immediately. I wish both of you a good day further."
Em "[player_name], expect a letter from me shortly detailing what we are planning to do with the comet."
c "My apologies for holding you up, but I have one last question to ask before you go."
c "What are you going to do with Reza’s body?"
Em frown "I have instructed the police force to return Reza’s body to humanity as a token of goodwill in hopes of salvaging our trade agreement."
Em ques "Since I am directly in charge of you and your former partner, I have the authority to order such a decision without consulting the council first."
Em normal "Are you satisfied with this answer?"
c "I am, Minister."
Em "Good. Farewell, [player_name]."

show emera normal flip with dissolve
hide emera with easeoutright
show remy at center with ease
show remy normal with dissolve

m "Emera rushed out of Remy’s office with my PDA in one of her claws. As she left, Remy looked at me with both intrigue and surprise."
$ renpy.pause (1.0)
Ry shy "I didn’t think that you could be so formal, [player_name]. And to think that you could stand on Emera’s level without it backfiring on you…"
c "All part of being an ambassador, Remy. I had to go through several courses on how to reason with even the most self-centred of people if I had any hope of negotiating with potentially selfish politicians."
Ry smile "Well, clearly those courses have paid off."

stop music fadeout (1.5)
Ry look "Though, now I’m starting to worry…"
$ renpy.pause (0.5)
play music "mx/fragments.ogg" fadein (1.0)

Ry sad "Is the world really at risk of a mass extinction event?"
c "I’m afraid so. If we don’t use the generators, then most forms of life will die."
Ry "..."
m "Remy seemed to be deep in thought for quite a while, slowly processing such a heavy truth. After some time had passed, he snapped back to reality."
Ry look "What can I do to help?"
c "Remy, remember that you’re still injured. It wouldn’t be a great idea to overexert yourself now."

show remy angry with dissolve
Ry "I’m not letting this world turn into a smouldering crater! If I can help in any way, then it is my duty to do so." with Shake ((0, 0, 0, 0), 2, dist=15)
$ renpy.pause (1.0)
Ry shy "I refuse letting everyone I care about die. {w}Not again. {w}Not ever." #Second Amelia reference!
c "That all depends on what the council decides will be the plan. For now, however, rest like me and Adine have suggested. You’re not going to help much if you can’t even walk properly."
$ renpy.pause (1.8)
Ry "Alright."
Ry look "Still, the added anxiety that our world is now in immense danger doesn’t really help with that plan to take it easy. Maybe I should have talked in private with Emera beforehand and avoided this conversation."

menu:
    "I refuse to let Emera bully you any further.":
        c "If you were alone, then Emera would just bully you further and blame you for everything, even if practically nothing was your fault."
        c "I haven’t mentioned this before, but on the day I was sent back to the portal when I returned with the case file you dropped, I heard how Emera belittled you for dropping the file on accident."
        c "For as long as I’m here, I refuse to let Emera make fun of you and make you the target of all her harsh words."
        Ry shy "You heard all of that?"
        c "I did, hence why I stopped Emera’s bullying today. Enough is enough."
        Ry "T-thank you, [player_name]. I don’t think I have the words to say how grateful I am for you standing at my side."
        c "All I’m doing is the right thing, Remy."
        Ry "And I’m happy about that."

    "It wouldn’t have changed much.":
        c "Since you work with the council at large, I’m sure that the information about the comet would eventually reach you, regardless if you like it or not."
        c "Besides, did you really want to have to deal with Emera this early in the morning?"
        Ry shy "I can see your points, [player_name]."
        Ry look "Sadly, it’s fairly often that I have to sit and suffer through Emera’s speeches so early in the morning."
        Ry shy "I’m almost sad to say that I’m used to it at this point, even if the emotional effects say otherwise."

    "And avoid your newly gained resolve?":
        c "If you weren’t here with me now, you wouldn’t have had that burst of resolve you just had."
        c "Perhaps that could allow you to help people like you did in your old job. I remember you wanting to help others again after your term with Emera was over, so how about doing so now with this opportunity?"
        Ry shy "I guess I could."

stop music fadeout (5.0)
$ renpy.pause (1.0)
Ry "..."
c "..."
Ry "I really think that I should get back to work now. I'm not free to take as long a break as I'd like. Besides, I wouldn’t want to upset Emera twice in a single day."
c "I understand."
Ry normal "I’ll let you know when I’m available, then we can grab some coffee with Adine and all catch up as a group."
c "Sounds good to me."
Ry "In that case, I won’t hold you any longer from your duties, as I imagine that you’re extra busy now."
Ry smile "Have a good day, [player_name]."
c "The same to you, Remy."

hide remy with dissolve
m "I left Remy’s office and let him continue his work despite both my and Adine’s advice. In the end, I concluded that Remy was to do whatever made him most comfortable, especially now that he knows the imminent danger his world now faces."
scene black with fade

$ renpy.pause (4.0)
scene town2 at Pan ((300, 400), (150, 400), 3.0) with dissolveslow

m "I took a stroll through the town, trying to gather my thoughts on what to do next when Sebastian suddenly appeared running to me from across the road."

play music "mx/infinite_kol.ogg"

show sebastian normal b with dissolvemed
Sb "Ah, there you are. I’ve been trying to find you, but you weren’t at the police office when I checked." #Deus Ex Machina FTW!
c "That’s because I had already been to the police office. I just finished having a nice long talk with Emera, so that’s probably why you couldn’t find me."
Sb drop b "Emera? Now why would you want to talk to her so much that you’d have to arrange an opportunity at this time?"
c "I don’t think you want to know, Sebastian, but that’s beside the point. Why were you in a hurry to come and find me?"
Sb "It’s about Reza. I’m guessing that since you spoke with Emera, you already know what task we’re stuck handling with right now."
c "Yeah."
Sb disapproval b "As you can imagine, returning Reza’s body to the humans could be the turning point of the trade agreement. If this goes wrong, then I’m afraid we won’t have those PDAs, and you won’t have those generators."
Sb drop b "And after hearing how life is like where you’re from, I can imagine that it won’t be really good for you."
c "That’s right. Without the generators from the trade, our city-state is doomed to collapse."
Sb disapproval b "Exactly."
Sb normal b "That’s why we’re going to need you as a temporary ambassador for dragonkind in this situation. Since you know the humans more than anybody else, having you explain what happened to Reza might soften the blow just a bit for the humans to consider continuing with the trade agreement."
c "And what would you have me do? If I were to go through the portal just to act as an ambassador, I’ll drain even more of the reserves of energy we have left. "
c "Besides, the portal on the human side is only operational for a select few moments per day to conserve as much energy as possible. It wouldn't be a good idea to send me through."
Sb smile b "That was never the intention."
Sb normal b "Our plan was to simply write a letter explaining what happened instead, as if we were to send someone from our side through, we might not exactly receive the warmest response."
Sb "If we were to send you through instead, then the possibility exists for the humans to decide not to send you back to us." #Foreshadowing to humanity's ultimatum, mayhaps?
Sb disapproval b "There are far too many risks, so a simple letter—even if it isn’t the best possible response to go at things—is our best bet."
c "And I’m guessing you want me to write the letter, right?"
Sb normal b "Yeah, that’s correct."
c "Figured."
Sb drop b "Best not to waste too much time, though. The faster this entire situation is over with, the better."
c "Alright."

scene black with fade
play sound "fx/steps/steps.ogg"
m "We went to the police station to arrange for Reza to be sent back to my world. We discussed a few things on our way there, such as how Reza was to be returned to the people back home, among other things."
$ renpy.pause (3.0)
stop sound fadeout (1.0)
scene koloutisdepolice at Pan ((0, 0), (0, 0), 4.0) with dissolve

show sebastian normal b with dissolve
Sb smile b "After you, [player_name]."
$ renpy.pause (2.0)
scene office at Pan ((128, 250), (0, 250), 3.0) with dissolveslow
$ renpy.pause (2.0)

m "Upon arriving back at the police station, I spotted Maverick looming over a desk filled with what I presumed to be notes on what we’re going to do."

show sebastian disapproval b with dissolve

$ renpy.pause (2.0)
Sb drop b "Since we don’t have Bryce with us right now, we’ll have to improvise a bit."
Sb normal b "Luckily, I already had a talk with the Chief just before I went to go and find you, so we have some advice on what we’re going to do."
Sb "He says that you’re going to need to provide an accurate report to explain what Reza did, but also keep it vague enough so that the humans don’t realise Maverick killed Reza out of his own free will."
$ renpy.pause (0.85)
Mv normal "Hmph."
$ renpy.pause (0.45)
Sb drop b "Sorry, Maverick."
Sb normal b "Do you think you’ll manage?"
c "Yeah. How long do I have?"
Sb "Until the guys from the morgue are here with Reza’s body, pretty much. My guess is about half of the day, maybe even more."
c "So be it."

scene black with fade
play sound "fx/scribbles.ogg"
$ renpy.pause (2.0)
m "I spent the next several hours trying to write a letter that fit the requirements given to me by Sebastian. After much revision and even more failed drafts, I eventually came up with a letter that gave a detailed yet accurate report without favouring one group over the other." #Yay, several hour paperwork! Lovely!
$ renpy.pause (4.5)
stop sound fadeout (1.0)

scene office at Pan ((0, 250), (0, 250), 3.0) with dissolveslow

show sebastian smile b at right
show maverick normal flip at Position(xpos = 0.15)
with dissolvemed

Sb "I’ll admit that this is some pretty solid stuff, [player_name]."
Sb normal b "Question is, do you think that the authorities back in your city would be willing to reason with us?"
c "They have no other choice. If they were to cancel the trade agreement, then we’ll lose everything." #lolnope, not anymore
c "Sure, Maverick’s actions are going to arouse many, {i}many{/i} suspicions, but with Reza’s murders, it would hopefully somewhat tip the scales in our favour."
c "Though, the authorities did care about Reza far more than they did for me, so I can’t say with certainty how this will all turn out."
Sb drop b "You could have said that a bit earlier during our brainstorming, you know."
c "It honestly wouldn’t have mattered that much. Regardless of what we came up with, this letter is our best shot."
Mv "Can you give that report to me? I need to make a copy for future reference."
c "Sure."
Mv "Thanks."

$ renpy.pause (0.5)
show maverick normal with dissolve
$ renpy.pause (0.5)
hide maverick with easeoutleft

m "I handed the letter to Maverick, who took it to a back room, presumably to make a copy. It wasn’t long before he returned with the original, albeit slightly crumpled document, as well as a copy." #...he did more than just make a copy, didn't he? Why else would it be crumpled?
$ renpy.pause (1.5)

show maverick normal flip at Position(xpos = 0.15) with easeinleft
Mv "Here."

play sound "fx/knocking1.ogg"
$ renpy.pause (1.0)

Mv "And what timing."

hide maverick with easeoutright

m "Maverick opened the door and talked with who I assumed to be a mortician. After a brief conversation and some signing of documents, Maverick looked back and informed us of what happened."

show sebastian disapproval b with dissolve
show sebastian at left with ease
show sebastian disapproval b flip with dissolve
$ renpy.pause (0.5)
show maverick normal at Position(xpos = 0.85) with easeinright

Mv "I’ve arranged for Reza’s body to be delivered at the portal in a coffin specifically designed for a human."
c "I didn’t think that everything would be prepared {i}that{/i} quickly."
Mv "Normally, it isn’t. However, due to Reza’s status, the documentation had to be filled immediately. As for the coffin, there were quite a lot of people rushing to make something that could fit Reza, as we’re not sure how quickly humans decompose."
c "(Could have put that in a lighter way.)" #It's Maverick. Do you really expect subtlety from him?
Mv "In short, everything has been prepared as fast as it possibly could. Now, let’s just get this over with already. Follow me."

scene black with fade
$ renpy.pause (0.5)
play sound "fx/steps/steps.ogg"
stop music fadeout (3.5)

m "The three of us walked to the portal at a semi-rushed pace, trying not to waste too much time. Sebastian did occasionally try to break the silence, but the urgency of this situation caused my mind to be focused on other things."

scene kolportalevening at Pan((200,200), (450,100), 6.0) with dissolveslow
$ renpy.pause (1.5)
stop sound fadeout (1.0)

m "As I looked around, I could see a wooden coffin near the portal’s commands. It appeared haphazardly constructed, but seemed to be accurate to how our coffins were built several decades ago."

show sebastian disapproval b at right
show maverick normal flip at Position(xpos = 0.15)
with dissolve

Mv "[player_name], type in the commands needed to start the portal. I’ll haul this coffin through."
Sb "At least let me stick the letter on the coffin before you start."
m "Sebastian moved over to the coffin and placed the letter on the lid. Afterwards, he placed a rock on the letter to secure it in place."

play sound "fx/paper2.ogg"
$ renpy.pause (0.5)
Sb "Done. [player_name]?"
c "On it."

hide maverick
hide sebastian
with dissolve

$ renpy.pause (0.5)
play sound "fx/telbuttons.ogg"
m "I typed in the commands necessary to send Reza back to our world. A wave of anxiety rushed over me as I considered the possibilities of what the authorities back home could do to both me and our trade agreement."
$ renpy.pause (0.35)

play sound "fx/telstart.ogg"
$ renpy.pause (0.5)
m "As the portal started up, all those anxieties within me dissipated, knowing that there was nothing I could do anymore. Several minutes passed before the portal was finished, leaving an eerie atmosphere of finality around me, Sebastian, and Maverick."
$ renpy.pause (3.5)

show sebastian normal b at right
show maverick normal flip at Position(xpos = 0.15)
with dissolveslow

$ renpy.pause (0.5)
Mv "And now the first wave has passed. Let us hope that the next won’t be hard on us all."
Sb drop b "Wait, what are you talking about, Maverick?"
Mv "..."
Mv "My apologies, but I have to go now. There’s something that still needs to be done."

hide maverick with dissolve
play sound "fx/takeoff.ogg"
$ renpy.pause (0.5)
m "Before either me or Sebastian could ask, Maverick took off and flew into the skies. Sebastian looked back at the portal once more and started walking off while slightly shaking his head."
$ renpy.pause (0.5)
Sb normal b "Best not to stay here any longer. I’d rather not be here for more than it’s necessary."
$ renpy.pause (0.75)

scene kolviewingspotevening with dissolve
$ renpy.pause (1.5)
show sebastian normal b with dissolve
$ renpy.pause (1.5)
m "We continued to walk in silence, taking in what we had just done. It didn't take long for that silence to be broken, however."
$ renpy.pause (0.5)
Sb smile b "Oh, and I completely forgot. Your scheduled meeting with Bryce starts in about twenty minutes. Down the roads until you’re at the centre, then make a sharp turn left. The hospital will be in a corridor on your right. Good luck." #Damn, Seb really do be just ditching you, huh?
hide sebastian with easeoutleft

m "Sebastian ran off, presumably back to the police station. I started walking back into town, annoyed that Sebastian only reminded me of my visit to Bryce after we had dealt with Reza."

scene black with fade
play sound "fx/steps/steps.ogg"
m "I hastily made my way through the streets, hoping to reach the hospital just in time for my scheduled visit."
$ renpy.pause (2.5)
stop sound

scene koloutsidehospitalevening at Pan((0, 125), (0, 360), 5.0) with dissolve
$ renpy.pause (2.5)
m "I eventually arrived at the hospital, albeit quite out of breath."
c "(And with a few minutes to spare. Nice.)"

m "I walked into the lobby and met the receptionist. He looked up towards me, smiled and directed me to the ward that Bryce was staying in."

$ renpy.pause (1.5)
scene kolhospitalcorridor with dissolve
$ renpy.pause (1.5)

m "As I entered the room, Bryce looked up to me with a mixture of both surprise and joy."

$ renpy.pause (0.5)
scene kolhospitalbed at Pan((0, 233), (0, 233), 0.0) with dissolve
$ renpy.pause (2.5)
play music "mx/enigma_kol.ogg" fadein (2.0)
show bryce smirk with dissolve
$ renpy.pause (1.0)

Br "Didn’t expect you here of all people."
c "Hey Bryce. How are you feeling so far?"
Br normal "Aside from the obvious pain from the bullets, I’d have to say pretty good."
Br smirk "Hell, I might even leave tomorrow depending on what the doc says about my condition."
c "That’s honestly great to hear. As you might have guessed, things are a bit chaotic back in the force."
Br stern "Yeah, I’ve heard as much. Heard you also were planning to send Reza through the portal. How’d that go?"
c "I think I did a good enough job with the letter. All that matters now is how the authorities back home will react."
Br "Don’t worry about it. Worst case scenario is that you’d be stuck here."
Br flirty "Not that I’d mind." #Because he doesn't know that you're in a relationship yet.

menu:
    "I guessed as much.":
        Br "See, maybe living here with us won’t be so bad."
        Br normal "It would certainly be an improvement from your city, at least."
        c "That is true, though I won’t be able to shake the feeling off that I failed everyone back home."
        Br "I guess that’s also a possibility, yeah."

    "I don’t think that I’d fit into society quite well.":
        c "Living here would be a huge undertaking, since almost everything here is suited to dragons in some way or another."
        c " I’d also have to get new clothes at some point, which could be pretty hard, as you might imagine."
        Br stern "A fair point."

    "I’m already taken.":
        $ renpy.pause (1.0)
        c "I’m already in a relationship, Bryce. I’m not willing to go that far."
        Br brow "Is that so? That’s news to me."
        Br laugh "Who’s the lucky person?"
        c "Remy."
        Br brow "Really? The klutzy librarian of all people?"
        c "Do you really need to talk about him like that, Bryce?"
        Br stern "Yeah, maybe shouldn’t have joked about the guy after what happened. Sorry."
        Br normal "Still friends, right?"
        c "Of course."

        $ brycestatus = "neutral"

        Br "Glad to hear that, then."

$ renpy.pause (1.0)
c "Now that I think about it, I never apologised about missing that barbeque you were having the other day."
Br laugh "Don’t worry about it, [player_name]. You only missed out on some top-notch bantering and some excellent meat, that’s all."
c "Seemed like a fun time. I wished I could have made it."
Br smirk "Well, there’s always next time. Care to make a reservation?"
c "I’ll call in at a later date. Wouldn’t want to pay a cancellation fee should things go wrong, now would I?"
Br laugh "Fair enough."

show bryce normal with dissolve
$ renpy.pause (1.5)

c "I also wanted to ask you about something. Earlier today, Maverick was in a pretty bad mood."
show bryce stern with dissolve
c "He seemed to calm down a bit when I talked to him, but I can’t help to shake the feeling off that he seems to be planning something again."
Br "Look, Maverick went to talk to me earlier today about working at the police force while I’m staying here. I didn’t trust him then due to him being responsible for Reza’s death." #THEN WHY DO YOU LET HIM TO WORK AT THE OFFICE WHILE YOU'RE IN THE HOSPITAL, BRYCE? THINK, DAMMIT!
Br "Sure, he was a murderer, but he was still necessary for the trade. That’s why I wanted to arrest Reza, not kill him."
Br "My guess is that Maverick didn’t like the way I treated him after all that, which is probably why he seemed to be in a bad mood."
Br sad "And then there’s the potential of me having to discharge Maverick."
$ renpy.pause (1.5)
Br stern "I’ll have to sort that out when I’m back in my office. Now, we’ll have to focus on the humans. I’m guessing that they won’t be happy with Reza being dead, so they’ll probably send a reply to us either later tonight or tomorrow morning."
c "So, what can I do to help?"
Br "Not much, I’m afraid. The police force will wait for a potential response and then hand that over to Emera. Afterwards, she’ll probably determine what goes on from there."
Br normal "Just take it easy until something happens."
c "Right."
$ renpy.pause (1.5)
m "I looked at the time and realised that I had only had a few minutes left before the visiting hours were over."
$ renpy.pause (0.5)
c "Damn it, looks like I’ll have to go now. Sorry for only staying with you for such a short time, Bryce." #What even was that? Like, 5 minutes or something? Poor Bryce.
Br sad "Aww, I just started to have a great time chatting with you, and now you’re leaving?"
c "Sadly. Visiting hours and all that."
Br normal "Well, let’s hope the next time you’ll see me again, I’m back in my chair."
Br smirk "Thanks for the visit, [player_name]. I really appreciate it."
c "It’s my pleasure."

scene black with fade
$ renpy.pause (1.5)
stop music fadeout (5.0)

m "I left the hospital and started walking back to my apartment. As the sun started to set on the horizon, I wondered what would be in store for me for the next couple of days. Emera will almost certainly keep me busy as we find a plan on how to redirect the comet, as well as keep me responsible during the negotiations with humanity."

scene o2 at Pan((0, 0), (0, 125), 3.5) with dissolvemed

m "As I entered my apartment, weary from today’s work, I saw that I had a new message on my answering machine."
c "(Let’s see here…)"

play sound "fx/answeringmachine.ogg"
$ renpy.pause (0.5)

Ry normal "Hello, this is Remy. I have some news about our little get-together with Adine."
Ry smile "We’ll be having some coffee at the café tomorrow afternoon, so do let me know if you’re available."
Ry normal "Have a good evening."

play sound "fx/answeringmachine.ogg"
$ renpy.pause (0.5)

c "(Let’s just hope that I will, in fact, have some free time tomorrow.)"
$ renpy.pause (0.5)
m "I decided that I should spend the rest of my evening taking it easy, especially considering I might have a very busy day tomorrow."

$ persistent.kol_tlh_chapter1A_skip = True

scene black with fade
$ renpy.pause (4.5)

# ===========================================
# END OF CHAPTER 1A
# ===========================================

label tlh_Chapter1B: # Need +2 to pass

$ save_name = (_("TLH - Chapter 1B"))

$ renpy.pause (2.5)
scene o4 at Pan((0, 0), (0, 250), 5.0) with dissolveslow
$ renpy.pause (3.0)

m "I awoke late in the morning, feeling exceptionally well rested. As I got out of bed, I thought about Remy's invitation, as well as all the other possibilities for what could happen today."

menu:
    "Take it easy.":
        $ renpy.pause (0.5)

        m "In the end, I decided that it might be worth it to stay at my apartment, just in case I received important news from either Emera, Sebastian, or both."

        scene black with fade
        $ persistent.kol_tlh_chapter1B_skip = True
        $ renpy.pause (2.0)
        jump tlh_Chapter2A

        #----------------------------------------------------------------------------
        #END OF CHAPTER 1
        #----------------------------------------------------------------------------

    "Meet with Remy.":
        $ renpy.pause (0.5)

        m "I began to prepare for today's events after deciding not to reject Remy's offer. I walked out of my apartment and towards the café after finishing my meal."

        play sound "fx/steps/clean2.wav"

        scene black with fade
        $ renpy.pause (2.0)
        scene cafe with dissolvemed

        if persistent.kol_tlh_chapter1B_skip:
            $ renpy.pause (1.75)
            c "(Wait, haven't I seen this before at some point?)"

            menu:
                s "(Do you want to skip forward?)"

                "Yes.":

                    $ renpy.notify("This outing with Remy and Adine had been successful.")
                    $ kol_tlh_chapter1B_mood = 2

                    stop sound fadeout (1.0)
                    stop music fadeout (1.0)

                    scene black with fade
                    $ renpy.pause (1.0)
                    $ kol_tlh_chapter1B_done = True
                    jump tlh_Chapter2A

                "No.":
                    $ renpy.pause (1.0)

        m "It wasn’t long, however, until I arrived at my destination. I entered the café and saw Remy already waiting for me in a corner. As I approached him, his face lit up."

        play music "mx/mountain_side_kol.ogg" fadein (2.0)
        show remy normal with dissolve
        Ry smile "Oh, hello [player_name]! I didn’t expect you here so soon!"

        menu:
            "The same could be said for you.":
                $ renpy.pause (0.5)
                Ry normal "I didn’t have anything to do really, as I already did quite a lot of work yesterday."
                Ry look "That, and Emera telling me to take today off, as you might guess."
                c "For good reason."
                Ry normal "For good reason indeed."

            "Better be safe than sorry.":
                $ renpy.pause (0.5)
                Ry normal "I suppose so. If you had arrived any later, then you might have had to sit through the town's rush hour."

            "I’m just lucky that I had the time to be here.":
                $ kol_tlh_chapter1B_mood += 1
                $ renpy.pause (0.5)
                Ry normal "Oh, for sure. With everything that’s happening and what’s going to happen, I can imagine just how busy you’ll become."
                Ry look "I almost want to say busier than before Reza’s death."
                c "Yeah, but despite that, I’ll try to make time for you."
                Ry normal "And I appreciate that, [player_name]."

        $ renpy.pause (0.5)
        c "Wait, where’s Adine? Shouldn’t she already be here working at the café?"
        Ry shy "Her shift is later today, so she is also off. If I remember, she went to the orphanage real quick before coming here."
        c "Let me guess, she wanted to drop Amely off?"
        Ry "How did you know?" #I am going to milk this line to death throughout the mod. Just saying...
        c "Just a hunch, that's all."
        Ry "I remember the last time I was at the orphanage, she always clung to Adine like a magnet of sorts."
        Ry "Though she did take some sort of interest in me. Maybe Adine influenced her in some way."
        Ry look "She also tried to play with Vara once, but I'm guessing she didn't like Vara's unwillingness to talk that much."
        Ry shy "I do wonder how Amely is doing right now."
        c "Maybe we could visit the orphanage after this? I’m sure Adine would appreciate it."
        Ry sad "I’d love to, [player_name], but I don’t think I can. I just think I need some time alone before going there again."
        m "Adine entered the café and came to our table just as Remy was finishing up speaking."

        show remy normal at Position(xpos = 0.85) with ease
        show adine normal b flip at left with easeinleft

        Ad giggle b flip "Hey, you two! Sorry for taking so long."
        Ry "It’s no problem, Adine."

        menu:
            "How was the orphanage?":
                $ renpy.pause (0.5)
                Ad think b flip "How did you know I was making a trip to the orphanage?"
                c "Remy told me."
                Ry shy "I just confirmed [player_name]’s suspicions, that’s all."
                Ad "Sure, Remy."
                Ad normal b flip "As for my trip, it was just your standard stuff. Nothing too interesting if that’s what you’re wondering about."

            "Could’ve arrived sooner.":
                $ kol_tlh_chapter1B_mood -= 1
                $ renpy.pause (0.5)
                Ad annoyed b flip "I’m actually on time, you know. It’s not my fault that you were here early."
                show remy shy with dissolvequick

            "Hey, Adine.":
                $ renpy.pause (0.5)
                Ad normal b flip "Glad you could make it, [player_name]. I was wondering if you’d be able to come thanks to your schedule."
                c "Looks like everything was in my favour today."
                Ad "It seems so."

        $ renpy.pause (1.0)
        show remy normal with dissolve
        c "So, should I call somebody to take our orders?"
        Ad giggle b flip "I just got here, [player_name]. I still need to decide what to eat."
        Ry normal "I know what I want, so it looks like we all have to wait for you."
        Ad annoyed b flip "Alright, I’ll try to think quickly."
        m "Adine looked at the menu for several minutes as she decided what to order while Remy and I patiently waited."
        $ renpy.pause (0.5)
        Ad think b flip "I think I decided on what I should get."
        c "Alright. If there’s no objections, then I’ll call for a waiter."
        Ry "None."
        Ad "Nothing."
        m "I called for a waiter to take our orders. Soon, a somewhat small dragon arrived carrying an even smaller notebook." #No, this isn't Lorem, even if it would be super cool.
        Ry "I’ll have some green tea, please. Extra strong." #:)
        Ry "Oh, and a chocolate muffin as well."
        Ad "I’ll have some coffee, but not too strong. I’ll have today’s special for something to eat."
        $ renpy.pause (0.25)

        menu:
            c "(What should I get to drink?)"

            "Soda":
                $ kol_tlh_chapter1B_drink = "Soda"
            "Coffee":
                $ kol_tlh_chapter1B_drink = "Coffee"
            "Tea":
                $ kol_tlh_chapter1B_drink = "Tea"
            "Water":
                $ kol_tlh_chapter1B_drink = "Water"

        $ renpy.pause (0.25)
        menu:
            c "(And what should I order to eat?)"

            "Doughnuts":
                $ kol_tlh_chapter1B_food = "Doughnuts"
            "Bagel":
                $ kol_tlh_chapter1B_food = "Bagel"
            "Salad":
                $ kol_tlh_chapter1B_food = "Salad"
            "Cake":
                $ kol_tlh_chapter1B_food = "Cake"
            "Sandwich":
                $ kol_tlh_chapter1B_food = "Sandwich"

        m "I gave the waiter my order, which he quickly scribbled down in his notebook. He speedily went to the kitchen and placed the orders."
        c "What’s the special, if I may ask?"

        if food == "fish":
            c "Is it the same special that I had the other day?"
            Ad giggle b flip "Oh no. Today’s special would be a bowl of mouflon ramen."
        else:
            Ad normal b flip "Today’s special would be a bowl of mouflon ramen."

        Ad think b flip "Sure, it’s a bit on the pricey side, but I’m willing to spend a little bit extra for today."
        Ad giggle b flip "I do consider this a special occasion, after all."
        Ry shy "It’s just another time when we could talk, Adine. There’s nothing too special about it."
        Ad normal b flip "That would be true if [player_name] wasn’t here with us."
        Ad think b flip "Besides, after what I’ve been hearing from you, I don’t think that I’m going to get another chance to talk with [player_name] anyway."
        Ry "I see."
        c "Well, I could just rearrange everybody’s schedules so that I could magically create more free time."
        Ad giggle b flip "That would be pretty nice if it were only that easy."
        c "Yeah."
        $ renpy.pause (1.0)
        c "So, how are you feeling, Remy?"
        Ry normal "I'm doing well. I'm still having a little bit of trouble walking around, but it's far easier than yesterday. You could even say that I'm rapidly getting better."
        Ry smile "I should be perfectly fine by tomorrow."
        Ad think b flip "You’re not lying, are you Remy?"
        Ad giggle b flip "I swear, it would look pretty weird if I had to carry you if you accidentally slipped or something."
        Ry shy "No, I’m serious. This time I’ll be in a better state to walk around."
        c "Now that I think about it, how did you even get here all by yourself, Remy? The café is pretty far from your home, you know."
        Ry "With much effort, [player_name]."
        Ad annoyed b flip "What did I tell you, Remy?"
        Ry "B-but I’m feeling better!"

        menu:
            "Listen to Adine, Remy.":
                $ kol_tlh_chapter1B_mood += 1
                $ renpy.pause (0.5)
                c "Maybe you need to listen to Adine, Remy. Sure, we both told you to take it easy yesterday, but if you’re only going to do so for a single day, then what’s the point?"
                Ry "I know. I just don’t want to bother you all by having you two constantly looking after me. Besides, it’s not as if I {i}can’t{/i} walk."

            "The more you say that, the less I believe you.":
                $ kol_tlh_chapter1B_mood -= 1
                $ renpy.pause (0.5)

                Ry look "..."
                Ad think b flip "..."
                c "..."
                $ renpy.pause (0.75)
                Ad "I believe you Remy, though feeling better doesn’t mean that you’re feeling good."
                Ry "I know."

            "But you still shouldn’t have gone alone.":
                c "Perhaps you needed to wait for Adine to come and get you first instead. After all, what if you injured yourself even more on the way here?"
                Ry look "I’m not that vulnerable, [player_name]. I can handle myself."
                c "I’m just afraid of what might happen, that’s all."
                Ry "I understand that, but still."

        $ renpy.pause (0.45)
        m "Adine wanted to say something, but was interrupted by the waiter bringing our orders. It didn't take long for our entire table to be filled with plates and cups."
        
        $ renpy.pause (0.5)
        play sound "fx/dishes.wav"
        show remy normal
        show adine normal b flip
        with dissolve

        m "I thanked the waiter, who simply nodded in return and went back to the kitchen."
        $ renpy.pause (0.4)

        if kol_tlh_chapter1B_food == "Doughnuts":
            m "I started to eat the doughnuts I had ordered. Surprisingly, they were far more delicious than I had expected, being extremely fresh and airy while not being too sweet. It wasn’t long before my plate was picked clean."
        
        elif kol_tlh_chapter1B_food == "Bagel":
            m "I started to eat the bagel I had ordered. Surprisingly, it was far more delicious than I had expected, being extremely crisp yet soft. It wasn’t long before my plate was picked clean."

        elif kol_tlh_chapter1B_food == "Cake":
            m "I started to eat the cake I had ordered. Surprisingly, it was far more delicious than I had expected, being fluffy and moist while providing a nice, sweet taste to bring everything together. It wasn’t long before my plate was picked clean."

        elif kol_tlh_chapter1B_food == "Salad":
            m "I started to eat the salad I had ordered. Unsurprisingly, it was just as I expected it to be: an average salad with a small amount of dressing."
            c "(What was I even expecting?)"
            m "Despite that, I took a bite, being surprised at how refreshing it was. It wasn't long before I ate everything."

        else:
            m "I started to eat the sandwich I had ordered. Surprisingly, it was far more delicious than I had expected, as all the ingredients blended perfectly together with the soft, salty bread. It wasn’t long before my plate was picked clean."

        Ad giggle b flip "I didn’t know you were {i}that{/i} hungry, [player_name]. Maybe I should have arranged our meeting earlier."
        c "The food was just delicious, that’s all."
        Ry shy "Well, you did make a great choice, so I can’t blame you there."
        Ad "If you think that was good, then maybe you should try today’s special."

        menu:
            "Alright, sure.":
                $ renpy.pause (0.5)
                c "You know, I’m feeling a bit adventurous. Let’s try your ramen."
                Ad normal b flip "Here you go."
                $ renpy.pause (0.5)
                m "Adine passed her bowl to me, eager to see what my reaction would be. As I tasted her food, my face lit up as the swirl of flavours danced around in my mouth. A rich yet tender meat suited the savoury taste of the ramen noodles perfectly."
                $ renpy.pause (0.3)
                m "All in all, perfection."
                Ad giggle b flip "I’m guessing that you liked it, right [player_name]?"
                c "\“Liking it\” would be an understatement. This honestly might be the best ramen I have ever eaten in my life."
                Ad "That good, huh? I honestly can’t blame you, as this is one of our most popular items every time it shows up on the menu."
            
            "I think I’ll pass.":
                $ renpy.pause (0.5)
                if food == "fish":
                    c "I think I’ll stick with what I ordered, thank you very much. I can’t say that I trust the special all too much, especially since the last time I tried it."
                else:
                    c "I think I’ll stick with what I ordered, thank you very much. I can’t say that I trust the special all too much, sorry."
                 
                Ad disappoint b flip "Oh, that’s a shame."
                Ad normal b flip "I’m just saying this now: you’re missing out."

        Ry normal "I can’t say that I’ve ever tried the mouflon ramen before, so I’m oblivious to the taste."
        Ad giggle b flip "Maybe you want a taste as well, Remy?"
        Ry shy "Not today, Adine. I’m enjoying my muffin very much."
        Ad normal b flip "So be it."
        play sound "fx/eating.wav"
        $ renpy.pause (1.25)
        m "We kept eating and drinking, with Adine occasionally cracking a joke to keep the conversation going. Eventually, all three of us were done."
        $ renpy.pause (1.5)
        stop sound fadeout (1.0)
        Ry smile "Well, that was a pretty great idea, Adine. Thanks for inviting all of us."
        c "I agree. It was pretty great to be here and properly hang out with you again."
        Ad normal b flip "No worries. I’m just glad that I could spend some time with my friends for once."
        Ad disappoint b flip "Besides, I’m not sure when I can get the chance to do so again."
        Ry normal "Who knows? Maybe an opportunity will arise at some point where we could meet each other again."
        c "Yeah, anything is possible."
        Ad normal b flip "Maybe I’m just being too pessimistic. With everything that’s happened recently, it’s a bit hard to think about the bright side of things."
        Ad think b flip "Let’s hope that we would, in fact, have another opportunity to chat over some coffee again."
        Ry "Agreed."
        $ renpy.pause (1.5)
        Ad normal b flip "...and my shift is coming up soon. Guess I have to start preparing for that."
        Ry shy "Already? I didn’t think that the time would fly so quickly."
        c "Strange how the time always seems to pass faster when you’re having fun, right?"
        Ry normal "For sure."
        Ad "Well, I’ll be heading into the kitchens now. I’ll see you later, Remy."
        Ad giggle b flip "And don’t think that you’re off the hook, [player_name]. The first opportunity I get…"
        c "Yeah, I know. See you, Adine."

        show adine normal b with dissolve
        hide adine with easeoutleft

        m "Adine went into the kitchens of the café, leaving both me and Remy alone at the tables."

        show remy normal at center with ease
        $ renpy.pause (1.5)
        Ry shy "Oh dear..."
        c "What’s wrong?"
        Ry "Adine accidentally forgot to pay for her meal. I’ll just have to pay for her and remind her about it later." #I mean, she works here, no? Couldn't the restaurant just, idk, deduct it from her wage or something?

        menu:
            "I could pay for all of us.":
                $ kol_tlh_chapter1B_mood += 1
                    
                c "You don’t need to do that, Remy. With my ambassador status, I could just pay for all of us without you having to pay a cent."
                Ry "I… forgot you could just do that."
                c "Don’t worry about it."
                $ renpy.pause (0.5)
                m "I asked our waiter to bring us our bill. Soon after, the small dragon reappeared in front of us. I handed him the special card I was given on the day of my arrival, which allowed the council to cover my expenses."
                $ renpy.pause (0.5)
                m "After I had paid, me and Remy got up from our seats and walked out of the café."
                $ kol_tlh_mcpaid = True

            "Well, that’s just kind of her.":
                $ renpy.pause (0.5)
                $ kol_tlh_chapter1B_mood -= 1

                Ry look "It’s alright. We all make mistakes every once in a while. Besides, it’s not that much of a hassle, anyway."

                show remy normal with dissolve
                $ renpy.pause (0.5)
                m "Remy called for the waiter to bring the bill. Once he finished paying, he got up from his seat and went outside the café. I did the same after I had paid for my part of our meal."

            "We could just call her.":
                $ renpy.pause (0.5)
                Ry "I don’t think that bothering her when she’s getting ready for work would be a good choice."
                Ry normal "Besides, it would be more convenient if I paid for everyone. There is no need to pay separate bills for just one meal, after all."
                c "I see your point."
                $ renpy.pause (0.5)
                m "Remy called for the waiter to bring the bill to us. After the food had been paid, me and Remy both got up from our tables and walked out of the café."
            
        play sound "fx/chair.wav"
        $ renpy.pause (1.5)
        scene town3 with dissolve
        $ renpy.pause (1.5)

        m "We strolled through the streets, with me watching Remy to make sure he didn't hurt himself in his injured state. During our walk, however, we came across Sebastian on patrol." #Once again, hello Seb. I swear, you're like a courier from Skyrim or something considering you *always* find the MC.
        m "When he spotted us, he seemed to flash a quick smile, though returned to the way he was before."

        show remy normal flip at Position(xpos = 0.2) with dissolve
        show sebastian normal b at right with easeinright

        Sb "Hello, [player_name]. Hello, Remy. I hope you two are feeling well today."
        c "I can't complain."
        Ry "Oh, I’m doing quite fine, officer."
        Sb smile b "Good to hear. I was just about to make a visit to [player_name]’s apartment, though it seems that circumstances determined that we should meet here."
        c "Why were you looking for me, Sebastian?"
        Sb normal b "I’ve got something to deliver. Your hands only, at that." #I WAS JOKING, DAMN IT!!!
        Sb "The humans sent two messages earlier today; one sealed message addressed to you, the human ambassador, and a simple envelope addressed to the council."
        Sb "I figured that you’d want to know as soon as possible."
        c "I see. Any idea as to what the messages say?"
        Sb drop b "I’m not one to pry into highly confidential information like that."
        Sb disapproval b "Though if I had to guess, both messages contain the same information, but addressed to separate groups."
        Sb normal b "Just my speculation, though."
        c "Well, thanks for delivering the message, at least. I’ll read it later when I’m back at home."
        Sb "Sure. Anyway, best for me to get back on patrol again. Have a good day."
        c "Same to you, Sebastian."

        show sebastian normal flip b with dissolve
        hide sebastian with easeoutright
        $ renpy.pause (0.5)
        show remy at center with ease
        show remy normal with dissolve
        $ renpy.pause (1.0)
        m "Sebastian turned around and went back down the roads. As we walked further through town, I wondered about what the message might contain."
        $ renpy.pause (1.0)
        Ry look "You’re thinking about it too, aren’t you?"

        menu:
            "Yeah.":
                pass

            "How’d you know I was thinking about the message?":
                $ kol_tlh_chapter1B_mood += 1
                Ry "You’ve been looking quite deep in thought since Sebastian left, so I guessed that it must be the message causing you to act like that."
                c "Looks like someone had started to get self aware about thinking deeply recently."
                show remy shy with dissolve
                $ renpy.pause (0.5)
                Ry "I guess so."
                Ry look "My point still stands, however."

            "What’s it got to do with you?":
                $ kol_tlh_chapter1B_mood -= 1
                Ry "More than you might think. If that message is similar to the one directed towards the council, then it means that Emera is going to assign me to some other project of hers relating to that message."

        $ renpy.pause (0.5)
        Ry "The thing is, I just can’t help to wonder why the humans would send two separate messages instead of one."
        c "Maybe it’s because they’re trying to hide something from either me or the council, or one could be about the trade, while the other could be about my extra duties now that Reza is gone."

        $ renpy.pause (0.5)
        show kolmoretown1 behind remy with dissolvemed 

        Ry "It still feels unsettling that Reza has now been sent back through the portal. The trade agreement between humans and dragons is now under a huge amount of pressure. If something goes wrong within the next few days…"
        c "Yeah, I know. Let’s try to not think about that, though. We still have to come up with a plan with my PDA first and foremost. All we can do right now is try to resolve this as peacefully as we can."
        Ry "Maybe I shouldn’t worry so soon, then."

        scene black with fade
        $ renpy.pause (1.5)
        m "Eventually, we reached Remy’s apartment. We said our parting words to each other and went back to our daily lives."
        $ renpy.pause (2.5)
        scene o at Pan((0, 0), (0, 250), 5.0) with dissolveslow
        $ renpy.pause (2.5)
        m "It wasn’t long before I reached my own apartment, where I slowly sat down on the couch and relaxed."
        stop music fadeout (5.0)
        m "I decided that I should open the message to see what it contained. Anxiety swept through me as I broke the seal."
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
        $ renpy.pause (0.5)
        m "Wondering what would soon happen to the trade between humans and dragons, I slowly put the message down and shifted my position on the couch."
        $ renpy.pause (0.5)
        c "(I wonder if the dragons’ message is similar considering the fact that the authorities announced that the trade will continue as normal.)"
        c "(Though, I’m guessing that they’d leave any information out about me needing to continue my duties in their letter.)"
        m "In the end, I decided to take my mind off of things and simply read through the books stored on my bookshelf. When I finished reading, I realised that the day had mostly passed and night was fast approaching."
        scene black with fade
        $ renpy.pause (1.5)
        m "Feeling a need to be prepared for tomorrow’s possibilities, I decided that I should go to bed early."

        $ kol_tlh_chapter1B_done = True
        $ persistent.kol_tlh_chapter1B_skip = True

        jump tlh_Chapter2A

                # NOTE: THE MAX MOOD VALUE FOR 1B IS 4, AND THE MINIMUM VALUE IS -4
                # TO PASS THE DATE, YOU WILL NEED AT LEAST 1 OR ABOVE
                # ZERO ATTENDANCE WILL COUNT AS AN AUTOMATIC FAIL