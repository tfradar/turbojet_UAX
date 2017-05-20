""
# Este .py se encargará de llamar a los datos clasificados y trabajar con ellos

import numpy as np
import cargadatos_turbojet_UAX as datos
from air_model import RealGas
from isentropic_gas import IsentropicGas

# Carga de funciones:
air = RealGas(cp_option='naca', gamma_option='standard')
gas = IsentropicGas(selected_cp_air_model='naca', selected_gamma_air_model='standard')


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

# Gasto corregido a funcionamiento nominal (108000 rpm)
Gc_108000 = gasto_corregido(datos.G_108000)

# Relación de compresión
def rel_comp(pf, pi):
    return pf / pi

#Relación de compresion difusor
pi20 = rel_comp(datos.p2t_108000, datos.p0t_108000)

# Relación de compresión compresor
pi32 = rel_comp(datos.p3t_108000, datos.p2t_108000)

# Relación de compresion camara de combustión
pi43 = rel_comp(datos.p4t_108000, datos.p3t_108000)

# Relación compresion turbina
pi54 = rel_comp(datos.p5t_108000, datos.p4t_108000)

# Función rendimiento compresor
def rendimiento_compresor(pi32, T2t, T3t):
    Tcomp = (T3t + T2t) / 2
    rend_comp = ((pi32 ** ((air.gamma_air(Tcomp) - 1) / air.gamma_air(Tcomp))) - 1) / ((T3t / T2t) - 1)

    return rend_comp

rend_comp_108000 = rendimiento_compresor(pi32, datos.T2t_108000, datos.T3t_108000)

# Función rendimiento turbina
def rendimiento_turbina(pi54, T4t, T5t):
    Tturb = (T5t + T4t) / 2
    rend_turb = ((T5t / T4t) - 1) / ((pi54 ** ((air.gamma_air(Tturb) - 1) / air.gamma_air(Tturb))) - 1)

    return rend_turb, Tturb

rend_turb_108000, Tturb = rendimiento_turbina(pi43, datos.T4t_108000, datos.T5t_108000)


print("Gasto corregido:", Gc_108000)
print('Relación de compresión del difusor:', pi20)
print('Relación de compresión del compresor:', pi32)
print("Rendimiento adiabático compresor:", rend_comp_108000)
print("T4t a 108000rpm:", datos.T4t_108000)
print('Relacion de compresión cámara de combustión:', pi43)
print('Consumo de combustible a 108000 RPM:', datos.c_108000)
print('Rendimiento adiabático de la turbina', rend_turb_108000)
print("Empuje a 36000 RPM:", datos.E_36000)
print("Empuje a 108000 RPM:", datos.E_108000)
print("Gasto a 108000 RPM:", datos.G_108000)


