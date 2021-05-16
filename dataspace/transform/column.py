import pandas as pd
from ..utils.messages import msg_warning


def _drop(df: pd.DataFrame, *cols):
    """
    Drops columns from the main dataframe

    :param cols: names of the columns
    :type cols: str

    :example: ``ds.drop("Col 1", "Col 2")``
    """
    try:
        index = df.columns.values
        for col in cols:
            if col not in index:
                msg_warning("Column", col, "not found. Aborting")
                return
            df = df.drop(col, axis=1)
    except Exception as e:
        raise ("Can not drop column", e)
