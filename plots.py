""
# Este .py sirve para representar los datos gráficamente y ayudar a seleccionar los importantes

import numpy as np
import matplotlib.pyplot as plt

datos_108000 = np.loadtxt('Datos/108000.ASC', comments='#')
datos_36000 = np.loadtxt('Datos/arrancada_36000.ASC', comments='#')

tiempo_108000 = datos_108000[:, 0]
p0t_108000 = datos_108000[:,1]
p2t_108000 = datos_108000[:,2]
p3t_108000 = datos_108000[:, 3]
p4t_108000 = datos_108000[:,4]
E = datos_108000[:, 14]
T2t_108000 = datos_108000[:, 7]
T3t_108000 = datos_108000[:, 8]
T4t1 = datos_108000[:, 9]
T4t2 = datos_108000[:, 10]
c = datos_108000[:, 15]
G = datos_108000[:, 16]

tiempo_36000 = datos_36000[:, 0]
E_36000 = datos_36000[:, 14]



plt.figure()
plt.subplot(2,1,1)
plt.plot(tiempo_108000,p4t_108000,'x-r',label='E')
plt.ylabel('T2t')
plt.legend()
plt.subplot(2,1,2)
plt.plot(tiempo_108000,T3t_108000,'+-b',label='T3t')
plt.xlabel('tiempo [s]')
plt.ylabel('T3t')
plt.legend()
plt.show()

