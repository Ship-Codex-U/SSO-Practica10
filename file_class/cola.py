class Cola:
    def __init__(self, maxTamanio) -> None:
        self.maxTamanio = maxTamanio
        self.contador = 0
        self.elementos = []
    
    def vacio(self):
        if len(self.elementos) == 0:
            return True
        else: 
            return False
    
    def lleno(self):
        if len(self.elementos) == self.maxTamanio:
            return True
        else: 
            return False
        
    def encolar(self, dato):
        if len(self.elementos) != self.maxTamanio:
            self.elementos.append(dato)
            self.contador += 1
        else:
            print("Cola Llena . . .")
    
    def desencolar(self):
        if self.vacio():
            print("Cola Vacia . . .")
        else:
            dato = self.elementos[0]
            self.elementos.pop(0)
            self.contador -= 1
            return dato
        
    def obtenerDatos(self):
        return self.elementos
    
    def imprimir(self):
        print(self.elementos)