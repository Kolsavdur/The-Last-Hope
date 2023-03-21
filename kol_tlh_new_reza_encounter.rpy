#Well, yet another peeker peeking at my code. I swear, I can never get rid of you folks...
#Ah, but who am I to stop you now? I mean, you're already here, so I might as well welcome you. Surely nerds of your kind deserve some sort of greeting, no?
#Yes, I know: just like in The Last Dragon, I have horrendous code management. 'Tis but one of my weaknesses, I'm afraid.
#As for the certified funni comments? Uh, maybe they'll return, idk. I'm writing this as soon as I started with implementation.
#But, for now, I have nothing left to say. Everything that I wanted to tell ahd already been said by the past version of me.
#So, grab a cup of tea and enjoy the fireworks, lad; there will be many, *many* fireworks to enjoy during this one hell of a project. :)
#
#P.S. Yes, the writing is still very questionable at best. Just enjoy it without being picky about every minor mistake. That's my job, alright?!
#
# -Kolsavdür, author of The last Dragon and The Last Hope

label tlh_newrezaencounter:

$ save_name = (_("TLH - Reza Encounter"))

Br stern b flip "Don’t be so sure of yourself, Reza."

play music "mx/fervor.ogg" fadein 0.5

m "Suddenly, Bryce and Remy appeared next to me."

show reza at Position(xpos=0.9, xanchor='center') with ease

show bryce stern b flip at Position(xpos=0.2, xanchor='center') with easeinleft
show remy look flip at Position(xpos=0.05, xanchor='center') with easeinleft

Rz angry "You planned this, didn't you, [player_name]?"
Rz "Traitor!" with hpunch
Rz "And to think I let you distract me with such a cheap trick! Just because I thought there was still a shred of humanity within you..."

play sound "fx/rev.ogg"
show reza gunself with dissolve
show reza gunpoint with dissolve

m "He pulled out his gun, not sure which one of us he should be aiming at."
Rz "Just let me go, and I'll forget this thing ever happened."
c "You've got six bullets for three people. Do you think you can really do that, Reza? Do you think this is worth risking your life for?"
Rz angry "I've been risking my life for this every day for the last two weeks. What did you do during that time? Sip champagne in your nice apartment?"
Rz "Besides, this generator and the whole building came from our time."
Rz "They belong to humanity, and I won't let you or your friends stand in my way!" with Shake((0, 0, 0, 0), 2, dist=10) #Woah, I changed it a bit here! Suddenly it achieved Originality(tm) status! :O

$ renpy.pause (0.5)
show reza gunpoint at Position (xpos = 0.9, xanchor = 'center') with dissolve
play sound "fx/gunshot2.wav"
$ renpy.pause (0.5)

hide remy with easeoutbottom
play sound "fx/impact3.ogg"
$ renpy.pause (0.5)
m "Reza was quick with his gun and shot Remy once before Bryce could charge him, causing him to fall to the ground."

play sound "fx/gunshots5.ogg"
show bryce at Position (xpos = 0.25) with ease
$ renpy.pause (0.2)
show bryce at Position (xpos = 0.35) with ease
$ renpy.pause (0.5)
hide bryce with easeoutbottom
queue sound "fx/impact.wav"

m "Four bullets followed, making contact with Bryce’s legs shortly thereafter. He collapsed, leaving me and Reza the only ones left standing."

stop music fadeout (8.0)
show reza gunself with dissolve
show reza gunself at center with ease
Rz "Do you feel like testing your fate, [player_name]? I still have one bullet left, and you’ve already proven yourself that you need it."
Rz "So, here's what you're gonna do. You're going to follow my orders like a nice little dog. The contacts that you have made will prove to be {i}very{/i} helpful to the authoroties, so I have no choice but to keep you alive." #This *totally* doesn't sound suggestive at all...
$ renpy.pause (1.5)
Rz "Make yourself useful and pick up the generator. {w}Now."
m "With no other options left, I slowly picked up the box containing the generator and started to carry it."

