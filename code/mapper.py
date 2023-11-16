# !/user/bin/env python

# import statements and libraries required to perform tf idf
import sys
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

# read input string from the input path provided in the system
FILE_PATH = sys.stdin

# this will read the data from the exported CSV
data = pd.read_csv(FILE_PATH)
# this will read only the body part from the exported CSV
bodyDf = data['body']

# print the data frame so that the reducer program can take it as an input and calculate tf idf
print(bodyDf)
