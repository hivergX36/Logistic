
class GraphVRP:
    def __init__(self):
        self.NbEdges = 0 
        self.NbNodes = 0 
        self.NbCar = 0
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
        tab = []
        for indice in range(len(lignes)):
            tab.append(self.Parsechecknumber(lignes,indice))
        self.NbEdges = len(tab) - 1
        self.NbNodes = len(tab[1])
        self.NbCar = tab[0][0]
        self.CostMatrix = tab[1:len(tab)]
        self.visit = [False for i in range(self.NbNodes)]
        print("The number of cities is:", self.NbNodes)
        print("The cost matrix is: ", self.CostMatrix)
        print("The Number of car is: ", self.NbCar)
        
    
        
    
        
        