import pyomo.environ as pyEnv
import GraphTSP as Gph
import os





fileName = "InstanceNN.txt"
os.chdir("NearestNeighbourPython")
print(os.getcwd()) 


nearestneighbor = Gph()
nearestneighbor.parseMatrix(fileName)
nearestneighbor.Nearest()


