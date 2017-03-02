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
        self._strategy = None
        self._users = None
        self._bids = None

    @property
    def strategy(self):
        if not self._strategy:
            self._strategy = Strategy()
        return self._strategy

    @property
    def users(self):
        if not self._users:
            self._users = Users()
        return self._users

    @property
    def bids(self):
        if not self._bids:
            self._bids = Bids()
        return self._bids

    @property
    def order(self):
        pass

    @property
    def priors(self):
        bid_prior = self.bids.priors
        value_prior = self.users.value_prior

        return bid_prior, value_prior
