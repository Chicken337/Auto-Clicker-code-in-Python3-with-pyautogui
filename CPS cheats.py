import pyautogui
pyautogui.PAUSE = 0.001
import time
print ("Get Ready!")
time.sleep (.5)
print ("go to the clicker project and click the green flag on the project")
time.sleep (1)
print ("starting code...")
time.sleep (3)
for i in range(400):
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')
print ("Done! you can now click out of the project.")
