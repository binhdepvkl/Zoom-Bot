# install pyautogui and keyboard using pip install command in the terminal or CMD eg:-pip install pyautogui.
import keyboard  # to make a keyboard press by the bot
import subprocess  # make the bot open a zoom app
import time  # to make the bot sleep for some time
import pyautogui  # make the bot click the butotns or enter things we tell them

meeting_id = "88334768973"  # enter your own MettingID
password = "812520"  # enter your own Meeting Password

print("Opening Zoom Application \n")  # It print the same in the console

# using subprocess to open zoom
# Popen mean popopen
subprocess.Popen("C:\\Users\\Occult\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

print("Waiting to open Zoom application\n ")
time.sleep(3)  # wait for 3 sec to open the Zoom App


print("Locating the join_a_metting button\n")
pyautogui.locateOnScreen('join_a_meeting.png')  # locates the button
pyautogui.moveTo('join_a_metting.png')  # Moves the cursor to the button
pyautogui.click()  # clicks the button.

time.sleep(3)
print("Entering the Meeting Id\n ")
pyautogui.write(meeting_id)  # enters the id that you mentioned on the top

time.sleep(3)
print("Clicking on Join Btn\n ")
pyautogui.locateOnScreen('join.png')  # locate the button
pyautogui.moveTo('join.png')  # move the curosr to join button
pyautogui.click()  # clicks the join button

time.sleep(3)
print("Entering the Meeting Password\n")
pyautogui.write(password)  # enters the password that you mentioned on the top

print("Clicking on Join Btn \n")
pyautogui.locateOnScreen('join_meeting.png')  # locate the button
pyautogui.moveTo('join_meeting.png')  # move the curosr to join button
pyautogui.click()  # clicks the join button

#
# ------------------------------------------------ THANK YOU FOR WATCHNG THE EASY WAY -----------------------------------------
# ---------------------------------------  IF YOU LIKE THIS DON'T FORGET TO LIKE AND SUBSCRIBE -----------------------------------------
