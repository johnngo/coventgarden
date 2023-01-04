### Backtesting and Performance Measurement

###KPIs use to measure both risk and return characteristics of the strategy
### CAGR | Standard Deviation | Sharpe Ratio | Sortino Ratio | Maximum Drawdown | Calmar Ratio

#**************************

# Import necesary libraries
import yfinance as yf

# Download historical data for required stocks
tickers = ["AMZN","GOOG","MSFT"]
ohlcv_data = {}

# looping over tickers and storing OHLCV dataframe in dictionary
for ticker in tickers:
    temp = yf.download(ticker,period='1yr',interval='1d')
    ##print(temp)
    temp.dropna(how="any",inplace=True)
    ohlcv_data[ticker] = temp

def CAGR(DF):
    "function to calculate the Cumulative Annual Growth Rate of a trading strategy"
    df = DF.copy()
   
    df["return"] = DF["Adj Close"].pct_change()  ##adding new lines in dataframe
    df["cum_return"] = (1 + df["return"]).cumprod() ##adding new lines in dataframe
    ##print(df)
    n = len(df)/252
    print(n)
    CAGR = (df["cum_return"][-1])**(1/n) - 1
    return CAGR

for ticker in ohlcv_data:
    print("CAGR of {} = {}".format(ticker,CAGR(ohlcv_data[ticker])))