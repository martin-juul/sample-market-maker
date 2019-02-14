# BitMEX Market Maker

This fork allowing configuring the bot via environment variables.

[Click here for the original readme](README.original.md)

## Getting started

Make sure you have python3 and pip3 installed.

__Install the dependencies:__

```bash
pip3 install -r requirements.txt
```

__Create the .env file__

```bash
cp .env-sample .env
```

__Configure the bot:__

```dotenv
# Connection/Auth
API_BASE_URL=https://testnet.bitmex.com/api/v1/ # Change this to https://www.bitmex.com/api/v1/ for trading on the real platform.
API_KEY=
API_SECRET=

# Target
INSTRUMENT=XBTUSD

# Order Size & Spread
ORDER_PAIRS=6
ORDER_START_SIZE=100
ORDER_STEP_SIZE=100
INTERVAL=0.005
MIN_SPREAD=0.01
MAINTAIN_SPREADS=True
RELIST_INTERVAL=0.01

# Trading Behavior
CHECK_POSITION_LIMITS=false
MIN_POSITION=-10000
MAX_POSITION=10000
POST_ONLY=False

# Misc Behavior, Technicals
DRY_RUN=True # Set to false to run it live.
DRY_BTC=1

LOOP_INTERVAL=5
API_REST_INTERVAL=1
API_ERROR_INTERVAL=10
TIMEOUT=7

ORDERID_PREFIX=b1_xbtusd_
```

_The sample prefixes all vars with export, so you can source them in your shell_ `source .env`

__Start the bot__

```bash
python3 ./marketmaker
```

## Reconfiguring the bot

Edit the .env file to your liking, then restart the bot.

## Docker