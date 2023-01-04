import time 
import pyautogui as pg

massage = input("Enter the massage: ")

num = int(input("Enter the number of massages you want to send: "))

time.sleep(4)
for i in range(num):
    pg.write(massage)
    pg.press('enter')
    time.sleep(1)
    
