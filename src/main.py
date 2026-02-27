from tests import test_extractor 
from src import data_extraction
from src import data_processing
from src.settings import TICKERS,START,END
if __name__ == "__main__":
    test_extractor.TestExtractor().test_extract_all_tickers()
    stock_data=data_extraction.extract_all_tickers(TICKERS)
    stock_data=data_processing.process_data(stock_data)
    print(stock_data[TICKERS[0]])  # Print the processed data for the first ticker in the list

