from gather import CollectData


class MaximizeProfit:

    def calculateProfit(self):
        collectData = CollectData()
        print(collectData.gatherCompanyDetails())


MaximizeProfit().calculateProfit()