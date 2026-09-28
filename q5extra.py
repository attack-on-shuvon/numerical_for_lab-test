def f(x):
    return x**3+x-1

def g1(x):
    return (1-x)**(1/3)

def g2(x):
    return (1-x**3)

def dg1(x):
    return 1/(3*(1-x)**(2/3))

def dg2(x):
    return  -3*x**2

x0=0.5

if abs(dg1(x0))<1:
    print("g1 is convergence")
    g=g1
    
else:
    print("g2 is convergence")
    g=g2
    
    
    
def fixed(x0,tolerance):
    x_old = x0
    for i in range(100):
        x_new = g(x_old)
        if i>0:
            error = abs(x_new-x_old)/abs(x_new)
            
            if error<tolerance:
                break
            
        x_old = x_new
        
    return i,x_new


res = fixed(0.5,0.0001)
print(res)
    
