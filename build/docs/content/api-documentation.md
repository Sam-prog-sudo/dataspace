<a name="dataspace"></a>
# dataspace

<a name="dataspace.core"></a>
# dataspace.core

<a name="dataspace.core.from_df"></a>
#### from\_df

```python
from_df(df: pd.DataFrame) -> DataSpace
```

Intialize a DataSpace from a pandas DataFrame

**Arguments**:

- `df`: a pandas DataFrame
- `rows`: int, optional

**Returns**:

a DataSpace
:rtype: DataSpace

:example: ``dataspace.from_df(df)``

<a name="dataspace.core.from_csv"></a>
#### from\_csv

```python
from_csv(url, **kwargs) -> DataSpace
```

Loads csv data in the main dataframe

**Arguments**:

- `url`: url of the csv file to load:
                        can be absolute if it starts with ``/``
                        or relative if it starts with ``./``
:type url: str
- `kwargs`: keyword arguments to pass to Pandas
                            ``read_csv`` function

:example: ``ds.from_csv("./myfile.csv")``

<a name="dataspace.core.from_django"></a>
#### from\_django

```python
from_django(query) -> DataSpace
```

Load the main dataframe from a django orm query

**Arguments**:

- `query`: django query from a model
:type query: django query

:example: ``ds.load_django(Mymodel.objects.all())``

<a name="dataspace.core.load"></a>
# dataspace.core.load

<a name="dataspace.core.frame"></a>
# dataspace.core.frame

<a name="dataspace.core.frame.select"></a>
# dataspace.core.frame.select

<a name="dataspace.core.frame.frame"></a>
# dataspace.core.frame.frame

<a name="dataspace.core.frame.frame.DataSpace"></a>
## DataSpace Objects

```python
class DataSpace()
```

<a name="dataspace.core.frame.frame.DataSpace.show"></a>
#### show

```python
 | show(rows: int = 5) -> pd.DataFrame
```

Display info about the dataframe

**Arguments**:

- `rows`: number of rows to show, defaults to 5
- `rows`: int, optional

**Returns**:

a pandas dataframe head
:rtype: pd.DataFrame

:example: ``ds.show()``

<a name="dataspace.core.frame.frame.DataSpace.cols_"></a>
#### cols\_

```python
 | cols_() -> pd.DataFrame
```

Returns a dataframe with columns info

**Returns**:

a pandas dataframe
:rtype: pd.DataFrame

:example: ``ds.cols_()``

<a name="dataspace.core.frame.frame.DataSpace.to_date"></a>
#### to\_date

```python
 | to_date(*cols: str, **kwargs) -> None
```

Convert some columns values to date type

**Arguments**:

- `cols`: names of the colums
:type cols: str, at least one
:param \*\*kwargs: keyword arguments for ``pd.to_datetime``
:type \*\*kwargs: optional

:example: ``ds.date("mycol")``

<a name="dataspace.core.frame.frame.DataSpace.to_int"></a>
#### to\_int

```python
 | to_int(*cols: str, **kwargs) -> None
```

Convert some column values to integers

:param \*cols: names of the columns
:type \*cols: str, at least one
:param \*\*kwargs: keyword arguments for ``pd.to_numeric``
:type \*\*kwargs: optional

:example: ``ds.to_int("mycol1", "mycol2", errors="coerce")``

<a name="dataspace.core.frame.frame.DataSpace.to_float"></a>
#### to\_float

```python
 | to_float(*cols: str, **kwargs) -> None
```

Convert colums values to float

**Arguments**:

- `cols`: name of the columns
:type cols: str, at least one
:param \*\*kwargs: keyword arguments for ``df.astype``
:type \*\*kwargs: optional

:example: ``ds.to_float("mycol1")``

<a name="dataspace.core.frame.frame.DataSpace.to_type"></a>
#### to\_type

```python
 | to_type(dtype: type, *cols: str, **kwargs) -> None
```

Convert colums values to a given type in the
main dataframe

**Arguments**:

- `dtype`: a type to convert to: ex: ``str``
:type dtype: type
:param \*cols: names of the columns
:type \*cols: str, at least one
:param \*\*kwargs: keyword arguments for ``df.astype``
:type \*\*kwargs: optional

:example: ``ds.to_type(str, "mycol")``

<a name="dataspace.core.frame.frame.DataSpace.limit"></a>
#### limit

```python
 | limit(r: int = 5) -> None
```

Limit selection to a range in the main dataframe

**Arguments**:

- `r`: number of rows to keep, defaults to 5
:type r: int, optional

<a name="dataspace.core.frame.frame.DataSpace.split_"></a>
#### split\_

```python
 | split_(col: str) -> Dict[str, "DataSpace"]
```

Split the main dataframe according to a column's unique values and
return a dict of dataswim instances

**Returns**:

list of dataswim instances
:rtype: list(Ds)

:example: ``dss = ds.slit_("Col 1")``

<a name="dataspace.core.frame.frame.DataSpace.sort"></a>
#### sort

```python
 | sort(col: str, **kwargs)
```

Sorts the main dataframe according to the given column

**Arguments**:

- `col`: column name
:type col: str

:example: ``ds.sort("Col 1")``

<a name="dataspace.core.frame.frame.DataSpace.bokeh"></a>
#### bokeh

```python
 | bokeh() -> None
```

Use the Bokeh charts engine

<a name="dataspace.core.frame.frame.DataSpace.altair"></a>
#### altair

