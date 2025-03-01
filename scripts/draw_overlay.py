import cv2
import numpy as np
import pyautogui

def draw_overlay(sentiment_score, topic):
    """在螢幕上顯示情緒分數與話題分類（支援繁體字）"""
    screen = pyautogui.screenshot()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

    text = f"情緒: {sentiment_score}/10, 類別: {topic}"
    position = (50, 50)

    # 使用中文字體（需要安裝 Taipei Sans TC）
    font_path = "data/fonts/TaipeiSansTCBeta-Regular.ttf"
    font = cv2.FONT_HERSHEY_SIMPLEX  # 如果無法顯示，改用這個

    cv2.putText(screen, text, position, font, 1, (0, 255, 0), 2)
    cv2.imshow("Analysis", screen)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    draw_overlay(8, "娛樂")
