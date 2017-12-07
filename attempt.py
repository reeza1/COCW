import random

def organiseData(raceData):
	organisedData = [[[] for i in range(len(raceData))] for i in range(len(raceData))]
	[organisedData[competition[1]][competition[2]].append(competition[0]) for competition in raceData]
	return(organisedData)

def calculateInitialKemenyRanking(solution, raceData):
	KemenyRank = 0
	for original in range(0, len(solution)):
 		competitor1 = solution[original]
 		for competition in range (original, len(solution)):
 			competitor2 = solution[competition]
 			if (len(raceData[competitor2][competitor1]) > 0) :
 				KemenyRank += raceData[competitor2][competitor1][0]

	return(KemenyRank)

def calculateNextKemenyRank(solution, previousRank, competitor1, competitor2, raceData):
	if len(raceData[competitor2][competitor1]) > 0:
		previousRank = previousRank - raceData[competitor2][competitor1][0]
	if len(raceData[competitor1][competitor2]) > 0:
		previousRank = previousRank + raceData[competitor1][competitor2][0]

	return(previousRank)

def changePositions(solution, numberOfPositions):
	position1 = random.randint(0, numberOfPositions)
	if position1 == 0:
		position2 = 1
	elif position1 == numberOfPositions:
		position2 = numberOfPositions -1
	else:
		choice = [-1,1]
		decision = random.choice(choice)
		position2 = position1 + decision
	solution[position1], solution[position2] = solution[position2], solution[position1]
	return(solution, position1, position2)

if __name__ == '__main__':
	import sys
	import string

	data = [cipher.rstrip('\n') for cipher in open(sys.argv[1], 'r')]
	numberOfPositions = int(data[0]) + 1
	candidates = data[1: numberOfPositions]
	raceData = data[numberOfPositions + 1:]
	candidateList = {}
	
	for candidate in candidates:
		candidate = candidate.rsplit(',', 2)
		candidateList[int(candidate[0])] = candidate[1]

	raceData = [competition.rsplit(',', 3) for competition in raceData]
	raceData = [[int(data) for data in competition] for competition in raceData]
	solution = list(range(1, numberOfPositions))
	raceData = organiseData(raceData)
	cost = calculateInitialKemenyRanking(solution, raceData)
	
	num_non_improve = 0
	TL = 5

	while num_non_improve < 5:
		for i in range(0,TL):
			newSolution = changePositions(solution, numberOfPositions)
			newCost = calculateNextKemenyRank(newSolution[0], cost, newSolution[1], newSolution[2], raceData) 
			if newCost <= cost:
				solution = newSolution
				cost = newCost
			else:
				random.uniform(0,1)
	



	
	
