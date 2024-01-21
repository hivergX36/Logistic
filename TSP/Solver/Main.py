from PackageTSP import * 

print(filename)
print(currentRepertory)


Graph = Gph.GraphTSP()
Graph.parseMatrix(filename)

TSPmodel = pyo.ConcreteModel(name = ("TSP"))

"""
The Set of our TSP
"""

cities = Nodes(Graph.NbVariable)
TSPmodel.sites =  pyo.Set(initialize=cities, domain=pyo.Any, doc="set of all sites to be visited (𝕊)")

"""
The roads of our TSP in our set cities × cities
"""

TSPmodel.valid_arcs = pyo.Set(initialize= TSPmodel.sites * TSPmodel.sites, filter= rule_domain_arcs, doc= rule_domain_arcs.__doc__)

"""
The distance of our model 
"""

TSPmodel.distance = pyo.Param()

print(TSPmodel)

 



