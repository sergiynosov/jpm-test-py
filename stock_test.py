
import sys
from stock.stock_test import *

print 'start ...'

stock_dict = populate_stock_data()
print_stock_data( stock_dict )

operations = populate_operations()
print_operations( operations )

test_devident_yield( stock_dict )
test_PE_ratio( stock_dict )
test_VWSP( operations )
test_geometric_mean( stock_dict )

print 'end ...'
sys.exit(0)
