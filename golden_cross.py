'''
Requirements:
100 days 50 should be under 200
Golden cross 50 moving above 200
based on daily
10 years

snapshot: buy: Date and price
----------------------------------------------
ClosePrice based on daily below 20
sell: Date, price

ClosePrice based on daily below 50
sell: Date, price
----------------------------------------------
diff(date, price)
'''


class Cross:
    def __init__(self, data, SMA):
        self.sma20 = SMA['20']
        self.sma50 = SMA['50']
        self.sma200 = SMA['200']
        for i in data:
            self.close = i['Close']
            self.date = i['Date']

    def golden_cross(self):
        crosses = []
        if self.sma50 is not None and self.sma200 is not None and self.close is not None:
            if self.close[-100:] < self.sma50:
                if self.sma50 > self.sma200:
                    crosses.append(
                        {'buy': {'sma50': self.sma50, 'sma200': self.sma200, 'date': self.date, 'price': self.close}})
                else:
                    pass
            else:
                pass
        else:
            pass
        return crosses

    def price_cross(self):
        crosses = []
        if self.sma50 is not None and self.sma20 is not None and self.close is not None:
            if self.close < self.sma50:
                crosses.append({'sell50': {'sma50': self.sma50, 'date': self.date, 'price': self.close}})
            elif self.close < self.sma20:
                crosses.append({'sell20': {'sma50': self.sma50, 'date': self.date, 'price': self.close}})
            else:
                pass
        else:
            pass
        return crosses
