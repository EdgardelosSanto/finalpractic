import unittest

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

class TestGenerarTrigramas(unittest.TestCase):
    
    def text_generador_trigramas(self):
        Texto ="I wish I may I wish I might"
        resultado = {
        ('I', 'wish'): ['I', 'I'], 
        ('wish', 'I'): ['may', 'might'], 
        ('I', 'may'): ['I'], ('may', 'I'): ['wish']
        }
        self.assertEqual(generar_trigramas(Texto), resultado)
    

if __name__ == "__main__":
    unittest.main()
    