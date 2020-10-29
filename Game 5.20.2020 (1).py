def menu():
        options=input("Play Language Exit")
        if options == "Play":
            for option in range(1):
                game()
        if options == "Language":
            for options in range(1):
                lang=input("Choose a language: English")
                menu()
        if options == "Exit":
            for options in range(1):
                print("Thank you for playing! Have a nice day!")
            
def game():
        enter=input("Press Enter to Start")
        if enter=="Enter":
                for name in range(1):
                        name=input("What's your name?")
                        print("Great...now, it's time to wake up...")
                        print("wake up...")

                for arrow in range(1):
                    print("Wake up?")
                    print("...I never thought waking up would be so hard.")
                    print("My eyelids feel so heavy, as if they are being weighted down by something.")
                    print("Unknown voice:",name,"is waking up!")
                    print(name,"is waking up!")
                    print("When I open my eyes, I am hit by a bright light before staring up at what looks like a ceiling.")
                    print("Unknown voice:'Don't move your head",name,". You have to keep it stable.'")
                    print("Who's speaking to me?")
                    print("A man appears in front of my vision.")
                    print("Unknown man:'It's okay",name,". Don't stress out.'")
                    print("I feel him holding one of my hands.")
                    
                    choiceone=input("I respond with...With confusion? With irritation? With sarcarsm?")
                    if choiceone == "With confusion":
                            print("I respond with confusion.")
                            print("You:'Why is it so bright in here? Where am I?'")
                            print("Unknown man:'You're in the hospital",name,"'.")
                            print("'A doctor is coming to check up on you.")
                            print("He lets go of my hand and brings his hand to his mouth, biting his nails nervously.")
                            print("Unknown man:'Hang in there,okay?'")
                    elif choiceone == "With irritation":
                            print("I respond with irritation.")
                            print("You:'*groans, tries to pull hand away with little strength* Let go of me man...'")
                            print("Unknown man:'Sorry!'")
                            print("He lets go of hand quickly, as if my words impaled him like a knife.")
                            print("Unknown man:'A-Are you in a lot of pain?'")
                    elif choiceone == "With sarcarsm":
                            print("I respond with sarcarsm.")
                            print("You:'Can't anyone get some peace and quiet in here?'")
                            print("The man laughs softly.")
                            print("Unknown voice:'I am glad to see that you're still the same",name,".'")
                            print("He lets go of my hand and caresses my face.")
                            print("Unknown man:'I would smooth out your hair, but I know your head must be giving you a lot of pain, right?'")
                            
                    print("You:'Yeah.'")
                    print("I feel searing pain completely within my skull.")
                    print("Did I hit my head against a brick wall and crack my noggin?")
                    print("Unknown man:'While we wait for the doctor, let me lift the back rest on your bed so the doctor can look over you properly.'") 
                    print("He moves away from my vision and I lay there, waiting.")
                    print("I soon feel the bed moving to help me in a sitting position.")
                    print("Once it stops, I realize that I can see more than the ceiling.")
                    print("I can see the entire room, so I process my new surrounding–the medical equipement, the tv hooked to the wall, and the loveseat that the guy is currently sitting on.")
                    print("I stare at him while he looks at his phone.")
                    print("He looks too young to be my dad and it would be so awkward if he is my boyfriend.")
                    print("Who is this guy?")
                    print("As I try to find answers to this question, he soon feels my stare and looks up at me with confusion of his own.")
                    print("Unknown man:'Um–why are you staring at me like that? You look as if you don't know me.'")
                    print("You:'...Do I know you?'")
                    print("Before he can say anything, the doctor and nurses burst into the room.")
                    print("I wish they came 10 seconds earlier...")
                    print("...to not only tell me why my head hurts so much, but...")
                    print("...to also spare me from seeing the distress written in the guy's face.")
                    print("After checking up on me, the doctor and nurses took that guy outside of the room.")
                    print("I hear them talk out there, but the walls make their words hard to understand.")
                    print("They talk for a while before the guy returns to the room, raking his fingers through his hair.")
                    
                    choicetwo=input("Based on how stressed out he looks, I do not know how to act...Concerned? Be Direct? Accuse him?")
                    if choicetwo == "Concerned":
                            print("After staring at him for a few more seconds, I feel concern for him.")
                            print("You:'Are you okay? I am sorry...I didn't mean to make you upset.'")
                            print("The guy goes slient. Then, he gives a sad smile.")
                            print("Unknown man:'You really don't remember me, huh?'")
                            print("I nod slowly.")
                            print("Unknown man:'...I'm your big brother, Johnny.'")
                    elif choicetwo == "Be Direct":
                            print("He's here for a reason, and I want to know.")
                            print("You:'How do you know me? Who are you?'")
                            print("The guy goes slient.")
                            print("Unknown man:'You really don't remember me, huh?'")
                            print("I nod slowly.")
                            print("Unknown man:'...I'm your big brother, Johnny.'")
                    elif choicetwo == "Accuse him":
                            print("I can't help but feel suspicious of this guy!")
                            print("You:'Are you the reason why I'm here? You look like you're guilty of something.'")
                            print("His eyebrows narrow before glaring at me.")
                            print("I am not the reason why you're here, so stop pointing fingers!")
                            print("Soon,the guy goes slient.")
                            print("Unknown man:'You really don't remember me, huh?'")
                            print("I nod slowly.")
                            print("Unknown man:'...I'm your big brother, Johnny.'")
                            
                    print("Brother?")
                    print("You:'You're my brother?'")
                    print("Johnny nods.")
                    print("Johnny:'Mom and Dad would be here too, but they're out of the country because of work; they're planning to take the next flight to see you.'")
                    print("Johnny:'They are not going to take your amnesia well, but I can take care of that, don't worry.'")
                    print("Johnny:'Is there anything you can remember?'")
                    print("I shake my head.")
                    print("You:'All I can remember is my name...'")
                    print("Johnny covers his eyes as he leans against the wall.")
                    print("Johnny:'This is not how I would imagine our reunion to be...'")
                    print("You:'Our reunion?'")
                    print("Johnny nods.")
                    print("Johnny:'It has been two years since we last saw each other.'")
            
                    choicethree=input("Two years? I can't help but feel...Guilt? Offended? Shock?")       
                    if choicethree == "Guilt":
                            print("...I can't help but feel so guilty.")
                            print("You:'2 years? That's a long time....'")
                            print("You:'I hope I didn't worry you too much.'")
                            print("Johnny sighs.")
                            print("Johnny:'I did worry, we hardly talked during these past two years. I'm glad to be here right now; I wanted to know what happened you and make sure you're okay.'")
                    elif choicethree == "Offended":
                            print("...I can't help but feel offended by that.")
                            print("You:'You haven't talked to me 2 years?!'")
                            print("Johnny frowns deeply at me.")
                            print("Johnny:'No,because you hardly picked up the phone! We only exchanged a few texts over the years, so I still can't over seeing you in the flesh since it's been awhile.'")
                    elif choicethree == "Shock":
                            print("...I can't help but feel shock!")
                            print("You:'Why has it been 2 years...?'")
                            print("Johnny sighs.")
                            print("Johnny:'You moved out of the house two years ago and ever since you left, you were so hard to contact. You would only text me a few messages over the two years.'")

                    print("You:'...So you don't know what happened to me then?'")      
                    print("Johnny:'Not really. All I know is that you and Mark got into a car accident.'")
                    print("Johnny:'Mark was driving the car and had little injuries, while you had more severe injuries.'")
                    print("Mark...? A car accident...?")
                    print("Johnny:'Oh! Wait! Maybe there's a way to jog your memory!'")
                    print("He digs inside his pants pocket and pulls out a smartphone before giving it to me.")
                    print("You:'A phone?")
                    print("Johnny:'It's your phone! Look what's inside your phone; maybe it can help you remember something.'")
                    print("Hopefully...I put my fingerprint on the lockscreen and soon, it unlocks, showing me all sorts of words and apps.")

                    choicefour=input("My finger hovers over the screen. I want to check...My photos? My messages?")
                    if choicefour == "My photos":
                            print("...I want to check my photos.")
                            print("I tap on the gallery app; many images appear on the screen.")
                            print("The last photo I took looks like I am inside a car with someone.")
                            print("I click on it to have a closer look.")
                            print("It looks like I took a selfie with a guy I don't recognize; he's behind the wheel while I was sitting in the passenger's seat.")
                            choicefive=input("I don't know who's next to me in this photo, nor when this was taken...I want ask Johnny about the man? Or when this was taken?")
                            if choicefive == "The man?":
                                    print("You:'Who is this guy, Johnny?")
                                    print("I give him the phone, so he can see.")
                                    print("Johnny:'Ah...that's our old friend, Mark.'")
                            elif choicefive== "When was this taken?":
                                    print("You:'When was this taken,Johnny?")
                                    print("I give him the phone, so he can see.")
                                    print("Johnny:'This was taken 12 hours ago...'")
                                    print("You:'How long have I been here?")
                                    print("Johnny:'At least 9 hours I think...I got here 7 hours ago and you were unconscious...'")
                                    print("Johnny:'You hit your head so hard in the accident, fortunately Mark called the paramedics on time.'")

                    elif choicefour == "My messages":
                            print("...I want to check my messages.")
                            print("I tap on the messages app; a list of contacts appear.")
                            choicefive2=input("It seems that I have some unread messages from Johnny, Mark, and Jeff. Which messages should I read...? Johnny's? Mark's? Jeff's?")
                            if choicefive2 == "Johnny's?":
                                    print("...I want to see what Johnny has texted me.")
                                    print("He texted me yesterday, most likely before the accident.")
                                    print("Johnny:'Hey",name,"'.")
                                    print("Johnny:'Please call me when you can. We need to plan a day for us to get together.'")
                                    print("Johnny:'Mom and dad really miss you;they want to see you, even for 10 minutes if that makes you happy.'")
                                    print("Johnny:'Please, man.'")
                                    print("...That's all he sent;he wasn't kidding when he said we haven't seen each other in a long time. I wonder why I hardly see my own family?")
                            if choicefive2 == "Mark's?":
                                    print("...I want to see what Mark has texted me.")
                                    print("He texted me yesterday, most likely before the accident.")
                                    print("Mark:'Yo",name,"'!")
                                    print("Mark:'I am waiting for you in the car!'")
                                    print("Mark:'Come on, we got things to do.'")
                                    print("Mark:'Why are you so bad at checking your texts? You can't ignore my messages; remember, we are in this for the long run.'")
                                    print("...That's all he sent; Who is Mark? And what did we do to make us stay 'for the long run?'")
                            if choicefive2 == "Jeff's?":
                                    print("...I want to see what Jeff has texted me.")
                                    print("He texted me yesterday, most likely before the accident.")
                                    print("Jeff:'",name,"'")
                                    print("Jeff:'You can't avoid me forever.'")
                                    print("Jeff:'Me and my boys will find you and Mark.'")
                                    print("Jeff:'We will show you what happens to those who try to stab people on the back.'")
                                    print("...That's all he sent; Who is Jeff? He sounds dangerous...it seems like I have some enemies.'")

                    print("*knock knock*")
                    print("Johnny and I look at the door...someone's here, but who?")
                    print("I watch my brother walk towards the door and opens it for us to see another guy waiting out in the hallway.")
                    print("Unknown man:'Hey...I heard",name,"is up.'")
                    print("Johnny looks at me and back at him.")
                    print("I can hear him whisper that he wants to talk to him in the hallway, but the unknown man shakes his head.")
                    print("Unknown man:'No need to man, I already know about the amnesia...I spoke with the doctor.'")
                    print("Unknown man gives me a look that I cannot decipher." )
                    print("Unknown man:'Let me speak to",name,"alone.'")
                    print("Johnny looks shocked; his mouth almost open as if he wants to refuse, but I speak up first.")
                    print("You:'Let him do it, Johnny. I can feel some memories returning and I believe he can help me understand them.'")
                    print("I lie. I don't feel anything returning right now, but I know this is the truth: this unknown man can help me understand what happened to me.")
                    print("Forunately, Johnny nods and leaves the room as the unknown man enters.")
                    print("The unknown man walks up to me and sits at the foot of the bed.")
                    print("Unknown man:'...Do you know who I am",name,"?'")

                    choicesix=input("He's...Johnny? Mark? Jeff?")
                    if choicesix == "Johnny":
                            print("You:'You're Johnny.'")
                            print("The unknown man chuckles.")
                            print("Unknown man:'No, I am not your brother, despite how much as I would like to be him. He's a cool guy.'")
                            print("Unknown man:'I'm Mark.'")
                    elif choicesix == "Mark":
                            print("You:'You're Mark.'")
                            print("The unknown man smiles.")
                            print("Unknown man:'You're right!'")
                            print("Unknown man:'I'm glad that you remember.'")
                    elif choicesix == "Jeff":
                            print("You:'You're Jeff.'")
                            print("The unknown man frowns.")
                            print("Unknown man:'No, I am not that bastard!'")
                            print("Unknown man:'...I'm Mark.'")

                    print("Mark soon winces; he looks down to his arm that is wrapped in bandages.")
                    print("He looks pretty beaten up;he has some scars on his face and his arm looks pretty bad.")

                    choiceseven=input("I want to ask: What happened to you? Why am I here? What's going on?")       
                    if choiceseven == "What happened to you?":
                            print("You:'What happened to you?'")
                            print("Mark gives me a sheepish grin.")
                            print("Mark:'My arm got most of the brunt in the accident.Fortunately, no bones are broken, but it has an ugly and sensitive bruise, so I have to cover it up.'")
                    if choiceseven == "Why am I here?":
                            print("You:'Why am I here?'")
                            print("Mark gives me a sad look.")
                            print("Mark:'You already know man...I was so scared on my way here. You hit your head so hard that you had to go to surgery to stop the bleeding.'")
                            print("Mark:'I had to wait til Johnny got here because the doctor only allowed kin to see you earlier.")
                    if choiceseven == "What's going on?":
                            print("You:'What's going on?'")
                            print("Mark gives me a confused look.")
                            print("Mark:'What do you mean?'")

                    print("I go slient for a few seconds.")
                    print("You:'How did we get into a car accident?'")
                    print("Mark's face quickly goes pale.")
                    print("Mark:'...To make a long story short: We were being chased down by another car. They know we got the money and we didn't want them to get the bag.'")
                    print("Mark:'As they were chasing us, they were able to bump us out of the road, making us hit a tree. That's what happened.'")

                    choiceeight=input("Wait, what?...He's skipping over some important details...They? Money? The bag?")       
                    if choiceeight == "They":
                            print("You:'Who's they?'")
                            print("Mark:'Jeff and his crew. We currently have bad blood with each other and they have always wanted to get revenge for the past few months.'")
                    elif choiceeight == "Money":
                            print("You:'What money?'")
                            print("Mark:'...we stole some money from Jeff and his crew; we all used to be good friends, but once things got sour, we took some money in order to get away from them.'")
                    elif choiceeight == "The bag":
                            print("You:'What bag?")
                            print("Mark:'...We have a bag of stuff that is not really legal to have, okay? I can't go into much detail in this kind of setting.")
                            print("Mark:'It's just...that bag should never fall into the hands of Jeff and his crew, the guys who chased us. We worked so hard to earn it.'")

                    print("Mark:'I know you have so many more questions",name,"and I promise to answer them when you get discharged...'")
                    print("Tears start to well up in his eyes.")
                    print("Mark:'...I am so sorry man; you're like my best friend and it hurts so much to see you like this when we have things to worry about.'")

                    choicenine=input("I can't help but feel...Confused? Sympathy? Anger?")       
                    if choicenine == "Confused":
                            print("...I can't help but feel so confused.")
                            print("You:'What did we get ourselves into...?'")
                            print("Mark wipes his eyes, trying to not let any tears spill out.")
                            print("Mark:'We got into some serious stuff...but don't worry, we'll get through this and help you get your memories back.'")
                    elif choicenine == "Sympathy":
                            print("...I can't help but feel sympathy for him.")
                            print("You:'Hey...it's okay, Mark. We are going to get through this, with memories or without memories.'")
                            print("Mark smiles at me, tears falling down his face.")
                            print("Mark:'Thanks man; I know we will...'")
                    elif choicenine == "Anger":
                            print("...I can't help but feel anger boiling inside me.")
                            print("You:'...You're sorry for me?! What did you get me into?!'")
                            print("Mark gasps at me, tears falling down his face.")
                            print("Mark:'Man, I'm really sorry–'")
                            print("You:'GET OUT! GET OUT OF MY ROOM!'")
                            print("Mark quickly jumps out of the bed and through the door.")

                    print("After a few seconds, I sigh as I look up at the ceiling for the second time that day.")
                    print("I really do hope my memories come back soon...before things get any worse...")
                    menu()
            
def main ():
    menu()
    game()
main()
