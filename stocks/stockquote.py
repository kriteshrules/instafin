from nsetools import Nse


class getQuotes:
    def __init__(self, symbol):
        self.nse = Nse()
        self.symbol = symbol
        self.stocknamelist = []
        self.closepricelist = []
        self.yearhighlist = []
        self.yearlowlist = []

    def run(self):
        import requests
        requests.packages.urllib3.disable_warnings()
        import ssl

        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context

        for i in self.symbol:
            q = self.nse.get_quote(i)
            closedprice = q.get("averagePrice")
            self.closepricelist.append(closedprice)
            companyName = q.get("companyName")
            self.stocknamelist.append(companyName)
            yearlyhigh = q.get("high52")
            self.yearhighlist.append(yearlyhigh)
            yearlylow = q.get("low52")
            self.yearlowlist.append(yearlylow)
