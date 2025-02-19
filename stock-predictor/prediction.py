import numpy as np
from sklearn.linear_model import LinearRegression

# Function to predict stock price trends
def predict_stock_trend(df):
    df['Day'] = np.arange(len(df))  # Convert date index to numeric days
    model = LinearRegression()
    model.fit(df[['Day']], df['Close'])

    next_day = np.array([[len(df)]])
    predicted_price = model.predict(next_day)

    return predicted_price[0]
