import easyocr
import cv2
import numpy as np

# 初始化 EasyOCR 讀取器（支援繁體中文 & 英文）
reader = easyocr.Reader(['ch_tra', 'en'])

def extract_text(image):
    """使用 OCR 讀取畫面上的貼文文字"""
    # 轉換成灰階（提高 OCR 準確度）
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 進行二值化處理（提高對比度）
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 執行 OCR 辨識
    results = reader.readtext(binary, detail=0)  # 只回傳文字
    return "\n".join(results)

if __name__ == "__main__":
    # 測試 OCR：請確保 `data/raw/sample.png` 內有 Twitter 截圖
    img = cv2.imread("data/raw/sample.png")
    text = extract_text(img)
    print("擷取到的文字：", text)
