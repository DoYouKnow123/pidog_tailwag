from pidog.stt import Vosk
import os
from pidog import Pidog
import time
from pidog.tts import Piper

tts = Piper()


vosk = Vosk(language="en-us")

print(vosk.available_languages)
my_dog = Pidog()

while True:
        print("Say something")
        result = vosk.listen(stream=False)
        if (result.find("move your tail") == 0):
                print("You said wag your tail!!!")
                print(tts.available_countrys())
                print(tts.available_models('en_us'))
                tts.set_model("en_US-ryan-low")
                tts.say("You said to wag my tail. Here goes...")
                my_dog.head_move([[0, 0, -30]], speed=80)
                wag_tail_actions = [
                [-30], [30],
                ]
                n=0
                while n<20: 
                        n+=1
                        my_dog.tail_move(wag_tail_actions, speed=100)
                        my_dog.wait_tail_done()
        print (result)