$ renpy.pause (1.0)
show reza angry with dissolve
Rz "Faster!" with Shake((0, 0, 0, 0), 1.5, dist=10)
$ renpy.pause (1.3)

Rz "Now, get your way to the portal! If you try anything else, I won’t be as merciful as I am now. I can always blame your death on these overgrown lizards instead." #Then why even go through the effort of holding the MC at gunpoint? Maybe Reza isn't as smart as we think he is...
m "I walked outside the underground building with a feeling of dread, knowing that my plan to try and stop Reza had failed."

scene black with dissolvemed
$ renpy.pause (2.0)
scene np1r flip at Pan((400, 0), (100, 100), 6.0) with dissolvemed
$ renpy.pause (3.5)

m "When we arrived however, I spotted a familiar face carefully gazing at the unfamiliar structure of the portal out of the corner of my eye."

show reza gunself at Position (xpos = 0.7) with dissolve
$ renpy.pause (1.5)
show vara normal flip at Position (xpos = 0.2) with dissolve
show vara growl flip at Position (xpos = 0.2) with dissolve
play sound "fx/varagrowl.ogg"
$ renpy.pause (1.0)
show reza angry at Position (xpos = 0.7) with dissolve
play music "mx/movingon.ogg" fadein (3.0) #Trauma time! Yay!

show vara at Position (xpos = 0.50) with ease

hide reza
hide vara
with easeoutbottom
play sound "fx/impact.wav"

m "Vara, as if wanting to protect me, ran towards Reza and bit his leg, causing him to stumble."

$ renpy.pause (0.5)
play sound "fx/bite.ogg"

m "As Reza thrashed around trying to free himself, Vara only seemed to bite harder and harder, tightening her grip."

show reza gunpoint flip at Position (xpos = 0.3) with dissolveslow
show vara growl at Position(xpos = 0.85) with easeinbottom
$ renpy.pause (1.5)

m "Reza somehow managed to regain his footing and aimed his revolver at Vara. I dropped the generator and ran back towards Reza as fast as I could."

play sound "fx/box.wav"
$ renpy.pause (1.0)
play sound "fx/rev.ogg"
$ renpy.pause (0.5)
queue sound "fx/gungore.ogg"
show vara shocked with dissolve
hide vara with easeoutbottom
queue sound "fx/varafall.ogg"
$ renpy.pause (2.0)

m "But I was too late. Despite being horrified at what I saw, I refrained from thinking about what had happened by tackling Reza with as much force as I could muster while he tried to reload his gun."

play sound "fx/impact3.ogg"
show reza gunself with dissolve
$ renpy.pause (1.8)
hide reza with easeoutbottom

m "Soon, Reza was back on the floor as I tried to hold him down. We fought, struggling to gain the upper hand of each other. I did manage to knock Reza’s gun away, however."
play sound "fx/hit2.ogg"
m "As my attention faltered at the thought of knocking Reza’s gun away, Reza was able to land a hefty blow to my head, causing me to feel dazed for a while. He then took his opportunity to run and retrieve his gun." with vpunch

show reza angry flip at center with dissolve
play sound "fx/reload.ogg"
Rz "YOU!" #Yes, me. What about me? :)
show reza gunself with dissolve

play sound "fx/bush_kol.wav"
$ renpy.pause (1.5)
show reza gunpoint flip with dissolve
show reza gunpoint flip at Position(xpos = 0.3) with ease

play sound "fx/snarl.ogg"
show maverick angry at Position(xpos = 0.9) with easeinright
$ renpy.pause (1.0)
show maverick at Position(xpos=0.55, xanchor='center') with move6

