import pyautogui
import pyttsx3
# import webbrowser
import subprocess
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def google_search(command):
    command = command.replace("google", "").strip()
    speak(f"searching: {command}")
    command=command+".com"
    subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe",command])