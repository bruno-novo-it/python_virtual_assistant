import speech_recognition as sr
from scripts.speaker import *
from scripts.timeservice import *
from scripts.util import *
import re
import json


def is_youtube_search_action(recognized_text):
    text = recognized_text.lower() #convert everything to lower case
    return "search for" in text and "on youtube" in text

def extract_youtube_search_term(recognized_text):
    text = recognized_text.lower()
    text = text.replace("search for","")
    text = text.replace("on youtube","")
    return text.strip() #remove any leading or trailing whitespace

def main():

    tts_speaker = TTSSpeaker()
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Say something!")
            audio = recognizer.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
            audio = recognizer.listen(source)                   # now when we listen, the energy threshold is already set to a good value, and we can reliably catch speech right away

        # Speech recognition using Google Speech Recognition
        try:
            # To use your API Key use: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            recognized_text  = recognizer.recognize_google(audio)
            print("You said: " + recognized_text)
            #Here we will use simple if statements to map the captured text to appropriate actions.
            if "local time" in recognized_text:
                tts_speaker.speak(TimeService().get_local_time())
            #should open a youtube search page?, sentence to match: search for {searchterm} on youtube
            if is_youtube_search_action(recognized_text):
                open_page("https://www.youtube.com/results?search_query=" + extract_youtube_search_term(recognized_text))
            else:
                tts_speaker.speak("I am sorry. I didn't get that!. There is no procedure available to handle your request")
        except sr.UnknownValueError:
            tts_speaker.speak("I am sorry. I didn't get that!")
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            tts_speaker.speak("I am sorry. I didn't get that!")
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    main()