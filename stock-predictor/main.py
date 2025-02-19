from flask import Flask, jsonify
from data_fetch import get_stock_data
from prediction import predict_stock_trend
from sentiment import analyze_sentiment
from ai_advisor import get_ai_advice

app = Flask(__name__)

@app.route('/predict/<symbol>')
def predict(symbol):
    df = get_stock_data(symbol)
    if df is None:
        return jsonify({"error": "Stock not found"})

    predicted_price = predict_stock_trend(df)
    sentiment = analyze_sentiment(symbol)
    advice = get_ai_advice(symbol, predicted_price, sentiment)

    return jsonify({
        "symbol": symbol,
        "predicted_price": predicted_price,
        "sentiment": sentiment,
        "investment_advice": advice
    })

if __name__ == '__main__':
    app.run(debug=True)
