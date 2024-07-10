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

def test_generar_trigramas():
    parrafo = "I wish I may I wish I might"
    esperado = {('I', 'wish'): ['I', 'I'], ('wish', 'I'): ['may', 'might'], ('I', 'may'): ['I'], ('may', 'I'): ['wish']}
    resultado = generar_trigramas(parrafo)
    
    assert resultado == esperado