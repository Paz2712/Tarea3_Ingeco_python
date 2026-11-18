# el %% sirve para activar el kernel de jupiter en vscode
# al crear una celda ejecutable
# %%

# ----------------------------------------------------------
# IMPORTACIÓN DE LIBRERÍAS
# ----------------------------------------------------------


import numpy as np
import numpy_financial as npf
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

#Tarea3_2025730294_García
#sea mi rol 202573029-4 ultimos 2 digitos componen la variable k = 94

def Factor_invercion(K):
    F = 1 + K/1000
    return(F)

#tasa de descuento real efectiva anual 
def TdescuentoRFA(K):
    R = 0.15 * K
    R= R+4
    R= R/100
    return(R)

def Sacar_FlujoCaja(**Base):
    FC = 0
    for Capital in Base:
        FC= Base[Capital]/((1+r)**i)
        print(FC)
        print(" || ")
    print("\n")
    return(FC)
    

# ==========================================================
# INICIO DEL PROGRAMA
# ==========================================================

k= 29
semilla= 2025730294
f= Factor_invercion(k)
r= TdescuentoRFA(k)

print(k, "(K) ", f, "(Factor de inversión) ", round(r,2), "(Tasa de descuento) ", semilla, "(rol)\n")
#calculos de flujo de caja
# ==========================================================
# PROYECTO A
# ==========================================================

FlujoDeCaja_A = {
    # La inversión inicial se ajusta por f
    'inversion_inicial (Año 0)': -18000000 * f,
        'Año 1':  5000000,
        'Año 2': 6500000,
        'Año 3': 7500000,
        'Año 4': 9000000,
        'Recuperacion(Año 4)': 2000000
}

FC = 0
i= 0
# Lista final de flujos usada para VAN y TIR
FlujoA= [0,0,0,0,0]

# Construcción del flujo de caja
for Capital in FlujoDeCaja_A:
    
    FC= FlujoDeCaja_A[Capital] #/((1+r)**i)
    if i == 5:
        FlujoA[4]+= FC
        i= i -1
        print(FlujoA[i], " ||")
    
    # Cuando llega la recuperación del año 4
    # se suma al flujo del mismo año
    else:
        FlujoA[i]= FC
        print(FlujoA[i], " ||")
        i+= 1
    
    
    
# Cálculo del VAN y la TIR
VanA= round(npf.npv(r,FlujoA),2)
TirA= round(npf.irr(FlujoA),2)
print("Van FC_ A: ",VanA, "Tir FC_ A: ", TirA*100 , "%")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

FlujoDeCaja_B = {
    'inversion_inicial (Año 0)': -36000000 * f,
            'Año 1':  7000000,
            'Año 2': 10000000,
            'Año 3': 14000000,
            'Año 4': 18000000,
            'Recuperacion(Año 4)': 4000000
}

FC= 0
i= 0
FlujoB= [0,0,0,0,0]
for Capital in FlujoDeCaja_B:
    
    FC= FlujoDeCaja_B[Capital] #/((1+r)**i)
    if i == 5:
        FlujoB[4]+= FC
        i= i -1
        print(FlujoB[i], " ||")
    else:
        FlujoB[i]= FC
        print(FlujoB[i], " ||")
        i+= 1
    
    
   
VanB= round(npf.npv(r,FlujoB),2)
TirB= round(npf.irr(FlujoB),2)
print("Van FC_ B: ",VanB, "Tir FC_ B: ", TirB*100, "%")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

FlujoDeCaja_C = {
    'inversion_inicial (Año 0)': -10000000 * f,
        'Año 1':  4500000,
        'Año 2': 3000000,
        'Año 3': 5500000,
        'Año 4': 3000000,
        'Recuperacion(Año 4)': 1000000
}

FC= 0
i= 0
FlujoC= [0,0,0,0,0]
for Capital in FlujoDeCaja_C:
    
    FC= FlujoDeCaja_C[Capital] #/((1+r)**i)
    if i == 5:
            FlujoC[4]+= FC
            i= i -1
            print(FlujoC[i], " ||")
    else:
        FlujoC[i]= FC
        print(FlujoC[i], " ||")
        i+= 1
    
    

VanC= round(npf.npv(r,FlujoC),2)
TirC= round(npf.irr(FlujoC),2)
print("Van FC_ B: ",VanC, "Tir FC_ B: ", TirC*100,"%")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# ==========================================================
# TABLAS RESUMEN
# ==========================================================

