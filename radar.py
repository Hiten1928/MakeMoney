from asyncio.log import logger
import csv
import pandas as pd
import yfinance as yf
from pandas_datareader import data, wb
import datetime

xls = pd.read_csv("data/June2022.csv")

# companyList = xls[((xls['Symbol']) & (str(xls['Div Yield'])) &
#                    (str(xls['Annualized'])))]

companyList = xls[[
    'Symbol',
    'Price',
    'DGR 5Y',
    'CF/Share',
    'Div Yield',
    'Current Div',
    'Annualized',
]]
start = pd.to_datetime('today')
end = pd.to_datetime('today')

comDetails: dict = {
    "tickr": "",
    "price": "",
    "yield": "",
}

comList = []

print(companyList)

for company in companyList.iterrows():
    try:
        if (company[1]['Div Yield'] > 4.00):
            comDetails: dict = {
                "tickr": "",
                "price": "",
                "yield": "",
            }
            # print('---------STOCK DETAILS----------')
            # print(company[1]['Symbol'])
            # print(type(com))
            # stock_info = yf.Ticker(company[1]['Symbol']).info
            # print('********* STOCK INFO ***********')
            # print(stock_info)
            comDetails["tickr"] = company[1]['Symbol']
            comDetails["price"] = company[1]['Price']
            comDetails["yield"] = company[1]['Div Yield']
            comDetails["dividend/quarter"] = company[1]['Current Div']
            comDetails["div_cash"] = (
                (comDetails["dividend/quarter"] * company[1]['Price']) / 100)
            # print(comDetails)
            comList.append(comDetails)
        # else:
        #     print(f"Dividend for {company[1]['Symbol']} is below 4.00")
    except Exception:
        print("exception occured")
        # print(Exception.with_traceback())
for ele in comList:
    print(ele)
# print(comList)
# newList = xls[((xls['No Years'] > 50) & (xls['5Y Avg Yield'] > 4.00) &
#                (xls['EPS 1Y'] > 1))]

# print(newList)