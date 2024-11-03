import pyttsx3 as py

names = []
while True:
    name = input("Enter A Name For Shoutout And 0 For Quit: ")
    if name == '0':         #when you are quit the program then shout out the names
        break
    names.append(name)

for name in names:
    engine = py.init()
    engine.say(f"Shoutout to {name}")
    engine.runAndWait()