# Tabla de flujos construidos
print("Resumen: (↓)\n")

TablaFlujos = pd.DataFrame({
    "Proyecto": ["A", "B", "C"],
    "Año 0": [FlujoA[0], FlujoB[0], FlujoC[0]],
    "Año 1": [FlujoA[1], FlujoB[1], FlujoC[1]],
    "Año 2": [FlujoA[2], FlujoB[2], FlujoC[2]],
    "Año 3": [FlujoA[3], FlujoB[3], FlujoC[3]],
    "Año 4": [FlujoA[4], FlujoB[4], FlujoC[4]]
})

TablaFlujos = TablaFlujos.set_index("Proyecto")

display(TablaFlujos)

# Tabla de indicadores financieros
TablaResultados = pd.DataFrame({
    "Proyecto":["A","B","C"],
    "VAN(CLP)":[VanA,VanB,VanC],
    "TIR (%)":[TirA*100,TirB*100,TirC*100],
    "Inversión Inicial":[FlujoA[0],FlujoB[0],FlujoC[0]]
})

TablaResultados= TablaResultados.set_index("Proyecto")

display(TablaResultados)

"""
Parte 2; en jupiter explicación de porque se escoje el proyecto A
"""


# ==========================================================
# PARTE 3 - ANÁLISIS DE SENSIBILIDAD
# ==========================================================

#sea el proyecto escojido el A
# Se analiza el proyecto seleccionado
mValores = [0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4]
# Lista donde se almacenarán los VAN calculados

VanSensibilidad = []

i=0

# Copia auxiliar del flujo original
Valor = [0,0,0,0,0]

while (i < 5):
    Valor[i] = FlujoA[i]
    i+= 1

Valores = [0,0,0,0,0]

# Evaluación de los nueve escenarios
for m in mValores:
    
    # La inversión inicial queda fija
    Valores[0] = Valor[0]
    
    # Los flujos operativos se multiplican por m
    Valores[1] = Valor[1] * m
    Valores[2] = Valor[2] * m
    Valores[3] = Valor[3] * m
    Valores[4] = Valor[4] * m     
    
    VAN = npf.npv(r, Valores)

    #agregamos VAN en cada ciclo
    VanSensibilidad.append(VAN)

    print("m =",m)
    print("VAN =",VAN)
    print("----------------")
    
    
# Tabla de sensibilidad
TablaSensibilidadesM = pd.DataFrame({
    "Valor de [ m ]": [0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4],
    "Van": [round(VanSensibilidad[0],2),round(VanSensibilidad[1],2),round(VanSensibilidad[2],2)
            ,round(VanSensibilidad[3],2),round(VanSensibilidad[4],2), round(VanSensibilidad[5],2)
            ,round(VanSensibilidad[6],2),round(VanSensibilidad[7],2),round(VanSensibilidad[8],2),
            ]
})

TablaSensibilidadesM = TablaSensibilidadesM.set_index("Valor de [ m ]")
display(TablaSensibilidadesM)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Resumen:")

# Gráfico VAN vs m
plt.figure(figsize=(8,5))

plt.plot(mValores,VanSensibilidad,marker="o")

plt.axhline(0,color="red")

plt.xlabel("Factor m")

plt.ylabel("VAN (CLP)")

plt.title("Sensibilidad del VAN")

plt.grid()

plt.show()

"""
explicacion grafico en jupyter
"""

# ==========================================================
# BÚSQUEDA DEL VALOR CRÍTICO DE m
# ==========================================================
# Se busca el valor de m donde VAN≈0
for m in np.arange(0.6,1.41,0.01):
    
    Valores[0] = Valor[0]
    Valores[1] = Valor[1] * m
    Valores[2] = Valor[2] * m
    Valores[3] = Valor[3] * m
    Valores[4] = Valor[4] * m     
        
    VAN = npf.npv(r, Valores)
    
    VanSensibilidad.append(VAN)

    
    # Se considera suficientemente cercano a cero
    if abs(VAN) < 50000:
        print("m critico =",m)
        print("VAN =",VAN)
        break


# ----------------------------------------------------------
# CREACIÓN DE LA TABLA DE SENSIBILIDAD
# ----------------------------------------------------------
# Se construye un DataFrame para mostrar
# los resultados del análisis de sensibilidad.
# Cada fila representa un valor distinto del factor m y
# su respectivo VAN calculado anteriormente.

