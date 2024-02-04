from PackageVRP import * 

"""Our graph from our Package TSP.py"""
print(filename)
print(currentRepertory)
Graph = Gph.GraphVRP()
Graph.parseMatrix(filename)
Nbcities = Graph.NbNodes
NbCar = Graph.NbCar
Capacity = Graph.Capacity

"""Déclaration of our type of model"""

VRPmodel = pyo.ConcreteModel(name = ("TSP"))

"""
The Set of our TSP
"""

def Nodes(NbVariable):
    Citylist = [i for i in range(NbVariable)]
    return Citylist

cities = Nodes(Graph.NbNodes)
VRPmodel.sites =  pyo.Set(initialize=[i for i in range(Graph.NbNodes)], doc="Our cities")
VRPmodel.siteswithoutinitial = pyo.Set(initialize = (i for i in range(1,Graph.NbNodes)), doc = "Our cities without the depots" )
VRPmodel.demand = pyo.Set(initialize= [i for i in Graph.demand], doc = "consummer demand")
"""
The roads of our TSP in our set cities × cities
"""

def rule_domain_arcs(model, i, j):
    """ All possible arcs connecting the sites (𝔸) """
    # only create pair (i, j) if site i and site j are different
    return (i, j) if i != j else None 


VRPmodel.valid_arcs = pyo.Set(initialize= ((i,j) for i in range(Graph.NbNodes) for j in range((Graph.NbNodes))), filter= rule_domain_arcs, doc = "Our arcs")

def rule_distance(model, i, j):
    return Graph.CostMatrix[i][j]

"""What is the difference between initialize and filter ?"""

VRPmodel.distance = pyo.Param(VRPmodel.valid_arcs, initialize = rule_distance, doc = "the costs of the arcs of our graph")

"""Declaration of demand"""

def rule_demand(model,d):
    return Graph.demand[d]

VRPmodel.d = pyo.Param(VRPmodel.siteswithoutinitial, initialize = rule_demand, doc = "The demands")


"""Déclaration of our decision Variables"""

VRPmodel.x = pyo.Var(VRPmodel.valid_arcs,within=pyo.Binary, doc = "whether we choose the arc (i,j) or not")

"""Variable of MTZ constraint, we use the rank of the cities in order to eliminate the subtours"""

def FcBound(model,i):
    return (0,Graph.upperbound[i])

VRPmodel.u = pyo.Var(VRPmodel.siteswithoutinitial,bounds=FcBound,  doc = "charge of vehicle after visiting consummer i")


"""Defitnition of objective function"""

def obj_function(model):
    return sum(model.x[i,j]*model.distance[i,j] for i in model.sites for j in model.sites if i != j)


VRPmodel.objective = pyo.Objective(rule = obj_function,sense = pyo.minimize, doc = "Our objective")

"""Definition of our constraints"""

"""Each site is enterend once"""

def rule_site_entered_once(model,M):
    return sum(model.x[i,M] for i in model.sites if i != M) == 1

VRPmodel.constraint1 = pyo.Constraint(VRPmodel.siteswithoutinitial,rule = rule_site_entered_once) 

"""Each site is exited once"""

def rule_site_outed_once(model,N):
    return sum(model.x[N,j] for j in model.sites if j != N) == 1

VRPmodel.constraint2 = pyo.Constraint(VRPmodel.siteswithoutinitial,rule = rule_site_outed_once) 


"""Number of depart equals number of arrival"""

def rule_depot_start(model):
    return sum(model.x[j,0] for j in model.siteswithoutinitial) == NbCar

VRPmodel.constraint_depot_start = pyo.Constraint(rule = rule_depot_start) 



"""Number of start to the depot"""

def rule_depot_entered(model):
    return sum(model.x[0,j] for j in model.siteswithoutinitial) == NbCar


VRPmodel.constraint_depot_entered = pyo.Constraint(rule = rule_depot_entered) 


"""Rank constraint"""


def VRP_rank_cosntraint(model,i,j):
    if  j!= i:
        return model.u[j] - model.u[i]  <= (1 - model.x[i,j]) * Capacity - model.d[j]
    else:
        return model.u[j] - model.u[i] == 0 
    
VRPmodel.constraint3 = pyo.Constraint(VRPmodel.siteswithoutinitial,VRPmodel.siteswithoutinitial, rule = VRP_rank_cosntraint)


"""Resolution"""

VRPmodel.pprint()
    

#Solves
solver = pyo.SolverFactory('glpk')
result = solver.solve(VRPmodel,tee = False)

#Prints the results
print(result)

List = list(VRPmodel.x.keys())
for i in List:
    if VRPmodel.x[i]() != 0:
        print(i,'--', VRPmodel.x[i]())