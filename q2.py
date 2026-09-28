def f(x):
    return x**3+x-1

def falsi(a,b,tolerance):
    x_old = 0
    
    for i in range(100):
        xr = (a*f(b)-b*f(a))/(f(b)-f(a))
        
        if i >0:
            error = abs(xr-x_old)/abs(xr)
            print("iteration",i,"xr",xr,"error",error)
            
            if error<tolerance:
                break
            
        if f(a)*f(xr)<0:
            b=xr
        else:
            a=xr
            
        x_old = xr
        
    return i,xr

a = float(input("enter a"))
b = float(input("enter b"))
tolerance = 0.0001

res  = falsi(a,b,tolerance)
print(res)