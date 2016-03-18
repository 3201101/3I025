# -*- coding: utf-8 -*-

class VoeuxSpe :

    # Initialisation
    def __init__(self, fic):

        # Lecture du fichier
        fichier = open(fic, "r")
        contenu = fichier.readlines()
        fichier.close()

        # Parsage des donnees
        self.nbEtu = contenu[0].split()[0]
        temp = contenu[1].split()
        self.nomSpe = []
        self.capaSpe = {} #dictionnaire des capacites des specialites indexé par nom de specialite
        self.voeux = {} #dictionnaire des voeux indexé par nom de specialite
        self.contient = {} #dictionnaire des etudiant integre indexé par nom de specialite, utilise par gS
        self.nVoeux = {} #dictionnaire du rang de voeux actuel indexé par nom de specialite, utilise par gS
        for i in range( 2, len(temp)+2):
            contenu[i]=contenu[i].split()
            self.nomSpe.append(contenu[i][0])
            self.voeux[contenu[i][0]] = [int(a) for a in contenu[i][1:]]
            self.contient[contenu[i][0]] = []
            self.nVoeux[contenu[i][0]] = 0
            self.capaSpe[contenu[i][0]] = int(temp[i-2])

    # Application de l'algorithme de Gale-Shapley
    def gS(self,etu):
        self.reset()
        etu.reset()
        speFull = {}
        # Tant que toutes les specialites ne sont pas pleines
        while True:
            # Pour chaque cle du dictionaire de la specialite
            for x in self.voeux:
                i = self.nVoeux[x]
                #print(x, i)
                #print(self.contient[x], self.capaSpe[x])
                if i > self.nbEtu :
                    print("Algorithme out of bound")
                    return
                # S'il reste des places dans la specialite
                if len(self.contient[x]) < self.capaSpe[x]:
                    speFull[x] = False                      # Initialisation de speFull
                    nEtu = self.voeux[x][i]                 # Numero de l'etudiant
                    nameAppaEtu = etu.tabEtu[nEtu]          # Nom et de la specialite actuelle de l'edutiant
                    #print(nEtu, nameAppaEtu, etu.voeux[nEtu].index(x))
                    # Si l'etudiant n'a pas dejà de specialite
                    if nameAppaEtu[1] == "":
                        self.contient[x].append(nEtu)
                        nameAppaEtu[1] = x
                    else:
                        #print(etu.voeux[nEtu].index(x), etu.voeux[nEtu].index(nameAppaEtu[1]))
                        if etu.voeux[nEtu].index(x) < etu.voeux[nEtu].index(nameAppaEtu[1]):    #Cas etu preferant la spe lui demandant
                            self.contient[nameAppaEtu[1]].remove(nEtu)
                            self.contient[x].append(nEtu)
                            nameAppaEtu[1] = x
                    self.nVoeux[x] += 1
                # Si la specialite est pleine
                else:
                    speFull[x] = True
                if isWholeTrue(speFull):
                    r = "Resultat algorithme de Gale-Shapley cote specialites : "
                    r += str(self.contient)
                    return r
                #print(self.contient)

    def insertEtu(self, spe, etu):
        if len(self.contient[spe]) < self.capaSpe[spe]:
            self.contient[spe].append(etu)
            return -1
        else:
            n = self.contient[spe][0]
            for i in self.contient[spe]:
                if self.voeux[spe].index(i) > self.voeux[spe].index(n):
                    n = i
            if self.voeux[spe].index(etu) > self.voeux[spe].index(n):
                return -2
            self.contient[spe].remove(n)
            self.contient[spe].append(etu)
            return n

    def reset(self):
        for i in self.contient:
            self.contient[i] = []
        for i in self.nVoeux:
            self.nVoeux[i] = 0


