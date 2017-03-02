'''
Main bids class
'''
import context

class BaseBids(object):
    '''
    Bids base class
    '''


class Bids(BaseBids):
    '''
    Bids class
    '''
    def __init__(self):
        self.bids = []
        pass

    @property
    def priors(self):
        return None

    def place_bid(self, bid):
        self.bids.append(bid)
