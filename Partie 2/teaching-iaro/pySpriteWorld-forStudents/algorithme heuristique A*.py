# -*- coding: utf-8 -*-

class APathFinder:
    
    def __init__(self, init, goal, wall):
        self.init = init
        self.goal = goal
        self.wall = wall
        
        self.path = algo(0, [], [(self.heur(init[0]),init[0])])
        self.iter = 0
        
    def algo(self, distance, path, border):
        
        for b in border:
            a = algo(distance+1, path.append(b), bord(b, path))
            if (a != []):
                return a
            i+= 1
            
            
        actu = init[0]
        
        
        #return c.extend(algo())
        
    def bord(self, b, p):
        a = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                c = (i, j)
                if p.count(c) + self.wall.count(c) == 0:
                    a.append(c)
        return sorted(a, )
        
       
    def heur(self, t):
        x = abs(t[0] - self.goal[0][0])
        y = abs(t[1] - self.goal[0][1])
        
        return (x + y)

        
    def nextPoint(self):
        r = path[iter]
        iter+= 1
        return r
        
        

