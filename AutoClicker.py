import pyautogui
import time

def Auto(wait_time):
    try:
        while True:
            pyautogui.click()
            time.sleep(wait_time)
    except:
        return True

