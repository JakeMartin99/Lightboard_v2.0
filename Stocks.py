import requests
import time
import json

'''def get_data(sym, res, dt):
    frm = 1597435200
    try:
        return requests.get('https://finnhub.io/api/v1/stock/candle?symbol=' + sym +
                            '&resolution=' + str(res) + '&from=' + str(frm) + '&to=' +
                            str(dt) + '&token=bsvo45f48v6oe6a5u750').json()
    except:
        return get_data(sym, res, dt - 60)

sym = input("Symbol: ").upper()
res = int(input("Timeframe (1, 5, 15, 30, 60): ")) # D, W, and M technically accepted by site
dt = time.time()

r = get_data(sym, res, dt)
ohlc = [r['o'][-8:], r['h'][-8:], r['l'][-8:], r['c'][-8:]]
print(ohlc)
t = r['t'][-8:]
print(t)'''

def get_data(sym):
    r = requests.get('https://finnhub.io/api/v1/quote?symbol=' + sym.upper() +'&token=bsvo45f48v6oe6a5u750')
    return r['c'], r['pc']
