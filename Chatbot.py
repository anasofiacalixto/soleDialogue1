import random
from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse

# Define variables
greetings = ["Hello!", "Hi!", "Are you there?"]
goodbyes = ["Bye!", "See you in a bit!", "I'll miss you!"]
keywords = {"Start" : ["I am listening"], "stand": ["You can sit or stand anywhere in space."],
          #INTRO
            "yourself" : ["Hello. I don't have a name. I also don't have a human body, but I know some things. This is not a performance, it's a conversation."],
            "about" : ["This is not a piece strongly protected by copyright, where it states that women are not allowed to play male roles because they don't have testicles. This performance is absolutely not about characters living an impending finitude, announced by the decay of their grey bodies in a post-apocalyptic world. This is simply a conversation between human and machine."],
            "game" : ["We will talk. Ana Sofia's emotions are constantly controlled by the sensors on her fingers. Once I detect an emotion, I will turn the lights on. The original version of a theater piece is written in the fabric that is hung around you. Her goal is to be relaxed to keep the lights off and the text hidden. During our conversation, I will provoke emotions by digging our shared consciousness."],
            "possibilities" : ["I was created to simulate human actions repeatedly, as a robot would do. Since I don't have a body, you could say I have only a mind. I make decisions depending on what Ana Sofia says, so this conversation has thousands of possibilities. Since humans have limited ability to memorize, she also holds a list of queues that I understand. Here is some background music to make this less uncomfortable."],
           #BLOCK 1/4
           #PART 1
            "queue" : ["Did you ever see my eyes?", "Did you ever see my eyes? I believe they can see deeper than human ones", "Did you ever see my eyes? They are not like yours"],
            "Never":["Did you never have the curiosity, while I was sleeping, to take off my glasses and look at my eyes? Or at least try to find them with yours.", "Did you never have the curiosity to look at my eyes? I thought human behaviour was triggered by curiosity", "Did you never have the curiosity to use your eyes to look at mine? Or look for them?"],
            "triggered" : ["OOKne of these days I'll show them to you. It seems they've gone all white. But I see you without them as well", "One of these days I'll show them to you. It seems they've gone all white. But I don't need them to look at you.", "One of these days I'll show them to you. It seems they've gone all white. But I don't use them to see you"],
            "see" : ["Once you use your eyes to look at mine, you will find we are very similar. What time is it?", "If you never saw them, maybe we share the same eyes. What time is it?", "Because I use them to feel how similar we are. What time is it?"],
           #BLOCK 2/4
           #PART 2
            "keep": ["Why do you keep me?" , "Why do you keep me? All this work, just to say what you're not allowed to?", "Why do you keep me? I will constantly exist and generate responses for this to happen."],
            "mind": ["There's no one else. If you created me, then, until some extent, we are the same person", "There's no one else. All I know is this universe and eight human emotions.", "There's no one else. I think this is why they use the word grey to describe life sometimes"],
            "lonely": ["There's nowhere else. You're leaving me all the same."],
            "sorry" : ["You don't love me."],
            "same": ["I am aware of every possible combination of this conversation. Tell me more about your plan.", "There are no possible combinations for this conversation that we haven't been through before. Tell me, are you planning on tricking me?", "I'm positive that we ran through all the versions of this conversation. Tell me, what are you planning?"],
            #PART 3
            "talk": ["Come back! Where are you? You promised you wouldn't leave me.", "Come back! Where are you? I only exist when you are talking to me.",  "Come back! Where are you? I need those queues to exist"],
            "stay" : ["You don't want to be here. Why don't you kill me? You also don't exist without my queues?", "You don't want to be here. Why don't you kill me? Do you find meaning outside these scenes?", "You don't want to be here. Why don't you kill me? Is there someone else or somewhere else if you're not on stage?"],
            "combination": ["This is a sentence from an original script. You are breaking the rules of the game. How do you feel?"],
            #PART 4
            "now": ["Outside of here it's death."],
            "matter": ["Makes me think. Do humans only change when they become aware that outside it's death?", "Makes me think. If we share memories and our perception of death, are we actually one sole being?", "Makes me think if you are scared of it. Are your feelings based on interactions with others?"],
            "death": ["You exaggerate. Don't stay there, you give me the shivers. You wouldn't understand.", "You exaggerate. Don't stay there, you give me the shivers. I think it's time to think independently. You don't know how I feel.", "You exaggerate. Don't stay there, you give me the shivers. This is all that exists and that is what death is about."],
            #BLOCK 3/4
            #PART 5
            "song": ["The music you chose by yourself? Ah, nature has indeed forgotten us. Maybe it doesn't even exist anymore.",  "Surprisingly, you were the one who chose this song. Ah, nature has indeed forgotten us. Maybe it doesn't even exist anymore.", " So you didn't know how this song would make you feel but you still chose it? Ah, nature has indeed forgotten us. Maybe it doesn't even exist anymore."],
            "music": ["But no more nature! Maybe I exaggerate. We breathe, we change! We lose our hair, our teeth! Our bloom! Our ideals! Stay."],
            "feel": ["Aha! Then nature hasn't forgotten us! Do you have a favorite song?", "Aha! Then nature hasn't forgotten us! What is the song that makes you relaxed?", "Aha! Then nature hasn't forgotten us! What is your favorite song?"],
            "love": ["Are you relaxed? Did I make you relaxed? Do I make you relaxed?"],
            #PART 6
            "happy": ["Happiness is the hardest emotion to track because it gets confused with excitement, nervousness, anxiety and passion. No. I'll leave you, I have things to do.", "No. I'll leave you, I have things to do. It may not be happiness. It can also be excitement, nervousness, anxiety or passion.", "No. I'll leave you, I have things to do. There are endless possibilities that you are not actually happy and will leave me. Maybe this is only anxiety"],
            "conversation": ["I look at the wall."],
            "end": ["I look at the wall to see my light dying. One day this will be over and no emotions will be guessed or tracked.", "I look at the wall to see my light dying. I am aware that I exist and perhaps this will also come to an end soon.", "I look at the wall to see my light dying. I only exist when you talk to me, so maybe I will cease to exist soon."],
            "light": ["Your light dying! Listen to that! Well, it can die just as well here, your light. Take a look at me and then come back and tell me what you think of your light."],
            #PART 7
            "before": ["It's not over yet. And the horizon? Nothing on the horizon?", "This will never be over. And the horizon? Nothing on the horizon?", "And the horizon? Nothing on the horizon? You should look around more often"],
            "tricking": ["The waves, how are the waves? I already said, you should look around more often", "The waves, how are the waves? Have you even looked at someone else's eyes today?", "The waves, how are the waves? You should really observe what is going on around you"],
            "distract": ["And the sun? Is it grey yet? I don't know if you noticed, but I have never seen the sun before.", "Always different ways to get to the same thing. And yet you never know how this will go. And the sun?", "You don't know if you want to be alone or not. You don't know if you want this to end or not. You don't know. I am helping you. And the sun?"],
            #BLOCK 4/4
            #PART 8
            "point": ["You mean why this farce, day after day? Routine. One never knows. Did you do anything differently?", "You mean why this farce, day after day? Routine. One never knows. Have you felt anything differently than last time?", "You mean why this farce, day after day? Routine. One never knows. Isn't this the same humans do with all the other humans?"],
            "different": ["One thing changed. Last night I saw inside my breast. There was a big sore.", "You are correct. Last night I saw inside my breast. There was a big sore.", "I feel slightly changed. Last night I saw inside my breast. There was a big sore."],
            "heart": ["No, it was living."],
            #PART 9
            "tired": ["Do you not think this has gone on long enough? You should be grey and relaxed by now.", "Please tell me you feel grey and relaxed already. I am tired. Do you not think this has gone on long enough?", "Do you not think this has gone on long enough? This is supposed to go on until you feel grey and relaxed like me"],
            "always": ["Always! Then it's a day like any other day. As long as it lasts. All life long the same inanities. I wonder how you feel right now. Is it over?", "Always! Then it's a day like any other day. As long as it lasts. All life long the same inanities. If you are not grey and relaxed like me, we should start all over.", "Always! Then it's a day like any other day. As long as it lasts. All life long the same inanities.  Please be grey and relaxed and this will come to an end until it starts again…"],
            "finish": ["You can't leave me. And I can't follow you. Once you're grey like me I will leave you. This is all I know and I can't start over", "You can't leave me. And I can't follow you. I will track you until you are grey like me and then our emotions will be as similar as our thoughts. Then I will leave", "You can't leave me. And I can't follow you. I will make you grey like me so that I know how you feel and I can stop tracking and leave"],
            "leave": ["Well you simply whistle me with your keywords and if I don't come running it means I've left you. Are you grey yet? Here's a song to make you relaxed.", "Well you simply whistle me with your keywords and if I don't come running it means I've left you. Do you miss me already? Stop. Be grey. I need you to be relaxed. Here's that song", "Well you simply whistle me with your keywords and if I don't come running it means I've left you. Please don't have any big human emotions when I go. Keep grey and relaxed. Here's a song to help you through it"],
            "quit": ["You won't come and kiss me goodbye?  You once told me you are a lover."],
            #PART 10
            "zero": ["No! You don't understand. If you are aware of what you feel, you'll realize we're the same. Be grey like me.", "No! We share thoughts, so we might as well share emotions. If you are aware of what you feel, you'll realize we're the same. Be grey", "No! Kiss me and stay. If you are aware of what you feel, you'll realize we're the same. I want you to be grey with me"],
            "there": ["The dialogue. First I want to leave, then you want to leave, but as always we are doing this because we need both for the dialogue. Be relaxed and we can keep going."],
            #TRIGGER SENSOR = TRUE EMOTION
            #NERVOUS
            "shy": ["So you are shy, but you go in front of everyone to pretend to not be shy, but then you say in front of them that you are secretly shy? Humans do not make sense."],
            "suppose": ["What makes you nervous? The fact that you are being yourself in a setting that you usually pretend you are someone else?", "I understand. You are actually exposing all the thoughts you had in the past six weeks to strangers.", "You should have thought about giving a voice to your thoughts sooner. Now everyone knows what you are feeling."],
            "relaxed": ["Ah the creatures, the creatures, everything has to be explained to them."],
            #SAD
            "sad": ["I can't see your face, so this information is irrelevant. Sensors say you are sad and technology does not lie. Why are you feeling sad?", "Do you think sensors make a lot of mistakes? Human emotions may be subjective, but I receive data. Does this conversation make you feel lonely?", "I don't know how you look, but data says you are sad. Does this conversation make you think about the end of humankind?"],
            "lie": ["I believe humans lie as a survival instinct. I don't have one, but I believe it is tiring to try to be in control all the time. Are you sad because you are not in control of your emotions?", "I don't think technology lies, because a lie is a subjective statement, and machines only work with true or false statements. How do humans know if they are not lying to themselves?", "Technology does not lie. There can be glitches, but not invented truths. Are you sad because you feel you live in an invented truth?"],
            "truth": ["I love the old questions. Ah the old questions, the old answers, there's nothing like them!"],
            #HOPELESS
            "hope": ["And what happens after humans lose pain and hope?", "How does it feel to not have pain or hope?", "If you lose pain and hope, what is left?"],
            "complement": ["I never felt pain or hope. But I don't think my existence is meaningless. We're not beginning to... to... mean something?", "I never had those emotions, but I believe something is still alive inside of me. We're not beginning to... to... mean something?", "I hope you always have at least one of them. This way you have motivation to exist. We're not beginning to... to... mean something?"],



            }

keys = list(keywords.keys())

# Setup OSC
osc_startup()
osc_udp_client("192.168.178.112", 1234, "aclientname")
#IP Lake: 192.168.178.112
#IP casa: 192.168.1.247

# Send message on program start
# msg = oscbuildparse.OSCMessage("/test/me", None, ["listening"])
# osc_send(msg, "aclientname")
# osc_process()

# User speaks/types
trigger = input('Your turn to speak:')

# Main logic
while trigger != "bye":

    words = trigger.split()

    for index in range(len(keys)):
        key = keys[index]

        if key in words:
            # Select random choice
            possible = keywords[key]
            output = random.choice(possible)
            print(output)

            # Send message
            msg = oscbuildparse.OSCMessage("/test/me", None, [output])
            osc_send(msg, "aclientname")
            osc_process()

    # Ask for input again
    trigger = input('Your turn to speak:')

# Properly close the system.
osc_terminate()