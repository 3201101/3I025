# -*- coding: utf-8 -*-

class APathFinder:
    
    def __init__(self, init, goal, wall, heur = self.manathan):
        self.init = init
        self.goal = goal
        self.wall = wall
        self.frontier = [self.init]
        self.seen = []
        self.heuristique = heur
        
        self.path = algo()
        self.iter = 0
        
    def algo(self):
        while(len(frontier) != 0):
            self.updateFronier()
            seen.add(frontier.pop(0))
            
    
    def updateFrontier(self):
        (x,y) = self.frontier[0]
        for (i,j) in [(0,-1),(1,0),(-1,0),(0,1)]:
            if((x+i,y+j) not in wall) and ((x+i,y+j) not in frontier) and self.isInBorder(x+i,y+j):
                if (x+i,y+j) in seen:
                    if 
                    self.frontier.append((x+i,y+j))
                    
    
    def isInBorder(self, x, y):
        return x>=0 and x<=20 and y>=0 and y<=20
            
    def manathan((x,y),(i,j)):
        return abs(i-x) + abs(j-y)
