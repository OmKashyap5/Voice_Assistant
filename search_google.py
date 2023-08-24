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
    pyautogui.press('enter')