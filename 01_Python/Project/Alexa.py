
import speech_recognition as sr
from datetime import datetime
from datetime import date
from time import sleep
from gtts import gTTS
from plyer import notification
from googletrans import Translator , LANGUAGES
from deep_translator import GoogleTranslator
from newsapi import NewsApiClient
import pyautogui
import webbrowser
import locale
import pywhatkit
import wikipedia
import pyjokes 
import psutil
import requests
import pyttsx3
import sys
import os 
import requests
import playsound
import pygame
import tempfile
from playsound import playsound

#===========================================================
#===========================================================

class voice_assistant:

    # speak to english 

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.translator = Translator()
        self.newsapi = NewsApiClient(api_key ='970de8708f664786931839418cccbc3b')
    
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
            self.speak("Sorry, I did not understand that.",'en')
            return None
        except sr.RequestError:
            self.speak("Sorry, my speech service is down.",'en')
            return None
    
    #=================================================================
    
    def speak(self, text, lang='en'):
        if lang == 'ar':
            tts = gTTS(text=text, lang=lang)
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
                temp_filename = fp.name
                tts.save(temp_filename)
                playsound(temp_filename)
                os.remove(temp_filename)
        else:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait() 
    #======================================================================

    def Who_I_Am(self):
        return "You are the creator of this virtual assistant. your name is hadeer"
    #=================================================================================
    # to Get the time  
    def Get_time(self):
      now = datetime.now()
      current_time = now.strftime("%H:%M:%S %p")
      return current_time

    #=================================================================
    # to take the screen shot 

    def take_screenshot(self,filename = 'screenshot.png'):
        self.speak(" Okay Sir ",'en')
        # Take screenshot
        screenshot = pyautogui.screenshot()
        # Save the screenshot
        screenshot.save(filename)
        print(f"Screenshot saved as {filename}")

    #======================================================================
    # to Get the date time 
    def Get_Date_today():
         today = datetime.now()
         date = today.strftime(" %a %d %m %Y %Z")
         return date
    #====================================================================
    # play song 

    def play_song_on_spotify(self):
        self.speak("What song would you like to play on Spotify?", 'en')
        
        song_name = None
        while not song_name:
            audio = self.Record_Audio()
            song_name = self.Reconize_speech(audio)
            if not song_name:
                self.speak("Sorry, I couldn't understand the song name. Please try again.", 'en')

        self.speak(f"Playing {song_name} on Spotify", 'en')
        try:
            # Open Spotify in the browser
            webbrowser.open_new_tab("https://open.spotify.com/")
            sleep(5)  # Wait for the page to load
            pyautogui.click(88,204)
            pyautogui.press("enter")
            sleep(2)
            pyautogui.moveTo(595,154)
            pyautogui.click(595 ,154 , button = "left")
            pyautogui.press("enter")
            sleep(2)
            pyautogui.typewrite(song_name)
            pyautogui.press("enter")
            sleep(2)
            pyautogui.moveTo(804 ,499)
            pyautogui.click(804,499)
        except Exception as e:
            print(f"An error occurred: {e}")
            self.speak("Sorry, there was an error fetching the information. Please try again later.", 'en')
    
    #==========================================================================================

    #===================================================================
    # to get percentage battery
    def get_battery_percentage(self):
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery.percent
        if plugged:
         return f"Charging at {percent}%"
        else:
            return f"Discharging at {percent}%"

    #=================================================================
    # open github 
    def Open_GitHub(self):
     self.speak(" Okay Sir........open github now",'en')
     webbrowser.open_new_tab("https://github.com/")
    #======================================================================
    def open_linkedin(self):
        self.speak(" Okay Sir........open LinkedIn now",'en')
        linkedin_url = "https://www.linkedin.com"
        webbrowser.open(linkedin_url)
    #===================================================================
    # to open the terminal 
    def Open_Terminal(self):
     self.speak(" Okay Sir............open terminal now",'en')
     try:
     # Wait a short while to make sure the OS is ready to receive input
        sleep(1)
        # Press Ctrl + Alt + T
        pyautogui.hotkey('ctrl', 'alt', 't')
        print("Terminal opened.")
     except Exception as e:
        print(f"An error occurred: {e}")

 #===================================================================
    def Open_ChatGPT(self):
         self.speak('Okay Sir open chatgpt','en')
         webbrowser.open_new_tab('https://chatgpt.com/')
    #====================================================================
    # tell some jokes
    def Tell_Me_Jokes(self):
         Joke = pyjokes.get_joke(language = 'en' ,category = "all")
         print(Joke)
         self.speak(Joke,'en')
     #=================================================================
     #===================================================================================
    def search_youtube_with_voice(self):
        self.speak("What do you want to youtube ",'en')
        audio = self.Record_Audio()
        query = self.Reconize_speech(audio)
        self.speak(f"Playing {query}")
        pywhatkit.playonyt(query)
        return f"Now playing {query}"             
    #==========================================================================================
    def Tell_summary(self):
        self.speak("What do you want to summarize in Wikipedia?",'en')
        audio = self.Record_Audio()
        topics = self.Reconize_speech(audio)
        if topics is None:
            self.speak("Sorry, I couldn't understand you. Please try again.",'en')
            return
        self.speak(f"Fetching information about {topics}",'en')
        try:
            response = pywhatkit.info(topic = topics, lines=3, return_value=True)
            if response:
                print(response)
                self.speak(response,'en')
            else:
                self.speak("Sorry, I couldn't find any information on Wikipedia about that topic.",'en')
        except Exception as e:
            print(f"An error occurred: {e}")
            self.speak("Sorry, there was an error fetching the information. Please try again later.",'en')

    #==========================================================================================
    def get_weather(self):

        self.speak("Choose the city name :- ",'en')
        
        audio = self.Record_Audio()
        city_name = self.Reconize_speech(audio)

        print(f"You said: {city_name}")
        if city_name:
            self.speak(f" weather in  {city_name} ",'en')
            api_key = "fae4e4336c31fe86cbbcc17161fec8e5"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            Weather_Description = data["weather"][0]["description"]
            Temperature = data["main"]["temp"]
            Temp_Max = data["main"]["temp_max"]
            Temp_Min = data["main"]["temp_min"]
            Humidity = data["main"]["humidity"]
            wind_speed = data['wind']['speed']
            weather_report = (
            f"The weather is {Weather_Description},\n"
            f"the temperature is {Temperature}°C,\n"
            f"the maximum temperature is {Temp_Max}°C,\n"
            f"the minimum temperature is {Temp_Min}°C,\n"
            f"the humidity is {Humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
         )
            print(weather_report)
            self.speak(weather_report ,'en')
        else :
            self.speak("Sorry, I didn't catch that. Please try again." ,'en')
 #======================================================================================================
    def get_location_ip(self):
        response = requests.get("https://ipinfo.io/json").json()
        location_data = {
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country"),     
        }
        return location_data
    #=======================================================================================================

    def set_alarm(self):
         self.speak("Please tell me the hour for the alarm.", 'en')
         alarm_hour = None
         while alarm_hour is None:
            audio = self.Record_Audio()
            spoken_hour = self.Reconize_speech(audio)
            if spoken_hour:
                try:
                    alarm_hour = int(str(spoken_hour))
                    if not (0 <= alarm_hour < 24):
                        raise ValueError
                except ValueError:
                    self.speak("Sorry, I didn't understand the hour. Please say a valid hour between zero and twenty-three.", 'en')
                    alarm_hour = None
            else:
                self.speak("Sorry, I couldn't understand the hour. Please try again.", 'en')

         self.speak("Please tell me the minutes for the alarm.", 'en')

         alarm_minute = None
         while alarm_minute is None:
            audio = self.Record_Audio()
            spoken_minute = self.Reconize_speech(audio)
            if spoken_minute:
                try:
                    alarm_minute = int(str(spoken_minute))
                    if not (0 <= alarm_minute < 60):
                        raise ValueError
                except ValueError:
                    self.speak("Sorry, I didn't understand the minutes. Please say a valid number of minutes between zero and fifty-nine.", 'en')
                    alarm_minute = None
            else:
                self.speak("Sorry, I couldn't understand the minutes. Please try again.", 'en')

         alarm_time = f"{alarm_hour:02}:{alarm_minute:02}"
         self.speak(f"Setting alarm for {alarm_time}.", 'en')

         sound_file = "file.mp3"
         pygame.mixer.init()  # Initialize the mixer module
         pygame.mixer.music.load(sound_file)  # Load the sound file

         while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if current_time == alarm_time:
                print("Alarm ringing!")
                self.speak("Alarm ringing!", 'en')
                pygame.mixer.music.play()  # Play the sound
                while pygame.mixer.music.get_busy():  # Keep the script running until the sound has finished
                   sleep(1)
                break  # Exit the loop after the alarm rings
            
         
            sleep(30)  # Check every 30 seconds
    #===========================================================
    def GoogleSearch(self):
         self.speak("What do you want to search for on Google?",'en')
         audio = self.Record_Audio()
         query = self.Reconize_speech(audio)
         if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            response = f"Searching Google for: {query}"
            self.speak(response,'en')
            return response
         else:
            error_message = "Failed to capture search query"
            self.speak(error_message,'en')
            return error_message
         #=============================================================================
    
    def send_notification(self, title, message):
        notification.notify(
            title=title,
            message=message,
            timeout=10  # Duration in seconds the notification will stay on screen
        )

    def notify_me(self):
       
       title = None
       message = None
        # Loop until valid title is received
       while not title:
        self.speak("Please tell me the title of the notification.")
        audio = self.Record_Audio()
        title = self.Reconize_speech(audio)
        if not title:
            self.speak("Sorry, I couldn't recognize the title. Please try again.")
        else:
            self.speak(f"Title set to: {title}")

        # Loop until valid message is received
       while not message:
        self.speak("Please tell me the message of the notification.")
        audio = self.Record_Audio()
        message = self.Reconize_speech(audio)
        if not message:
            self.speak("Sorry, I couldn't recognize the message. Please try again.")
        else:
            self.speak(f"Message set to: {message}")

        self.speak("Now, the notification is ready.")
        self.send_notification(title, message)

    #=================================================================================
    #=================================================================================
    #==================================calcualtor====================================
    def get_number(self, prompt):
        self.speak(prompt)
        while True:
            audio = self.Record_Audio()
            text = self.Reconize_speech(audio)
            try:
                number = float(str(text))
                return number
            except ValueError:
                print("Sorry, I did not understand the number. Please say it again.")
                self.speak("Sorry, I did not understand the number. Please say it again.")
                

    def get_operator(self):
        self.speak("Please say the operator.")
        while True:
            audio = self.Record_Audio()
            operator = self.Reconize_speech(audio)
            if operator in ["plus", "minus", "times", "divided by", "add", "subtract", "multiply", "divide"]:
                return operator
            else:
                self.speak("Sorry, I did not understand the operator. Please say it again.")
                print("Sorry, I did not understand the operator. Please say it again.")

    def calculate(self, num1, operator, num2):
        if operator in ["plus", "add"]:
            return num1 + num2
        elif operator in ["minus", "subtract"]:
            return num1 - num2
        elif operator in ["times", "multiply"]:
            return num1 * num2
        elif operator in ["divided by", "divide"]:
            return num1 / num2
        else:
            self.speak("Invalid operator.")
            return None

    def voice_calculator(self):
        while True:
            num1 = self.get_number("Please say the first number.")
            operator = self.get_operator()
            num2 = self.get_number("Please say the second number.")
            
            result = self.calculate(num1, operator, num2)
            print(result)
            if result is not None:
                self.speak(f"The result is {result}")
            else:
                self.speak("I couldn't perform the calculation.")
                print("I couldn't perform the calculation.")
            # Ask if user wants to perform another calculation
            self.speak("Do you want to perform another calculation? Say 'yes' or 'no'.")
            audio = self.Record_Audio()
            response = self.Reconize_speech(audio)
            if response and response in ["no", "stop", "exit"]:
                self.speak("Goodbye!")
                break
            

    #=================================================================================================
    #================================================================================================
    def get_news(self):
        top_headlines = self.newsapi.get_top_headlines(language='en', country='us')
        articles = top_headlines['articles']
        if not articles:
            self.speak("Sorry, I couldn't fetch any news at the moment.")
            print("Sorry, I couldn't fetch any news at the moment.")
            return

        for i, article in enumerate(articles[:5], 1):  # Limit to 5 articles
            self.speak(f"News {i}: {article['title']}")
            print(f"News {i}: {article['title']}")
    
    def tell_news(self):
        self.speak("Fetching the latest news...")
        print("Fetching the latest news...")
        self.get_news()
        self.speak("That's all for now.")

    #================================================================
    def open_whatapp(self):
        webbrowser.open_new_tab("https://web.whatsapp.com/")


    def send_whatsapp_message(self, phone_number, message):
        try:
            pywhatkit.sendwhatmsg_instantly(phone_number, message, 10, True, 2)
            self.speak("Message sent successfully.")
        except Exception as e:
            self.speak(f"An error occurred: {e}")

    def voice_whatsapp_message(self):
        # Record audio for phone number
        self.speak("Please say the phone number including the country code, like plus one for US.")
        audio = self.Record_Audio()
        phone_number = self.Reconize_speech(audio)
        if phone_number:
            phone_number = phone_number.replace(" ", "").replace("plus", "+")
            print(phone_number)

        else:
            self.speak("Sorry, I couldn't get the phone number.")
            return

        # Record audio for the message
        self.speak("Please say the message you want to send.")
        audio = self.Record_Audio()
        message = self.Reconize_speech(audio)
        print(message)
        if not message:
            self.speak("Sorry, I couldn't get the message.")
            return

        # Send the WhatsApp message
        self.send_whatsapp_message(phone_number, message)


    #============================================================================================
    #============================================================================================
    def translate_text(self, text, src_lang='en', dest_lang='ar'):
        try:
            translated = self.translator.translate(text, src=src_lang, dest=dest_lang)
            return translated.text
        except Exception as e:
            self.speak(f"An error occurred during translation: {e}")
            return None

    def voice_translation(self):
        while True:
            self.speak("Please say the text you want to translate.")
            audio = self.Record_Audio("Listening for the text to translate...")
            text = self.Reconize_speech(audio)
            print(text)
            if text:
                while True:
                    self.speak("Please say the target language. For example, 'Arabic' or 'French'.")
                    audio = self.Record_Audio("Listening for the target language...")
                    target_language = self.Reconize_speech(audio)
                    print(target_language)

                    # Map target language to code
                    lang_code = self.get_language_code(target_language)
                    if lang_code:
                        translated_text = self.translate_text(text, src_lang='en', dest_lang=lang_code)
                        if translated_text:
                            self.speak(f"The translated text is: {translated_text}", lang_code)
                            print(translated_text)
                            return  # Exit after successful translation
                        else:
                            self.speak("Sorry, I couldn't translate the text. Please try again.")
                    else:
                        self.speak("Sorry, I didn't recognize the language. Please try again.")
            else:
                self.speak("Sorry, I couldn't recognize the text. Please try again.")

    def get_language_code(self, language_name):
        if language_name:
            language_name = language_name.strip().lower()
            for code, name in LANGUAGES.items():
                if name.lower() == language_name:
                    return code
        return None
    
    #===================================================================================================

    def Respond_to_Speech(self,voice_audio):
        if "hello" in voice_audio or "hi" in voice_audio or "Hi There" in voice_audio:
             self.speak("Hello sir, Tell me How can i help you ?",'en') 

        elif "who are you" in voice_audio or "what is my name" in voice_audio or "who i am" in voice_audio:
             response = self.Who_I_Am()
             print(response)
             self.speak(response,'en')

        elif "take screen" in voice_audio or " screen shot "  in voice_audio or  "photo" in voice_audio or "ScreenShot" in voice_audio:
         screen = self.take_screenshot('my_screenshot.png')
         response = f"the screenskot is take {screen}"
         print(response)
         self.speak(response,'en')
        
        elif "time" in voice_audio or "clock" in voice_audio or "time now" in voice_audio or "what is time now ?" in voice_audio:
         current_time = self.Get_time()
         response = f"The current time is {current_time}"
         print(response)
         self.speak(response,'en')
        
        elif "today"  in voice_audio or "data"  in voice_audio or "what is date"  in voice_audio or  "what is day " in voice_audio or "day" in voice_audio:
         data_time = self.Get_Date_today()
         response = f" today is {data_time}"
         print(response)
         self.speak(response,'en')
        
        elif "play" in voice_audio or "listening" in voice_audio or "music" in voice_audio or "podcast" in voice_audio:
         self.speak("Okay Sir , playing song now ",'en')
         self.play_song_on_spotify()    
        
        elif "battery"  in voice_audio or "charging " in voice_audio or "Battery percentage " in voice_audio or "what is charge device" in voice_audio:
         battery = self.get_battery_percentage()
         response = f" the percentage battery is {battery}"
         print(response)
         self.speak(response,'en')
        
        elif "git"  in voice_audio or "github"  in voice_audio or "hub" in voice_audio:
            self.Open_GitHub()
        
        elif " open terminal"  in voice_audio or  "terminal" in voice_audio or "cmd" in voice_audio:
            self.Open_Terminal()
        
        elif "chatgpt"  in voice_audio or "chat"  in voice_audio or "chat ai" in voice_audio or "gpt" in voice_audio:
            self.Open_ChatGPT()
        
        elif "linkedin" in voice_audio or "jobs" in voice_audio:
            self.open_linkedin()
        
        elif "tell me jokes"  in voice_audio or "some joke"  in voice_audio or "jokes" in voice_audio:
            self.speak(" Okay Sir...............",'en')
            response = self.Tell_Me_Jokes()
            print(response)
            self.speak(response,'en')
        elif "you tube " in voice_audio or "tube" in voice_audio or "video" in voice_audio or "channel" in voice_audio:
         self.speak("Okay Sir , Open you tube.............",'en')
         return self.search_youtube_with_voice()

        elif "weather" in voice_audio or "weather report" in voice_audio or "tell me weather"  in voice_audio or "temperature" in voice_audio:
         self.get_weather()
        
        elif "location" in voice_audio or "city" in voice_audio or "where i live?" in voice_audio:
            self.speak("OKay Sir......... I tell your location",'en')
            print(self.get_location_ip())
            self.speak(self.get_location_ip(),'en')
        elif "alarm" in voice_audio  :
            self.speak("okay sir , I will set alarm",'en')
            self.set_alarm()
        
        elif "Search" in voice_audio or "google" in voice_audio or " search google about " in voice_audio:
          self.speak("Okay sir..............",'en')
          response = self.GoogleSearch()
          self.speak(response,'en')
        
        elif "Tell me a summary" in voice_audio or "summary" in voice_audio or "intro" in voice_audio:
         self.speak("okay sir .........",'en')
         self.Tell_summary()

        elif "notification" in voice_audio or "reminder" in voice_audio:
             self.notify_me()
      
      
        elif "calculate" in voice_audio or "calculator" in voice_audio or "math" in voice_audio:
            self.speak("Okay sir.............Calculator is ready")
            self.voice_calculator()

        elif "tell me a news" in voice_audio or "news" in voice_audio or "news today" in voice_audio:
            self.speak("Okay sir ...... I will some headline news now")
            self.tell_news()
        elif "open what's app" in voice_audio or "open whats up" in voice_audio:
            self.open_whatapp()

        elif "send message " in voice_audio or " send what's up" in voice_audio or "message app" in voice_audio or "what's" in voice_audio:
            self.speak("okay sir...... what'sapp ready")
            self.voice_whatsapp_message()
        elif  "translate" in voice_audio or "translation" in voice_audio or "convert to " in voice_audio:
            self.speak("Okay sir....")
            self.voice_translation()
            
        elif "thank you" in voice_audio or "thanks" in voice_audio:
         self.speak("you welcome , any thing help you again",'en')
        
        elif "no" in voice_audio:
         self.speak("OKay Sir ... BYE BYE")
         sys.exit()
        
        elif "exit"  in voice_audio or "stop" in voice_audio or "bye" in voice_audio or "shut down" in voice_audio:
         self.speak("Okay Sir ........" ,'en')
         self.speak("GOODBYE!" ,'en')
         sys.exit()
        
        else:
         response = f" Sorry, I can't understand Please say again"
         self.speak(response ,'en')
         return None



#===============================================================================================

def main():
   assistant = voice_assistant()
   assistant.speak("Hello! how can i help you sir",'en')
   while True:
        audio = assistant.Record_Audio()
        data = assistant.Reconize_speech(audio)
        if data:
            print(data)
            assistant.Respond_to_Speech(str(data))
      
if __name__ == "__main__":
    main()
