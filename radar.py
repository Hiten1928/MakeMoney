from asyncio.log import logger
import csv
import pandas as pd
# import yfinance as yf
from pandas_datareader import data, wb
import datetime

xls = pd.read_csv("data/June2022.csv")
# champions = pd.read_csv(csv, "Champions")

print(xls)

# print(xls.loc[:, "No Years"])

companyList = list(xls['Symbol'])
print(type(companyList))
start = pd.to_datetime('2022-06-23')
end = pd.to_datetime('today')

comDetails: dict = {
    "tickr": "",
    "price": "",
    "yield": "",
}

comList = []

try:
    for com in companyList:
        print(com)
        df = data.DataReader(com, 'yahoo', start, end)
        print(df)
except Exception:
    logger.info("exception occured")

newList = xls[((xls['No Years'] > 50) & (xls['5Y Avg Yield'] > 4.00) &
               (xls['EPS 1Y'] > 1))]

print(newList)