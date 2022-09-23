from gather import CollectData
from buy import TradeStock


class MaximizeProfit:

    def calculateProfit(self):
        collectData = CollectData().gatherCompanyDetails()
        print(collectData)
        maxPrice = self.maxStockPrice(stockData=collectData)
        finalStocksList = self.normalizedStockList(stockData=collectData,
                                                   maxStockPrice=maxPrice)
        buy = TradeStock().get_account_details()
        print(buy)
        print("***********************************************************")
        print(finalStocksList)

    def normalizedStockList(self, stockData, maxStockPrice):
        stockStandardPriceList: list = []
        for stock in stockData:
            stockCountMap: dict = {}
            stockCountMap["numOfStock"] = maxStockPrice / stock["price"]
            stockCountMap["tickr"] = stock["tickr"]
            stockCountMap["totalInvestmentPrice"] = stock[
                "price"] * stockCountMap["numOfStock"]
            stockCountMap["price/stock"] = stock["price"]
            stockCountMap["totalDividend"] = stock["div_cash"] * stockCountMap[
                "numOfStock"]
            stockStandardPriceList.append(stockCountMap)
        list = self.sortedCompanyListDividend(stockStandardPriceList)
        return list

    def maxStockPrice(self, stockData):
        maxStockPrice = 0
        for stock in stockData:
            if stock["price"] > maxStockPrice:
                maxStockPrice = stock["price"]
        return maxStockPrice

    def sortedCompanyListDividend(self, stockList):
        stockList = sorted(stockList,
                           key=lambda k: k['totalDividend'],
                           reverse=True)
        return stockList


print(MaximizeProfit().calculateProfit())