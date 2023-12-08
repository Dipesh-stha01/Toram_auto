import pyautogui as pag
import time


max_create_count = 15

time.sleep(5)

while (True):
    
    pag.moveTo(x=2981, y=638, duration=1)
    pag.click(x=2981, y=638)
    time.sleep(1)
    
    pag.moveTo(x=2930, y=222, duration=1)
    pag.click(x=2930, y=222)
    time.sleep(1)
    
    pag.moveTo(x=2268, y=697, duration=1)
    pag.click(x=2268, y=697)
    time.sleep(1)
    
    pag.moveTo(x=2669, y=699, duration=1)
    pag.click(x=2669, y=699)
    time.sleep(4.5)
    
    
    pag.moveTo(x=2669, y=699, duration=1)
    pag.click(x=2669, y=699)
    time.sleep(3)
    

    max_create_count = max_create_count -1
    print(max_create_count)
    
    if(max_create_count <=1):
       break