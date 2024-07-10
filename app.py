import json
import os

def main():
    pair = os.getenv('CURRENCY')
    sdev = os.getenv('SDEV')

    # Print
    print(f'Currency pair: {pair}')
    print(f'Standard deviation: {sdev}')

    data = 'test.json'
    with open(data, 'r') as f:
        d = json.load(f)

    for r in d:
        record = json.dumps(r)
        print(record)

if __name__ == '__main__':
    main()
