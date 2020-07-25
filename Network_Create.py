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


track = 0

count = 0

correl = pd.read_csv("Correlations.csv")

for i in details.itertuples():
	sector = i.Industry
	symbol = i.Symbol

	group = i.Company_Name
	group = group.split()
	group = group[0]
	
	count2 = 0

	print(symbol)

	for j in details.itertuples():
		group2 = j.Company_Name
		group2 = group2.split()
		group2 = group2[0]

		if(symbol != j.Symbol):
			if(sector == j.Industry):
				graph[count][count2] = 1

			if(group == group2):
				graph[count][count2] = 1

			if(correl.iloc[count][count2] >= 0.2):
				graph[count][count2] = 1




		count2 = count2+1

	count = count+1

print(track/2)

print(graph)


with open("Graph.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(graph)

print(graph)

