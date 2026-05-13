# from gtts import gTTS
# import os
# import time


# def generate_voice_summary(text: str, language: str = "English") -> str:
#     if not text or not text.strip():
#         return ""

#     os.makedirs("outputs", exist_ok=True)

#     lang_code = "hi" if language.lower() == "hindi" else "en"

#     filename = f"outputs/voice_summary_{int(time.time())}.mp3"

#     tts = gTTS(text=text[:4000], lang=lang_code)
#     tts.save(filename)

#     return filename
import os
import time
import pyttsx3


def generate_voice_summary(text: str, language: str = "English") -> str:
    try:
        if not text or not text.strip():
            return None

        os.makedirs("outputs", exist_ok=True)

        filename = f"outputs/voice_summary_{int(time.time())}.mp3"

        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1.0)

        # Short text only, otherwise it may take long
        short_text = text[:1800]

        engine.save_to_file(short_text, filename)
        engine.runAndWait()

        return filename

    except Exception as e:
        print("Voice generation error:", e)
        return None