from PackageVRP import * 

"""Our graph from our Package TSP.py"""
print(filename)
print(currentRepertory)
Graph = Gph.GraphVRP()
Graph.parseMatrix(filename)
Nbcities = Graph.NbNodes
NbCar = Graph.NbCar

"""Déclaration of our type of model"""

TSPmodel = pyo.ConcreteModel(name = ("TSP"))

"""
The Set of our TSP
"""


def Nodes(NbVariable):
    Citylist = [i for i in range(NbVariable)]
    return Citylist

cities = Nodes(Graph.NbNodes)
TSPmodel.sites =  pyo.Set(initialize=[i for i in range(Graph.NbNodes)], doc="Our cities")
TSPmodel.siteswithoutinitial = pyo.Set(initialize = (i for i in range(1,Graph.NbNodes)), doc = "Our cities without the depots" )
"""
The roads of our TSP in our set cities × cities
"""

def rule_domain_arcs(model, i, j):
    """ All possible arcs connecting the sites (𝔸) """
    # only create pair (i, j) if site i and site j are different
    return (i, j) if i != j else None 


TSPmodel.valid_arcs = pyo.Set(initialize= ((i,j) for i in range(Graph.NbNodes) for j in range((Graph.NbNodes))), filter= rule_domain_arcs, doc = "Our arcs")

def rule_distance(model, i, j):
    return Graph.CostMatrix[i][j]

"""What is the difference between initialize and filter ?"""
TSPmodel.distance = pyo.Param(TSPmodel.valid_arcs, initialize = rule_distance, doc = "the costs of the arcs of our graph")


"""Déclaration of our decision Variables"""

TSPmodel.x = pyo.Var(TSPmodel.valid_arcs,within=pyo.Binary, doc = "whether we choose the arc (i,j) or not")

"""Variable of MTZ constraint, we use the rank of the cities in order to eliminate the subtours"""

TSPmodel.r = pyo.Var(TSPmodel.siteswithoutinitial, within = pyo.Integers, doc = "Rank of the variable")


"""Defitnition of objective function"""

def obj_function(model):
    return sum(model.x[i,j]*model.distance[i,j] for i in model.sites for j in model.sites if i != j)


TSPmodel.objective = pyo.Objective(rule = obj_function,sense = pyo.minimize, doc = "Our objective")

"""Definition of our constraints"""

"""Each site is enterend once"""

def rule_site_entered_once(model,M):
    return sum(model.x[i,M] for i in model.sites if i != M) == 1

TSPmodel.constraint1 = pyo.Constraint(TSPmodel.sites,rule = rule_site_entered_once) 

"""Each site is exited once"""

def rule_site_outed_once(model,N):
    return sum(model.x[N,j] for j in model.sites if j != N) == 1

TSPmodel.constraint2 = pyo.Constraint(TSPmodel.siteswithoutinitial,rule = rule_site_outed_once) 


"""Number of depart equals number of arrival"""

def rule_depot_start(model):
    return sum(model.x[j,0] for j in model.siteswithoutinitial) == NbCar

TSPmodel.constraint_depot_start = pyo.Constraint(rule = rule_depot_start) 



"""Number of start to the depot"""

def rule_depot_entered(model):
    return sum(model.x[0,j] for j in model.siteswithoutinitial) == NbCar


TSPmodel.constraint_depot_entered = pyo.Constraint(rule = rule_depot_entered) 


"""Rank constraint"""


"""def rank_cosntraint(model,i,j):
    if i != j:
        return model.r[i] - model.r[j] + model.x[i,j] * Nbcities - model.x[i,j] <= Nbcities - 2
    else:
        return model.r[i] - model.r[j] == 0 
    
TSPmodel.constraint3 = pyo.Constraint(TSPmodel.siteswithoutinitial,TSPmodel.siteswithoutinitial, rule = rank_cosntraint)"""


"""Resolution"""

TSPmodel.pprint()
    

#Solves
solver = pyo.SolverFactory('glpk')
result = solver.solve(TSPmodel,tee = False)

#Prints the results
print(result)

List = list(TSPmodel.x.keys())
for i in List:
    if TSPmodel.x[i]() != 0:
        print(i,'--', TSPmodel.x[i]())