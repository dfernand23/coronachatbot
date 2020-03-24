from enum import Enum
import logging
from collections import namedtuple
import os.path as path
import pandas as pd

CSSEGIS_DIR = path.join(path.curdir, 'resources', 'cssegis')
TIME_SERIES_DIR = path.join(CSSEGIS_DIR, 'csse_covid_19_data', 'csse_covid_19_time_series')


class DataSets(Enum):
    CONFIRMED = 'Confirmed'
    DEATHS = 'Deaths'
    RECOVERED = 'Recovered'


Troika = namedtuple('Troika', 'Confirmed Deaths Recovered')


def get_time_series_pandas():
    template = 'time_series_19-covid-{}.csv'
    series_names = [e.value for e in DataSets]

    result = dict()
    for series in series_names:
        # build file path to the next .csv
        file = path.join(TIME_SERIES_DIR, template.format(series))

        data: pd.DataFrame = pd.read_csv(file)
        data.head(4)

        result[series] = data

    ret = result

    return ret
