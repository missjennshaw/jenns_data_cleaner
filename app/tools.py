import pandas as pd
from sys import argv

def split_csv(filename):
	#filename = argv[1]
	df = pd.read_csv(filename)

	storage = []
	counter = 0
	part = 1
	tmp_df = pd.DataFrame()
	name = filename.split(".")[0]
	for i in df.index:
		if counter < 200:
			tmp_df = tmp_df.append(df.ix[i],ignore_index=True)
			counter += 1
		else:
			counter = 0
			tmp_df.to_csv(name+str(part)+".csv")
			part += 1
	return part

def name_spliter(name,part):
	filenames = []
	for i in range(1,part+1):
		filenames.append(name+str(part)+".csv")
	return filenames