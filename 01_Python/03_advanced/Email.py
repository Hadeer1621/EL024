import pyautogui
import webbrowser
import time

# URL of your webmail login page
webmail_url = 'https://mail.google.com/'  # Replace with your webmail URL

# Image files of the elements to interact with
unread_email_image = 'unread_email.png'
mark_as_read_image = 'mark_as_read.png'

# Function to open the webmail interface
def open_webmail():
    webbrowser.open(webmail_url)
    time.sleep(10)  # Wait for the browser to open and the page to load

# Function to find and click on the first unread email
def open_first_unread_email():
    email_location = pyautogui.locateOnScreen(unread_email_image, confidence = 0.8)
    if email_location:
        pyautogui.click(email_location)
        time.sleep(3)  # Wait for the email to open
      
    else:
        print("Unread email not found.")

# Function to find and click on the mark as read button
def mark_email_as_read():
    mark_as_read_location = pyautogui.locateOnScreen(mark_as_read_image, confidence = 0.8)
    if mark_as_read_location:
        pyautogui.click(mark_as_read_location)
        time.sleep(1)  # Wait for the action to complete
    else:
        print("Mark as read button not found.")

# Main function to execute the steps
def main():
    open_webmail()
    open_first_unread_email()
    mark_email_as_read()

if __name__ == "__main__":
    main()
