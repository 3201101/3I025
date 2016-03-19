import heapq

def distanceManathan(pos, obj):
	
	return obj[0] - pos[0] + obj[1] - pos[1]

# Applique l'algorithme A*
def doAStar(start, objective, walls, h = distanceManathan):
	

	def tracePath(obj):
		
		t = obj
		l = [obj]
		while not t == start:
			osef, t = visited[t]
			l.append(t)
		l.reverse()
		
		return l

	def isInside(pos):
		
		x,y = pos
		return x >= 0 and x < 20 and y >= 0 and y <  20

	# Initlalisation
	def heur(pos):
		
		return h(pos, objective)

	visited = {}
	visited[start] = (0, None)

	frontier = []
	heapq.heappush(frontier, (0+heur(start), start))

	# Parcours de la carte jusqu'a la decouverte de l'objectif
	while not len(frontier) == 0:
		
		val, here = heapq.heappop(frontier)
		newVal = visited[here][0] + 1

		if here == objective:
			
			return tracePath(objective)

		x,y = here
		r = [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]
		for i in r:
			
			
			if i not in walls and (i not in visited or visited[i][0] > newVal) and isInside(i):
				
				
				heapq.heappush(frontier, (newVal+heur(i), i))
				visited[i] = (newVal, here)
				

		

	
