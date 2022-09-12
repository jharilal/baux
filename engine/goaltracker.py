"""Uses other files to track goals"""
from turtle import back
import pandas as pd
from dateops import DateOps
from pandasop import PandasOp


class Goaldb:
    """Will be the main backbone to the webapp"""
    backend_db = PandasOp.initialize_df()


    @staticmethod
    def return_earliest_date():
        return PandasOp.series_to_list(Goaldb.back_df.start_date)

    @staticmethod
    def current_column_headers():
        pass

    def add_goal():
        pass

    def del_goal():
        pass

    def confirm_activity():
        pass

    def create_date():
        pass

    def check_streak():
        pass
