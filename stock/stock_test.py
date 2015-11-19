
import random
import math
from stock.stock_data import *
from stock.stock_operation import *
from stock.stock_algorithm import *

def generate_test_symbols():
    return { 'TEA', 'POP', 'ALE', 'GIN', 'JOE', 'XXX' }

def generate_test_price(num=5):
    random.seed(0)
    return [random.randint(1,100) for i in range(num)]


def populate_stock_data():
    stock_dict = {}
    stock_dict["TEA"] = stock_data( 0, 100 )
    stock_dict["POP"] = stock_data( 8, 100 )
    stock_dict["ALE"] = stock_data( 23, 60 )
    stock_dict["GIN"] = stock_data( 8, 100, 2, stock_data.PREFERRED )
    stock_dict["JOE"] = stock_data( 13, 250 )
    return stock_dict;

def print_stock_data( stock_dict ):
    print 'GBCE data:'
    for k, v in sorted( stock_dict.items() ): print '[' + k + ']: ' + str(v)
    print


def populate_operations():
    operations = []
    random.seed(0)
    op_time = datetime.now() - timedelta(minutes=20)
    for i in range(10):
        for s in sorted( generate_test_symbols() ):
            for p in generate_test_price():
                q = random.randint(1,10)
                ind = stock_operation.BUY if i % 2 else stock_operation.SELL
                operations.append( stock_operation( s, p, q, ind, op_time ) )
        op_time += timedelta(seconds=60)
    return operations

def print_operations( operations ):
    print 'Trade data:'
    for op in operations: print str(op)
    print


def test_devident_yield( stock_dict ):
    try:
        for s in sorted( generate_test_symbols() ):
            for p in generate_test_price():
                y = calc_divident_yield( stock_dict, s, p )
                print 'stock symbol = [' + s + '], price = ' + '{:3}'.format(p) + 'p, divident yield = ' + '{:6.3f}'.format(y)
    except stock_exception as e:
        print 'ERROR: ' + str(e)
    print

def test_PE_ratio( stock_dict ):
    try:
        for s in sorted( generate_test_symbols() ):
            for p in generate_test_price():
                pe = calc_PE_ratio( stock_dict, s, p )
                print 'stock symbol = [' + s + '], price = ' + '{:3}'.format(p) + 'p, P/E Ratio = ' + '{:6.3f}'.format(pe)
    except stock_exception as e:
        print 'ERROR: ' + str(e)
    print

def test_VWSP( operations ):
    try:
        vwsp = calc_VWSP( operations, timedelta(minutes=20) )
        print 'Volume Weighted Stock Price = ' + '{:.3f}'.format(vwsp)
    except stock_exception as e:
        print 'ERROR: ' + str(e)
    print

def test_geometric_mean( stock_dict ):
    try:
        gm = calc_geometric_mean( stock_dict )
        print 'GBCE All Share Index = ' + '{:.3f}'.format(gm)
    except stock_exception as e:
        print 'ERROR: ' + str(e)
    print

# eof
