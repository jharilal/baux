"""Contains the CsvReader class"""

import pandas as pd
import datetime as dt


class CsvOperator:
    """Reads a csv using pandas"""
    df = pd.read_csv('pandasdb.csv')

    @staticmethod
    def add_goal():
        