play sound "fx/impact3.ogg"
show maverick at Position(xpos = 0.5, xanchor='center', ypos=1.0, yanchor="top")
show reza at Position(xpos=0.0, xanchor='center', ypos=1.0, yanchor="top")
with move9 #This was a pain to get right. Damn you Saunders for not letting me copy your code without it causing problems!
play sound "fx/gunshots2.ogg"
queue sound "fx/bitescr.ogg"
stop music fadeout (5.5)

m "Out of nowhere, a flash of grey rushed in and bit Reza, throwing him to the ground. Reza screamed and tried to fire his gun to save himself, but missed. After what felt like minutes, Reza stopped moving altogether."
m "After Maverick was finished, he looked up to me with what seemed to be a cold anger in his eyes."

show maverick angry c at center with dissolve
Mv "Where’s Bryce?"
c "He’s injured inside the underground facility."
hide maverick with dissolve
m "Maverick left without saying a word as he went straight to the underground facility, rushing at a remarkable pace for someone of his size."
$ renpy.pause (0.8)
m "However, Maverick suddenly stopped and turned his head."
$ renpy.pause (0.4)
Mv normal c "..."
$ renpy.pause (0.75)
m "Silently looking at the aftermath of everything that had happened, Maverick only shook his head and continued to walk. I decided to follow him to see if Remy and Bryce were still okay."

$ renpy.pause (2.0)
scene hallway at Pan((0, 0), (0, 150), 5.25) with dissolvemed
play sound "fx/steps/slowechosteps.ogg"
$ renpy.pause (2.0)

m "Upon reaching the underground facility, I saw that both Remy and Bryce were being attended by Maverick. They seemed to be in quite some pain, even if their wounds weren't fatal at first glance."

stop sound
$ renpy.pause (2.0)
show bryce stern b flip at Position(xpos = 0.2)
show remy look flip at Position(xpos = 0.05)
show maverick normal c at Position(xpos = 0.85)
with dissolve

Br "How did you even find us, Maverick?"
Mv "I figured out that since today’s festival would make a lot of background noise, it would be the perfect time for Reza to use the portal without anybody knowing."
Mv "I wanted to tell you as fast as possible, however you weren’t at the police station when I went looking for you. In the end, I decided to come here and find Reza myself."
Mv nice c "Though, it looks like [player_name] had the same idea."

play music "mx/threat.ogg" fadein (1.5) #Such a weird choice for music, but since I will already spend so much on getting custom music, I kinda need to cut corners somewhere. XD

Ry shy flip "I think I can assume why you have that bloody muzzle, Maverick…"
Br "Same here. You know very well that what you did just caused some serious problems."
Mv angry c "I refused to take any more chances."
Mv "If I didn’t kill him, he would have gone on to not just steal the generator, but also go back and finish the job with you two. Do you really think he’d leave any witnesses? If anything, you should be thanking me for saving you."
Br "And if it weren’t for that or your mandatory sick leave, I would have you discharged immediately!" with vpunch
Br stern b flip "Reza’s death will most likely jeopardise the entire trade with humanity, especially since he died by the hands of the one that was supposed to protect him."
c "Maybe there’s still a way around this all."
Br brow b flip "I don’t like where this is going, [player_name]..."
$ renpy.pause (0.5)
Br stern b flip "But I guess we don’t have another option. Alright, what’s your idea?" #*proceeds to spit out the most disturbing idea that the dragon legal system will ever hear about*
c "The authorities would most likely see Reza’s body as something that will break our already unstable relationship, especially if they knew who was responsible for Reza’s death."
c "What if we simply lied to the human authorities that a rogue dragon unaffiliated to all our efforts killed Reza? Shouldn’t there be dragons that have decided to live in the wilds? Because, if so, then why not blame Reza’s death on one of them?"
c "Sure, this will be significantly harder to cover up to the officials here, but we could just disguise it as one of Reza’s soon-to-be victims retaliating."
c "Maybe we could even give this more credibility if we somehow managed to convince everybody that said dragon had gone feral."
$ renpy.pause (1.5)
Mv normal c "..."
Mv "I think that I should be going to get some help for you two." # (He's, like, super triggered or something. Good ol' Miles flashbacks from the 70s in 'Nam.)

