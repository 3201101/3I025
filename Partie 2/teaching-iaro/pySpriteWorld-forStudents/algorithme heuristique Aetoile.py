# -*- coding: utf-8 -*-

def manathan((x,y),(i,j)):
    return abs(i-x) + abs(j-y)

class APathFinder:
    
    def __init__(self, init, goal, wall, heur = manathan):
        self.init = init
        self.goal = goal
        self.wall = wall
        self.frontier = [self.init]
        self.seen = []
        self.heuristique = heur
        
        self.path = self.algo()
        self.iter = 0
        
    def algo(self):
        while(len(self.frontier) != 0):
            self.updateFronier()
            self.seen.add(self.frontier.pop(0))
            
    
    def updateFrontier(self):
        (x,y) = self.frontier[0]
        for (i,j) in [(0,-1),(1,0),(-1,0),(0,1)]:
            pt = (x+i,y+j)
            if(pt not in self.wall) and (pt not in self.frontier) and self.isNotOutside(pt):
                if (pt) in self.seen:
                    if self.seen[list.index(pt)][2] > self.heuristique(pt,self.goal):
                        self.frontier.append((pt,self.heuristique(pt,self.goal)))
                    
    
    def isNotOutside(self, pt):
        return pt[0]>=0 and pt[0]<=20 and pt[1]>=0 and pt[1]<=20
            