import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

selection = 0.5

#benefit = 
#cost = 

fitness = []

for i in range(0,501):
	fitness.append([0]*1000)

nature = []

nature = np.random.randint(2,size=501)

graph = pd.read_csv("Graphwo.csv")

mktcap = pd.read_csv("NSEMkt.csv")

print(graph)

edges = 0

fitness_study = []

for i in range(0,500):

	k = np.random.randint(0,500)
	
	coop = 0
	defe = 0

	row = graph.iloc[k,]

	row = row.dropna()

	edges = edges+len(row)

	for j in row:

		j = int(j)

		fitness[j][i] = 1-selection

		row2 = graph.iloc[j,]
		row2 = row2.dropna()

		for l in row2:

			#print(l)

			l = int(l)

			comp2 = mktcap.iloc[l][0]
			comp1 = mktcap.iloc[j][0]
			print(comp1)
			print(comp2)
			benefit = comp2/comp1
			cost = comp1/100000
	
			if(l!=k):

				if((nature[j] == 1) and (nature[l] == 1)):
					fitness[j][i] = fitness[j][i] + selection*(benefit-cost)
					coop = fitness[j][i]
				elif((nature[j] == 1) and (nature[l] == 0)):
					fitness[j][i] = fitness[j][i] + selection*(-1*cost)
					coop = fitness[j][i]
				elif((nature[j] == 0) and (nature[l] == 1)):
					fitness[j][i] = fitness[j][i] + selection*(benefit)
					defe = fitness[j][i]	

	print(coop)
	print(defe)
	if((coop >= 0 ) and (defe >= 0)):
		y = np.random.uniform(0,coop+defe)
		if(y <= min(coop,defe)):
			if(coop<=defe):
				nature[k] = 1
			else: 
				nature[k] = 0
		else:
			if(coop<=defe):
				nature[k] = 0
			else:
				nature[k] = 1

	if((coop <= 0 ) and (defe <= 0)):
		y = np.random.uniform(coop+defe,0)
		if(y >= max(coop,defe)):
			if(coop<=defe):
				nature[k] = 0
			else: 
				nature[k] = 1
		else:
			if(coop<=defe):
				nature[k] = 1
			else:
				nature[k] = 0

	if((coop <= 0 ) and (defe >= 0)):
		y = np.random.uniform(coop,defe)
		if(y < 0):
			if(coop<=defe):
				nature[k] = 0
			else: 
				nature[k] = 1
		else:
			if(coop<=defe):
				nature[k] = 1
			else:
				nature[k] = 0

	fitness_study.append(sum(nature)/len(nature))

print(edges/501)

plt.scatter(range(0,500),fitness_study)
plt.xlabel("Time (t)")
plt.ylabel("Ratio of Cooperators to Total Population")
plt.show()

