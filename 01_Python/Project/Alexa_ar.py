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
import subprocess
import arabic_reshaper
from bidi.algorithm import get_display

#====================class to speak arabic language ================================================
#===================================================================================================
#===================================================================================================

class Alexa:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.translator = Translator()
        wikipedia.set_lang("ar")
        locale.setlocale(locale.LC_ALL, 'ar_EG.UTF-8')

    def speak(self, text):
        tts = gTTS(text=text, lang="ar", slow=False)
        tts.save("audio.mp3")
        playsound("audio.mp3")
        os.remove("audio.mp3")

    def record_audio(self, prompt=None):
        if prompt:
            self.speak(prompt)
        with sr.Microphone() as source:
            print("Listening...")
            self.speak("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        return audio
    #==================================================================================
    def recognize_speech(self, audio, lang='ar-EG'):
        try:
            command = self.recognizer.recognize_google(audio, language=lang)
            print(f" انت تقول : {command}")
            self.speak(f" انت تقول {command}")
            return command.lower()
        except sr.UnknownValueError:
            self.speak("أنا آسفة لأنني لا أفهمك , قول تاني ")
            print("أنا آسفة لأنني لا أفهمك , قول تاني ")
            return None
        except sr.RequestError:
            self.speak("Sorry, my speech service is down.")
            return None
    #============================================================================================
    def print_arabic(self,text):
        reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
        bidi_text = get_display(reshaped_text) 
        print(bidi_text)
    #================================================================================
    def search_words_in_string(self, words_list, text):
        found_words = [word for word in words_list if word in text]
        return len(found_words) != 0
    #=========================================================================================
    def Who_I_Am(self):
        name = self.speak("اسمك هدير")
        print(name)
    #===============================================================================================
    def time_now(self):
        current_time = datetime.now().time()
        arabic_time = current_time.strftime('%I:%M:%S %p').replace('AM', 'صباحاً').replace('PM', 'مساءً')
        self.speak(arabic_time)
        print(arabic_time)

    #================================================================================================
    def Get_Date_today(self):
        today = datetime.now()
        date = today.strftime('%A %d/%m/%Y')        
        self.speak(date) 
    #========================================================================
    def get_battery_percentage(self):
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery.percent
        if plugged:
         return f"Charging at {percent}%"
        else:
            return f"Discharging at {percent}%"
        
    #=========================================================================================
    #=================================================================
    # open github 
    def Open_GitHub(self):
     self.speak(" حاضر يا كبير سوف افتح جيت هاب الان ")
     webbrowser.open_new_tab("https://github.com/")
    #======================================================================
    def open_linkedin(self):
        self.speak(" حاضر يا ;كبير ... سيتم فتح لينكدان الان ")
        linkedin_url = "https://www.linkedin.com"
        webbrowser.open(linkedin_url)
    #===================================================================
    # to open the terminal 
    def Open_Terminal(self):
     self.speak(" حاضر يا كبير سوف افتح ترمينال الان ")
     try:
         # Open terminal in Ubuntu
        subprocess.Popen(['gnome-terminal'])
        print("Terminal opened.")
     except Exception as e:
        print(f"An error occurred: {e}")

    #===================================================================
    def Open_ChatGPT(self):
         self.speak("حاضر يا كبير .... سوف افتح شات جي بي تي الان ")
         webbrowser.open_new_tab('https://chatgpt.com/')
    #====================================================================
    # tell some jokes
    def Tell_Me_Jokes(self):
         Joke = pyjokes.get_joke(language = 'en' ,category = "all")
         My_joke_ar= self.translator.translate(Joke,dest='ar').text
         print(My_joke_ar)
         self.speak(My_joke_ar)
    #=====================================================
    def get_weather(self):
            
            city_name = 'Cairo'
            self.speak(f" {city_name} الطقس في اليوم ")
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
                f"الطقس هو {Weather_Description},\n"
                f" درجة الحراره هي {Temperature},\n"
                f"درجة الحراره العظمى هي {Temp_Max},\n"
                f"درجة الحراره الضغرى هي {Temp_Min},\n"
                f"الرطوبه هي {Humidity}%,\n"
                f"سرعة الرياح هي {wind_speed}\n"
         )
            Weathe_ar= self.translator.translate(weather_report, dest ='ar').text
            print(weather_report)
            self.speak(Weathe_ar )
            

  
 #======================================================================================================
   
    #=======================================================================================================
     #=================================================================
    def GoogleSearch(self):
         self.speak("ماذا تريد ابحث عنه في جوجل ")
         audio = self.record_audio()
         query = self.recognize_speech(audio)
         if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            response = f"{query} البحت عن"
            response_ar = self.translator.translate(response, dest ='ar').text
            self.speak(response_ar)
            print(response_ar)
         else:
            error_message = "Failed to capture search query"
            self.speak(error_message)
            return error_message
    ##===========================================================================
    #==============================================================================================
    def Translator(self):
        self.speak(" اختر اللغة التى ستترجم منهايمكنك الإخيار بين العربية او الإنجليزية")
        while True:
            audio = self.record_audio()
            text = self.recognize_speech(audio)            
            if(text == "العربيه"):
                self.speak("اتفضل اتكلم و انا هترجم للإنجليزية")
                audio_ar = self.record_audio()
                arabic_sentence = self.recognize_speech(audio_ar)
                translated_sentence = self.translator.translate(arabic_sentence,dest="en").text
                self.speak(translated_sentence)
                break
            elif(text == "الانجليزيه"):
                self.speak("اتفضل اتكلم و انا هترجم للعربية")
                audio_en = self.record_audio()
                English_sentence = self.recognize_speech(audio_en,'en')
                translated_sentence = self.translator.translate(English_sentence,dest="ar").text
                self.speak(translated_sentence)
                break
            else:
                self.speak(" مفهمتش قول تاني")
        #=========================================================================================
    def take_screenshot(self,filename = 'screenshot.png'):
        screenshot = pyautogui.screenshot()
        # Save the screenshot
        screenshot.save(filename)
        print(f"Screenshot saved as {filename}")

        #==========================================================
    def search_youtube_with_voice(self):
        self.speak("اتفضل قول  ماذا تبخت عنه في يوتيوب ")
        audio = self.record_audio()
        query = self.recognize_speech(audio)
        pywhatkit.playonyt(query)
        return f"  تشتغل الان {query}"  
    #============================================================================

    def Tell_summary(self):
        self.speak("اتقضل ماذا تريد ان ابحت عنه في ويكبيديا")
        audio = self.record_audio()
        topics = self.recognize_speech(audio)
        if topics is None:
            self.speak("أسفة مفهمتش ممكن تقول تاني")
            return
        self.speak(f" البحث عن {topics}")
        try:
            response = pywhatkit.info(topic = topics, lines=3, return_value=True)
            if response:
                print(response)
                self.speak(response)
            else:
                self.speak("Sorry, I couldn't find any information on Wikipedia about that topic.")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.speak("Sorry, there was an error fetching the information. Please try again later.")

    #============================================================================================================

    def Send_to_whatsapp(self):
             # Ask for the phone number
        self.speak("تمام قول النمره لو سمحت")
        number = ""
        while not number.isnumeric():
            audio = self.record_audio()
            number = self.recognize_speech(audio).replace(" ", "")
            if not number.isnumeric():
                self.speak("مفهمتش قول تاني" )
    
            # Ensure the phone number starts with '0'
        if number[0] != '0':
            number = '0' + number
    
         # Ask for the message content
        self.speak("تمام قول المسدج لو سمحت")
        audio = self.record_audio()
        message = self.recognize_speech(audio)
        if  not message:
            self.speak(" أسفة , من فضلك قول  الرساله مره اخرى")
        # Send the message instantly via pywhatkit
        pywhatkit.sendwhatmsg_instantly("+2" + number, message)
            # Click on the chat and send the message
        sleep(1)  # Additional wait to ensure WhatsApp is ready
        pyautogui.click(839, 568)
        pyautogui.press('enter')

    #======================================================================
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
        self.speak(" أتفضل قولي عنوان الاشعار لو سمحت ")
        audio = self.record_audio()
        title = self.recognize_speech(audio)
        if not title:
            self.speak("أسفة مفهمتش قول مره اخرى ")
        else:
            self.speak(f"Title set to: {title}")

        # Loop until valid message is received
       while not message:
        self.speak("من فضلك قولي الرسالة لو سمحت ")
        audio = self.record_audio()
        message = self.recognize_speech(audio)
        if not message:
            self.speak("أسفة مفهمتش قول تاني ")
        else:
            self.speak(f"Message set to: {message}")

        self.speak("ألان الاشعار جاهز ")
        self.send_notification(title, message)

    #=======================================================================
    def open_gmail(self):
        self.speak("حاضر يا كبير ")
        webbrowser.open("https://mail.google.com")
        self.speak(" فتح ال جي ميل الان ")
        print("Opening Gmail inbox...")

    def SendEmail(self):
        To = None
        Subject = None
        body = None

        self.speak("يمكنك ارسال ايميل ----")
        self.open_gmail()
        sleep(3)
        pyautogui.click(43,213)
        pyautogui.press("enter")
        while not To:
            self.speak("من فضلك قول الارسال الي من الانجليزيه")
            audio = self.record_audio()
            To = self.recognize_speech(audio ,'en')
        sleep(3)
        pyautogui.moveTo(1306,458)
        pyautogui.click(1306,458)
        pyautogui.typewrite(To+"@ gmail.com")
        pyautogui.press("enter")
        self.speak(" تمام ايميل الشخص ")

        while not Subject:
            self.speak("من فضلك قولي الموضوع الان بالانجليزية")
            audio = self.record_audio()
            Subject = self.recognize_speech(audio ,'en')
        
        sleep(3)
        pyautogui.moveTo(1307,489)
        pyautogui.click(1307,489)
        pyautogui.typewrite(Subject)
        pyautogui.press("enter")
        self.speak("تمام الموضوع")

        while not body:
            self.speak(" من فضلك اخبرني محتوي ايميل ")
            audio = self.record_audio()
            body = self.recognize_speech(audio,'en')
        sleep(3)
        pyautogui.moveTo(1321,557)
        pyautogui.click(1321,557)
        pyautogui.typewrite(body)
        pyautogui.press("enter")
        self.speak(" تمام محتوي ايميل ")

        # sent
        sleep(3)
        pyautogui.moveTo(1307,980)
        pyautogui.click(1307,980)
        pyautogui.press("enter")
        self.speak(" تمام تم ارسال ايميل الان ")

    #================================================================================================
    def greet_user(self):
        # Get the current time
        now = datetime.now()
        current_hour = now.hour
        # Determine the appropriate greeting
        if 5 <= current_hour < 12:
            greeting = "  صباح الخير يومك سعيد "
            self.speak(greeting)
        elif 12 <= current_hour < 17:
            greeting = " مساء الخير لقد خان وقت الضهر "
            self.speak(greeting)
        elif 17 <= current_hour < 21:
            greeting = " مساء الخير لقد حان موعد الليل "
            self.speak(greeting)
        else:
            greeting = " تصبح علي خير احلام سعيدة"
            self.speak(greeting)
        
        return greeting


    #==========================================================================================================
     #=================================================================================================================================
    def Create_File(self):
        self.speak("من فضلك اخبرني اسم الفايل الجديد  بالانجليزية ")
        while True:
            audio = self.record_audio()
            file_name = self.recognize_speech(audio ,'en')
            if file_name == '0':
                self.speak(" أسفة مفهمتش قول تاني ")
                continue

            try:
                with open(file_name, 'a'):
                    pass  # Just to create the file without writing anything
                self.speak(f"File '{file_name}' created successfully.")
                break  # Exit the loop after successfully creating the file
            except Exception as e:
                self.speak(f"An error occurred: {e}")
                self.speak(" مفهمتش قول تاني ")

    #=========================================================================================================================================
    def ReadFile(self):
        self.speak(" من فضلك اخبرني اسم الفايل الذي تريد ان تقرا بالانجليزية ")
        while True:
            audio = self.record_audio()
            file_name = self.recognize_speech(audio,'en')
            if file_name == '0':
                pass
            else:
                break
            self.speak(" أسفة مفهمتش قول تاني ")
        
        try:
            with open(file_name, 'r') as file:
                content = file.read()
                self.speak(content)
        except FileNotFoundError:
            self.speak(f"File '{file_name}' not found.")
        except Exception as e:
            self.speak(f"حدث خطأ أثناء قراءة الملف")

  #==================================================================================================================================================
    def WriteFile(self):
        file_name = None
        lang = None
        content = None
        while not file_name:
            self.speak(" من فضلك اخبرني اسم الفايل الذي تريد انت تكتب فيه بالانجليزية")
            audio = self.record_audio()
            file_name = self.recognize_speech(audio ,'en')
        while True:    
                if file_name == '0':
                    pass
                else:
                    break
                self.speak("  أسفة مفهمتش  ملف قول تاني")

        while not lang:
                self.speak("ما اللغة الذي تريد الكتابة بيها العربية او الانجليزية")
                audio = self.record_audio()
                lang = self.recognize_speech(audio)

        if lang == "الانجليزيه":
            self.speak("Please tell me the content to write.")
            while True:
                while not content:
                            audio = self.record_audio()
                            content = self.recognize_speech(audio ,'en')
                if content == '0':
                     pass
                else:
                     break
                
                self.speak("Sorry, I can't understand what you said. Please try again.")

        elif lang == "العربيه":
                    self.speak("من فضلك اخبرني ماذا اكتب ")
                    while True:
                        while not content:
                            audio = self.record_audio()
                            content = self.recognize_speech(audio )

                        if content == '0':
                            pass
                        else:
                            break
                       
                        self.speak("أسفة مفهمتش  محتوى قول تاني ")
        else:
                    self.speak("أسفه مفهمتش اللغة قول تانى")

        try:
                with open(file_name, 'w') as file:
                    file.write(content)
                self.speak(f"المحتوى المكتوب إلى ملف' {file_name} ' بنجاح.")
        except Exception as e:
                self.speak(f"حدث خطأ أثناء الكتابة إلى الملف")
    
    #=====================================================================================
    def GetRandomQuote(self):
        self.speak("سوف اخبرك اقتباس")
        api_url = "https://api.quotable.io/random"
        response = requests.get(api_url, params={"lang": "ar"}) 
        if response.status_code == 200:
            data = response.json()
            return data.get('content', 'No quote found.')
        else:
            return 'Failed to retrieve quote.'
    
    def get_and_speak_quote(self):
        quote = self.GetRandomQuote()
        quote_ar = self.translator.translate(quote,dest='ar').text
        print(f"Quote: {quote_ar}")
        self.speak(quote_ar)

    #=========================================================================================
    def GetToDoListFromFile(self):
        try:
            with open("Todo_ar.txt", 'r') as file:
                tasks = file.readlines()

            if not tasks:
                self.speak("Your to-do list is empty.")
                return

            todo_message = "Here is your to-do list:"
            for i, task in enumerate(tasks, start=1):
                todo_message += f"\n{i}. {task.strip()}"
            self.speak(todo_message)
        except FileNotFoundError:
            self.speak("The to-do list file was not found.")
        except Exception as e:
            self.speak(f"An error occurred: {e}")


    
    #======================================================================
    def respond_to_speech(self, text):
        if self.search_words_in_string(["انا اسمي ايه","اسمي","ما اسمي"],text):
            self.Who_I_Am()
        elif self.search_words_in_string(["الوقت", "الساعه", "التوقيت الان"], text):
            current_time = self.time_now()
            response = f"{current_time} التوقيت الان "
            self.speak(response)
        elif self.search_words_in_string(["تاريخ اليوم"," اليوم ايه","النهارده ايه"],text):
            data_time = self.Get_Date_today()
            response = f"{data_time} اليوم هو "
            self.speak(response)
        elif self.search_words_in_string(["البطارية","شحن ","بطاريه","الشاحن"],text):
                  battery = self.get_battery_percentage()
                  response = f"البطارية هي : {battery}"
                  self.speak(response)
                  print(response)
        elif self.search_words_in_string(["git hub" ,"جيت هاب ","هاب" ,"جيت"],text):
                 self.Open_GitHub()
        
        elif self.search_words_in_string(["جديده","ترمنال"," ترمينال"],text):
            self.Open_Terminal()
        
        elif self.search_words_in_string(["شات جي بي تي","chat gpt"],text):
            self.Open_ChatGPT()
        
        elif self.search_words_in_string(["لينكدان" ,  "موقع الوظائف", "لينكد ان ","لينك"],text):
            self.open_linkedin()
        
        elif self.search_words_in_string(["نكته","ضحكيني","قولي نكته"],text):
            self.speak("حاضر   سيدي.......................... ")
            response = self.Tell_Me_Jokes()
            self.speak("ها ها ها ها ها ها ها ها ها ")
            print(response)

        elif self.search_words_in_string(["الطقس","درجة الحراره","ما هو الطقس الان"],text):
            self.speak("حاضر  يا كبير ")
            self.get_weather() 
       
        elif self.search_words_in_string(["ابحث في جوجل","جوجل","ابحث"],text):
            self.speak("حاضر يا كبير ")
            self.GoogleSearch()
        
        elif(self.search_words_in_string(["ترجم لي","اترجم", "ترجمه"],text)):
            self.Translator()

        elif self.search_words_in_string(["صوره", " سكرين شوت" ," سكرين"],text):
            self.speak("حاضر يا كبير  ")
            self.take_screenshot()

        elif(self.search_words_in_string(["كلميني","ويكبيديا"],text)):
            self.Tell_summary()
        
        elif(self.search_words_in_string(["يوتيوب" ,"شغل اغنيه" ,"فيديو" ,"قناة"],text)):
            self.search_youtube_with_voice()
        
        elif self.search_words_in_string(["واتساب" ,"واتس اب","وتساب"],text):
            self.speak(" حاضر يا كبير ")
            self.Send_to_whatsapp()

        elif self.search_words_in_string(["اٍشعار","ذكرني","نوتوفيكاشن"],text):
            self.notify_me()

        elif self.search_words_in_string(["ارسال" ,"ايميل"] ,text):
            self.SendEmail()

        elif self.search_words_in_string(["انشاء" ,"ملف جديد"],text):
            self.speak("حاضر يا كبير ")
            self.Create_File()
        
        elif self.search_words_in_string ([ "قراءه","اقرا ملف"],text):
            self.speak("حاضر يا كبير ")
            self.ReadFile()
        
        elif self.search_words_in_string(["اكتب"],text):
            self.speak("حاضر يا كبير ")
            self.WriteFile()
        
        elif self.search_words_in_string(["اقتباس" , "مقوله"],text):
            self.speak("حاضر يا كبير ")
            self.get_and_speak_quote()
        
        elif self.search_words_in_string(["انا هعمل ايه النهارده" , "روتين" ,"ماذا افعل "],text):
            self.speak("حاضر يا كبير ")
            self.GetToDoListFromFile()

        elif self.search_words_in_string(["تحيه" ,"كلمه حلوه"],text):
            self.greet_user()
        
        elif self.search_words_in_string(["توقف","اغلق","stop"],text):
            self.speak("حاضر يا كبير")
            self.speak(" مع السلامه")
            sys.exit()
        
        else:
            self.speak("مفهمتش، قول تاني")

#=====================================================================================================================
#=====================================================================================================================


def main():
    assistant = Alexa()
    assistant.greet_user()
    assistant.speak(" مرحبا ! كيف يمكنني مساعدتك؟ ")
    while True:
        audio = assistant.record_audio()
        data = assistant.recognize_speech(audio)
        if data:
            assistant.respond_to_speech(data)

if __name__ == "__main__":
    main()
