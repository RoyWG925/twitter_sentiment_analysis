from transformers import pipeline

# 使用 BERT 進行情緒分析
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def get_sentiment_score(text):
    """將情緒結果轉換為 0-10 分"""
    result = sentiment_pipeline(text)[0]
    score_mapping = {
        "1 star": 0, "2 stars": 2, "3 stars": 5, "4 stars": 7, "5 stars": 10
    }
    return score_mapping.get(result["label"], 5)

if __name__ == "__main__":
    text = "這次的電影真的超好看！"
    score = get_sentiment_score(text)
    print(f"情緒分數: {score}/10")
