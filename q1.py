def f(x):
    return x**3-4*x-9

def bisection(a,b,tolerance):
    mid_old = 0
    
    if f(a)*f(b)>=0:
        print("need <0")
    else:
        for i in range(100):
            
            mid = (a+b)/2
            if i >0:
                
                error = abs(mid-mid_old)/abs(mid)
                print("iteration",i,"mid",mid,"error:",error)
            
                if error<tolerance:
                    
                    break
            
            if f(a)*f(mid)<0:
                b=mid
            else:
                a=mid
            mid_old = mid
            
        return mid,i
    


a = float(input("enter a"))
b = float(input("enter b"))
tolerance = 0.001

res = bisection(a,b,tolerance)
print(res)
