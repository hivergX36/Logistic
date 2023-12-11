from Graph import Graph
import random
import os


fileName = "InstanceNN.txt"
os.chdir("NearestNeighbourPython")
print(os.getcwd()) 


nearestneighbor = Graph()
nearestneighbor.parseMatrix(fileName)
nearestneighbor.Nearest()

