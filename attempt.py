import random

def organiseData(raceData, numberOfPositions):
	organisedData = [[[] for i in range(numberOfPositions)] for i in range(numberOfPositions)]
	[organisedData[competition[1] - 1][competition[2] - 1].append(competition[0]) for competition in raceData]
	print(organisedData)
	return(organisedData)

def calculateInitialKemenyRanking(solution, raceData):
	KemenyRank = 0
	for original in range(0, len(solution)):
 		competitor1 = solution[original]
 		for competition in range (original, len(solution)):
 			competitor2 = solution[competition]
 			if (len(raceData[competitor2 - 1][competitor1 - 1]) > 0):
 				KemenyRank += raceData[competitor2 - 1][competitor1 - 1][0]
	return(KemenyRank)

def calculateNextKemenyRank(solution, previousRank, competitor1, competitor2, raceData):
	print(competitor1 -1)
	print(competitor2 -1)
	print('length1 : {}'.format(raceData[competitor1 - 1][competitor2 - 1]))
	if len(raceData[competitor1 - 1][competitor2 - 1]) > 0:
		previousRank = previousRank + raceData[competitor1 - 1][competitor2 - 1][0]
		print('ranking after sdding: {}'.format(previousRank))
	print('length2 : {}'.format(raceData[competitor2 - 1][competitor1 - 1]))
	if len(raceData[competitor2 - 1][competitor1 - 1]) > 0:
		previousRank = previousRank - raceData[competitor2 - 1][competitor1 - 1][0]
		print('ranking after Deleting: {}'.format(previousRank))

	print(previousRank)
	return(previousRank)

def changePositions(solution, numberOfPositions):
	position1 = random.randint(0, numberOfPositions - 1)
	# if position1 == 0:
	# 	position2 = 1
	# elif position1 == numberOfPositions - 1:
	# 	position2 = numberOfPositions -1
	# else:
	# 	choice = [-1,1]
	# 	decision = random.choice(choice)
	# 	position2 = position1 + decision
	position1 = 3
	position2 = 4

	solution[position1], solution[position2] = solution[position2], solution[position1]
	return(solution, position1, position2)

if __name__ == '__main__':
	import sys
	import math

	data = [cipher.rstrip('\n') for cipher in open(sys.argv[1], 'r')]
	numberOfPositions = int(data[0])
	candidates = data[1: numberOfPositions + 1]
	raceData = data[numberOfPositions + 2:]
	candidateList = {}
	
	for candidate in candidates:
		candidate = candidate.rsplit(',', 2)
		candidateList[int(candidate[0])] = candidate[1]

	raceData = [competition.rsplit(',', 3) for competition in raceData]
	raceData = [[int(data) for data in competition] for competition in raceData]
	solution = (list(range(1, numberOfPositions + 1)),0,0)
	raceData = organiseData(raceData, numberOfPositions)
	cost = calculateInitialKemenyRanking(solution[0], raceData)
	
	num_non_improve = 0
	TL = 5
	T = TL
	a = 0.99

	while num_non_improve < 1:
		print('iteration: {}'.format(num_non_improve))
		for i in range(0,TL):
			newSolution = changePositions(solution[0], numberOfPositions)
			print('New Solution: {}'. format(newSolution))
			newCost = calculateNextKemenyRank(newSolution[0], cost, newSolution[1], newSolution[2], raceData) 
			print()
			costChange = cost - newCost
			if costChange <= 0:
				solution = newSolution
				cost = newCost
			else:
				q = random.uniform(0,1)
				if q < (math.exp((-costChange/T))) :
					solution = newSolution
					cost = newCost
				else:
					num_non_improve += 1
		T = a * T

	print('solution = {}'.format(solution[0]))
	print('KemenyRank = {}'. format(cost))


	
	
