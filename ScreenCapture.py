from __future__ import print_function
import desktopmagic
from desktopmagic.screengrab_win32 \
import(getDisplayRects,saveScreenToBmp,getScreenAsImage,getRectAsImage,getDisplaysAsImages)
from datetime import date
from datetime import datetime
import os

os.system("mode con cols=40 lines=5")

screens=(getDisplayRects())

day = datetime.now().date().strftime('%A')
myDate = date.today()

if day == 'Monday':
    subject = 'HM9'
if day == 'Tuesday':
    subject = input('Enter Subject (1)STS, (2)REED4 > ')
if day == 'Wednesday':
    subject = input('Enter Subject (1)PEE, (2)PE4 > ')
if day == 'Thursday':
    subject = 'Laboratory'
if day == 'Friday':
    subject = input('Enter Subject (1)HM8, (2)RPH > ')

while True: 
    print('### Full Screen Capture ###')
    print('### Hit "ctrl+c" to quit ###\n')
    while True:
        try:
            myScreen = int(input('Which Screen? (0-9): '))
            break
        except ValueError:
            print('Input only numbers from 0 - 9')

    while True:
        timeInOut = int(input('(1)Time in, (2)Time out: '))
        if timeInOut == 1:
            phrase = "Time In"
            break
        elif timeInOut == 2:
            phrase = "Time out"
            break
        else:
            print('Invalid choice')

    path = rf'G:/JOHN/APCSM/2nd Year 2nd Sem/{subject}/Attendance/{myDate}'
    if not os.path.exists(path):
        os.makedirs(path)

    rect = getRectAsImage(screens[myScreen])
    rect.save(rf'G:/JOHN/APCSM/2nd Year 2nd Sem/{subject}/Attendance/{myDate}/{phrase}.png', format='png')
