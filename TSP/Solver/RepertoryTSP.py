import random
import os
import pyomo.environ as pyo
import GraphTSP as Gph
import os


"""
The current path of our repertory 
    
"""

currentRepertory =  os.path.dirname(os.path.realpath(__file__))

""" 
Here choose your file, for intance the file "InstanceTSP.txt" is used
"""

filename = os.path.join(currentRepertory, "InstanceTSP.txt")