import math

#Dos motores trifásicos de 460 V, conexiones en delta, cargas continuas, están conectados a un #alimentador como se muestra en la figura 2, el motor de 50 HP es de rotor devanado con factor de
#potencia 0.85 y el de 40 es de jaula de ardilla con factor de potencia de 0.8. Ambos motores se les
#corrigen el factor de potencia de forma individual a 0.95 para evitar la multa por bajo factor de potencia.
#Aplicando los artículos 430 del NEC, 460.8 y 460.9, determine:




#a) Los conductores THHN según NEC 310.15(B)(16); de los ramales de los motores y del alimentador. (5%)

# Corriente nominal (plena carga) de los motores según el NEC 430.250
# motor 50 hp, a 460 V
vl_50 = 460 # V
ipc_50 = 65 # A
# motor 40 hp, a 460 V
vl_40 = 460 # V
ipc_40 = 52 # A

# Estos se deben tener al 125% según el NEC 430.6
print(ipc_50*1.25)
print(ipc_40*1.25)

# Además, se calcula la corriente que pasa por el ramal de la carga instalada
i_carga = 48e3*0.75/(480*math.sqrt(3))
#i_carga *= 1.25
print(i_carga)

# Se buscan los conductores que cumplan con estos valores según NEC 310.15(B)(16) o 310.15(B)(19)
# como los amperajes son menores a 100 A se usa la columnda de 60ºC
# Para el ramal de 50 hp se tienen 81.25 A por lo que se usa un #3 AWG pero este no está disponible
# en CR, entonces se opta por #2
# Para el ramal de 40 hp se tienen 65.0 A por lo que se usa un #4 AWG
# Para el ramal de la carga se tienen 43.3 A por lo que se usa un #6 AWG

# Calcular la corriente en el alimentador, se toma el 125% del motor más potente, más el 100% de los
# demás motores y cargas del conjunto
i_alimentador = (ipc_50 + i_carga)*1.25 + ipc_40
print(i_alimentador)
# Como la corriente es de 187.38 A se usa la columna de 75ºC, por lo que se usa un AWG #3/0




#b) La sobrecarga y contactores NEMA de los motores. (5%)

# Contactores del motor según tablas NEMA
# NEMA 4 (máximo 100 hp) para 460 V, trifásico, 50 hp
# NEMA 3 (máximo 50 hp) para 460 V, trifásico, 40 hp




#c) El disyuntor termomagnético de tiempo inverso del circuito ramal de los motores y del alimentador. (5%)




#d) El tamaño en VAR trifásicos de cada capacitor requerido por cada motor. (2.5% cada uno)

#Un HP es equivalente a 746 Watts, por lo tanto se define la conversión de HP a kW
hp_a_kw = lambda hp: hp*746/1000

#Conversión de kW a kVA se divide por el FP, por lo tanto se define como
kw_a_kva = lambda kw,fp : kw/fp

#Obtención de kVAR (Potencia Reactiva) a partir de kVA (Potencia Aparente) y el FP
def kva_a_kvar(kva, fp):
    #ang = math.acos(fp)*180/3.1415167915
    ang = math.acos(fp)
    kvar = math.sin(ang)*kva
    return(kvar)

#Calculo de kW a partir de distintos valores
def calc_kw(il,vl,fp):
    return(math.sqrt(3)*il*vl*fp/1000)

#Correción de potencia reactiva para motores a partir de kw
def kw_banco_kvar(kw, fpi, fpf):
    s1 = kw/fpi
    s2 = kw/fpf
    q1 = s1*math.sin(math.acos(fpi))
    q2 = s2*math.sin(math.acos(fpf))
    return(q1-q2)

#Correción de potencia reactiva para motores a partir de hp
def hp_banco_kvar(hp, fpi, fpf):
    p = hp_a_kw(hp)
    return(p*(math.tan(math.acos(fpi))-math.tan(math.acos(fpf))))

def main():
    print(hp_banco_kvar(calc_kw(ipc_40,vl_40,0.85),0.85,0.95))
    print(hp_banco_kvar(calc_kw(ipc_50,vl_50,0.85),0.8,0.95))

main()

#460.9
#
#ajuste de sobrecarga con la suma con el campo de capacitores
#
#para conductor no se considera corriente corregida
