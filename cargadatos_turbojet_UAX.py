""
# Este Archivo procesa los archivos de datos y te los devuelve ordenados""

import numpy as np

# Carga de datos recogidos
datos_108000 = np.loadtxt('Datos/108000.ASC', comments='#')   # 108000 rpm
datos_36000 = np.loadtxt('Datos/arrancada_36000.ASC', comments='#') # 36000 rpm


# Se clasifican los datos a 108000 rpm
tiempo_108000 = datos_108000[:,0]
p0t_108000 = datos_108000[:,1]
p2t_108000 = datos_108000[:,2]
p3t_108000 = datos_108000[:,3]
p4t_108000 = datos_108000[:,4]
p5t_108000 = datos_108000[:,5]
E_108000 = datos_108000[:,14]
T2t_108000 = datos_108000[:, 7]
T3t_108000 = datos_108000[:, 8]
T4t1_108000 = datos_108000[:,9]
T4t2_108000 = datos_108000[:,10]
T5t1_108000 = datos_108000[:,11]
T5t2_108000 = datos_108000[:,12]
c_108000 = datos_108000[:,15]
G_108000 = datos_108000[:,16]

# Se clasifican los datos a 36000 rpm
E_36000 = datos_36000[:,14]

# Se recogen unicamente los datos interesantes
p0t_108000 = np.mean(p0t_108000[30:40])
p2t_108000 = np.mean(p2t_108000[25:35])
p3t_108000 = np.mean(p3t_108000[25:35])
p4t_108000 = np.mean(p4t_108000[25:40])
p5t_108000 = np.mean(p5t_108000[25:40])
E_108000 = np.mean(E_108000[35:40])
T2t_108000 = np.mean(T2t_108000[25:35])
T3t_108000 = np.mean(T3t_108000[28:38])
T4t1_108000 = np.mean(T4t1_108000[32:40])
T4t2_108000 = np.mean(T4t2_108000[25:35])
T5t1_108000 = np.mean(T5t1_108000[32:40])
T5t2_108000 = np.mean(T5t2_108000[25:35])
T5t_108000 = (T5t1_108000 + T5t2_108000) / 2
T4t_108000 = (T4t1_108000 + T4t2_108000) / 2
c_108000 = np.mean(c_108000[32:40])
G_108000 = np.mean(G_108000[28:38])


E_36000 = np.mean(E_36000[-10:])




