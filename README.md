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
- Other interesting checks you might implement
- Your approach to solving the task, and any issues with implementation
    - Population/Sample calculation considerations with standard deviation
- The time it took you to write it

## Scoring

- Running the code, per instructions, verifying it executes as expected.
- Scoring the code with pylint, gofmt, shellcheck, or eq. linter
- Reviewing code style
- Reviewing attached documentation
- Quality of documentation for running code
