import pyautogui as pag
import time
import schedule


play_on = True


while True:
    
    reduced_mana =0;
    print("initial: "+ str(reduced_mana))
    
    
    
    for turn in range(3):
        pag.press('f')
        time.sleep(0.5)
        pag.press('2')
        reduced_mana = reduced_mana + 5
        time.sleep(4.5)
        print(str(turn)+") charge : "+str(reduced_mana))
        # print("After dmg: "+str(reduced_mana))
        if(reduced_mana >= 12 ):
            print("charging")
            pag.press('q')
            time.sleep(1)
            pag.press('e')
            time.sleep(1)
            reduced_mana = 0
            print("Restored: "+str(reduced_mana))    
    
    
    
    