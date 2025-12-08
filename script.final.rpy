# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rosen")
define j = Character("Jinn")
define c = Character("Carrie")
define d = Character("Dr. Maddie")
define s = Character("Susie")
define o = Character("Officer")



# The game starts here.

label start:
    scene bg dneee
    play music "audio/forest.mp3"
    r  "How did I get here."
    r " I wonder where the others went."
    r  "Maybe I can see if that house over there can help me."
    scene bg don
    r ' "Do Not Enter" Thats weird.' 
    r ' I should still knock.'
    stop music fadeout 1.0
    play music "audio/knock.mp3" loop
    r ' Someone! Please help me!'
    stop music
    scene bg inside
    r 'Hello! Is anyone in here?'
    play music "audio/slam.mp3"
    r 'What was that!'
    stop music
    r ' I need some food.'
    scene bg emp
    r ' great, no food.' 
    play music "audio/ring.mp3"
    r ' where is that coming from.'
    r 'I"ve gotta find that phone, maybe its help!'
    scene bg phone
    stop music fadeout 2.0
    j ' I told you not to enter my house!'
    j ' Now you must suffer.'
    scene bg seep
    r 'Ok that was weird.'
    r ' I need to get some rest.'
    scene bg hour
    '*'
    scene bg inside 
    r 'Cant sleep, man I wish I was back home.'
    c 'Psst, Hey, who are you.'
    r ' My name is Rosen. I am a professor at Temple University.'
    r ' I was on the road with my TAs for research and...'
    c ' you shouldnt have come here.'
    c ' You have to get out as soon as you can.'
    c ' or else youll end up like...'
    #scene end
    r ' Oh man who was I just talking to.'
    r ' Im losing my mind.'
    r ' Im just gonna leave while I can.'
    r 'This is getting weird.'
    "*door locked*"
    r ' What the hell.'
    play music "audio/ring.mp3"
    r ' Not that damn phone again!'
    scene bg seep
    stop music fadeout 2.0
    scene bg phone
    r ' Is it you again? Please let me go im sorry.'
    j ' sorry didnt do it, you did.'
    j 'you WILL die. Just like Carrie did.'
    scene bg seep
    scene bg fff
    play music "audio/scary.mp3" loop
    r ' Where am I now?'
    c ' Hey.'
    c ' This is the first step towards your death.'
    c ' If you want to stay alive, you have to follow my instructions.'
    r ' Okay.'
    r ' What do i have to do?'
    c ' You must find the telephone and keep Jinn talking for as much time as possible.'
    c ' The more it uses the phone the less power it has.'
    c ' But you must be quick. It gains power back after some time.'
    "Objective: Find the phone"
    scene bg seep
    j 'HAHAHAHAHA'
    r 'Why are you doing this me.'
    scene bg fff
    r 'What did I do to deserve this?'
    c 'You disturbed its house and peace.'
    c 'I made that same mistake.'
    r 'How do you know this?'
    c ' Because I was in your position once.'
    scene bg years
    c 'I got lost on a school camping trip 30 years ago.'
    scene bg camp
    '*.'
    scene bg chouse
    c ' Thats when I came across this house.'
    c ' That was the biggest mistake of my life.'
    c ' I want to help you get out so you dont end up like me.'
    c ' Do you want my help?'
    scene bg fff
    menu:
        'No, I can do it by myself.':
            jump no_help
        'Yes, we need to work together.':
            jump help
label help:
    c 'Ok great'
    c 'You have to go to the phone and keep it talking for some time.'
    r 'But carrie, Im scared.'
    c 'Dont worry. I know you can do it.'
    c 'Go to the phone'
    scene bg seep                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    jump good_ending



label no_help:
    c 'Very well, your path from now on will be short.'
    scene bg han
    r 'Now that I got that girl to go away, I need to get out of here.'
    r 'Still gotta find that phone.'
    scene bg phone
    r 'Hey!'
    j 'You should have taken her help'
    j 'Now there is no way out'
    r 'Dont worry ill find a way'
    j 'Is that what you think?'
    j 'I would love to see you try'
    menu:
        'Tell Jinn you know its weakness?':
            jump bad_ending
        'Keep it a secret':
            jump good_ending
label bad_ending:
    r 'I know your weakness. That I have to keep you on the phone'
    j 'Oh? is that true?'
    j 'So what happens if I hang up the phone?'
    "*Phone goes dead*"
    r 'Hello?'
    r 'SHIT!,SHIT!,SHIT!'
    scene bg demon
    play music "audio/jss.mp3"
    #r 'AHHHHHHHHH!'
    jump endd

label good_ending:
    scene bg phone
    r 'So tell me just what exactly do you want from me?'
    j'I want you to get out of my house'
    r 'So why dont you let me leave?'
    j 'Because you are already here. There is no way out now.'
    r "We'll see about that"
    jump end 
label end:
    'Great, you kept it on the phone for long enough'
    stop music fadeout 2.0 
    'Run to the door and get out of here!'
    play music "audio/run.mp3"
    "*"
    stop music
    scene bg forest
    play music "audio/forest.mp3"
    c 'Congradulations, you have successfully escaped the Jinn'
    stop music fadeout 3.0
    scene bg pic
    '*'
    stop music
    scene bg hos
    d ' Congratulations, you have finished your six month mental treatment'
    d 'You are free to go'
    r 'Thank you Doctor'
    scene bg drive
    r 'People wanna make me seem crazy'
    r 'I know what I saw'
    scene bg happy
    s 'Look son, your father is almost home!'
    scene bg angry
    s 'You cannot still be on about this.'
    s 'We sent you away so that you could get better.'
    r 'Its the truth!'
    r "There is no \'getting better'"
    r "I guess i\'ll have to make you believe with your own eyes"
    scene bg leave
    "*"
    scene bg ten
    '*'
    scene bg cabin
    "*"
    scene bg board
    r 'I finnaly did it!'
    r 'It all makes sense now'
    r 'Susie, Im coming home'
    scene bg overhead
    r "Man I can\'t wait to prove them wrong"
    r 'I am not crazy'
    scene bg driver
    play music "audio/ring.mp3"
    r 'Is that what I think it is?'
    r "It can\'t be"
    scene bg darkroad
    r "What\'s happening"
    stop music fadeout 3.0
    play music "audio/jss.mp3"
    scene bg demon
    j "Did you think that you could escape me?"
    r 'AHHHHHHHHHHHHH!!!!'
    jump endd
label endd:
    j 'There IS NO ESCAPE.'
    stop music 
    scene bg youdie
    "*"
    scene bg crash
    play music "audio/violin.mp3" loop
    o 'Im sorry miss but hes gone.'
    o 'We found him like this about an hour ago.'
    s 'That crazy idiot got himself killed.'
    scene bg funeral
    s 'Your father was a brave man.'
    s 'Never forget him.'
    scene bg end
    "*"






