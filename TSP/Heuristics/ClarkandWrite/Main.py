from ClarkandWrite import ClarkandWrite
import random
import os


fileName = "InstanceNN.txt"
os.chdir("ClarkandWrite")
print(os.getcwd()) 


clarkandWrite = ClarkandWrite()
clarkandWrite.parseMatrix(fileName)
clarkandWrite.resolve()