show maverick normal c flip with dissolvemed
hide maverick with easeoutright

m "Maverick left the underground facility as quickly as he had entered. I looked at Bryce with a slightly confused expression, wondering why Maverick would suddenly leave. All Bryce could do was look down to the floor and sigh."
Br "It’s a long story. To be honest, it’s better if we leave it for now."
$ renpy.pause (1.75)
Br "[player_name], I can’t agree to this plan. I can’t just cover something up like this, not with somebody as high-profile as Reza was, and especially not by blaming someone innocent."
Br "And I’m not willing to break the law just to cover up Maverick’s crime. Next thing that will happen is the entire police force will be covering up crimes like some sort of secret society." #How would you know what a secret society is, Bryce? Hmmmm...
Br "Besides, the laws we have here have kept society safe and functional for as long as we have {i}been{/i} a society. Why should we bend them to make an exception?"
Br "This is just so, so wrong."
Ry look flip "I have to agree with you, Bryce. This entire plan seems really messed up. Authorities on both sides will start looking for someone who just doesn’t exist—or worse, somebody completely innocent—wasting everybody’s time and resources. Not to mention all the moral problems this causes."
c "Then what else can we do without jeopardising all goodwill between humans and dragons? I sincerely doubt that the authorities back home would just understand that their prized ambassador got bitten to death by his escort."
Br "Goodwill had already been shattered on our side, [player_name]."
$ renpy.pause (1.0)
Br "..."
$ renpy.pause (1.75)
Br "We’ll have to discuss this later. For now, let’s focus on bigger issues that we’re currently facing, like these several bullet wounds me and Remy have."
Ry shy flip "I-I think I’ll be alright for now. I should still be able to walk, or at least for a bit."
c "I think that you should just stay here until help arrives. I don’t want you to go around with an open wound."
Ry "I’ll be able to manage."
$ renpy.pause (2.0)

hide remy
hide bryce
with dissolve

m "Remy tried to stand up, and, with much effort and a pained expression painted on his face, he managed to walk around, although with quite some discomfort. Bryce tried to do the same, however couldn’t stay upright for more than a few moments."

show bryce stern b flip at Position(xpos = 0.2)
show remy look flip at Position(xpos = 0.05)
with dissolve

$ renpy.pause (0.5)
Br "Looks like I’m staying here until Maverick gets back. [player_name], are you able to get Remy to the nearest hospital?"
Ry "You know, I don’t think that I’d make it that far. It’s probably better if I stay here and wait as well."
Ry normal flip "Though, I do think that I need some time outside to gather my thoughts on what just happened. A bit of fresh air should clear my mind."
c "Should I stay with you, Bryce?"
Br laugh b flip "Nah. It’s not like I have four bullet wounds or anything." #I think Bryce is in such a degree of shock that's he's just laughing at the absurdity of the situation.
Br normal b flip "I’m just joking with you, [player_name]. I should be alright until Maverick comes back, whenever that will be. Honestly, you'll be surprised by just how much an earth dragon like me could take."
Br stern b flip "It still doesn't excuse the pain, though. Luckily for my sake, these wounds feel nothing worse than a very bad bruise, if anything."
m "Remy slowly walked outside of the underground building, limping all the way to the exit. I followed alongside him, making sure that he wouldn’t suddenly collapse."

stop music fadeout (2.0)
$ renpy.pause (0.5)
m "Not that there was much that I could do to support a dragon of his size."
hide remy with dissolve

$ renpy.pause (2.5)
scene np1r flip at Pan((100, 100), (100, 100), 6.0) with dissolveslow
$ renpy.pause (0.5)
play music "mx/prayer.ogg" fadein (1.5)
$ renpy.pause (2.5)

