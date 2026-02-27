from prophet import Prophet
import pandas as pd
from src.settings import PROPHET_PARAMS

class ProphetModel:
    def __init__(self):
        self.model: Prophet | None=None
    def fit(self, price_series: pd.Series):
        df=pd.DataFrame({"ds": price_series.index, "y": price_series.values})
        prophet_params=PROPHET_PARAMS.copy()
        self.model.fit(df, **prophet_params)



    def predict(self, periods: int):
        future = self.model.make_future_dataframe(periods=periods)
        forecast = self.model.predict(future)
        return forecast