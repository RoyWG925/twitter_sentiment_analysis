from capture_screen import capture_screen
from extract_text import extract_text
from classify_sentiment import get_sentiment_score
from classify_topic import classify_topic
from draw_overlay import draw_overlay

def main():
    img = capture_screen()
    text = extract_text(img)
    if text:
        sentiment = get_sentiment_score(text)
        topic = classify_topic(text)
        draw_overlay(sentiment, topic)

if __name__ == "__main__":
    main()