TablaSensibilidadesM = pd.DataFrame({

    # Valores evaluados para el factor de ajuste m
    "Valor de [ m ]": [0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4],

    # VAN obtenido para cada valor de m.
    # Se utiliza round(...,2) para mostrar los resultados
    # con dos decimales y facilitar la lectura.
    "Van": [
        round(VanSensibilidad[0],2),
        round(VanSensibilidad[1],2),
        round(VanSensibilidad[2],2),
        round(VanSensibilidad[3],2),
        round(VanSensibilidad[4],2),
        round(VanSensibilidad[5],2),
        round(VanSensibilidad[6],2),
        round(VanSensibilidad[7],2),
        round(VanSensibilidad[8],2),
    ]
})

TablaSensibilidadesM = TablaSensibilidadesM.set_index("Valor de [ m ]")

# Muestra la tabla en formato tabular dentro del Notebook.
display(TablaSensibilidadesM)
print("~~~~~~~~~~~~~~~~~~~~~+")

# ==========================================================
# PARTE 4 - SIMULACIÓN DE MONTE CARLO
# ==========================================================


# Generador aleatorio reproducible
rng = np.random.default_rng(2025730294)

# Distribución uniforme
m_uniforme = rng.uniform(0.60,1.40,1000)

VanUniforme = []

# Cálculo de 1000 VAN
for m in m_uniforme:
    
    Valores[0] = Valor[0]
    Valores[1] = Valor[1] * m
    Valores[2] = Valor[2] * m
    Valores[3] = Valor[3] * m
    Valores[4] = Valor[4] * m     
            
    VAN = npf.npv(r, Valores)

    VanUniforme.append(VAN)


# Distribución triangular
m_triangular = rng.triangular(0.60,1.00,1.40,1000)

VanTriangular = []

for m in m_triangular:

    Valores[0] = Valor[0]
    Valores[1] = Valor[1] * m
    Valores[2] = Valor[2] * m
    Valores[3] = Valor[3] * m
    Valores[4] = Valor[4] * m     
            
    VAN = npf.npv(r, Valores)

    VanTriangular.append(VAN)

# ----------------------------------------------------------
# HISTOGRAMA DISTRIBUCIÓN UNIFORME
# ----------------------------------------------------------


plt.hist(VanUniforme,bins=20)

plt.axvline(0,color='red')

plt.title("Monte Carlo Uniforme")

plt.xlabel("VAN")

plt.ylabel("Frecuencia")

plt.show()

# ----------------------------------------------------------
# HISTOGRAMA DISTRIBUCIÓN TRIANGULAR
# ----------------------------------------------------------

plt.hist(VanTriangular,bins=20)

plt.axvline(0,color='red')

plt.title("Monte Carlo Triangular")

plt.xlabel("VAN")

plt.ylabel("Frecuencia")

plt.show()

# ----------------------------------------------------------
# ESTADÍSTICAS RESUMEN
# ----------------------------------------------------------

PositivosU = np.sum(np.array(VanUniforme) > 0)
NegativosU = np.sum(np.array(VanUniforme) < 0)

PositivosT = np.sum(np.array(VanTriangular) > 0)
NegativosT = np.sum(np.array(VanTriangular) < 0)

print("UNIFORME")
print("Positivos:",PositivosU)
print("Negativos:",NegativosU)
print("% Positivos:",PositivosU/1000*100)
print("VAN Promedio:",np.mean(VanUniforme))
print("Desv.Est:",np.std(VanUniforme))

print()

print("TRIANGULAR")
print("Positivos:",PositivosT)
print("Negativos:",NegativosT)
print("% Positivos:",PositivosT/1000*100)
print("VAN Promedio:",np.mean(VanTriangular))
print("Desv.Est:",np.std(VanTriangular))

# ----------------------------------------------------------
# TABLA COMPARATIVA FINAL
# ----------------------------------------------------------


TablaResultadosHistogramas = pd.DataFrame({
    "Histogramas":["Uniforme","Triangular"],
    "Positivos":[PositivosU,PositivosT],
    "Negativos:": [NegativosU,NegativosT],
    "% Positivos:":[PositivosU/1000*100,PositivosT/1000*100],
    "Inversión Inicial":[round(np.mean(VanUniforme),2), round(np.mean(VanTriangular),2)],
    "Desv.Est:":[round(np.std(VanUniforme),2) , round(np.std(VanTriangular),2)]
})

TablaResultadosHistogramas= TablaResultadosHistogramas.set_index("Histogramas")
display(TablaResultadosHistogramas)

# %%
