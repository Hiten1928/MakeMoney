from gather import CollectData


class MaximizeProfit:

    def calculateProfit(self):
        collectData = CollectData().gatherCompanyDetails()

        maxMoney = 500

        maxStockPrice = 0
        for stock in collectData:
            if stock.price > maxStockPrice:
                maxStockPrice = stock.price
                print("max stock price", maxStockPrice)
        return collectData


print(MaximizeProfit().calculateProfit())