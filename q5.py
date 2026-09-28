import sympy as sp

def f(x):
    return x**3+x-1

g1_fun = "(1-x)**(1/3)"
g2_fun="(1-x**3)"



#derivative of g1
x = sp.symbols('x')
g1_exp = sp.sympify(g1_fun)
dg1_exp = sp.diff(g1_exp,x)
dg1 = sp.lambdify(x,dg1_exp)
g1 = sp.lambdify(x,g1_fun)

#derivative of g2

g2_exp = sp.sympify(g2_fun)
dg2_exp = sp.diff(g2_exp,x)
dg2 = sp.lambdify(x,dg2_exp)
g2 = sp.lambdify(x,g2_fun)
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
            print(i,x_new,error)
            
            if error<tolerance:
                break
            
        x_old = x_new
        
    return i,x_new

x0= 0.5

tolerance = 0.0001

res = fixed(x0,tolerance)
print(res)
            
            

