from src.data_extraction import extract_all_tickers, extract_data_for_a_ticker
import pandas as pd
from src.settings import TICKERS, START, END


class TestExtractor:
    def test_extract_all_tickers(self):
        stock_data=extract_all_tickers(TICKERS)

        assert isinstance(stock_data, dict)
        assert isinstance(stock_data[TICKERS[0]], pd.DataFrame)
        assert len(stock_data) == len(TICKERS)
        assert all(isinstance(stock_data[ticker], pd.DataFrame) for ticker in TICKERS)
