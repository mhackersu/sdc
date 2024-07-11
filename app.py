import json
import os
from decimal import *
import requests
from datetime import datetime, timezone
import math

def main():
    currency = os.getenv('CURRENCY')
    threshold= os.getenv('THRESHOLD')
    # getcontext().prec = 6
    
    def sdevCalc(currency):
        sd = 0
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
                # DEBUG
                # print(f'Closing price: {currency} Sum: {sum}')

            # Get last price
            la = d[-1]
            el = la[4]
            # DEBUG
            # print(f'last price: {el}')

            e = len(d)
            # DEBUG
            # print(f'Quantity of closing prices: {e}')

            am = sum / e
            # DEBUG
            # print(f'Arithmetic mean: {am}')

            tvs = 0
            for c in d:
                cp = c[4]
                # Deviation = Closing price - Arithmetic mean
                d = cp - am
                sq = d ** 2
                # Total of variance squared
                tvs += sq
                # Arithmetic mean of squared variances
                ams = tvs / e
                # Square root
                sqn = math.sqrt(ams)
 
            
            sdc = sqn / am
            sd = Decimal(sdc)
            # DEBUG
            # print(f'Standard deviation: {sd}')
        
        else:
            print(f'Failed to fetch data: {res.status_code}')

        print(f'Avg price: {am}')
        print(f'Last price: {el}')

        return sd
    
    # Calculate Standard Deviation for Given Currency
    sdc = sdevCalc(currency)
    # Absolute value of sd
    asd = abs(sdc)
    # Quantize Decimal // TODO
    # sdval = Decimal(sdc).quantize(Decimal('0.000001'), rounding=ROUND_UP)
    t = Decimal(threshold)
    print(f'Currency pair: {currency}')
    print(f'Threshold: {t}')
    # print(type(t))
    print(f'Standard deviation: {asd}')
    # print(type(sdc))
    
    # Timestamp
    ct = datetime.now(timezone.utc)
    # Convert timestamp to ISO 8601
    ts = ct.isoformat()
    # Print timestamp
    print(f'Timestamp: {ts}')

    # TODO Conditional statements not working correctly
    # print(asd<t)

    # TODO Print JSON
    # data = 'test.json'
    # with open(data, 'r') as f:
    #     d = json.load(f)

    # for r in d:
    #     record = json.dumps(r)
    #     print(record)

if __name__ == '__main__':
    main()
