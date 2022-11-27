from __future__ import print_function
from desktopmagic.screengrab_win32 \
import(getDisplayRects,getRectAsImage)
from datetime import *
from PIL import Image
import os, win32gui, win32con

os.system("mode con cols=50 lines=7")
conWin = win32gui.GetForegroundWindow()

screens=(getDisplayRects())

day = datetime.now().date().strftime('%A')
myDate = date.today()
hour = datetime.now().time().hour
minute = datetime.now().time().minute
days = ['Saturday', 'Sunday', 'Tuesday']

if day == 'Monday':
    subject = 'HM12'

if day == 'Wednesday':
    subject = 'PIMC' if hour <= 12  else 'GS'

if day == 'Thursday':
    subject = 'HM11'

if day == 'Friday':
    subject = 'HM10' if hour <= 12  else 'FL1'

if day in days:
    subject = input('Subject: ')

while True: 
    print(f'\nSubject => {subject}')
    print('\n### Full Screen Capture ###')
    print('### Type "quit" or "exit" to quit ###\n')
    while True:
        screen = ['0', '1']
        myScreen = input('Which Screen? (0 or 1) > ')
        if myScreen not in screen:
            if myScreen.upper() == 'QUIT' or myScreen.upper() == 'EXIT':
                quit()
            print('### Input only 0 or 1 ###')
        else:
            myScreen = int(myScreen)
            break

    while True:
        labels = {'1':'Time In', '2':'Time Out'}
        timeInOut = input('(1)Time in, (2)Time out: ')
        if timeInOut.upper() == 'QUIT' or timeInOut.upper() == 'EXIT':
            quit()
        if timeInOut not in labels:
            print('### Input only 1 or 2 ###')
        if timeInOut == '1':
            phrase = labels[timeInOut]
            break
        if timeInOut == '2':
            phrase = labels[timeInOut]
            break

    path = rf'G:/JOHN/APCSM/3rd Year 1st Sem/{subject}/Attendance/{myDate}'
    if not os.path.exists(path):
        os.makedirs(path)

    win32gui.ShowWindow(conWin, win32con.SW_HIDE)

    rect = getRectAsImage(screens[myScreen])
    rect.save(rf'{path}/{phrase}.png', format='png')

    win32gui.ShowWindow(conWin, win32con.SW_SHOW)

    while True:
        choices = ['I', 'F', 'Q']
        dir = os.path.realpath(path)
        viewFile = input('(I)Open image, (F)View folder, (Q)Exit: ')
        vf = viewFile.upper()

        if vf == 'QUIT' or vf == 'EXIT':
            quit()
        if vf == choices[0]:
            im = Image.open(rf'{path}/{phrase}.png')
            im.show()
        elif vf == choices[1]:
            os.startfile(dir)
        elif vf == choices[2]:
            break
        else:
            print('### Input I, F, or Q only ###')
