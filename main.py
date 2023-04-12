import pyautogui
import time

#How many times it will loop
trys = 5

#Picture Name
name = input("Name: ")

#Path from the image
path = "YOUR PATH TO YOUR IMAGES"

#1st Check for Buttons
target_victim = pyautogui.locateOnScreen(f"{path}\{name}.png")         ##can be added for faster work [region=(x1, y1, x2,y2)]
pyautogui.rightClick(target_victim)
call = pyautogui.locateOnScreen(f"{path}\call.png")                    ##can be added for faster work [region=(x1, y1, x2,y2)]
pyautogui.click(call)

counter=0

#If Buttons not Found it will loop until it have all data
while call is None:
    target_victim = pyautogui.locateOnScreen(f"{path}\{name}.png")    ##can be added for faster work [region=(x1, y1, x2,y2)]
    pyautogui.rightClick(target_victim)
    call = pyautogui.locateOnScreen(f"{path}\call.png")               ##can be added for faster work [region=(x1, y1, x2,y2)]
    pyautogui.click(call)

while counter < trys:
    def call_spam():
            
        #Profile RightClick
        pyautogui.rightClick(target_victim)
        print("Target Found!")
        time.sleep(1)
            
        #Click on Call
        pyautogui.click(call)
        print("Call!")
            
        #Profile RightClick
        pyautogui.rightClick(target_victim)
        print("Target Found!")
            
        #Click on Cancel
        pyautogui.click(call)
        print("Cancel Call!")
            


    counter += 1
    call_spam()
    
if(counter == trys):
    print("Finished")
