# Standard Deviation Calculator

## Run the program

`./entrypoint.sh <CURRENCY-PAIR> <DEVIATION-THRESHOLD>`

eg.

`./entrypoint.sh btcusd 1.1`

## AC

Write a program that fetches prices for each currency pair that Gemini trades, calculates standard deviation and prints output via JSONL.

## Struct

```
"timestamp": "ISO8601",
"level": "INFO, ERROR, DEBUG",
"trading_pair": "str",
"deviation": bool, 
"data": {
  "last_price": "decimal",
  "average": "decimal",
  "change": "decimal",
  "sdev": "decimal"
}
```

### API Calls
- `/symbols` - Fetches the pairs of symbols
- `/candle/symbol/1day` - Fetch the symbol details for each pair

### Functions

- fetchPairs - Get pairs
- fetchSymbolDetails - Get candles
- sdevCalc - Calc standard deviation

## Questions

- What would you do next to improve the script
  - Adding a data persistence layer
  - Error handling for threshold, must be integer or decimal, not string
- Other interesting checks you might implement
  - Error handling for currency pair that does not exist
- Your approach to solving the task, and any issues with implementation
  - Using closing prices on 1 Day candles to calculate sdev
- The time it took you to write it
  - 1 hr on container and shell script
  - 3 hrs on code

## Continuing work

- Given additional time, items to complete
  - Properly round decimal, ran into some issue with rounding
  - Finish bool comparison operation, ran into some fiddly issue with comparing Decimal values
  - Organize output and format as JSONL to console


## Scoring

- Running the code, per instructions, verifying it executes as expected.
- Scoring the code with pylint, gofmt, shellcheck, or eq. linter
- Reviewing code style
- Reviewing attached documentation
- Quality of documentation for running code
