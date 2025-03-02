import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageFont, ImageDraw, Image

font_path = "data/fonts/TaipeiSansTCBeta-Regular.ttf"

def draw_overlay(img, sentiment, topic):
    """在畫面上標記情緒與話題（使用 Matplotlib 顯示）"""
    pil_img = Image.fromarray(img)
    draw = ImageDraw.Draw(pil_img)
    
    font = ImageFont.truetype(font_path, 30) if font_path else None
    draw.text((50, 50), f"情緒: {sentiment}/10", font=font, fill=(0, 255, 0))
    draw.text((50, 100), f"話題: {topic}", font=font, fill=(255, 0, 0))

    img = np.array(pil_img)

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis("off")  # 隱藏座標軸
    plt.show()

if __name__ == "__main__":
    img = np.zeros((400, 800, 3), dtype=np.uint8)
    draw_overlay(img, 8, "娛樂")
