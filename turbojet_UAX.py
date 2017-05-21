""
# Este .py se encargará de llamar a los datos clasificados y trabajar con ellos

import numpy as np
import cargadatos_turbojet_UAX as datos
from air_model import RealGas
from isentropic_gas import IsentropicGas

# Carga de funciones:
air = RealGas(cp_option='naca', gamma_option='standard')
gas = IsentropicGas(selected_cp_air_model='naca', selected_gamma_air_model='standard')

# Datos
p = 93832.2187500  # Pa, pres ese día
T = 302  # K, Temp ese día
Tsl = 288  # K, Temp estandar
psl = 101325  # Pa, pres estandar
rho0 = psl / (287 * Tsl)
L = 46

# Datos turbina
radio_ext = 0.04
radio_int = 0.01
A0 = (radio_ext ** 2) * np.pi - (radio_int ** 2) * np.pi

# Función de Gasto corregido
def G_corregido(G):
    theta = T / Tsl
    delta = p / psl
    Gc = G * (np.sqrt(theta) / delta)

    return Gc

def c_corregido(G):
    theta = T / Tsl
    delta = p / psl
    Cc = G * (np.sqrt(theta) / delta)

    return Cc

# Relación de compresión
def rel_comp(pf, pi):
    return pf / pi

# Función rendimiento compresor
def rendimiento_compresor(pi32, T2t, T3t):
    Tcomp = (T3t + T2t) / 2
    rend_comp = ((pi32 ** ((air.gamma_air(Tcomp) - 1) / air.gamma_air(Tcomp))) - 1) / ((T3t / T2t) - 1)

    return rend_comp

# Función rendimiento turbina
def rendimiento_turbina(pi54, T4t, T5t):
    Tturb = (T5t + T4t) / 2
    rend_turb = ((T5t / T4t) - 1) / ((pi54 ** ((air.gamma_air(Tturb) - 1) / air.gamma_air(Tturb))) - 1)

    return rend_turb

# Velocidad entrada
def vel_entrada(Gc):
    v0 = Gc / (rho0 * A0)
    return v0

def tobera(T2t, T5t, p5t):
    p9 = p
    Ttob = (T5t + T2t) * 0.5
    T9 = (((p9 / p5t) ** ((air.gamma_air(Ttob) - 1) / air.gamma_air(Ttob)) - 1) + 1) * T5t

    return T9

# Velocidad salida
def vel_salida(T5t, T9):
    v9 = gas.velocity_from_stagnation_temperature(T5t, T9)

    return v9

# Actuaciones
def empuje_teorico(Gc, Cc, v8, v0):
    return (Gc + Cc) * v8 - Gc * v0
def eneto(Gc, Cc, v8, v0):
    return (Gc + Cc) * v8 - Gc * v0
# Impulso específico
def imp_esp(E, Gc):
    return E / Gc


# Rendimiento motor, propulsor y motopropulsor:
def rendimiento_TB(E, Cc, v9, v0, Gc):
    # Rendimiento motor:
    eta_m = (E * v0 + 0.5 * (Gc + Cc) * (v9 - v0) ** 2 - 0.5 * Cc * v0 ** 2) / (Cc * L)

    # Rendimiento propulsor:
    eta_p = E * v0 / (E * v0 + 0.5 * (Gc + Cc) * (v9 - v0) ** 2 - 0.5 * Cc * v0 ** 2)

    # Rendimiento motopropulsor:
    eta_mp = eta_m * eta_p

    return eta_m, eta_p, eta_mp

# Funcionamiento nominal (108000 RPM)

# Gasto corregido aire
Gc_108000 = c_corregido(datos.G_108000)

# Gasto corregido combustible
Cc_108000 = G_corregido(datos.c_108000)

#Relación de compresion difusor
pi20_108000 = rel_comp(datos.p2t_108000, datos.p0t_108000)

# Relación de compresión compresor
pi32_108000 = rel_comp(datos.p3t_108000, datos.p2t_108000)

# Relación de compresion camara de combustión
pi43_108000 = rel_comp(datos.p4t_108000, datos.p3t_108000)

# Relación compresion turbina
pi54_108000 = rel_comp(datos.p5t_108000, datos.p4t_108000)

# Rendimiento compresor
rend_comp_108000 = rendimiento_compresor(pi32_108000, datos.T2t_108000, datos.T3t_108000)

# Velocidad entrada
v0_108000 = vel_entrada(Gc_108000)

# Temperatura estatica salida
T9_108000 = tobera(datos.T2t_108000, datos.T5t_108000, datos.p5t_108000)

# Velocidad salida
v9_108000 = vel_salida(datos.T5t_108000, T9_108000)
print('v9 --------->', v9_108000)

# Empuje neto
Eneto_108000 = eneto(Gc_108000, Cc_108000, v9_108000, v0_108000)

# Rendimiento turbina
rend_turb_108000 = rendimiento_turbina(pi54_108000, datos.T4t_108000, datos.T5t_108000)
#Empuje teórico
E_teorico_108000 = empuje_teorico(Gc_108000, Cc_108000, v9_108000, v0_108000)
# Impulso específico
Ie_108000 = imp_esp(datos.E_108000, Gc_108000)

print("Gasto corregido a 108000 RPM:", Gc_108000)
print('Relación de compresión del difusor:', pi20_108000)
print('Relación de compresión del compresor:', pi32_108000)
print("Rendimiento adiabático compresor:", rend_comp_108000)
print("T4t a 108000rpm:", datos.T4t_108000)
print('Relación de compresión cámara de combustión:', pi43_108000)
print('Consumo de combustible a 108000 RPM:', datos.c_108000)
print('Rendimiento adiabático de la turbina', rend_turb_108000)
print('Empuje teórico a 108000 RPM', E_teorico_108000)
print('Empuje neto a 108000 RPM', Eneto_108000)
print("Empuje a 36000 RPM:", datos.E_36000)
print("Empuje a 108000 RPM:", datos.E_108000)
print("Impulso específico a 108000 RPM:", Ie_108000)


