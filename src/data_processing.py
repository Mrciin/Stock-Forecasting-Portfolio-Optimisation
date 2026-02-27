import pandas as pd 
import datetime as dt
from datetime import timedelta
from src.settings import TICKERS,START,END

def process_for_singular_ticker(data: pd.DataFrame) -> pd.DataFrame:
    # 1. Move the index (Date) into a regular column
    data = data.reset_index()
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(1)
    
    # 2. Now 'Date' exists as a column and can be selected
    processed_data = data[['Date', 'Close']].copy()
    
    # 3. Rename and convert as before
    processed_data = processed_data.rename(columns={'Close': 'y', 'Date': 'ds'})
    processed_data['ds'] = pd.to_datetime(processed_data['ds'])
    
    return processed_data

def process_data(data: dict[str: pd.DataFrame])-> dict[str: pd.DataFrame]:
    processed_data={}
    for ticker, df in data.items():
        processed_data[ticker]=process_for_singular_ticker(df)

    return processed_data
 
def check_for_missing_dates(data: dict[str:pd.DataFrame]) -> bool:
    quantity = len(TICKERS)
    start_date=pd.to_datetime(START)
    end_date=pd.to_datetime(END)
    amount_of_days=end_date-start_date
    is_missing={}
    for ticker in TICKERS:    
        is_missing[ticker]=0

    for i in amount_of_days:
        new_date=start_date + timedelta(days=i)


