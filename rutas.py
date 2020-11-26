def contar_rutas_mas_cortas(C): 
    matriz = C

    # Valores de ancho y largo de la matriz
    rows=len(matriz)
    col=len(matriz[0])
    
    # Llena la primera fila y columna con 1's
    for i in range(rows): 
        matriz[i][0] = 1; 
    
    for j in range(col): 
        matriz[0][j]= 1; 
 
    # Aquí hace el conteo de las rutas
    for i in range(1, rows): 
        for j in range(1, col): 
            if matriz[i][j] == 0:
                matriz[i][j] = matriz[i-1][j] + matriz[i][j-1]
            else:
                matriz[i][j] = 0
            
    return matriz[rows-1][col-1] 


# C = [[0, 0, 0, 0],
#     [0, 1, 0, 0],
#     [0, 0, 1, 0],
#     [0, 0, 0, 0]]
# print(contar_rutas_mas_cortas(C))
