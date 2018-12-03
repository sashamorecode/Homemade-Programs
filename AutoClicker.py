try:
    from pynput.keyboard import Key, Controller
except:
    print("install pynput , using pip command 'pip install pynput'")
    quit()
import time
import re
import sys
import os
try:
    import keyboard
except:
    print ("install keyboard , using pip command 'pip install keyboard'")
    quit()
i=0
pause = False

### START ###
time.sleep(3)

#Run Information Query
print ("Keypresser by Questwalker")
print ('\n')
keys = input ("What keys do you want to press? ")
loop = input ("Loop?(Y/N) ")
delay = input ("Delay the keypresses by? (In seconds) ")
keypresses =list (keys)
print ('\n')

#"Loop" variable Must Be True or False (Y/N)
while not loop == True:
    if loop == "Y":
        loop = True
        break
    elif loop == "y":
        loop = True
        break
    elif loop == "N":
        loop = False
        break
    elif loop == "n":
        loop = False
        break
    else:
        loop = input("Please enter a valid Loop.(Y/N) ")
    if loop == False:
        break
print("")

#Stop Loop Shortcut
if loop == True:
    pause = input("What key should be be used to stop this program? ")

#Remove Any Extra Numbers From "Delay" Variable
re.sub('[abcdefghijklmnopqrstuvwxyz]', '', delay)
delay = re.sub('[abcdefghijklmnopqrstuvwxyz]', '', delay)

#Countdown to Start Program
print ("Starting in.. 5", end="\r")
time.sleep(1)
print ("Starting in.. 4", end="\r")
time.sleep(1)
print ("Starting in.. 3", end="\r")
time.sleep(1)
print ("Starting in.. 2", end="\r")
time.sleep(1)
print ("Starting in.. 1")
time.sleep(1)

delay = float(delay)

#Loop and exit Scripts
if loop == True:
    print ("Close this program tab to leave")
    while 1 == 1:
        if i > len(keypresses)-1:
            i = 0
            time.sleep(1)

        keyboard.press(keypresses[i])
        keyboard.release(keypresses[i])
        i += 1
        time.sleep(delay)

        if keyboard.is_pressed(pause):
            break


if loop == False:
    while not i == len(keypresses):

        keyboard.press(keypresses[i])
        keyboard.release(keypresses[i])
        i += 1
        time.sleep(delay)

print ("Done!")
quit ()
