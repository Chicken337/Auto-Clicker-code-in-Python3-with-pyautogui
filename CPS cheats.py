import pyautogui                                        # We could also use win32api, but as you might have guessed, that only works on windows.
import keyboard                                         # For reading user inputs
import threading                                        # We are going to do the actual clicking on a seperate thread.
import time                                             # For delays
import os                                               # For shutdown

pyautogui.PAUSE = 0.001                                 # The delay between each click / 2

clickFlag = False                                       # This is the flag to determine if we should click or not.
closeFlag = False                                       # This is set to True to begin the shutdown process.



def clickLoop():                                        # Self explanatory
    global closeFlag
    while True:
        global clickFlag
        while clickFlag:
            pyautogui.mouseDown(button='left')
            pyautogui.mouseUp(button='left')
        time.sleep(0.001)
        if closeFlag:
            exit()                                      # We have to terminate the thread first.

def on_key_press(event):                                # Self explanatory
    global clickFlag
    global closeFlag
    if event.name == '[':
        if clickFlag == False:
            clickFlag = True

    if event.name == ']':
        if clickFlag == True:
            clickFlag = False

    if event.name == '-':
        closeFlag = True
        t.join                                          # Then we merge the thread with the main Python program to ensure that it is fully shut down.
        time.sleep(0.1)
        print("Shutting down...")
        os._exit(0)                                     # Then we force kill the program, to ensure we don't have any memory/CPU leaks.



print ("Booting up...")

t = threading.Thread(target=clickLoop, daemon=True)     # Initialize the Threading target.
t.start()                                               # Start the thread
keyboard.on_press(on_key_press)                         # Start listening for keypresses

print ("Done.")

keyboard.wait()                                         # Start the loop