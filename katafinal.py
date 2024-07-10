def generar_trigramas(texto):
    palabras = texto.split()
    trigramas = {}
    
    for i in range (len(palabras) - 2):
        clave = (palabras[i], palabras [i + 1])
        siguiente = palabras[i +2]
        
        if clave in trigramas:
            trigramas[clave].append(siguiente)
        else:
            trigramas[clave] = [siguiente]
            
    return trigramas

if __name__ =="__main__":
    parrafo = "I wish I may I wish I might"
    trigramas = generar_trigramas(parrafo)
    print(trigramas)

            