'''
Main user class
'''
import context


class BaseUsers(object):
    '''
    User base class
    '''


class Users(BaseUsers):
    '''
    User class
    '''
    def __init__(self):
        self.pool = set()
        self.distribution = self._get_distribtion()

    def __getitem__(self, user):
        return self.pool[user]

    def __len__(self):
        return len(self.pool)

    def draw(self):
        return random.sample(self.pool)

    def remove(self, user):
        del self.pool[user]

    @property
    def value_prior(self):
        return None

    def _get_distribtion(self):
        return NotImplemented
