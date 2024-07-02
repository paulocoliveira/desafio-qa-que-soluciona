def countingValleys(path):
    #Variável para controlar o nível atual
    level = 0
    #Variável para controlar o número de vales percorridos
    valleys = 0
    #Variável para controlar se o caminhante está em um vale
    in_valley = False

    for step in path:       
        #Se subir um nível, adiciona 1 ao level    
        if (step == "U"):
            level = level + 1
        #Se descer um nível, diminui 1 ao level
        elif (step == "D"):
            level = level - 1
        
        #Se o nível for -1 significa que acabou de entrar em um vale
        if (level == -1):
            #Seta a variável para true informando que está em um vale
            in_valley = True
        #Se o nível for 0 e o caminhante estava num vale
        elif (level == 0 and in_valley == True):
            #Contabiliza mais um vale percorrido
            valleys = valleys + 1
            #Seta a variável para false informando que não está mais em um vale
            in_valley = False
    #Retorna o total de vales percorridos
    return valleys

print(countingValleys("DDUUDDUDUUUD"))
print(countingValleys("UDUUUDUDDD"))
print(countingValleys("DUDUDUDUDUDUDU"))
print(countingValleys("DDUUUUDDDUUUDDDU"))


