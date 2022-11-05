import pyautogui
from colorama import init 
init(autoreset=True)
from colorama import Fore, Back, Style

class Mouse:

    def move_right(seconds_left):
        while int(seconds_left) > 0:
            seconds_left -= 1
            pyautogui.moveRel(100,0)

    def move_left(seconds_left):
        while int(seconds_left) > 0:
            seconds_left -= 1
            pyautogui.moveRel(0, 100)
    
    def click(quatity_clicks, seconds_left):
        if quatity_clicks < seconds_left or quatity_clicks > seconds_left:
            print(Fore.RED + 'ERROR ARGUMENTS IS DIFFERENT')

        while seconds_left > 0:
            seconds_left -= 1
            pyautogui.click()

