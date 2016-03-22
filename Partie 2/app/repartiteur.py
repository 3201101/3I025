import heapq
from AStar import doAStar
import sys, os

cwd = os.getcwd()
if sys.platform == "win32" :
	sys.path.append(cwd.replace("Partie 2\\app", "Partie 1\\MasterMatchingGui", 1))
else :
	sys.path.append(cwd.replace("Partie 2/app", "Partie 1/MasterMatchingGui", 1))

from PartyMatcher import PartyMatcher

# Variante Encheres des objectifs
def repEnchere(initStates, goalStates, wallStates):
	nbPlayers = len(initStates)
	nbObj = len(goalStates)
	path = range(nbPlayers)
	playerPath = [range(nbPlayers) for i in range(nbObj)]
	pathSorter = []

	for i in range(nbObj):
		for j in range(nbPlayers):
			playerPath[i][j] = doAStar(initStates[j], goalStates[i], wallStates)
			heapq.heappush(pathSorter, (len(playerPath[i][j]), (i, j)))

	cpt = 0
	iList = []
	jList = []
	while cpt < nbPlayers:
		act = heapq.heappop(pathSorter)
		i,j = act[1]
		if(iList.count(i) == 0 and jList.count(j) == 0):
			path[j] = playerPath[i][j]
			iList.append(i)
			jList.append(j)
			cpt += 1
	#print(path)

	return path

# Variante Dynamique de meilleure reponse
def repDynamique(initStates, goalStates, wallStates):

	# Initialisation
	nPlayers = len(initStates)
	nObjectives = len(goalStates)
	sObjectives = [0 for i in range(nObjectives)]
	aPath = [range(nPlayers) for i in range(nObjectives)]

	# Generation des chemins
	for i in range(nPlayers):
		for j in range(nObjectives):
			aPath[i][j] = doAStar(initStates[i], goalStates[j], wallStates)
		aPath[i].sort(key = lambda a: len(a))

	# Encheres
	while sObjectives.count(0) > 0:
		for i in nPlayers:
			if sObjectives[i] >= nObjectives:
				print "boucle infinie"
				return repEnchere(initStates, goalStates, wallStates)
				#raise Exception('Echec de la resolution')
			if sObjectives[i] >= 0 and sObjectives[i] < nObjectives:
				o = aPath[sObjectives[i]%2]
				if sObjectives.count(o) == 0:
					sObjectives[i] = o
				else:
					sObjectives[i]+= 1
					sObjectives.remove(o)

# Variante Gale-Shapley
def repGaleShapley(initStates, goalStates, wallStates):

	# Initialisation
	nPlayers = len(initStates)
	nObjectives = len(goalStates)
	allPath = [range(nPlayers) for i in range(nObjectives)]
	pPath = []
	pPathGS = []
	oPath = []
	oPathGS = []

	# Generation des chemins
	for i in range(nPlayers):
		for j in range(nObjectives):
			allPath[i][j] = doAStar(initStates[i], goalStates[j], wallStates)
		pPath.append(range(nObjectives))
		pPath[i].sort(key = lambda a : len(allPath[i][a]))
		pPathGS.append([i] + pPath[i])
		#	print("PATH INDEX OBJ : ", goalStates.index(pPath[i][j][-1]))


	# Choix pour les objectifs
	for i in range(nObjectives):
		oPath.append(range(nPlayers))
		oPath[i].sort(key = lambda a : len(allPath[a][i]))
		oPathGS.append([i] + oPath[i])

	# Gale-Shapley
	matcher = PartyMatcher()
	matcher.setApplicants(oPathGS)
	matcher.setProviders(pPathGS)
	matcher.match()
	matches = matcher.getMatch()

	# Application
	path = range(nPlayers)
	for i in range(len(matches)):
		#print("MATCH : ", matches[i][1])
		#print("PATH  : ", pPath[i][pPathGS[i].index(matches[i][1])])
		x,y = matches[i]
		path[x] = allPath[x][y]
		#path[i] = pPath[i][pPathGS[i].index()]

	return path