"""Prepares the DB for frontend interaction"""
from pandasop import PandasOp
from goaltracker import Goaldb



class FrontDB:


    @staticmethod
    def return_earliest_date(list_of_dates: list):
        return min(list_of_dates)