class VoeuxEtu :

    def __init__(self, fic):

        fichier = open(fic, "r")
        contenu = fichier.readlines()
        fichier.close()

        self.nbEtu = int(contenu[0].split()[0])
        self.tabEtu = [] #liste des liste comprenant le nom de l'etudiant et sa specialite affecte, utilise par gS
        self.voeux = [] #liste des voeux des etudiants
        self.nVoeux = [] #liste des rangs de voeux actuel des etudiant, utilise par gS
        for i in range( 1, self.nbEtu+1):
            contenu[i]=contenu[i].split()
            self.voeux.append(contenu[i][1:])
            self.nVoeux.append(0)
            self.tabEtu.append([contenu[i][0], ""])

    # Application de l'algorithme de Gale-Shapley
    def gS(self,spe):
        spe.reset()
        self.reset()
        # Tant que toutes les etu ne sont pas appareille
        while not self.isFull():
            # Pour chaque cle du dictionaire de la specialite
            for x in range(self.nbEtu):
                i = self.nVoeux[x]
                #print(x, i)
                if i > len(spe.capaSpe) :
                    print("Algorithme out of bound")
                    return
                # Si l'etu n'est pas appareillé
                if self.tabEtu[x][1] == '':
                    nameSpe = self.voeux[x][i]                 # Nom spe
                    #print(nameSpe)
                    t = spe.insertEtu(nameSpe, x)
                    #print(t)
                    if t != -2:
                        self.tabEtu[x][1] = nameSpe
                    if t != -1 and t != -2:
                        self.tabEtu[t][1] = ''
                    self.nVoeux[x] += 1
                #print(self.tabEtu[x])
            #print(self.tabEtu)
            #print(spe.contient)
            #print('')
        r = "Resultat algorithme de Gale-Shapley cote etudiants : "
        r += str(self.tabEtu)
        return r

    def isFull(self):
        for i in self.tabEtu :
            if i[1] == '':
                return False
        return True

    def reset(self):
        for i in self.tabEtu :
            i[1] = ''
        for i in self.nVoeux:
            self.nVoeux[i] = 0

def isWholeTrue(l):
    val = True
    for i in l:
        val = val and l[i]
    return val

def PLNEMinimize(etu, spe):
    ligne = []
    ligne.append("Minimize")
    ligne.append("obj : ")
    ligne.append("Subject To")
    binar = ""
    for i in range(len(spe.capaSpe)):
        tempS = "cspe" + str(i)+": "
        for j in range(etu.nbEtu):
            #print(i, j)
            ligne[1] += str(etu.voeux[j].index(spe.nomSpe[i]) + spe.voeux[spe.nomSpe[i]].index(j)) + " x" + str(i) + "," + str(j) + " + "
            binar += " x" + str(i) + "," + str(j)
            tempS += " x" + str(i) + "," + str(j) + " +"
        tempS = tempS[:-2]
        tempS += " = " + str(spe.capaSpe[spe.nomSpe[i]])
        ligne.append(tempS)
    for j in range(etu.nbEtu):
        tempS = "cetu" + str(j)+": "
        for i in range(len(spe.capaSpe)):
            tempS += " x" + str(i) + "," + str(j) + " +"
        tempS = tempS[:-2]
        tempS += " = " + str(1)
        ligne.append(tempS)
    ligne[1] = ligne[1][:-3]
    ligne.append("Binary")
    ligne.append(binar)
    ligne.append("End")
    s = ""
    #print(ligne)
    for i in ligne:
        s += i + "\n"
    return s

def PLNEEquite(etu, spe, n):
    ligne = []
    ligne.append("Minimize")
    ligne.append("obj : ")
    ligne.append("Subject To")
    binar = ""
    for i in range(len(spe.capaSpe)):
        tempS = "cspe" + str(i)+": "
        for j in range(etu.nbEtu):
            #print(i, j)
            ligne[1] += str(etu.voeux[j].index(spe.nomSpe[i]) + spe.voeux[spe.nomSpe[i]].index(j)) + " x" + str(i) + "," + str(j) + " + "
            binar += " x" + str(i) + "," + str(j)
            tempS += " x" + str(i) + "," + str(j) + " +"
        tempS = tempS[:-2]
        tempS += " = " + str(spe.capaSpe[spe.nomSpe[i]])
        ligne.append(tempS)
    for j in range(etu.nbEtu):
        tempS = "cetu" + str(j)+": "
        for i in range(len(spe.capaSpe)):
            tempS += " x" + str(i) + "," + str(j) + " +"
            ligne.append("cequispe" + str(i) + "," + str(j) + ": " + str(spe.voeux[spe.nomSpe[i]].index(j)) + " x" + str(i) + "," + str(j) + " <= " + str(n-1))
            ligne.append("cequietu" + str(i) + "," + str(j) + ": " + str(etu.voeux[j].index(spe.nomSpe[i])) + " x" + str(i) + "," + str(j) + " <= " + str(n-1))
        tempS = tempS[:-2]
        tempS += " = " + str(1)
        ligne.append(tempS)


    ligne[1] = ligne[1][:-3]
    ligne.append("Binary")
    ligne.append(binar)
    ligne.append("End")
    s = ""
    #print(ligne)
    for i in ligne:
        s += i + "\n"
    return s

def createFichier(nomFic, contenu):
    monFichier=open(nomFic,"w")
    monFichier.write(contenu)
    monFichier.close()

def test():
    s = VoeuxSpe("FichierPrefSpe.txt")

    e = VoeuxEtu("FichierPrefEtu2.txt")

    print(s.gS(e))
    print("")
    print(e.gS(s))
    print("")
    createFichier("PLNEMinimize.lp", PLNEMinimize(e, s))
    createFichier("PLNEEquite.lp", PLNEEquite(e, s, 2))
