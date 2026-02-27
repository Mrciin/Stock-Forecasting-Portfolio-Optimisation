import datetime as dt
import pandas as pd


TICKERS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']

START=dt.datetime.strftime(dt.datetime(2022,1,1), "%Y-%m-%d")
END=dt.datetime.strftime(dt.datetime.today(), "%Y-%m-%d")

PROPHET_PARAMS={
        "yearly_seasonality": True,
        "weekly_seasonality": True,
        "daily_seasonality": False,
    }
