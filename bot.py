# before you run the app go to any of your chats on any social media platform and press on the chat area

import time 
import pyautogui as pg

massage = input("Enter the massage: ")

num = int(input("Enter the number of massages you want to send: "))

time.sleep(3)     

for i in range(num):
    pg.write(massage)
    pg.press('enter')
    time.sleep(1)
    
