""
# Este .py se encargará de llamar a los datos clasificados y trabajar con ellos

import numpy as np
import cargadatos_turbojet_UAX as datos


# Función de Gasto corregido
def gasto_corregido(G):
    Tsl = 288           # K, Temp estandar
    psl = 101325        # Pa, pres estandar
    p = 93832.2187500   # Pa, pres ese día
    T = 302             # K, Temp ese día
    theta = T / Tsl
    delta = p / psl
    Gc = G * (np.sqrt(theta) / delta)

    return Gc

print(datos.G_108000)
print(gasto_corregido(datos.G_108000))