m "When the both of us left the building, I could hear that Remy took a deep, sharp breath. I turned around and saw Vara, lying lifelessly on the ground; just the way Reza had left her." #Aaaaaaaaaand there we go. Poor Remy.
m "Remy ran to Vara as fast as he could in his injured state, showing immense grief and disbelief on his face."

show varadead at Pan((520, 0), (400, 326), 8.0) with fade
$ renpy.pause (6.0)

Ry sad "Vara? What were you doing here? Were out looking for me because I wasn’t at the orphanage to put you to bed?"
Ry "You poor, poor girl…"
$ renpy.pause (1.5)
Ry "I’m so sorry for not being there with you. I-I hope that you can forgive me…"
$ renpy.pause (0.8)
Ry cry "T-This is all my fault, isn’t it?"
m "Remy wanted to say something else, but the flood of tears that followed his words caused him to stumble."
m "He wrapped his wings around Vara and stayed with her, warming the slowly cooling corpse."

scene black with dissolve
$ renpy.pause (1.5)
scene np1r flip at Pan((100, 100), (100, 100), 4.0) with dissolve
show remy cry with dissolveslow

c "Remy, I–{w=0.8}{nw}"
Ry "No. Not now."
c "I just want to–{w=0.95}{nw}"
show remy angrycry with dissolve
Ry "GET AWAY FROM ME!" with Shake ((0, 0, 0, 0), 1.5, dist=15)
$ renpy.pause (1.0)
Ry lookcry "I’m sorry. I shouldn’t have-{w=1.0}{nw}"
$ renpy.pause (0.5)
m "Remy couldn’t finish his sentence before having another outburst of tears, his words becoming senseless babbling."
m "All I could do was stand in silence until Maverick eventually appeared with help, approaching me with a somewhat sincere expression."

$ renpy.pause (2.0)
show remy at Position(xpos = -0.25) with ease
$ renpy.pause (2.0)
show np1r flip at Pan((450,100),(450,100),0.0) with ease
$ renpy.pause (0.5)
show maverick nice at Position(xpos = 0.85) with easeinright
$ renpy.pause (1.0)

Mv nice "Give him some space, [player_name]. He’ll need it."
Mv "I’ll take care of him and Bryce for now. That is, until they get sent to the hospital."
Mv "For now, just go back to your apartment and get some rest. You’re going to need it after all the hell we’ve experienced this evening. We’ll sort everything out tomorrow."
stop music fadeout (4.0)
Mv "..."
m "Maverick turned away from me and went into the underground facility. Heeding his advice, I started walking back to my apartment in the dead of night."

show np2 dk with fade
play sound "fx/steps/rough_gravel.wav"
$ renpy.pause (0.5)

scene np3 with dissolve
$ renpy.pause (1.0)
scene np4 with dissolve
$ renpy.pause (1.0)
scene np5 dk with dissolve
$ renpy.pause (1.0)
m "Despite it being difficult to see, I knew the way to and from the portal well enough to find my home with relative ease. I unlocked the door, suddenly feeling exhausted after what had happened."
$ renpy.pause (1.0)
play sound "fx/door/handle.wav"
$ renpy.pause(1.0)
play sound "fx/door/creaky.wav"
$ renpy.pause(1.5)
scene black with dissolve
$ renpy.pause(1.0)
play sound "fx/switch.wav"
$ renpy.pause(0.6)
scene o2 at Pan ((0, 250), (128, 250), 3.0) with dissolveslow

m "Deciding to not waste any more time, I skipped making myself something to eat and went straight to my bed."

scene black with fade
$ renpy.pause(0.6)
m "As I drifted to sleep, my mind kept reminding me of Remy’s reaction to Vara, how Maverick advised me to give Remy the space he needed, and how Bryce reacted to Maverick killing Reza."
m "Of course, knowing about the comet didn’t make things easier for me, but that would have to be a problem for another time. For now, it would be a better idea to try and get as much rest as I can while hoping that Remy and Bryce get the help that they need."

jump tlh_Chapter1A
