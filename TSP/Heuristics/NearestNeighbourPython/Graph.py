
class Graph:
    def __init__(self):
        self.NbEdges = 0 
        self.NbNodes = 0 
        self.CostMatrix = []
        self.Solution = []
        self.chemin = []
        self.visit = []
        
    
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
        print("La table est: ", tab)
        print("La matrice des coût est: ", self.CostMatrix)
        
        
    def minlist(self,List):
        MinVector = min(List, key = lambda k: k[0])
        print("MinVector:" , MinVector)
        Min = MinVector[0]
        print("Min:" , Min)
        ind_min = MinVector[1]
        print("ind_Min: ", ind_min)
        return Min, ind_min 
        
        
        
    def Nearest(self):
        count = 0
        prec = 0
        succ = 0 
        cost = 0 
        listchoice = []
        self.visit[prec] = True
        while count < self.NbVariable - 1:
            listchoice = [[self.CostMatrix[prec][i],i] for i in range(self.NbVariable) if self.visit[i] == False]
            print(listchoice)
            cost,succ = self.minlist(listchoice)
            print("cost: ", cost, "succ: ", succ  )
            
            self.Solution.append([(prec,succ),cost])
            prec = succ
            self.visit[prec] = True
            count += 1 
        print(self.Solution)
        
    def displaySolution(self):
        
        print("Le chemin est: ")
        print(0, "->", end = " ")
        for i in range(len(self.Solution)):
            print(self.Solution[i][0][1], "->", end = " ")
    
        print(0)
        
        