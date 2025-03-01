from transformers import pipeline

# 使用 BART 進行多類別分類
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_topic(text):
    """用 Transformer 模型分類話題"""
    topics = ["政治", "娛樂", "遊戲", "金融"]
    result = classifier(text, topics)
    return result["labels"][0]  # 取最高分的分類

if __name__ == "__main__":
    sample_text = "比特幣價格大漲，金融市場震盪！"
    topic_category = classify_topic(sample_text)
    print(f"文章分類（BERT）：{topic_category}")
