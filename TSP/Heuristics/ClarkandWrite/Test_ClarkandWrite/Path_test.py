import os
import sys
currentRepertory =  os.path.dirname(os.path.realpath(__file__))
PrecRepertory = os.path.split(currentRepertory)[0]
sys.path.append(PrecRepertory)
from PackageClarkAlgorithme import  ClarkandWrite
