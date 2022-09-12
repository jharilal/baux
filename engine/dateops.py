"""Holds the date ops class"""
import datetime as dt


class DateOps:
    """Returns a variety of date structures based on need"""
    
    def get_start_date():
        return dt.date.today().strftime('%Y-%m-%d')

    def return_date_range():
        return