""
# Este .py procesa los archivos de datos y te los devuelve ordenados""

import numpy as np

# Carga de datos recogidos
datos_108000 = np.loadtxt('Datos/108000.ASC', comments='#')   # 108000 rpm


# Se clasifican los datos a 108000 rpm
tiempo_108000 = datos_108000[:,0]
p3t_108000 = datos_108000[:,3]
E_108000 = datos_108000[:,14]
T4t1_108000 = datos_108000[:,9]
T4t2_108000 = datos_108000[:,10]
c_108000 = datos_108000[:,15]
G_108000 = datos_108000[:,16]

# Se recogen unicamente los datos interesantes
p3t_108000 = np.mean(p3t_108000[25:35])
E_108000 = np.mean(E_108000[35:40])
T4t1_108000 = np.mean(T4t1_108000[32:40])
T4t2_108000 = np.mean(T4t2_108000[25:35])
T4t_108000 = (T4t1_108000 + T4t2_108000) / 2
c_108000 = np.mean(c_108000[32:40])
G_108000 = np.mean(G_108000[28:38])

