import numpy as np
def area_trapezoidal(x,y,b):
    n=np.size(x); total_area=0; na= np.zeros(n-1)
    for k in range(n-1):
        if b==0:
                area = ((y[k]+y[k+1])/2)*(x[k+1]-x[k])
                total_area = total_area + area
        elif b==1:
                area =(( y[k] + y[k+1]) / 2) * (x [k+1]-x[k])
                total_area = total_area + area
                na[k] = total_area
        else:
            total_area = "No esta dentro de las opciones "
            return total_area
    if b==0:
        return total_area
    elif b==1:
        return na