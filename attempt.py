def organiseData(raceData):
	oranisedData = []
	for competition in racedata:


def calculateKemenyRanking(solution, raceData):
	for rank in solution:
		for competition in raceData



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



	
	
