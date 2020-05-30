import pyautogui
from PIL import Image, ImageGrab
import time

x1 = 440
x2 = 450
y1 = 563
y2 = 690
xx1 = 440
xx2 = 450
yy1 = 410
yy2 = 563
pixel = 100


def collide(data):
    for i in range(x1, x2):
        for j in range(y1, y2):
            if data[i, j] < pixel:
                pyautogui.keyDown("up")
                return
    for i in range(xx1, xx2):
        for j in range(yy1, yy2):
            if data[i, j] < pixel:
                pyautogui.keyDown("down")
                return
    return


if __name__ == '__main__':
    print("Game Loading......")
    time.sleep(3)

    pyautogui.keyDown("up")

    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        collide(data)
        '''
        break
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            data[i, j] = 0
    for i in range(xx1, xx2):
        for j in range(yy1, yy2):
            data[i, j] = 0
    image.show()
    '''