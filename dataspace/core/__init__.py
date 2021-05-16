import pandas as pd

from dataspace.core.space import DataSpace
from dataspace.core.load import _load_csv, _load_django


def from_df(df: pd.DataFrame) -> DataSpace:
    """
    Intialize a DataSpace from a pandas DataFrame

    :param df: a pandas ``DataFrame``
    :return: a DataSpace
    :rtype: ``DataSpace``

    :example: `dataspace.from_df(df)`
    """
    return DataSpace(df)


def from_csv(url, **kwargs) -> DataSpace:
    """
    Loads csv data in the main dataframe

    :param url: url of the csv file to load:
                            can be absolute if it starts with ``/``
                            or relative if it starts with ``./``
    :type url: ``str``
    :param kwargs: keyword arguments to pass to Pandas
                                ``read_csv`` function
    :return: a DataSpace
    :rtype: ``DataSpace``

    :example: `dataspace.from_csv("./myfile.csv")`
    """
    return DataSpace(_load_csv(url, **kwargs))


def from_django(query) -> DataSpace:
    """
    Load the main dataframe from a django orm query

    :param query: django query from a model
    :type query: django query

    :return: a DataSpace
    :rtype: ``DataSpace``

    :example: `dataspace.load_django(Mymodel.objects.all())`
    """
    return DataSpace(_load_django(query))
