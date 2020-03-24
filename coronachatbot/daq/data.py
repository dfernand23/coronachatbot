import coronachatbot.daq.file_util as fu
from coronachatbot.daq.file_util import DataSets, Troika

from datetime import datetime
from datetime import timedelta


class CSSE:

    def __init__(self):
        self.data = fu.get_time_series_pandas()

    def time_slice(self, start=0, period=None):
        """
        Gives a time slice between [start .. start+period]
        :param start: number of days after 1/22/20
        :param period: number of days after :param start
        :return:
        """
        results = dict()
        for key, df in self.data.items():
            col_names = list(df.columns.values)

            # 0:4 for the header + a number of days
            filter = col_names[0:4 + period]

            r = df.filter(filter)
            results[key] = r

        return results

    def country_slice(self, countries):
        """
        Gives a horizontal slice for given counties
        :param countries: a list of country names
        :return:
        """
