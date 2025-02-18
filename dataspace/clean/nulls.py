import pandas as pd


def _drop_nan(df: pd.DataFrame, col: str = None, method: str = "all", **kwargs) -> None:
    try:
        if col is None:
            return df.dropna(how=method, **kwargs)
        else:
            df = df[df[col].notnull()]
        df.reset_index(drop=True)
    except Exception as e:
        raise Exception("Error dropping nan values", e)


def _fill_nan(df: pd.DataFrame, val, *cols: str) -> None:
    if len(cols) == 0:
        cols = df.columns.values
    for col in cols:
        df[col].fillna(val, inplace=True)


def _fill_nulls(df: pd.DataFrame, val, *cols: str, nulls):
    if len(cols) == 0:
        cols = df.columns.values
    for col in cols:
        df[col].replace(nulls, val, inplace=True)
