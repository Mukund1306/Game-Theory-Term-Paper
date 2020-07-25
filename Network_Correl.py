import pandas as pd 
import numpy as np
from scipy import stats
import csv

details = pd.read_csv("../Dataset/ind_nifty500list.csv")

graph = []

correl = []

for i in range(0,501):
	graph.append([0]*501)
	correl.append([0]*501)

count = 0

track = 0

for i in details.itertuples():
	symbol = i.Symbol

	print(symbol)

	comp1 = pd.read_csv("../Dataset/"+symbol+".csv")

	Adj_Close = comp1["Adj Close"]

	retns1 = np.log(Adj_Close/Adj_Close.shift(1))

	retns1 = retns1[-123:]

	count2 = 0

	for j in details.itertuples():

		symbol2 = j.Symbol

		comp2 = pd.read_csv("../Dataset/"+symbol2+".csv")

		Adj_Close2 = comp2["Adj Close"]

		retns2 = np.log(Adj_Close2/Adj_Close2.shift(1))

		retns2 = retns2[-123:]

		cor = stats.pearsonr(retns1,retns2)

		track = track+1


		correl[count][count2] = cor[0]

		count2 = count2+1
	print(correl[count])
	count = count+1

count = 0

print(correl)

with open("Correlations.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(correl)


