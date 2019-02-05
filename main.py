import pyscreenshot as ImageGrab
from pyautogui import press
import time

if __name__ == '__main__':
    time.sleep(5)
    for i in range(1, 50):
    # skip 
        for j in range(1, 5):
            press('right')
        # grab fullscreen
        im = ImageGrab.grab()
        # im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2

        # # save image file
        im.save( 'screenshot' + str(i) + ".png" ) 