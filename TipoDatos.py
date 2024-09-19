print("Clases V2 Angel Tadeo De Leon Ceniceros")

# Zona de clases
class Datos:
    # El constructor funcion
    def __init__(self,estatura,peso):
        self.estatura=estatura
        self.peso=peso
    def Mostrar_datos(self):
        print(f"Estatura: {self.estatura} Mts, Peso: {self.peso} Kg")
    # Lista    
    def Mi_lista(self):
         Celulares=["Samsung A52","Iphone 11","Chafa"]
         print(Celulares)   
         for x in Celulares:
             print(x)
    # Tupla
    def Mi_tupla(self):
        Nombreperros=("Wanona","Destructor de realidades","Princesita")
        print(Nombreperros)
        for x in Nombreperros:
            print(x)
    # Sets
    def Mi_Set(self):
        Espacio={"Luna","Sol","Estrellas"}
        print(Espacio)
        for x in Espacio:
            print(x)
    # Diccionario
    def Mi_Diccionario(self):
        Nombreyapellidos={
            "Angel Tadeo":"De Leon Ceniceros",
            "Carlos":"Quinto",
            "Susana":"Horia"
        }
        print(Nombreyapellidos)
        for x,y in Nombreyapellidos.items():
            print(x,y)                 
# Creacion de objetos
info=Datos(1.75,70.5)

# Utilizando el obj
info.Mostrar_datos()
print("Lista de celulares:")
info.Mi_lista()
print("Lista de nombre de perros:")
info.Mi_tupla()
print("Lista de elementos del espacio:")
info.Mi_Set()
print("Lista de nombres y apellidos:")
info.Mi_Diccionario()
