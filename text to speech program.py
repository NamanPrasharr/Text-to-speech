import pyttsx3  

engine = pyttsx3.init()  

if __name__ == '__main__':
    while True:
        print("Welcome to text-to-speech program by Naman")
        x = input("Enter what you want me to speak: ")
        if x == "q":
            engine.say("    Bye bye friend")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
