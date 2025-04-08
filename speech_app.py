import speech_recognition as sr
import datetime

def recognize_and_save(filename="output_file.txt", language="en-US", attempts=3):
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Calibrating microphone for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=2)

            for attempt in range(attempts):
                print(f"\nAttempt {attempt + 1} of {attempts}")
                print("You can start talking now...")

                try:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                    print("Processing...")

                    text = recognizer.recognize_google(audio, language=language)
                    print("Recognized:", text)

                    # Save to file with timestamp
                    with open(filename, "a", encoding="utf-8") as file:
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        file.write(f"[{timestamp}] {text}\n")

                except sr.WaitTimeoutError:
                    print("Listening timed out while waiting for phrase to start.")
                except sr.UnknownValueError:
                    print("Sorry, I couldn't understand what you said.")
                except sr.RequestError:
                    print("Could not connect to the speech recognition service.")
                except Exception as e:
                    print("An unexpected error occurred:", str(e))

    except OSError:
        print("Microphone not found or not accessible.")

if __name__ == "__main__":
    recognize_and_save()
