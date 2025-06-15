import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Initialize Gemini API
genai.configure(api_key="Enter here")  # Replace this

model = genai.GenerativeModel("gemini-2.0-flash")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is not available.")
        return ""

def ask_gemini(question):
    response = model.generate_content(question)
    return response.text

def main():
    while True:
        query = listen()
        if query:
            if 'exit' in query or 'stop' in query:
                speak("Goodbye!")
                break
            response = ask_gemini(query)
            print(f"🤖 Gemini: {response}")
            speak(response)

main()
