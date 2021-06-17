import pandas as pd
from ..utils.messages import msg_warning


def _drop(df: pd.DataFrame, *cols):
    try:
        index = df.columns.values
        for col in cols:
            if col not in index:
                msg_warning("Column", col, "not found. Aborting")
                return
            df = df.drop(col, axis=1)
        return df
    except Exception as e:
        raise ("Can not drop column", e)
