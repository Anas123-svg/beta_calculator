from fastapi import FastAPI, Query
from app.services.beta_calculator import calculate_beta
from app.services.covariance_calculator import calculate_covariance
from app.services.data_fetcher import fetch_data
from app.utils.calculate_returns import calculate_simple_returns
import numpy as np

async def get_beta(stock: str, index: str, start_date: str):
    if not stock or not index or not start_date:
        raise ValueError("Stock, index, and start date must be provided")
    try:
        stock_prices = await fetch_data(stock, start_date)
        index_prices = await fetch_data(index,start_date)
        beta = calculate_beta(stock_prices, index_prices)
        return {
            "stock": stock,
            "index": index,
            "beta": round(beta, 4)
        }
    except Exception as e:
        return {"error": str(e)}
    
async def get_covariance(stock1: str, stock2: str, start_date: str):
    if not stock1 or not stock2 or not start_date:
        raise ValueError("Both stocks and start date must be provided")
    try:
        stock1_prices = await fetch_data(stock1,start_date)
        stock2_prices = await fetch_data(stock2,start_date)
        covariance = calculate_covariance(stock1_prices, stock2_prices)
        return {
            "stock": stock1,
            "index": stock2,
            "covariance": round(covariance, 4)
        }
    except Exception as e:
        return {"error": str(e)}

async def get_mean_returns(stock: str, start_date: str):
    if not stock or not start_date:
        raise ValueError("Stock and start date must be provided")
    try:
        stock_prices = await fetch_data(stock, start_date)
        stock_returns = calculate_simple_returns(stock_prices)
        stock_returns = stock_returns.mean()
        return {
            "stock": stock,
            "mean_return": round(stock_returns, 4)
        }
    except Exception as e:
        return {"error": str(e)}
    
async def get_geometric_returns(stock: str, start_date: str):
    if not stock or not start_date:
        raise ValueError("Stock and start date must be provided")
    try:
        stock_prices = await fetch_data(stock, start_date)

        stock_prices['SimpleReturn'] = stock_prices['Close'].pct_change()

        simple_returns = stock_prices['SimpleReturn'].dropna()
       # simple_returns = simple_returns[(1 + simple_returns) > 0]  
        log_returns = np.log1p(simple_returns)  
        mean_log_return = np.mean(log_returns)
        geometric_return = np.expm1(mean_log_return)  
        if not np.isfinite(geometric_return):
            raise ValueError("Geometric return calculation resulted in an invalid number")

        return {
            "stock": stock,
            "geometric_return": round(geometric_return, 6)
        }

    except Exception as e:
        return {"error": str(e)}


async def get_capm(stock: str, market_index: str, risk_free_rate: str, start_date: str):
    if not stock or not market_index or not start_date or not risk_free_rate :
        raise ValueError("Both stock and start date must be provided")
    try:
        stock_prices = await fetch_data(stock,start_date)
        index = await fetch_data(market_index,start_date)
        stock_returns = calculate_simple_returns(stock_prices)
        market_returns = calculate_simple_returns(index)
        beta = calculate_beta(stock_returns, market_returns)
        risk_free_rate = float(risk_free_rate) / 100
        expected_return = risk_free_rate + beta * (market_returns.mean() - risk_free_rate)
        return {
            "stock": stock,
            "index": market_index,
            "beta": round(beta, 4),
            "expected_return": round(expected_return, 4)
        }
    except Exception as e:
        return {"error": str(e)}
