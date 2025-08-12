import os
import time
import argparse
import tempfile

import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound


def translate(text: str, target_language: str) -> str:
    """Translate text to the target language using googletrans.

    Args:
        text: The input text to translate.
        target_language: Language code to translate into (e.g., 'zh-CN').
    Returns:
        Translated text as a string.
    """
    translator = Translator()
    result = translator.translate(text, dest=target_language)
    return result.text


def speak(text: str, language: str) -> None:
    """Convert text to speech and play it.

    Args:
        text: Text to be spoken.
        language: Language code for pronunciation (e.g., 'yue' or 'zh-cn').
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts = gTTS(text=text, lang=language)
        tts.save(fp.name)
        playsound(fp.name)
        os.unlink(fp.name)


def listen(language: str) -> str:
    """Listen from the microphone and return the recognized text.

    Args:
        language: Expected language code for recognition
                 (e.g., 'yue-Hant-HK' for Cantonese, 'zh-CN' for Mandarin).
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio, language=language)
    except sr.UnknownValueError:
        return ""


def main() -> None:
    parser = argparse.ArgumentParser(description="Real-time translator between Cantonese and Mandarin")
    parser.add_argument(
        "--direction",
        choices=["cantonese_to_mandarin", "mandarin_to_cantonese"],
        default="cantonese_to_mandarin",
        help="Translation direction",
    )
    args = parser.parse_args()

    if args.direction == "cantonese_to_mandarin":
        source_lang_rec = "yue-Hant-HK"
        target_lang_trans = "zh-CN"
        target_lang_speech = "zh-cn"
    else:
        source_lang_rec = "zh-CN"
        target_lang_trans = "yue"
        target_lang_speech = "yue"

    while True:
        text = listen(source_lang_rec)
        if not text:
            print("No speech detected, retrying...")
            continue
        print(f"You said: {text}")
        translated = translate(text, target_lang_trans)
        print(f"Translated: {translated}")
        speak(translated, target_lang_speech)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
