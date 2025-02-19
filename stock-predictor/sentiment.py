from transformers import pipeline

# Load Hugging Face financial sentiment model
sentiment_analyzer = pipeline("text-classification", model="mrm8488/finance-bert")

# Analyze stock-related news sentiment
def analyze_sentiment(stock_name):
    # Example: You can integrate a real-time news API
    news = f"Latest news about {stock_name}: Stock market is volatile."
    result = sentiment_analyzer(news)
    return result[0]['label']  # 'positive', 'negative', 'neutral'
