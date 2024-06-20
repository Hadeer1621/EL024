
# first import the module 
import webbrowser 
  
# then make a url variable 
Github_web = "https://github.com/"
Linkedin_web = "https://www.linkedin.com/"
Facebook_web = "https://www.facebook.com/"
Google_web = "https://www.google.co.uk"

# impelementation function firebox 

def firebox (fav_url):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe" 
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path)) 
    urL = ["https://www.linkedin.com/","https://www.google.co.uk","https://www.facebook.com/","https://github.com/"]
    if fav_url in urL:
        webbrowser.get('chrome').open(fav_url) 

    
