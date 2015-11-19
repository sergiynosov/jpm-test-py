
from stock.stock_data import *
from stock.stock_operation import *
from stock.stock_exception import *

def calc_divident_yield( stock_dict, stock_symbol, price ):
    result = 0.0
    data = stock_dict.get( stock_symbol )
    if data is not None:
        result = data.calc_divident_yield( price )
    else:
        raise stock_exception( 'Stock Symbol [' + stock_symbol + '] not found' );
    return result

def calc_PE_ratio( stock_dict, stock_symbol, price ):
    result = 0.0
    data = stock_dict.get( stock_symbol )
    if data is not None:
        result = data.calc_PE_ratio( price )
    else:
        raise stock_exception( 'Stock Symbol [' + stock_symbol + '] not found' );
    return result

def calc_VWSP( operations, interval ):
    cutoff_time = datetime.now() - interval
    n = 0.0;
    d = 0.0;
    for op in reversed( operations ):
        if op.timestamp < cutoff_time: break
        #print 'DEBUG: ' + str(op)
        n += float( op.price ) * op.quantity
        d += op.quantity
    r = n / d if d > 0 else 0.0
    return r

def calc_geometric_mean( stock_dict ):
    r = 1.0
    for data in stock_dict.values(): r *= data.p()
    n = float( 1 ) / len(stock_dict)
    return pow( r, n )

# eof
