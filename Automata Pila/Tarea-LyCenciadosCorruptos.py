class AutomataPila:
    def __init__(self):
        self.pila_a = []  # Para manejar 'a' y 'c'
        self.pila_b = []  # Para manejar 'b' y 'd'

    def procesar_cadena(self, cadena):
        for simbolo in cadena:
            if simbolo == 'a':
                self.pila_a.append('a')  # Apilar 'a'
            elif simbolo == 'b':
                self.pila_b.append('b')  # Apilar 'b'
            elif simbolo == 'c':
                if self.pila_a:
                    self.pila_a.pop()  # Desapilar 'a'
                else:
                    return False  # Error: No hay 'a' para desapilar
            elif simbolo == 'd':
                if self.pila_b:
                    self.pila_b.pop()  # Desapilar 'b'
                else:
                    return False  # Error: No hay 'b' para desapilar
            else:
                return False  # Simbolo no válido

        return len(self.pila_a) == 0 and len(self.pila_b) == 0  # Acepta si ambas pilas están vacías

if __name__ == "__main__":
    automata = AutomataPila()
    cadena = input("Ingrese una cadena: ")  # Permitir entrada desde la terminal
    resultado = automata.procesar_cadena(cadena)
    print("Cadena aceptada" if resultado else "Cadena rechazada")
