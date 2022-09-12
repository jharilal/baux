"""Used to perform pandas operations"""
import pandas as pd

class PandasOp:

    @staticmethod
    def initialize_df():
        back_df = pd.read_csv('goalsdb.csv')
        back_df = back_df.set_index('goal_ID')
        back_df['start_date'] = pd.to_datetime(back_df['start_date'])
        return back_df

    @staticmethod
    def series_to_list(pandas_series: pd.Series):
        return list(pandas_series)

