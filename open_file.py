import speech_recognition as sr
import os
import pyttsx3  #voice response
# import shutil   #copy            #unins     #add copy parts
# import pyautogui#mouse clicks    #unins     #add select and open
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def find_file_path_by_name(file_name):
    for root, dirs, files in os.walk("/"):  # Start from the root directory
        if file_name in files:
            return os.path.join(root, file_name)
    return None
def fileopen(command):
    file_name = command.replace("open file", "").strip()
    print(file_name)
    file_path=find_file_path_by_name(file_name)
    print(file_path)
    if file_path:
        try:
            os.startfile(file_path)  # For Windows
            # You can use other methods for opening files depending on the OS you are using.
            # For macOS, you can use `subprocess.call(["open", file_name])`
            # For Linux, you can use `subprocess.call(["xdg-open", file_name])`
            speak(f"Opening file: {file_name}")
        except Exception as e:
            speak(f"Error opening file: {e}")
    else:
        speak("not found")