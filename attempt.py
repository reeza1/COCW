from collections import defaultdict

def organiseData(raceData):
	organisedData = [[[]for i in range(len(raceData))] for i in range(len(raceData))]
	for competition in raceData:
		organisedData[competition[1]][competition[2]]

	print(organisedData)


#def calculateKemenyRanking(solution, raceData):
 #	for competitor1 in solution 





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
	



	
	
