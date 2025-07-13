from app.services.data_collector import get_stock_data  

from app.utils.cache_utils import redis_get_df, redis_set_df
async def fetch_data(symbol, date_range=''):
    if not symbol or not date_range:
        raise ValueError("Symbol and date range must be provided")
    df = get_stock_data(symbol, date_range)
    #stock_key = f"{symbol}_{date_range}_data"
    #df = redis_get_df(stock_key)
    #if df is None:
     #   df = get_stock_data(symbol, date_range)
      #  redis_set_df(stock_key, df)
    return df