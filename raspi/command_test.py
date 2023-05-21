import os 
import sys
dir = os.path.realpath(__file__)
print(os.path.dirname(dir))
print(os.path.dirname(os.path.dirname(dir)))
print(sys.path)