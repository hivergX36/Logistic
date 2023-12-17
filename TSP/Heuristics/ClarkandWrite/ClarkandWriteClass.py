
class ClarkandWrite:
    def __init__(self):
        self.NbEdges = 0 
        self.NbNodes = 0 
        self.CostMatrix = []
        self.Solution = []
        self.Saving = []
        self.visit = []
        self.cost = 0 
        
    
    def Parsechecknumber(self,lignes,indice):
        ParsedList = []
        compteur1 = 0
        compteur2 = 0
        while(lignes[indice][compteur1] != '\n' and lignes[indice][compteur2] != '\n'):
              while(lignes[indice][compteur2] != " " and lignes[indice][compteur2] != '\n'):
                    compteur2 += 1
              ParsedList.append(int(lignes[indice][compteur1:compteur2]))
              compteur1 = compteur2 + 1
              compteur2 = compteur1

   
              if compteur1 > len(lignes[indice]) - 1:
                    break
                
        
        return ParsedList
 
      
    def parseMatrix(self,text):
        fichier = open(text, "r",encoding="utf8")
        lignes = fichier.readlines()
        print(lignes)
        tab = [self.Parsechecknumber(lignes,indice) for indice in range(len(lignes))]
        self.NbEdges = len(tab)
        self.NbVariable = len(tab[0])
        self.CostMatrix = tab
        self.visit = [False for i in range(self.NbVariable)]
        self.saving = [[self.CostMatrix[0][i] + self.CostMatrix[0][j] - self.CostMatrix[i][j],[i,j]] for i in range(1,self.NbVariable) for j in range(i + 1,self.NbVariable)]
        print("La table est: ", tab)
        print("La matrice des coût est: ", self.CostMatrix)
        print("Les savings sont: ", self.saving)
        
 

    def intersection(self,l1,l2):
        nbintersection = 0
        for i in range(len(l1)):
            for j in range(len(l2)):
                if l1[i] == l2[j]:
                    nbintersection += 1
        return nbintersection
    
        
    #Vérifier l'intersection à droite où à gauche   
    
    
    def assigned(self,l1,l2):
        if(l1[0] == l2[0]):
            l1.insert(0,l2[-1])
        elif(l1[0] == l2[-1]):
            l1.insert(0,l2[0])
        elif(l1[-1] == l2[0]):
            l1.append(l2[-1])
        elif(l1[-1] == l2[-1]):
            l1.append(l2[0])
        return l1
    
    
    
    def Petalfusion(self):
        print("petal fusion")
        nbintersection = 0
        indlist = []
        for k in range(len(self.Solution) - 1):
            for j in range(k,len(self.Solution)):
                nbintersection = self.intersection(self.Solution[k],self.Solution[j])
                if nbintersection == 1:
                    print("petal intersection: ", nbintersection)
                    indlist.append(j)
                    self.Solution[k] = self.assigned(self.Solution[k],self.Solution[j])
        
        self.Solution = [self.Solution[i] for i in range(len(self.Solution)) if i not in indlist]
                
            
        

           
            
        
                
    #Terminer la fonction de résolution, ajouter liste plus récursivité   
        
        
    def resolve(self):
        nbitersection = 0 
        count = 0
        self.Solution = []
        self.saving.sort(key = lambda k: k[0], reverse = True)
        self.Solution.append(self.saving[0][1])
        print("saving", self.saving)
        print("choix", self.Solution)
        for k in range(len(self.saving)):
            count = 0 
            for i in range(len(self.Solution)):
                count += 1 
                print("count", count)
                print("Solution", self.Solution)
                print("Solution_",i, self.Solution[i])
                nbintersection = self.intersection(self.Solution[i],self.saving[k][1])
                print("saving", self.saving[k][1])
                print("nb intersection", nbintersection)
                if nbintersection == 1:
                    self.Solution[i] =  self.assigned(self.Solution[i],self.saving[k][1])
                    print("Un petal est renforce")
                    break
                elif nbintersection == 0 and count == len(self.Solution):
                    self.Solution.append(self.saving[k][1])
                    print("un nouveau chemin est cree")
                elif nbintersection == 2:
                    print("Le chemin existe deja")
                    break
            self.Petalfusion()
        
        self.Solution = self.Solution[0]
        print(self.Solution)
                    
            
        
     
        
    def displaySolution(self):
        print("Le chemin est: ")
        print(0, "->", end = " ")
        for i in range(len(self.Solution)):
            print(self.Solution[i], "->", end = " ")
        print(0)
        