from asyncio.log import logger
import csv
import pandas as pd
import yfinance as yf
from pandas_datareader import data, wb
import datetime

xls = pd.read_csv("August2022.csv")


class CollectData():

    def gatherCompanyDetails(self):
        companyList = xls[[
            'Symbol',
            'Price',
            'DGR 5Y',
            'CF/Share',
            'Div Yield',
            'Current Div',
            'Annualized',
        ]]

        comDetails: dict = {
            "tickr": "",
            "price": "",
            "yield": "",
        }

        comList = []

        for company in companyList.iterrows():
            try:
                if (company[1]['Div Yield'] > 4.00):
                    comDetails: dict = {
                        "tickr": "",
                        "price": "",
                        "yield": "",
                    }
                    comDetails["tickr"] = company[1]['Symbol']
                    comDetails["price"] = company[1]['Price']
                    comDetails["yield"] = company[1]['Div Yield']
                    comDetails["dividend/quarter"] = company[1]['Current Div']
                    comDetails["div_cash"] = ((comDetails["dividend/quarter"] *
                                               company[1]['Price']) / 100)
                    # print(comDetails)
                    comList.append(comDetails)
                # else:
                #     print(f"Dividend for {company[1]['Symbol']} is below 4.00")
            except Exception:
                print("exception occured")
        return comList