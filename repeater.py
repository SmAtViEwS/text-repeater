# text repeater #

import time
import numbers
import os
os.system('pip install pyfiglet==0.7')
from pyfiglet import Figlet


figlet = Figlet(font="Standard")
print(figlet.renderText("SmAtViEwS"))

txt = "SMART VIEWS TEXT REPEATER"
print(txt)
print("   ")

def main():
    ask = input('ENTER A TEXT :-')
    cmd = int(input('ENTER A NUMBER :-'))

    while True:
        for i in range(cmd):
            time.sleep(0.2)
            print(ask)

        input('Press Enter to continue...')


        try:
            user_input = input('Do you want to restart? (y/n)')
        except ValueError:
            print('Invalid input. Please try again.')
            continue

        if user_input == 'y':
            continue
        else:
            break

if __name__ == '__main__':
    while True:
        main()
        input('Press Enter to restart the program...')
