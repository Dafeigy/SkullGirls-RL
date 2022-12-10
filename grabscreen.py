import win32gui,win32con, win32api, win32ui
import numpy as np
import cv2
import time

def grab_screen(window_name, region=None):
    '''
    Args:
        `window_name` : String of the captured window.

        `region` : tuple (start_x, start_y, end_x, end_y) 
        or Basically Current full window capture.

    return:
        `numpy` array shape in [W,H,C]
    '''
    hwin = win32gui.FindWindow(None, window_name)
    # hwin = win32gui.GetDesktopWindow()

    if region:
        left,top,right,bot = region
            
    else:
        # width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        # height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        # left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        # top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

        left, top, right, bot = win32gui.GetWindowRect(hwin)
    
    width = right - left + 1
    height = bot - top + 1


    hwindc = win32gui.GetWindowDC(hwin)
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

if __name__ == "__main__":

    time.sleep(2)
    while True:
        img = grab_screen('Clash for Windows')
        cv2.imshow('test',img)
        cv2.waitKey(1)