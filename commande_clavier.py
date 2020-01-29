import time
import math
import pyautogui
import legmoves
pyautogui.PAUSE = 2.5

def clav():
    while True:
        while pyautogui.press('z'):
            legmoves.forward()
        while pyautogui.press('s'):
            legmoves.back()   
        while pyautogui.press('q'):
            legmoves.left()  
        while pyautogui.press('d'):
            legmoves.right()