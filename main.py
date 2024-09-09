import pyttsx3

if __name__ == '__main__':
    print("Robo speaker")
    while(True):
        x = input("Enter what you want to pronounce: ")
        if(x=="q"):
            break
        # Initialize the speaker engine
        engine = pyttsx3.init()

        # Set properties (optional)
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

        # Speak the input
        engine.say(x)
        engine.runAndWait()

