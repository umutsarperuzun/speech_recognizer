import speech_recognition as sr

# Create a recognizer
recognizer = sr.Recognizer()

# Get the voice input
with sr.Microphone() as source:
    print("You can start talking now...")
    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

    try:
        # Use Google's speech recognition
        text = recognizer.recognize_google(audio, language="en-EN")
        print("Recognized:", text)

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")

    except sr.RequestError:
        print("Could not connect to the service.")

# Save the recognized text to a file
with open("output_file.txt", "a") as file:
    file.write(text + "\n")
