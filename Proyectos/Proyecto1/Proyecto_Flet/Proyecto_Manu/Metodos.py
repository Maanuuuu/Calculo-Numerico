import numpy as np

def base_a_decimal(numero, base):
        decimal = 0
        for i in range(len(numero)):
            digito = int(numero[len(numero) - 1 - i], base)
            decimal += digito * (base ** i)
        return decimal

def determinar_base(value):
        if value=="Decimal":
            base=10
        elif value=="Binario":
            base=2
        elif value=="Octal":
            base=8
        elif value=="Hexadecimal":
            base=16
        
        return base

def decimal_a_base(decimal, base):
        if decimal == 0:
            return "0"

        caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        resultado = ""
        while decimal > 0:
            resultado = caracteres[decimal % base] + resultado
            decimal //= base

        return resultado

# Método de Gauss-Jordan
# Solución a Sistemas de Ecuaciones
# de la forma A.X=B

def eliminacion_gauss_jordan(coeficientes, matriz_constantes):
    
    coeficientes = np.array(coeficientes, dtype=float)
    
    matriz_aumentada = np.concatenate((coeficientes, matriz_constantes), axis=1)
    copia = np.copy(matriz_aumentada)

    # Se realiza un pivoteo parcial por filas
    size_matriz = np.shape(matriz_aumentada)
    num_filas = size_matriz[0]
    num_columnas = size_matriz[1]

    for i in range(0, num_filas - 1, 1):
        
        columna = abs(matriz_aumentada[i:, i])
        indice = np.argmax(columna)
    
        
        if (indice != 0):
            # se intercambian las filas
            fila = np.copy(matriz_aumentada[i, :])
            matriz_aumentada[i, :] = matriz_aumentada[indice + i, :]
            matriz_aumentada[indice + i, :] = fila
        
    matriz_aumentada_pivoteo = np.copy(matriz_aumentada)

    # Proceso de eliminación hacia adelante
    for i in range(0, num_filas - 1, 1):
        pivote = matriz_aumentada[i, i]
        fila_debajo = i + 1
        for k in range(fila_debajo, num_filas, 1):
            factor = matriz_aumentada[k, i] / pivote
            matriz_aumentada[k, :] = matriz_aumentada[k, :] - matriz_aumentada[i, :] * factor
    matriz_aumentada_eliminacion_adelante = np.copy(matriz_aumentada)

    # Proceso de eliminación hacia atrás
    ultima_fila = num_filas - 1
    ultima_columna = num_columnas - 1
    for i in range(ultima_fila, -1, -1):
        pivote = matriz_aumentada[i, i]
        fila_arriba = i - 1 
        for k in range(fila_arriba, -1, -1):
            factor = matriz_aumentada[k, i] / pivote
            matriz_aumentada[k, :] = matriz_aumentada[k, :] - matriz_aumentada[i, :] * factor
        
        matriz_aumentada[i, :] = matriz_aumentada[i, :] / matriz_aumentada[i, i]
    solucion = np.copy(matriz_aumentada[:, ultima_columna])
    solucion = np.transpose([solucion])

    return solucion

def transformacion(valores_matriz, matriz, vector):

    for i in range(len(valores_matriz)):
        filas_matriz = []
        filas_vector = []
        for j in range(len(valores_matriz[0])):

            if(j == len(valores_matriz[0]) - 2):
                pass
            
            elif(j == len(valores_matriz[0]) - 1):
                filas_vector.append(int(valores_matriz[i][j]))
            
            else:
                filas_matriz.append(int(valores_matriz[i][j]))
        matriz.append(filas_matriz)
        vector.append(filas_vector)

def realizar_GaussJordan(valores_matriz):

    lista_matriz = []
    lista_vector = []

    transformacion(valores_matriz, lista_matriz, lista_vector)

    
    a = np.array(lista_matriz)
    b = np.array(lista_vector)

    resultado = eliminacion_gauss_jordan(a,b)
    
    return resultado
