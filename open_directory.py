import os
import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def find_directory_path_by_name(directory_name):
    for root, dirs, files in os.walk("/"):
        if directory_name in dirs:
            return os.path.join(root, directory_name)
    return None
def directoryopen(command):
    directory_name = command.replace("open directory", "").strip()
    directory_path=find_directory_path_by_name(directory_name)
    if directory_path:
        try:
            os.startfile(directory_path)    # For Windows
                                            # For macOS, you can use `subprocess.call(["open", file_name])`
                                            # For Linux, you can use `subprocess.call(["xdg-open", file_name])`
            speak(f"Opening directory: {directory_name}")
        except Exception as e:
            speak(f"Error opening directory: {e}")
    else:
        speak("not found")