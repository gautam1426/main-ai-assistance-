import speech_recognition as sr
import pyttsx3
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize pyttsx3
engine = pyttsx3.init()

# Get API key from environment
openai.api_key = os.getenv("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")

# System setup
messages = [{"role": "system", "content": "You are Miku, an anime-style virtual assistant. Speak in a cute, friendly tone and keep responses concise (1-2 lines)."}]

def configure_anime_voice():
    voices = engine.getProperty('voices')
    
    # Try to find a high-pitched, female English voice (closest to anime style)
    preferred_voices = [
        'english-us', 'english_rp', 'english_wmids',  # Common English voices
        'zira', 'hazel', 'eva'  # Some female voice names
    ]
    
    for voice in voices:
        voice_id = voice.id.lower()
        # Check if voice is female and English
        if ('female' in voice_id or 
            any(v in voice_id for v in ['zira', 'hazel', 'eva']) or
            'english' in voice_id):
            engine.setProperty('voice', voice.id)
            print(f"Selected voice: {voice.name}")
            break
    
    # Configure for anime-style speech
    engine.setProperty('rate', 160)  # Slightly faster for energetic character
    engine.setProperty('volume', 0.9)  # Slightly lower volume
    engine.setProperty('pitch', 150)  # Higher pitch for anime girl voice

def get_response(user_input):
    try:
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        ChatGPT_reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        return ChatGPT_reply
    except Exception as e:
        return f"Gomen nasai! I encountered an error: {str(e)}"

def listen_for_trigger():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.dynamic_energy_threshold = 3000
        
        try:
            print("Listening for 'Miku'...")
            audio = recognizer.listen(source, timeout=5.0)
            text = recognizer.recognize_google(audio).lower()
            print(f"Heard: {text}")
            return "miku" in text
        except sr.UnknownValueError:
            print("Didn't understand audio")
            return False
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return False
        except sr.WaitTimeoutError:
            print("Listening timed out")
            return False

def main():
    print("Starting Miku Virtual Assistant!")
    print("Say 'Miku' to activate me!")
    configure_anime_voice()
    
    # Test voice
    engine.say("Konichiwa! I'm Miku, your virtual assistant!")
    engine.runAndWait()
    
    while True:
        if listen_for_trigger():
            try:
                print("Miku detected! Listening for question...")
                engine.say("Yes? How can I help?")
                engine.runAndWait()
                
                with sr.Microphone() as source:
                    audio = sr.Recognizer().listen(source, timeout=5.0)
                    question = sr.Recognizer().recognize_google(audio)
                    print(f"Question: {question}")
                    
                    response = get_response(question)
                    print(f"Response: {response}")
                    
                    # Add some anime-style expressions randomly
                    expressions = ["", "Hai! ", "Eto... ", "Nano desu! "]
                    import random
                    final_response = random.choice(expressions) + response
                    
                    engine.say(final_response)
                    engine.runAndWait()
            except Exception as e:
                print(f"Error in main loop: {e}")
                engine.say("Sumimasen! I didn't catch that.")
                engine.runAndWait()

if __name__ == "__main__":
    main()
