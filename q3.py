import sympy as sp

fun = "x**3-2*x-5"
def f(x):
    return eval(fun)

x = sp.symbols('x')
fun_exp = sp.sympify(fun)
dfun_exp = sp.diff(fun_exp,x)

dfun = sp.lambdify(x,dfun_exp)




def newton(x0,tolerance):
    x_old = x0
    
    if (dfun(x_old)==0):
        print("undefined")
    else:
        for i in range(100):
            x_new = x_old - f(x_old)/dfun(x_old)
            if i >0:
                error = abs(x_new-x_old)/abs(x_new)
                print(i,x_new,error)
                
                if error<tolerance:
                    break
                
            x_old = x_new
            
        return i,x_new
    
    


x0 = float(input("enter one initial guess"))
tolerance = float(input("enter tolernce"))
res = newton (x0,tolerance)
print(res)


