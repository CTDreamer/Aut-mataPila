# Grupo: LyCenciados Corruptos
# Este código implementa un Autómata a Pila (AP) que verifica si una cadena
# pertenece a un lenguaje específico basado en las reglas de apilado y desapilado.
# Utiliza dos pilas para controlar la correspondencia entre los símbolos.

class AutomataPila:
    def __init__(self):
        self.pila_1 = []  # Pila para manejar los símbolos 'a' y 'c'
        self.pila_2 = []  # Pila para manejar los símbolos 'b' y 'd'

    def procesar_cadena(self, cadena):
        for simbolo in cadena:
            if simbolo == 'a':
                self.pila_1.append('a')  # Apilar 'a' en pila_1
            elif simbolo == 'b':
                self.pila_2.append('b')  # Apilar 'b' en pila_2
            elif simbolo == 'c':
                if self.pila_1:
                    self.pila_1.pop()  # Desapilar 'a' si existe en pila_1
                else:
                    return False  # Error: no hay 'a' para desapilar
            elif simbolo == 'd':
                if self.pila_2:
                    self.pila_2.pop()  # Desapilar 'b' si existe en pila_2
                else:
                    return False  # Error: no hay 'b' para desapilar
            else:
                return False  # Error: símbolo no válido

        # Acepta la cadena si ambas pilas están vacías al finalizar
        return len(self.pila_1) == 0 and len(self.pila_2) == 0  

if __name__ == "__main__":
    automata = AutomataPila()
    cadena = input("Ingrese una cadena: ")  # Solicita cadena desde la terminal
    resultado = automata.procesar_cadena(cadena)
    print("Cadena pertenece al lenguaje" if resultado else "Cadena rechazada, no pertenece al lenguaje")
