class equipo:
    def __init__(self, nombre, genero="masculino"):
        self.nombre = nombre
        self.demanda_total = 0
        self.cantidad_equipos = 0
        self.genero=genero
    def agregar(self, demanda, cantidad=1):
        self.cantidad_equipos += cantidad
        self.demanda_total += demanda*cantidad
    def obtener_total(self):
        return(self.demanda_total/self.cantidad_equipos)
    def reiniciar(self):
        self.demanda_total = 0
        self.cantidad_equipos = 0
    def renombrar(self, nombre):
        self.nombre = nombre
    def hablada(self):
        if (self.cantidad_equipos < 0):
            print("Por favor primero agregar equipos")
            return(1)
        if (self.genero == "masculino"):
            print("Con base en los "+str(self.cantidad_equipos)+" "+self.nombre+" analizados de tres fabricantes distintos, estos dan en promedio un consumo de "+str(self.obtener_total())+" Watts")
        else:
            print("Con base en las "+str(self.cantidad_equipos)+" "+self.nombre+" analizadas de tres fabricantes distintos, estas dan en promedio un consumo de "+str(self.obtener_total())+" Watts")

