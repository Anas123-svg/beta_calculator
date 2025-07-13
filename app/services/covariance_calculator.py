import pandas as pd
import numpy as np
from app.utils.calculate_returns import calculate_simple_returns
 
def calculate_covariance(stock_prices: pd.DataFrame, market_prices: pd.DataFrame) -> float:
    stock_returns = calculate_simple_returns(stock_prices)
    market_returns = calculate_simple_returns(market_prices)

    covariance = np.cov(stock_returns['SimpleReturn'], market_returns['SimpleReturn'])[0][1]
    return covariance
    