def contar_rutas_mas_cortas(C): 
    matriz = C
    rows=len(matriz)
    col=len(comatrizunt[0])
    
    for i in range(rows): 
        matriz[i][0] = 1; 
    
    for j in range(col): 
        matriz[0][j]= 1; 
 
    for i in range(1, rows): 
        for j in range(1, col): 
            if matriz[i][j] == 0:
                matriz[i][j] = matriz[i-1][j] + matriz[i][j-1]
            else:
                matriz[i][j] = 0
            
    return matriz[rows-1][col-1] 
