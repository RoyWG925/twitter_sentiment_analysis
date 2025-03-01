import cv2
import pyautogui
import numpy as np

def capture_screen():
    """擷取螢幕畫面"""
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    return screenshot

if __name__ == "__main__":
    img = capture_screen()
    cv2.imshow("Screenshot", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
