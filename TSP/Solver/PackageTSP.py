import random
import os
import pyomo.environ as pyo
import GraphTSP as Gph
import os


"""
The package and the path to uses the ClarkandWrite Algorithm 
"""

currentRepertory =  os.path.dirname(os.path.realpath(__file__))

""" 
Here choose your file, for intance the file "InstanceCW_01.txt" is used
"""

filename = os.path.join(currentRepertory, "InstanceTSP.txt")

"""
Here the function rules to describe our variables and problems sets      
"""

def Nodes(NbVariable):
    Citylist = ["city_" + str(i) for i in range(NbVariable)]
    return Citylist


def rule_domain_arcs(model, i, j):
    """ All possible arcs connecting the sites (𝔸) """
    # only create pair (i, j) if site i and site j are different
    return (i, j) if i != j else None 



    