
class GraphTSP:
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
        print("The number of cities is:", self.NbVariable)
        print("The cost matrix is: ", self.CostMatrix)
        
    
        
    
        
        