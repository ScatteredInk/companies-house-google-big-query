from sys import argv
import os
import json

import pandas as pd
from numpy import NaN
from big_query import sanitise_names, load_schema, list_columns_by_type

def uk_date_to_gbq_date(x):
	if pd.isnull(x):
		return NaN
	else:
		return x[6:]+ "-" + x[3:5] + "-" + x[0:2]

def coh_to_gbq(filename):
	df = pd.read_csv(filename, dtype = str)
	schema = load_schema()
	date_columns = list_columns_by_type(schema)
	int64_columns = list_columns_by_type(schema, "INT64")
	df.columns = sanitise_names(df.columns)
	df[date_columns] = df[date_columns].applymap(lambda x: uk_date_to_gbq_date(x))
	return df

if __name__ == '__main__':
    f = argv[1]
    gbq = coh_to_gbq(f)
    gbq.to_csv("gbq_" + os.path.splitext(f)[0] + ".csv", header = False, index = False)


