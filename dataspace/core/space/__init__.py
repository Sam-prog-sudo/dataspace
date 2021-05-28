from typing import Dict, List

from numpy import nan
import pandas as pd

from dataspace.charts.base import DsChart
from dataspace.core.env import is_notebook
from dataspace.charts import DsChart
from dataspace.core.export import _export_csv
from dataspace.clean import (
    _to_date,
    _to_int,
    _to_float,
    _to_type,
    _drop_nan,
    _fill_nan,
    _fill_nulls,
    _fdate,
    _timestamps,
    _strip,
    _strip_cols,
    _roundvals,
    _replace,
)
from dataspace.utils.messages import msg_ok

from .view import _show
from .info import _cols


class DataSpace:
    df: pd.DataFrame = None
    _chartEngine: DsChart = None

    def __init__(self, df: pd.DataFrame = None) -> None:
        self.df = df

    def __repr__(self) -> str:
        num = 0
        if self.df is not None:
            num = len(self.df.index)
        msg = "<DataSpace object | " + str(num) + " rows>"
        if is_notebook is True:
            self.df.head()
            return str(self.df.head(5))
        return msg

    # **************************
    #           info
    # **************************

    def show(self, rows: int = 5) -> pd.DataFrame:
        """
        Display info about the dataframe

        :param rows: number of rows to show, **default**: 5
        :param rows: ``int`` *optional*
        :return: a pandas dataframe head
        :rtype: ``DataFrame``

        :example: `ds.show()`
        """
        return _show(rows, self.df)

    def cols_(self) -> pd.DataFrame:
        """
        Returns a dataframe with columns info

        :return: a pandas dataframe
        :rtype: ``DataFrame``

        :example: `ds.cols_()`
        """
        return _cols(self.df)

    # **************************
    #           clean
    # **************************

    def to_date(self, *cols: str, **kwargs) -> None:
        """
        Convert some columns values to date type

        :param cols: names of the colums
        :type cols: ``str`` *at least one*
        :param \*\*kwargs: keyword arguments for ``pd.to_datetime``
        :type \*\*kwargs: optional

        :example: `ds.to_date("mycol")`
        """
        _to_date(self.df, *cols, *kwargs)

    def to_int(self, *cols: str, **kwargs) -> None:
        """
        Convert some column values to integers

        :param \*cols: names of the columns
        :type \*cols: ``str`` *at least one*
        :param \*\*kwargs: keyword arguments for ``pd.to_numeric``
        :type \*\*kwargs: optional

        :example: `ds.to_int("mycol1", "mycol2", errors="coerce")`
        """
        _to_int(self.df, *cols, *kwargs)
        if is_notebook is True:
            msg_ok("Converted columns values to integers")

    def to_float(self, *cols: str, **kwargs) -> None:
        """
        Convert colums values to float

        :param cols: name of the columns
        :type cols: ``str`` *at least one*
        :param \*\*kwargs: keyword arguments for ``df.astype``
        :type \*\*kwargs: optional

        :example: `ds.to_float("mycol1")`
        """
        _to_float(self.df, *cols, *kwargs)
        if is_notebook is True:
            msg_ok("Converted columns values to floats")

    def to_type(self, dtype: type, *cols: str, **kwargs) -> None:
        """
        Convert colums values to a given type in the
        main dataframe

        :param dtype: a type to convert to: ex: ``str``
        :type dtype: ``type``
        :param \*cols: names of the columns
        :type \*cols: ``str`` *at least one**
        :param \*\*kwargs: keyword arguments for ``df.astype``
        :type \*\*kwargs: optional

        :example: ``ds.to_type(str, "mycol")``
        """
        _to_type(self.df, dtype, *cols, *kwargs)
        if is_notebook is True:
            msg_ok(f"Converted columns values to {dtype}")

    def drop_nan(self, col: str = None, method: str = "all", **kwargs) -> None:
        """
        Drop rows with ``NaN`` values from the main dataframe

        :param col: name of the column, defaults to None. Drops in
        :type col: ``str`` *optional*
        :param method: ``how`` param for ``df.dropna``, **default**: "all"
        :type method: ``str`` *optional*
        :param \*\*kwargs: params for ``df.dropna``
        :type \*\*kwargs: optional

        :example: `ds.drop_nan("mycol")`
        """
        _drop_nan(self.df, col, method, **kwargs)

    def fill_nan(self, val: str, *cols):
        """
        Fill NaN values with new values in the main dataframe

        :param val: new value
        :type val: ``str``
        :param \*cols: names of the colums
        :type \*cols: ``str`` *at least one*

        :example: ``ds.fill_nan("new value", "mycol1", "mycol2")``
        """
        _fill_nan(self.df, val, *cols)

    def fill_nulls(self, val=nan, *cols: str, nulls=[None, ""]):
        """
        Fill all null values with NaN values in a column.
        Null values are ``None`` or en empty string

        :param cols: columns names
        :type cols: ``str`` *at least one*

        :example: `ds.fill_nulls("mycol")`
        """
        _fill_nulls(self.df, val, *cols, nulls=nulls)

    def index(self, col: str) -> pd.DataFrame:
        """
        Set an index to the main dataframe

        :param col: column name where to index from
        :type col: ``str``

        :example: `ds.index("mycol")`
        """
        self.df.set_index(self.df[col], inplace=True)

    def dateindex(self, col: str) -> pd.DataFrame:
        """
        Set a datetime index from a column

        :param col: column name where to index the date from
        :type col: ``str``

        :example: `ds.dateindex("mycol")`
        """
        index = pd.DatetimeIndex(self.df[col])
        self.df.set_index(index, inplace=True)

    def fdate(self, *cols, precision: str = "S", format: str = None):
        """
        Convert column values to formated date string

        :param \*cols: names of the colums
        :type \*cols: str, at least one
        :param precision: time precision: Y, M, D, H, Min S, defaults to "S"
        :type precision: ``str`` *optional*
        :param format: python date format, defaults to None
        :type format: str, optional

        :example: `ds.fdate("mycol1", "mycol2", precision="D")`
        """
        _fdate(self.df, *cols, precision=precision, format=format)

    def timestamps(self, col: str, **kwargs):
        """
        Add a timestamps column from a date column

        :param col: name of the timestamps column to add
        :type col: ``str``
        :param \*\*kwargs: keyword arguments for ``pd.to_datetime``
        :type \*\*kwargs: optional

        :example: ``ds.timestamps("mycol")``
        """
        _timestamps(self.df, col, **kwargs)

    def strip(self, *cols: str):
        """
        Remove leading and trailing white spaces column's values

        :param col: name of the column
        :type col: ``str``

        :example: `ds.strip("mycol")`
        """
        _strip(self.df, *cols)

    def strip_cols(self):
        """
        Remove leading and trailing white spaces in columns names

        :example: `ds.strip_cols()`
        """
        _strip_cols(self.df)

    def roundvals(self, col: str, precision: int = 2):
        """
        Round floats in a column. Numbers are going to be
        converted to floats if they are not already

        :param col: column name
        :type col: ``str``
        :param precision: float precision, defaults to 2
        :param precision: ``int`` *optional*

        :example: `ds.roundvals("mycol")`
        """
        _roundvals(self.df, col, precision)

    def replace(self, col: str, searchval: str, replaceval: str):
        """
        Replace a value in a column in the main dataframe

        :param col: column name
        :type col: ``str``
        :param searchval: value to replace
        :type searchval: ``str``
        :param replaceval: new value
        :type replaceval: ``str``

        :example: `ds.replace("mycol", "value", "new_value")`
        """
        _replace(self.df, col, searchval, replaceval)

    # **************************
    #           select
    # **************************

    def limit(self, r: int = 5) -> None:
        """
        Limit selection to a range in the main dataframe

        :param r: number of rows to keep, **default**: 5
        :type r: ``int`` *optional*

        :example: `ds.limit(100)`
        """
        self.df = self.df[:r]

    def unique_(self, col: str) -> List[str]:
        """
        Returns a list of unique values in a column

        :param col: the column to select from
        :type col: ``str``
        :return: a list of unique values in the column
        :rtype: ``List[str]``

        :example: `ds.unique_("col1")`
        """
        try:
            df = self.df.drop_duplicates(subset=[col], inplace=False)
            return list(df[col])
        except Exception as e:
            raise Exception("Can not select unique data", e)

    def wunique_(self, col) -> pd.DataFrame:
        """
        Weight unique values: returns a dataframe with a count
        of unique values

        :param col: the column to select from
        :type col: ``str``
        :return: a dataframe with a count of unique values in the column
        :rtype: ``pd.DataFrame``

        :example: `ds.unique_("col1")`
        """
        try:
            s = pd.value_counts(self.df[col].values)
            df = pd.DataFrame(s, columns=["Number"])
            return df
        except Exception as e:
            raise Exception("Can not weight unique data", e)

    # **************************
    #        transform
    # **************************

    def split_(self, col: str) -> Dict[str, "DataSpace"]:
        """
        Split the main dataframe according to a column's unique values and
        return a dict of DataSpace instances

        :return: list of DataSpace instances
        :rtype: ``List[DataSpace]``

        :example: `dss = ds.slit_("Col 1")`
        """
        dss = {}
        try:
            unique = self.df[col].unique()
            for key in unique:
                df2 = DataSpace(self.df.loc[self.df[col] == key])
                dss[key] = df2
        except Exception as e:
            raise ("Can not split dataframe", e)
        return dss

    def sort(self, col: str, **kwargs):
        """
        Sorts the main dataframe according to the given column

        :param col: column name
        :type col: ``str``

        :example: `ds.sort("Col 1")`
        """
        try:
            self.df = self.df.sort_values(col, **kwargs)
        except Exception as e:
            raise Exception("Can not sort the dataframe from column ", col, e)

    def indexcol(self, col: str):
        """
        Add a column from the index

        :param col: name of the new column
        :type col: str

        :example: ``ds.index_col("New col")``
        """
        try:
            self.df[col] = self.df.index.values
        except Exception as e:
            self.err(e)
            return
        if is_notebook is True:
            msg_ok("Column", col, "added from the index")

    # **************************
    #           charts
    # **************************

    def bokeh(self) -> None:
        """
        Use the Bokeh charts engine

        :example: `ds.bokeh()`
        """
        if self._chartEngine is None:
            self._chartEngine = DsChart()
        self._chartEngine.engine = "bokeh"

    def altair(self) -> None:
        """
        Use the Altair charts engine

        :example: `ds.altair()`
        """
        if self._chartEngine is None:
            self._chartEngine = DsChart()
        self._chartEngine.engine = "altair"

    def axis(self, x_axis_col: str, y_axis_col: str):
        """
        Set the columns to use for the chart x and y axis

        :param x_axis_col: name of the column to use for x axis chart
        :type r: ``str``
        :param y_axis_col: name of the column to use for y axis chart
        :type r: ``str``

        :example: `ds.axis("col1", "col2")`
        """
        if self._chartEngine is None:
            self._chartEngine = DsChart()
        return self._chartEngine.set_axis(x_axis_col, y_axis_col)

    def line_(self, **kwargs):
        """
        Draw a line chart

        :rtype: Bokeh or Altair chart

        :example: `ds.line_()`
        """
        return self._chartEngine.chart(self.df, "line", **kwargs)

    def point_(self, **kwargs):
        """
        Draw a point chart

        :rtype: Bokeh or Altair chart

        :example: `ds.point_()`
        """
        return self._chartEngine.chart(self.df, "point", **kwargs)

    def bar_(self, **kwargs):
        """
        Draw a bar chart

        :rtype: Bokeh or Altair chart

        :example: `ds.bar_()`
        """
        return self._chartEngine.chart(self.df, "bar", **kwargs)

    def bar_num_(self, **kwargs):
        """
        Draw a bar chart with numbers. Only for Altair

        :rtype: Altair chart

        :example: `ds.bar_num_()`
        """
        if self._chartEngine.engine != "altair":
            raise Exception(
                """This chart is only available for the Altair engine
            Please switch to Altair like this: ds.altair()
            """
            )
        return self._chartEngine.chart(self.df, "bar_num", **kwargs)

    def area_(self, **kwargs):
        """
        Draw an area chart

        :rtype: Bokeh or Altair chart

        :example: `ds.area_()`
        """
        return self._chartEngine.chart(self.df, "area", **kwargs)

    def hline_(self, **kwargs):
        """
        Draw an horizontal mean line for the y axis

        :rtype: Bokeh or Altair chart

        :example: `ds.hline_()`
        """
        return self._chartEngine.chart(self.df, "hline", **kwargs)

    # **************************
    #           export
    # **************************

    def export_csv(self, filepath: str, **kwargs) -> None:
        """
        Write the main dataframe to a csv file

        :param filepath: path of the file to save
        :type filepath: ``str``
        :param \*\*kwargs: arguments to pass to ``pd.to_csv``

        :example: `ds.export_csv("myfile.csv", header=false)`
        """
        return _export_csv(self.df, filepath, **kwargs)
