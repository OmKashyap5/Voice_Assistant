import pyautogui
import pyttsx3
import urllib.parse
import time
import pyperclip
# import webbrowser
import subprocess
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def google_search(command):
    command = command.replace("google", "").strip()
    speak(f"searching: {command}")
    pyperclip.copy(command)
    subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    # pyautogui.write("")  # Write the URL
    pyautogui.press('enter')



    # command = command.replace("google", "").strip()
    # speak(f"searching: {command}")
    # # command=command+".com"
    # # commnad = urllib.parse.quote(command, safe=" :/?&=")
    # # print(command)
    # # subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe",command])
    # # browser_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    # pyautogui.press("win")  # Open the Start menu
    # pyautogui.write("C:\Program Files\Google\Chrome\Application\chrome.exe")  # Type the browser path
    # pyautogui.press("enter")  # Press Enter

    # # Wait for the browser to open (adjust duration if needed)
    # time.sleep(3)

    # # Simulate typing the command in the search bar
    # pyautogui.hotkey("ctrl", "t")  # Open a new tab
    # pyautogui.write(command)  # Type the command
    # pyautogui.press("enter")  # Press Enter
    # time.sleep(5)