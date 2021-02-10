import time

import requests

KEY = '136bc10d003b8d6a8fb7863d530a7b34'


def get_data(symbol, period):
    uri = f"https://financialmodelingprep.com/api/v3/technical_indicator/daily/{symbol}?period={period}&type=sma&apikey={KEY}"
    r = requests.get(uri)
    return r.json()


def manipulated_data(symbol):
    data = []
    sma20 = get_data(symbol, '20')
    sma50 = get_data(symbol, '50')
    sma200 = get_data(symbol, '200')
    time.sleep(5)
    for i in sma20:
            data.append(
                {'sma20' : {'date': i['date'], 'close': i['close'], 'sma20': i['sma']}})
    for i in sma50:
        data.append({'sma50': i['sma']})
    for i in sma200:
        data.append({'sma200': i['sma']})

    print(data)
    return data
