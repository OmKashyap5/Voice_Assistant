from open_file import fileopen
from open_directory import directoryopen
from search_google import google_search
from chatgpt import chat_gpt
import speech_recognition as sr
import pyttsx3  #voice response
# import shutil   #copy            #unins     #add copy parts
# import pyautogui   #mouse click & add select and open

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# def perform_mouse_click(action):
#     if "left click" in action:
#         pyautogui.click()
#         print("Performed left click.")
#     elif "right click" in action:
#         pyautogui.click(button='right')
#         print("Performed right click.")
#     else:
#         print("Command not recognized.")
# def perform_copy_file(file_name):
#     global copied_file
#     if os.path.exists(file_name):
#         copied_file = file_name
#         print(f"File '{file_name}' copied.")
#     else:
#         print(f"File '{file_name}' not found.")

# def perform_paste_to_destination(destination_folder):
#     global copied_file
#     if copied_file:
#         if os.path.exists(destination_folder):
#             shutil.copy(copied_file, destination_folder)
#             print(f"File copied to '{destination_folder}'.")
#         else:
#             print(f"Destination folder '{destination_folder}' not found.")
#     else:
#         print("No file has been copied yet.")
def main():

    recognizer = sr.Recognizer()
    a=0
    # Voice activation: Listen for the wake word "hello stephen"
    with sr.Microphone() as wake_source:
        print("Listening for wake word")
        recognizer.adjust_for_ambient_noise(wake_source)
        try:
            a=2
            wake_audio = recognizer.listen(wake_source,timeout=5)
        except sr.WaitTimeoutError:
            a=1
            print("Timeout. No speech input received.")
        except Exception as e:
            a=1
            print(f"Error during audio recording: {e}")
    if(a!=1):
        try:
            detected = recognizer.recognize_google(wake_audio)
            print(detected)
            if detected.lower()=="hello stephen":
                print("Wake word 'Hello steven' detected. Listening for commands...")
                while(True):
                    a=0
                    with sr.Microphone() as source:

                        recognizer.adjust_for_ambient_noise(source)
                        try:
                            audio = recognizer.listen(source,timeout=5)
                        except sr.WaitTimeoutError:
                            break
                            print("Timeout. No speech input received.")
                        except Exception as e:
                            a=1
                            print(f"Error during audio recording: {e}")
                    if(a!=1):
                        try:
                            recognized_text = recognizer.recognize_google(audio)
                            # print("You said:", recognized_text)
                            if "how are you" in recognized_text.lower():
                                speak("Hello. I am good. How may I help you")
                            elif "open file" in recognized_text.lower():
                                fileopen(recognized_text.lower())
                            elif "open directory" in recognized_text.lower():
                                directoryopen(recognized_text.lower())
                            elif "google" in recognized_text.lower():
                                google_search(recognized_text.lower())
                            elif "chat gpt" in recognized_text.lower():
                                chat_gpt(recognized_text.lower())
                            # elif "copy file" in recognized_text.lower():
                            #     file_name = recognized_text.lower().replace("copy file", "").strip()
                            #     perform_copy_file(file_name)
                            # elif "paste to" in recognized_text.lower():
                            #     destination_folder = recognized_text.lower().replace("paste to", "").strip()
                            #     perform_paste_to_destination(destination_folder)
                            elif "stop" in recognized_text.lower():
                                break
                            else:
                                print("Command not recognized.")
                        except sr.UnknownValueError:
                            print("Could not understand audio.")
                        except sr.RequestError as e:
                            print(f"Error during request to Google Web Speech API: {e}")

            else:
                print("Wake word not detected.")

        except sr.RequestError as e:
            print(f"Error during request to Google Web Speech API: {e}")


if __name__ == "__main__":
    main()