import win32gui,win32con, win32api, win32ui
import numpy as np
import cv2
import time

def grab_screen(hwin, region:tuple):
    '''
    Args:
        `hwin` : Handle of window.

        `region` : tuple of source (start_x, start_y, end_x, end_y) 

    return:
        `numpy` array shape in [W,H,C]
    '''
    
    # hwin = win32gui.GetDesktopWindow()

    
    left,top,right,bot = region
            

    width = right - left + 1
    height = bot - top + 1


    hwindc = win32gui.GetWindowDC(win32gui.GetDesktopWindow())
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
    
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height,width,4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    return img

def get_region(window_name:str):
    '''
    Args:
        `window_name` : src window name
    Return:
        `region`: tuple of screen position (left,top,right,bot);
        `hwin`: handle of the window
        ``
    '''
    hwin = win32gui.FindWindow(None, window_name)
    region = win32gui.GetWindowRect(hwin)
    
    return hwin, region

if __name__ == "__main__":
    # Skullgirls Encore
    # Clash for Windows
    # hwin, region = get_region('Skullgirls Encore') # If you don't move the current window
    time.sleep(2)
    while True:
        hwin, region = get_region('Skullgirls Encore')  #move it out if you don't move the window
        img = grab_screen(hwin, region)
        cv2.imshow('test',img)
        cv2.waitKey(1)