# Algorithmic-Trading
Algorithmic trading signal prediction. The project aims at analyzing how SMA (short moving average) and EMA (exponential moving average) can be used to generate buy/sell signals.

For this project I'm using `Adjusted Closing Price` to compare with EMA. This is done because ACP provides a more accurate inight into the stock's market movement, while `Closing Price` only shows the price at which the stock was last traded at.

As stock prices are highly affected by financial news, I'm using `Sentiment Score` of news articles as a feature while defining the trading startegy. The news aricles are scraped from `Reuters`.

The list of words to calculate Sentiments is taken from the work presented [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1331573)

# Backtesting and Value-at-Risk
In order to test the implemeted strategy, I have implemented backtesting as well. The idea is to start with an amount of $100000 and using the trading signals generated from the strategy, calculate the annual return from stock and VAR from the returns. 

VAR is calculated using the Variance-Covariance method.
