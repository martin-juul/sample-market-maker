from os.path import join
import logging
import environ
from decimal import Decimal

env = environ.Env(
    API_BASE_URL=(str, 'https://testnet.bitmex.com/api/v1/'),
    API_KEY=(str, ''),
    API_SECRET=(str, ''),
    INSTRUMENT=(str, 'XBTUSD'),
    ORDER_PAIRS=(int, 6),
    ORDER_START_SIZE=(int, 100),
    ORDER_STEP_SIZE=(int, 100),
    INTERVAL=(Decimal, 0.005),
    MIN_SPREAD=(Decimal, 0.01),
    MAINTAIN_SPREADS=(bool, True),
    RELIST_INTERVAL=(Decimal, 0.01),
    CHECK_POSITION_LIMITS=(bool, False),
    MIN_POSITION=(int, -10000),
    MAX_POSITION=(int, 10000),
    POST_ONLY=(bool, False),
    DRY_RUN=(bool, False),
    DRY_BTC=(int, 50),
    LOOP_INTERVAL=(int, 5),
    API_REST_INTERVAL=(int, 1),
    API_ERROR_INTERVAL=(int, 10),
    TIMEOUT=(int, 7),
    ORDERID_PREFIX=(str, 'mm_bitmex_'),
)

environ.Env.read_env()

########################################################################################################################
# Connection/Auth
########################################################################################################################

# API URL.
BASE_URL = env('API_BASE_URL')
# BASE_URL = "https://www.bitmex.com/api/v1/" # Once you're ready, uncomment this.

# The BitMEX API requires permanent API keys. Go to https://testnet.bitmex.com/app/apiKeys to fill these out.
API_KEY = env('API_KEY')
API_SECRET = env('API_SECRET')

########################################################################################################################
# Target
########################################################################################################################

# Instrument to market make on BitMEX.
SYMBOL = env('INSTRUMENT')

########################################################################################################################
# Order Size & Spread
########################################################################################################################

# How many pairs of buy/sell orders to keep open
ORDER_PAIRS = env('ORDER_PAIRS')

# ORDER_START_SIZE will be the number of contracts submitted on level 1
# Number of contracts from level 1 to ORDER_PAIRS - 1 will follow the function
# [ORDER_START_SIZE + ORDER_STEP_SIZE (Level -1)]
ORDER_START_SIZE = env('ORDER_START_SIZE')
ORDER_STEP_SIZE = env('ORDER_STEP_SIZE')

# Distance between successive orders, as a percentage (example: 0.005 for 0.5%)
INTERVAL = env('INTERVAL')

# Minimum spread to maintain, in percent, between asks & bids
MIN_SPREAD = env('MIN_SPREAD')

# If True, market-maker will place orders just inside the existing spread and work the interval % outwards,
# rather than starting in the middle and killing potentially profitable spreads.
MAINTAIN_SPREADS = env('MAINTAIN_SPREADS')

# This number defines far much the price of an existing order can be from a desired order before it is amended.
# This is useful for avoiding unnecessary calls and maintaining your ratelimits.
#
# Further information:
# Each order is designed to be (INTERVAL*n)% away from the spread.
# If the spread changes and the order has moved outside its bound defined as
# abs((desired_order['price'] / order['price']) - 1) > settings.RELIST_INTERVAL)
# it will be resubmitted.
#
# 0.01 == 1%
RELIST_INTERVAL = env('RELIST_INTERVAL')

########################################################################################################################
# Trading Behavior
########################################################################################################################

# Position limits - set to True to activate. Values are in contracts.
# If you exceed a position limit, the bot will log and stop quoting that side.
CHECK_POSITION_LIMITS = env('CHECK_POSITION_LIMITS')
MIN_POSITION = env('MIN_POSITION')
MAX_POSITION = env('MAX_POSITION')

# If True, will only send orders that rest in the book (ExecInst: ParticipateDoNotInitiate).
# Use to guarantee a maker rebate.
# However -- orders that would have matched immediately will instead cancel, and you may end up with
# unexpected delta. Be careful.
POST_ONLY = env('MAINTAIN_SPREADS')

########################################################################################################################
# Misc Behavior, Technicals
########################################################################################################################

# If true, don't set up any orders, just say what we would do
# DRY_RUN = True
DRY_RUN = env('DRY_RUN')

# If we're doing a dry run, use these numbers for BTC balances
DRY_BTC = env('DRY_BTC')

# How often to re-check and replace orders.
# Generally, it's safe to make this short because we're fetching from websockets. But if too many
# order amend/replaces are done, you may hit a ratelimit. If so, email BitMEX if you feel you need a higher limit.
LOOP_INTERVAL = env('LOOP_INTERVAL')

# Wait times between orders / errors
API_REST_INTERVAL = env('API_REST_INTERVAL')
API_ERROR_INTERVAL = env('API_ERROR_INTERVAL')
TIMEOUT = env('TIMEOUT')

# Available levels: logging.(DEBUG|INFO|WARN|ERROR)
LOG_LEVEL = logging.INFO

# To uniquely identify orders placed by this bot, the bot sends a ClOrdID (Client order ID) that is attached
# to each order so its source can be identified. This keeps the market maker from cancelling orders that are
# manually placed, or orders placed by another bot.
#
# If you are running multiple bots on the same symbol, give them unique ORDERID_PREFIXes - otherwise they will
# cancel each others' orders.
# Max length is 13 characters.
ORDERID_PREFIX = env('ORDERID_PREFIX')

# If any of these files (and this file) changes, reload the bot.
WATCHED_FILES = [join('market_maker', 'market_maker.py'), join('market_maker', 'bitmex.py'), 'settings.py']

########################################################################################################################
# BitMEX Portfolio
########################################################################################################################

# Specify the contracts that you hold. These will be used in portfolio calculations.
CONTRACTS = ['XBTUSD']
