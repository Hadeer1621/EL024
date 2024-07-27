import subprocess
import pyautogui 
import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import sys
import time


# main class to chooose between english or arabic language 

class main:


    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()


    def Record_Audio(self,prompt = None):
        if prompt:
            self.speak(prompt)
        with sr.Microphone() as source:
            print("listening........")
            self.speak("listening....")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        return audio

    #=================================================================

    def Reconize_speech(self,audio):
        try:
            command = self.recognizer.recognize_google(audio)
            print(f"You said: {command}")
            self.speak(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            self.speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            self.speak("Sorry, my speech service is down.")
            return None
    
    #=================================================================
    
    def speak(self, text):
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait() 
    #======================================================================

    def pre_main(self):
        self.speak("Which language would I speak: English or Arabic?")
        text = None
        while not text:
            audio = self.Record_Audio()
            text = self.Reconize_speech(audio)
            if not text:
                self.speak("Sorry, I couldn't understand the language. Please try again.")
        
        if text.lower() == "english":
            self.open_terminal_and_run_command("python3  Alexa_en.py")
        elif text.lower() == "arabic":
            self.open_terminal_and_run_command("python3  Alexa_ar.py")
        else:
            self.speak("Sorry, I can't understand what you said. Please try again.")
            self.pre_main()  # Recursively call the function again to retry

    def open_terminal_and_run_command(self, command):
      subprocess.run(['gnome-terminal', '--', 'bash', '-c', command + '; exec bash'])
      #self.speak(f"The terminal is open and the command '{command}' is being executed.")
      sys.exit()




def Sec_main():
   assistant = main()
   assistant.speak("welcome to voice assistant Alexa")
   assistant.pre_main()
      
if __name__ == "__main__":
    Sec_main()




