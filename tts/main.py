
import pyttsx3 as tts
engine = tts.init()

rate = engine.getProperty('rate')
print(rate)

voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)
    print(voice.id)
    engine.say('The quick brown fox jumped over the lazy dog')
engine.runAndWait()