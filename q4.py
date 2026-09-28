

def f(x):
     return x**3-x-2
 
 

def secant(x0,x1,tolerance):
    x_prev =x0
    x_old = x1
     
     
    for i in range(100):
         
        x_new = x_old - f(x_old)*(x_old-x_prev)/(f(x_old)-f(x_prev))
        if i >0:
             
            error = abs(x_new-x_old)/abs(x_new)
             
            if error<tolerance:
                 break
             
        x_prev = x_old
        x_old = x_new
    return x_new
    
res = secant(1,2,0.0001)
print(res)
        
         