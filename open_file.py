import os
import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def find_file_path_by_name(file_name):
    for root, dirs, files in os.walk("/"):
        if file_name in files:
            return os.path.join(root, file_name)
    return None
def fileopen(command):
    file_name = command.replace("open file", "").strip()
    file_path=find_file_path_by_name(file_name)
    if file_path:
        try:
            os.startfile(file_path) # For Windows
                                    # For macOS, `subprocess.call(["open", file_name])`
                                    # For Linux, `subprocess.call(["xdg-open", file_name])`
            speak(f"Opening file: {file_name}")
        except Exception as e:
            speak(f"Error opening file: {e}")
    else:
        speak("not found")