'''
Main acution class
'''
import context
from bids.bids import Bids
from strategy.strategy import Strategy
from users.users import Users


class BaseAuction(object):
    '''
    Auction base class
    '''


class Auction(BaseAuction):
    '''
    Main auction class
    '''
    def __init__(self):
        self.strategy = None
        self.users = None
        self.bids = None

    def get_strategy(self):
        self.strategy = Strategy()

    def get_users(self):
        self.users = Users()

    def get_bids(self):
        self.bids = Bids()

    def get_order(self):
        pass

    def get_priors(self):
        bid_prior = self.bids.get_priors()
        value_prior = self.users.get_value_prior()

        return bid_prior, value_prior
