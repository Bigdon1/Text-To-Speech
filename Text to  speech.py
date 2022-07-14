import pyttsx3

engine = pyttsx3.init()

for voice in engine.getProperty("voices"):
    print(voice)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 140)

def Speak(Audio):
    engine.say(Audio)
    engine.runAndWait()

text = input("Enter your text here: ")

Speak(text)