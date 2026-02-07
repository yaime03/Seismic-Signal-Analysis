import numpy as np
def pendiente_central(x,y):
    num = np.size(x)
    pendientes = np.zeros(num-2)
    for idx in range(num - 2):
        pendientes[idx] = (y[idx + 2] - y[idx])/(x[idx + 2] - x[idx])
    return pendientes
