import mss
import numpy as np
import cv2

def capture_twitter_post():
    """擷取 Twitter 貼文區域（不存檔，直接回傳畫面）"""
    with mss.mss() as sct:
        monitor = {"top": 200, "left": 400, "width": 800, "height": 400}  # 調整成 Twitter 貼文區域
        screen = sct.grab(monitor)
        img = np.array(screen)
        return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

if __name__ == "__main__":
    while True:
        img = capture_twitter_post()
        cv2.imshow("Twitter Posts", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按 Q 停止
            break

    cv2.destroyAllWindows()
