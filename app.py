import json
import os
from decimal import *
import requests

def main():
    currency = os.getenv('CURRENCY')
    threshold = os.getenv('THRESHOLD')

    getcontext().prec = 6
    
    def sdevCalc(currency, threshold):
        sdev: float = 0
        candleLength: str = '/1day'
        candleUrl: str = 'https://api.gemini.com/v2/candles/'
        url = f'{candleUrl}{currency}{candleLength}'
        # DEBUG
        # print(f'URL: {url}')

        res = requests.get(url)

        if res.status_code == 200:
            d = res.json()
            # DEBUG
            # print(d)

            # Get all closing prices for 1 day candle
            sum = 0
            for c in d:
                currency = c[4]
                sum += c[4]
                print(f'Closing price: {currency} Sum: {sum}')

            e = len(d)
            print(f'Total closing prices: {e}')

            am = sum / e
            print(f'Arithmetic mean: {am}')

            sdsum = 0
            for c in d:
                currency = c[4]
                # Deviation = Closing price - Arithmetic mean
                d = currency - am
                sdsum += d
            
            sd: float = sdsum / am
            print(f'Standard deviation: {sd}')
        
        else:
            print(f'Failed to fetch data: {res.status_code}')

        return sd
    
    t = float(threshold)
    sdc = sdevCalc(currency, threshold)

    print(f'SD: {sdc}')
    print(type(sdc))
    print(f'Threshold: {t}')
    print(type(t))

    print(sdc > t)

    # if sdc > t:
    #     sdev = True
    # else:
    #     sdev = False

    # Print
    print(f'currency pair: {currency}')
    print(f'sdev threshold: {threshold}')
    # print(f'Exceeds Threshold: {sdev}')

    data = 'test.json'
    with open(data, 'r') as f:
        d = json.load(f)

    for r in d:
        record = json.dumps(r)
        print(record)

if __name__ == '__main__':
    main()
