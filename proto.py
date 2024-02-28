import numpy as np

minimo = -128
maximo = 127

def saturado(x):
    return np.where(x > maximo, maximo, np.where(x < minimo, minimo, x))

def filtro_fir(senal, coeficientes):  
    senal_float = senal.astype(float) #Señal a punto flotante
    coeficientes_float = coeficientes.astype(float) #Coheficientes a punto flotante
    longitud_senal = len(senal) 
    longitud_coeficientes = len(coeficientes)
    senal_filtrada = np.zeros(longitud_senal) # Señal filtrada en flotante

    for n in range(longitud_senal):
        suma = 0.0
        for k in range(longitud_coeficientes):
            producto = senal_float[n - k] * coeficientes_float[k] # Señal * coeficiente
            suma = suma + producto

        senal_filtrada[n] = suma

    resultado_q78 = saturado(np.round(senal_filtrada * 128).astype(np.int16)) # Señal filtrada a Q7.8

    return resultado_q78

if __name__ == "__main__":
    x = np.array([-5, -4, -2, -1, 0, 1, 2, 3, 4, 5])
    b = np.array([0.01, 0.02, 0.03, 0.04, 0.05])

    resultado = filtro_fir(x, b)

    print("Señal de entrada:", x)
    print("Coeficientes:", b)
    print("Resultado del filtrado FIR:", resultado)




