# -*- coding: utf-8 -*-

class VoeuxSpe :
    
    def __init__(self, fic):
        
        fichier = open(fic, "r")
        contenu = fichier.readlines()
        fichier.close()
        
        self.nbEtu = contenu[0].split()[0]
        temp = contenu[1].split()
        self.capaSpe = {}
        self.voeux = {}
        self.contient = {}
        for i in range( 2, len(self.capaSpe)):
            contenu[i]=contenu[i].split()
            self.voeux[contenu[i][0]] = contenu[i][1:]
            self.contient[contenu[i][0]] = []
            self.capaSpe[contenu[i][0]] = temp[i]
        
class VoeuxEtu :
    
    def __init__(self, fic):
        
        fichier = open(fic, "r")
        contenu = fichier.readlines()
        fichier.close()
        
        self.nbEtu = int(contenu[0].split()[0])
        self.tabEtu = []
        self.voeux = []
        for i in range( 1, self.nbEtu):
            contenu[i]=contenu[i].split()
            self.voeux.append(contenu[i][1:])
            self.tabEtu.append((contenu[i][1], ""))

def gCSpe( etu, spe):
    dic = {}
    i = 0
    while dicAnd(dic):
        for x in spe.voeux:
            if len(spe.contient[x]) < spe.capaSpe):
                dic[x] = False
                etuAppa = etu.tabEtu[spe.voeux[x][i]]
                if etuAppa[1] == "":
                    spe.contient[x][len(spe.contient[x])-1] = spe.voeux[x][i]
                    etuAppa[1] = x
                else:
                    if etu.voeux[spe.voeux[x][i]].index(x) > etu.voeux[spe.voeux[x][i]].index(etuAppa[1])
            else:
                dic[x] = True
    i++
          
def dicAnd(dic):
    val = True
    for i in dic:
        val = val and i
    return val