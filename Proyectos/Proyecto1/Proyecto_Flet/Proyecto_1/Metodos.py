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

def gauss_jordan(A,B):

    # PROCEDIMIENTO
    casicero = 1e-15 # Considerar como 0

    # Evitar truncamiento en operaciones
    A = np.array(A,dtype=float) 

    # Matriz aumentada
    AB = np.concatenate((A,B),axis=1)
    AB0 = np.copy(AB)

    # Pivoteo parcial por filas
    tamano = np.shape(AB)
    n    = tamano[0]
    m = tamano[1]

    # Para cada fila en AB
    for i in range(0,n-1,1):
        # columna desde diagonal i en adelante
        columna = abs(AB[i:,i])
        dondemax = np.argmax(columna)
    
        # dondemax no está en diagonal
        if (dondemax !=0):
            # intercambia filas
            temporal = np.copy(AB[i,:])
            AB[i,:] = AB[dondemax+i,:]
            AB[dondemax+i,:] = temporal
        
    AB1 = np.copy(AB)

    # eliminacion hacia adelante
    for i in range(0,n-1,1):
        pivote = AB[i,i]
        adelante = i + 1
        for k in range(adelante,n,1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
    AB2 = np.copy(AB)

    # elimina hacia atras
    ultfila = n-1
    ultcolumna = m-1
    for i in range(ultfila,0-1,-1):
        pivote = AB[i,i]
        atras = i-1 
        for k in range(atras,0-1,-1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
        # diagonal a unos
        AB[i,:] = AB[i,:]/AB[i,i]
    X = np.copy(AB[:,ultcolumna])
    X = np.transpose([X])

    return X

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

    resultado = gauss_jordan(a,b)
    
    return resultado
