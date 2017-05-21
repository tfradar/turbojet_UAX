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
T2t_108000 = datos_108000[:, 7]
T3t_108000 = datos_108000[:, 8]
T4t1_108000 = datos_108000[:,9]
T4t2_108000 = datos_108000[:,10]
T5t1_108000 = datos_108000[:,11]
T5t2_108000 = datos_108000[:,12]
T8t_108000 = datos_108000[:,13]
E_108000 = datos_108000[:,14]
c_108000 = datos_108000[:,15]
G_108000 = datos_108000[:,16]

# Se recogen unicamente los datos estables
p0t_108000 = np.mean(p0t_108000[30:40])
p2t_108000 = np.mean(p2t_108000[25:35])
p3t_108000 = np.mean(p3t_108000[25:35])
p4t_108000 = np.mean(p4t_108000[25:40])
p5t_108000 = np.mean(p5t_108000[25:40])
T2t_108000 = np.mean(T2t_108000[25:35])
T3t_108000 = np.mean(T3t_108000[28:38])
T4t1_108000 = np.mean(T4t1_108000[32:40])
T4t2_108000 = np.mean(T4t2_108000[25:35])
T5t1_108000 = np.mean(T5t1_108000[32:40])
T5t2_108000 = np.mean(T5t2_108000[25:35])
T4t_108000 = (T4t1_108000 + T4t2_108000) / 2
T5t_108000 = (T5t1_108000 + T5t2_108000) / 2
T8t_108000 = np.mean(T8t_108000[25:35])
E_108000 = np.mean(E_108000[35:40])
c_108000 = np.mean(c_108000[32:40])
G_108000 = np.mean(G_108000[28:38])

# Se clasifican los datos a 36000 rpm
tiempo_36000 = datos_36000[:,0]
p0t_36000 = datos_36000[:,1]
p2t_36000 = datos_36000[:,2]
p3t_36000 = datos_36000[:,3]
p4t_36000 = datos_36000[:,4]
p5t_36000 = datos_36000[:,5]
T2t_36000 = datos_36000[:, 7]
T3t_36000 = datos_36000[:, 8]
T4t1_36000 = datos_36000[:,9]
T4t2_36000 = datos_36000[:,10]
T5t1_36000 = datos_36000[:,11]
T5t2_36000 = datos_36000[:,12]
T8t_36000 = datos_36000[:,13]
E_36000 = datos_36000[:,14]
c_36000 = datos_36000[:,15]
G_36000 = datos_36000[:,16]

# Se recogen unicamente los datos estables
p0t_36000 = np.mean(p0t_36000[-10:])
p2t_36000 = np.mean(p2t_36000[-10:])
p3t_36000 = np.mean(p3t_36000[-10:])
p4t_36000 = np.mean(p4t_36000[-10:])
p5t_36000 = np.mean(p5t_36000[-10:])
T2t_36000 = np.mean(T2t_36000[-10:])
T3t_36000 = np.mean(T3t_36000[-10:])
T4t1_36000 = np.mean(T4t1_36000[-10:])
T4t2_36000 = np.mean(T4t2_36000[-10:])
T5t1_36000 = np.mean(T5t1_36000[-10:])
T5t2_36000 = np.mean(T5t2_36000[-10:])
T5t_36000 = (T5t1_108000 + T5t2_36000) / 2
T4t_36000 = (T4t1_108000 + T4t2_36000) / 2
T8t_36000 = np.mean(T8t_36000[-10:])
E_36000 = np.mean(E_36000[-10:])
c_36000 = np.mean(c_36000[-10:])
G_36000 = np.mean(G_36000[-10:])