```python
 | altair() -> None
```

Use the Altair charts engine

<a name="dataspace.core.frame.frame.DataSpace.axis"></a>
#### axis

```python
 | axis(x_axis_col: str, y_axis_col: str)
```

Set the columns to use for the chart x and y axis

**Arguments**:

- `x_axis_col`: name of the column to use for x axis chart
:type r: str
- `y_axis_col`: name of the column to use for y axis chart
:type r: str
:rtype: None

:example: ``ds.chart("col1", "col2")``

<a name="dataspace.core.frame.frame.DataSpace.line_"></a>
#### line\_

```python
 | line_(**kwargs)
```

Draw a line chart

:rtype: chart

:example: ``ds.line_()``

<a name="dataspace.core.frame.frame.DataSpace.point_"></a>
#### point\_

```python
 | point_(**kwargs)
```

Draw a point chart

:rtype: chart

:example: ``ds.point_()``

<a name="dataspace.core.frame.frame.DataSpace.bar_"></a>
#### bar\_

```python
 | bar_(**kwargs)
```

Draw a bar chart

:rtype: chart

:example: ``ds.bar_()``

<a name="dataspace.core.frame.frame.DataSpace.area_"></a>
#### area\_

```python
 | area_(**kwargs)
```

Draw an area chart

:rtype: chart

:example: ``ds.area_()``

<a name="dataspace.core.frame.frame.DataSpace.hline_"></a>
#### hline\_

```python
 | hline_(**kwargs)
```

Draw an area horizontal mean line for y axis

:rtype: chart

:example: ``ds.hline_()``

<a name="dataspace.core.frame.frame.DataSpace.to_csv"></a>
#### to\_csv

```python
 | to_csv(filepath: str, **kwargs) -> None
```

Write the main dataframe to a csv file

**Arguments**:

- `filepath`: path of the file to save
:type filepath: str
- `index`: [description], defaults to False
- `index`: bool, optional
:param \*args: arguments to pass to ``pd.to_csv``

:example: ``ds.to_csv_("myfile.csv", header=false)``

<a name="dataspace.core.frame.view"></a>
# dataspace.core.frame.view

<a name="dataspace.core.frame.calculations"></a>
# dataspace.core.frame.calculations

<a name="dataspace.core.frame.calculations.regression"></a>
# dataspace.core.frame.calculations.regression

<a name="dataspace.core.frame.transform"></a>
# dataspace.core.frame.transform

<a name="dataspace.core.frame.info"></a>
# dataspace.core.frame.info

<a name="dataspace.core.export"></a>
# dataspace.core.export

<a name="dataspace.core.env"></a>
# dataspace.core.env

<a name="dataspace.utils"></a>
# dataspace.utils

<a name="dataspace.utils.colors"></a>
# dataspace.utils.colors

<a name="dataspace.utils.messages"></a>
# dataspace.utils.messages

<a name="dataspace.utils.messages.msg_info"></a>
#### msg\_info

```python
msg_info(*msg)
```

Prints a message with an info prefix

<a name="dataspace.utils.messages.msg_start"></a>
#### msg\_start

```python
msg_start(*msg)
```

Prints an start message

<a name="dataspace.utils.messages.msg_end"></a>
#### msg\_end

```python
msg_end(self, *msg)
```

Prints an end message with elapsed time

<a name="dataspace.utils.messages.msg_warning"></a>
#### msg\_warning

```python
msg_warning(*msg)
```

Prints a warning

<a name="dataspace.utils.messages.msg_ok"></a>
#### msg\_ok

```python
msg_ok(*msg)
```

Prints a message with an ok prefix

<a name="dataspace.charts"></a>
# dataspace.charts

<a name="dataspace.charts.base"></a>
# dataspace.charts.base

<a name="dataspace.charts.bokeh"></a>
# dataspace.charts.bokeh

<a name="dataspace.charts.bokeh.BokehChart"></a>
## BokehChart Objects

```python
class BokehChart()
```

<a name="dataspace.charts.bokeh.BokehChart.chart"></a>
#### chart

```python
 | chart(df: pd.DataFrame, chart_type, **kwargs)
```

Get a Bokeh chart object

<a name="dataspace.charts.altair"></a>
# dataspace.charts.altair

<a name="dataspace.charts.altair.AltairChart"></a>
## AltairChart Objects

```python
class AltairChart()
```

<a name="dataspace.charts.altair.AltairChart.chart"></a>
#### chart

```python
 | chart(df: pd.DataFrame, chart_type, opts={}, style={}, encode={}) -> Chart
```

Get an Altair chart object

<a name="dataspace.charts.altair.AltairChart._altair_chart_num_"></a>
#### \_altair\_chart\_num\_

```python
 | _altair_chart_num_(df: pd.DataFrame, chart_type: str, opts, style2, encode) -> Chart
```

Get a chart + text number chart

<a name="dataspace.charts.altair.AltairChart._altair_hline_"></a>
#### \_altair\_hline\_

```python
 | _altair_hline_(df: pd.DataFrame, opts, style, encode) -> Chart
```

Get a mean line chart

<a name="dataspace.clean"></a>
# dataspace.clean

<a name="dataspace.clean.convert"></a>
# dataspace.clean.convert

<a name="dataspace.transform"></a>
# dataspace.transform

<a name="dataspace.transform.column"></a>
# dataspace.transform.column

