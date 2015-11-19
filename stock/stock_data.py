
class stock_data:

    COMMON, PREFERRED = range(2)

    last_divident = 0
    par_value = 0
    fixed_divident = -1
    stock_type = COMMON

    def __init__(self, ld, pv, fd =-1, st =COMMON):
        self.last_divident = ld
        self.par_value = pv
        self.fixed_divident = fd
        self.stock_type = st

    def __str__(self):
        txt = ''
        txt += 'type = [' + ( 'PRF' if self.stock_type == self.PREFERRED else 'CMN' ) + ']'
        txt += ', last devident = [' + '{:3}'.format(self.last_divident) + ']'
        txt += ', fixed devident = [' + '{:3}'.format(self.fixed_divident) + ']'
        txt += ', par value = [' + '{:3}'.format(self.par_value) + ']';
        return txt

    def calc_divident_yield(self, price):
        result = 0.0
        if self.stock_type == self.COMMON:
            result = float( self.last_divident ) / price
        else:
            result = float( self.fixed_divident ) / 100 * self.par_value / price
        return result

    def calc_PE_ratio(self, price):
        result = 0.0
        if self.last_divident > 0:
            result = float( price ) / self.last_divident
        return result

    def p(self):
        return self.par_value

# eof
