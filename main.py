
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from config import *



# CONFIG:
btc= yf.Ticker(TICKER_NAME)
btc_usd_historical = btc.history(period=PERIOD_VAL, interval=INTERVAL_VAL)



### №1 - rolling window (RW)
rol_RW = btc_usd_historical['Close'].mean()
print('Стратегия №1', 'купить' if btc_usd_historical['Close'].iloc[-1] > rol_RW else 'продать')

### №2 - simple moving average strategy (SMA)
rol_SMA_1 = btc_usd_historical['Close'].rolling(window=15, center=False).mean()
rol_SMA_2 = btc_usd_historical['Close'].rolling(window=30, center=False).mean()
print('Стратегия №2', 'купить' if rol_SMA_1.iloc[-1] > rol_SMA_2.iloc[-1] else 'продать')

### №3 - exponentially weighted moving average strategy (EWMA)
rol_EWMA_1 = btc_usd_historical['Close'].ewm(span=15, adjust=False).mean()
rol_EWMA_2 = btc_usd_historical['Close'].ewm(span=30, adjust=False).mean()
print('Стратегия №3', 'купить' if rol_EWMA_1.iloc[-1] > rol_EWMA_2.iloc[-1] else 'продать')

### №4 - RSI strategy
rol_RSI = btc_usd_historical['Close'].ewm(span=14, adjust=False).mean()
print('Стратегия №4', 'купить' if rol_RSI.iloc[-1] > btc_usd_historical['Close'].iloc[-1] else 'продать')

### №5 - MACD strategy
rol_MACD = btc_usd_historical['Close'].ewm(span=12, adjust=False).mean() - btc_usd_historical['Close'].ewm(span=26, adjust=False).mean()
rol_MACD_signal = rol_MACD.ewm(span=9, adjust=False).mean()
print('Стратегия №5', 'купить' if rol_MACD.iloc[-1] > rol_MACD_signal.iloc[-1] else 'продать')

### №6 - RSI and MACD strategy
rol_RSI = btc_usd_historical['Close'].ewm(span=14, adjust=False).mean()
rol_MACD = btc_usd_historical['Close'].ewm(span=12, adjust=False).mean() - btc_usd_historical['Close'].ewm(span=26, adjust=False).mean()
rol_MACD_signal = rol_MACD.ewm(span=9, adjust=False).mean()
print('Стратегия №6', 'купить' if rol_RSI.iloc[-1] > rol_MACD_signal.iloc[-1] else 'продать')

### №7 - Triple exponential average strategy
rol_TEMA = btc_usd_historical['Close'].ewm(span=9, adjust=False).mean() - btc_usd_historical['Close'].ewm(span=18, adjust=False).mean() + btc_usd_historical['Close'].ewm(span=36, adjust=False).mean()

### №8 - Williams %R strategy
rol_Williams = (btc_usd_historical['High'] - btc_usd_historical['Close']) / (btc_usd_historical['High'] - btc_usd_historical['Low']) * 100
print('Стратегия №8', 'купить' if rol_Williams.iloc[-1] > 0 else 'продать') 

########## Learning mean-reversion strategy ####################

### №9 - bollinger bands strategy
btc_usd_historical['Middle Band'] = btc_usd_historical['Close'].rolling(window=20, center=False).mean()
btc_usd_historical['Upper Band'] = btc_usd_historical['Middle Band'] + btc_usd_historical['Close'].rolling(window=20, center=False).std() * 2
btc_usd_historical['Lower Band'] = btc_usd_historical['Middle Band'] - btc_usd_historical['Close'].rolling(window=20, center=False).std() * 2
print('Стратегия №9', 'купить' if btc_usd_historical['Close'].iloc[-1] > btc_usd_historical['Upper Band'].iloc[-1] else 'продать')

### #10 - pairs trading strategy
print('Стратегия №10', 'купить' if btc_usd_historical['Close'].iloc[-1] > btc_usd_historical['Open'].iloc[-1] else 'продать')


########## Learning mathematical model-based strategies ####################

### №11 - minimization of the portfolio volatility strategy with monthly trading

### №12 - maximum sharpe ratio strategy with monthly trading

########## Learning time-series prediction-based strategies ####################

### №13 - SARIMAX strategy

### #14 - Prophet strategy


# df = pd.read_csv('data.csv')

# df.plot()

# plt.show()