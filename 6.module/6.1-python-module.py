# importing modules
import math,os

squaroot = math.sqrt(36)
print(squaroot)

#print cpu count

cpu = os.cpu_count()
currentsir =os.getcwd
print(cpu,currentsir)

#from module import specific_name 
from math import sqrt, pi
print("Square root of 36:",sqrt(36))
print("Value of PI: ",pi)

#import module ad alias_name

import math as m

s= m.sqrt(25)
p=m.pi
print(s)
print(p)

# wild card import
from math import *

from math import sqrt, pi
print("Square root of 49:",sqrt(49))
print("Value of PI: ",pi)