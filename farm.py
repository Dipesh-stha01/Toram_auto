import pyautogui as pag
import time
import schedule


def summon():
    pag.press('4')
    time.sleep(0.5)
    pass

while True: 
    
    # schedule.every(3.5).minutes.do(summon)
    # schedule.run_pending()
    # time.sleep(1)
    reduced_mana = 20
    pag.press('f')
    time.sleep(0.5)
    pag.press('3')
    reduced_mana = reduced_mana - 1
    time.sleep(5.5)
    
    if( reduced_mana < 2 ):
        pag.press('q')
        time.sleep(1)
        pag.press('e')
        time.sleep(1)
        reduced_mana = 20
     
        
    
    