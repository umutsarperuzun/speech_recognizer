# 🎙️ Voice Recognition with Python

This project is a simple speech-to-text application using Python and the `speech_recognition` library. It captures audio from your microphone, converts it into text using Google's Speech Recognition API, and saves the recognized text into a file.

## 📦 Requirements

Make sure you have the following installed:

- Python 3.x  
- `speechrecognition`  
- `pyaudio` (for microphone input)

You can install the dependencies using pip:

```bash
pip install SpeechRecognition
pip install pyaudio
```

> Note: Installing `pyaudio` may require additional setup depending on your OS. For Windows, you can use a precompiled wheel.

## 🚀 How It Works

1. The script activates your microphone.
2. It listens for your voice input (max 10 seconds).
3. Converts the speech to text using Google Web Speech API.
4. Prints the recognized text.
5. Appends the text to a file called `output_file.txt`.

## 🧠 Sample Usage

Run the script with Python:

```bash
python your_script_name.py
```

Speak clearly when prompted. If the recognition is successful, your speech will be printed and saved to `output_file.txt`.

## ⚠️ Error Handling

- If the speech is not understood, it shows:  
  `"Sorry, I couldn't understand what you said."`
- If the API request fails (e.g., no internet), it shows:  
  `"Could not connect to the service."`

## 📁 Output

Recognized text is saved in:
```
output_file.txt
```
Each new line corresponds to a new recognition session.

## 📄 License

This project is open-source and free to use.

