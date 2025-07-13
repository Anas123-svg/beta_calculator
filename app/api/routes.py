from fastapi import FastAPI, Query
from app.controllers.financial_controller import get_beta, get_covariance, get_mean_returns, get_geometric_returns, get_capm
from fastapi import APIRouter
router = APIRouter()

@router.get("/beta")
async def beta(stock: str = Query(...), index: str = Query(...), start_date: str = Query(...)):
    return await get_beta(stock, index, start_date)

@router.get("/covariance")
async def covariance(stock1: str = Query(...), stock2: str = Query(...), start_date: str = Query(...)):
    return await get_covariance(stock1, stock2, start_date)

@router.get("/mean-returns")
async def mean(stock: str = Query(...), start_date: str = Query(...)):
    return await get_mean_returns(stock, start_date)

@router.get("/geometric-returns")
async def geometric_returns(stock: str = Query(...), start_date: str = Query(...)):
    return await get_geometric_returns(stock, start_date)


@router.get("/capm")
async def capm(
    stock: str = Query(...),
    market_index: str = Query(...),
    risk_free_rate: str = Query(...),
    start_date: str = Query(...)
):
    return await get_capm(stock, market_index, risk_free_rate, start_date)
