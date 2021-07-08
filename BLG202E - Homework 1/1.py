import math

def funct(x,h):
  
    derivative_f = (2 *math.cos(x + h/2) * math.sin(h/2)) / h
  
    return derivative_f
   
x0 = float(1.2)         #given approximation point for 𝑓′(1.2)

for power in range(-20,0):
    
    h = 10**power       #for h =⁡1e-20, 1e-19, ..., 1
    
    print(round(funct(x0,h),4))