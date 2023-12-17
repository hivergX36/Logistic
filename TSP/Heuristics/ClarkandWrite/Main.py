from PackageClarkAlgorithme import * 

print("fileName: ", filename)

print(filename)


clarkandWrite = ClarkandWrite()
clarkandWrite.parseMatrix(filename)
clarkandWrite.resolve()
clarkandWrite.displaySolution()