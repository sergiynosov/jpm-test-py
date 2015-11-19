
from datetime import *

class stock_operation:

    BUY, SELL = range(2)

    symbol = ''
    price = 0
    quantity = 0
    indicator = BUY
    timestamp = datetime.now()

    def __init__(self, s, p, q, i, t=datetime.now() ):
        self.symbol = s
        self.price = p
        self.quantity = q
        self.indicator = i
        self.timestamp = t

    def __str__(self):
        txt = ''
        txt += str(self.timestamp) + ': '
        txt += '[' + self.symbol + ']'
        txt += ', price = [' + '{:3}'.format(self.price) + ']'
        txt += ', quantity = [' + '{:2}'.format(self.quantity) + ']'
        txt += ', type = [' + ( 'BUY' if self.indicator == self.BUY else 'SELL' ) + ']'
        return txt

# eof
