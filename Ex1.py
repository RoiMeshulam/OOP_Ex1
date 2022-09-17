import sys
from MyAlgo import *

building_json = sys.argv[1]
calls_csv = sys.argv[2]
output_csv = sys.argv[3]

algo = MyAlgo(building_json,calls_csv,output_csv)
algo.allocate()
algo.writeTocsv()