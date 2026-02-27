import pandas as pd
import yfinance as yf
from src.settings import TICKERS, START, END



def extract_data_for_a_ticker(ticker: str,start: str, end: str)-> pd.DataFrame:
    return yf.download(ticker, start=START,end=END, progress=False)


def extract_all_tickers(list_of_tickers: list) -> dict[str, pd.DataFrame]:
    stocks_data={}
    
    for ticker in TICKERS:
        stocks_data[ticker]= extract_data_for_a_ticker(ticker, START, END)
    return stocks_data

def extract_holidays():
    pass
