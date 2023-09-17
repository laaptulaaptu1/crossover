import os, sys, argparse
import pandas as pd
import backtrader as bt
from backtrader import Cerebro
from strategies.GoldenCross import GoldenCross
from strategies.BuyHold import BuyHold

cerebro = bt.Cerebro()

strategy_to_run = 'golden_cross' #input('Enter the strategy to run, 1. golden_cross, 2. buy_hold ')
asset_to_analyse = 'ASIANPAINT.NS' #input('Enter the asset ')

prices = pd.read_csv('data/daily_nifty/'+asset_to_analyse+'.csv', index_col='Date', parse_dates=True)

# initialize the Cerebro engine
cerebro = Cerebro()
cerebro.broker.setcash(100000)

# add OHLC data feed
feed = bt.feeds.PandasData(dataname=prices)
cerebro.adddata(feed)

strategies = {
    "golden_cross": GoldenCross,
    "buy_hold": BuyHold
}

# parse command line arguments

if not strategy_to_run in strategies:
    print("Invalid strategy, must select one of {}".format(strategies.keys()))
    sys.exit()

#download.download_data()
cerebro.addstrategy(strategy=strategies[strategy_to_run])
cerebro.run()
cerebro.plot()