import pyautogui
import pyttsx3
import time
import pyperclip
import subprocess
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def chat_gpt(command):
    command = command.replace("chat gpt", "").strip()
    speak(f"searching: {command}")
    pyperclip.copy(command)
    subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe","https://chat.openai.com/"])
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'v')
    # pyautogui.write("")  # Write the URL
    pyautogui.press('enter')