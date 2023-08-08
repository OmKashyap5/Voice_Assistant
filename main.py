from open_file import fileopen
import speech_recognition as sr
import os
import pyttsx3  #voice response
# import shutil   #copy            #unins     #add copy parts
# import pyautogui#mouse clicks    #unins     #add select and open
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
# def custom_command_handler(command):
#     if "open" in command:
#         # Logic to open an application or perform an action
#         print("Opening application...")
#     elif "close" in command:
#         # Logic to close an application or perform an action
#         print("Closing application...")
#     else:
#         print("Command not recognized.")
# def custom_command_handler(command):
#     if "open directory" in command:
#         # Logic to open a directory
#         directory_name = command.replace("open directory", "").strip()
#         try:
#             os.startfile(directory_name)  # For Windows
#             # You can use other methods for opening directories depending on the OS you are using.
#             # For macOS, you can use `subprocess.call(["open", directory_name])`
#             # For Linux, you can use `subprocess.call(["xdg-open", directory_name])`
#             speak(f"Opening directory: {directory_name}")
#         except Exception as e:
#             print(f"Error opening directory: {e}")
#     elif "open file" in command:
#         # Logic to open a file
#         file_name = command.replace("open file", "").strip()
#         try:
#             os.startfile(file_name)  # For Windows
#             # You can use other methods for opening files depending on the OS you are using.
#             # For macOS, you can use `subprocess.call(["open", file_name])`
#             # For Linux, you can use `subprocess.call(["xdg-open", file_name])`
#             speak(f"Opening file: {file_name}")
#         except Exception as e:
#             print(f"Error opening file: {e}")
#     elif "close" in command:
#          # Logic to close an application or perform an action
#          print("Closing application...")
#     else:
#         print("Command not recognized.")

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
    # recognizer = sr.Recognizer()

    # with sr.Microphone() as source:
    #     print("Say something...")
    #     recognizer.adjust_for_ambient_noise(source)
    #     audio = recognizer.listen(source)

    # try:
    #     recognized_text = recognizer.recognize_google(audio)
    #     print("You said:", recognized_text)
    #     custom_command_handler(recognized_text.lower())
    # except sr.UnknownValueError:
    #     print("Could not understand audio.")
    # except sr.RequestError as e:
    #     print(f"Error during request to Google Web Speech API: {e}")





    recognizer = sr.Recognizer()
    a=0
    # Voice activation: Listen for the wake word "rex"
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
    print(a)
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
                        # audio = recognizer.listen(source,timeout=5)
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
                            if "open file" in recognized_text.lower():
                                # fileopen(recognized_text.lower())
                                fileopen(recognized_text.lower())
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
        







    # try:
    #     detected = recognizer.recognize_google(wake_audio)
    # except sr.RequestError as e:
    #     print(f"Error during request to Google Web Speech API: {e}")

    # if detected.lower()=="rex":
    #     with sr.Microphone() as source:
    #         print("Wake word 'rex' detected. Listening for commands...")

    #         recognizer.adjust_for_ambient_noise(source)
    #         audio = recognizer.listen(source,timeout=5)

    #     try:
    #         recognized_text = recognizer.recognize_google(audio)
    #         print("You said:", recognized_text)

    #         if "copy file" in recognized_text.lower():
    #             file_name = recognized_text.lower().replace("copy file", "").strip()
    #             perform_copy_file(file_name)
    #         elif "paste to" in recognized_text.lower():
    #             destination_folder = recognized_text.lower().replace("paste to", "").strip()
    #             perform_paste_to_destination(destination_folder)
    #         else:
    #             print("Command not recognized.")
    #         break  # Break the loop if a command is received
    #     except sr.UnknownValueError:
    #         pass  # Ignore unknown speech input
    #     except sr.RequestError as e:
    #         print(f"Error during request to Google Web Speech API: {e}")

    #     # if time.time() - start_time >= 5:
    #     #     print("Timeout. No command received.")
    # else:
    #     print("Wake word not detected.")


if __name__ == "__main__":
    main()