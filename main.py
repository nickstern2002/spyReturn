import yfinance as yf
import pandas as pd

ticker = "SPY"
df = yf.Ticker(ticker).history(period="1mo", interval="1d", auto_adjust=False)

prices = df["Close"]  # or "Adj Close" if present
returns = prices / prices.shift(1) - 1

returns = (prices / prices.shift(1) - 1) * 100
returns = returns.map(lambda x: f"{x:.2f}%")

result = pd.DataFrame({"Price": prices, "Daily Return": returns}).dropna()
print(result)
