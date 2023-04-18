import sys, time, random
from datetime import datetime
import pyautogui

pyautogui.FAILSAFE = False

minutes = input("Enter number of minutes (blank defaults to 3): ")

if minutes == "":
    minutes = 3

print ("Starting mouse position: {}".format(pyautogui.position()))

while(True):
    x = 0

    while(x < int(minutes)):
        time.sleep(60)
        x += 1
    
    rando = random.randint(1, 1920)
    rando2 = random.randint(1, 1200)

    pyautogui.moveTo( rando, rando2 )

    print("{}: Mouse moved to {}".format(datetime.now().time(), pyautogui.position()))
