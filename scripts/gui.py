import sys
import cv2
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import QTimer
from capture_screen import capture_twitter_post
from extract_text import extract_text
from classify_sentiment import get_sentiment_score
from classify_topic import classify_topic
from draw_overlay import draw_overlay

class SentimentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer = QTimer(self)       # 使用 QTimer 進行定時任務
        self.timer.timeout.connect(self.analysis)  # 定時呼叫 analysis 函數

    def initUI(self):
        self.setWindowTitle("Twitter Sentiment Analysis")
        self.resize(400, 200)

        layout = QVBoxLayout()

        # 狀態標籤，顯示分析結果
        self.status_label = QLabel("狀態: 停止", self)
        layout.addWidget(self.status_label)

        # 開始分析按鈕
        self.start_button = QPushButton("開始分析", self)
        self.start_button.clicked.connect(self.startAnalysis)
        layout.addWidget(self.start_button)

        # 暫停分析按鈕
        self.pause_button = QPushButton("暫停分析", self)
        self.pause_button.clicked.connect(self.pauseAnalysis)
        layout.addWidget(self.pause_button)

        # 結束程式按鈕
        self.stop_button = QPushButton("結束程式", self)
        self.stop_button.clicked.connect(self.close)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)

    def startAnalysis(self):
        self.status_label.setText("狀態: 分析中...")
        self.timer.start(1000)  # 每 1000 毫秒執行一次分析

    def pauseAnalysis(self):
        self.timer.stop()
        self.status_label.setText("狀態: 暫停")

    def analysis(self):
        # 擷取畫面
        img = capture_twitter_post()
        # 使用 OCR 取得文字
        text = extract_text(img)
        if text:
            sentiment = get_sentiment_score(text)
            topic = classify_topic(text)
            self.status_label.setText(f"情緒: {sentiment}/10, 話題: {topic}")
            draw_overlay(img, sentiment, topic)
        else:
            self.status_label.setText("狀態: 未偵測到貼文文字")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SentimentApp()
    window.show()
    sys.exit(app.exec())
