import pandas as pd
from ..utils.messages import msg_start, msg_end, msg_warning


def _load_csv(url, **kwargs) -> pd.DataFrame:
    msg_start("Loading csv...")
    try:
        return pd.read_csv(url, **kwargs)
    except FileNotFoundError:
        msg = "File " + url + " not found"
        msg_warning(msg)
        return
    except Exception as e:
        raise Exception("Can not load csv file", e)
    msg_end("Finished loading csv")


def _load_django(query) -> pd.DataFrame:
    try:
        df = pd.DataFrame(list(query.values()))
        return df
    except Exception as e:
        raise Exception("Can not create dataspace from query", e)
