import numpy as np
from matplotlib import  pyplot as plt

def gasto_corregido(G, T, p):
    Tsl = 288 # Grados K, Temp estandar
    psl = 101325 # Pa, pres estandar
    theta = T / Tsl
    delta = p / psl
    Gc = G * (np.sqrt(theta) / delta)

    return Gc

datos_arrancada = np.loadtxt('Datos/arrancada_36000.ASC', comments='#')
#t[s] P0 [Pa]	P2 [Pa]	P3t [Pa]	P4t [Pa]	P5t [Pa]	P6t [Pa]	T2t [K]	T3t [K]	T4t1 [K]	T4t2 [K]	T5t1 [K]	T5t2 [K]	T8t [K]	Empuje [N]	fuel [kg/s]	aire [kg/s]	/s]
tiempo = datos_arrancada[:,0]
p3t = datos_arrancada[:,3]
E = datos_arrancada[:,14]
T4t1 = datos_arrancada[:,9]
T4t2 = datos_arrancada[:,10]
c = datos_arrancada[:,15]
G = datos_arrancada[:,16]


plt.figure()
plt.plot(tiempo,p3t)
plt.xlabel('tiempo [s]')
plt.ylabel('p3t')
plt.show()