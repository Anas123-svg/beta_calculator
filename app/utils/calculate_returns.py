import pandas as pd
import numpy as np
def calculate_simple_returns(price_df: pd.DataFrame) -> pd.DataFrame:
    price_df = price_df.copy()
    price_df['SimpleReturn'] = price_df['Close'].pct_change()
    price_df.dropna(inplace=True)
    return price_df