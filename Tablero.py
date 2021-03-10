from Ficha import *

class Tablero:

    #Defina aquí los atributos de Tablero
    
    final = 0
    bonus = []
    trampas = []
    final = 0
    inicio = 0 
    distanci = 0
    jugadores = []

    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno


    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos
    def __init__(self):
        self.distancia = 50
        self.final = 50
        self.inicio = 0
        self.trampas = [4, 6,19, 32 , 23]
        self.bonus = [3, 5, 20, 18, 20, 34, 45, 48]
        self.jugadores = []

        #inicialice aquí todos los atributos
        #no olvide usar self.atributo para acceder el atributo de la clase

    #defina aquí los métodos de Tablero
    #recuerde que el primer parámetro de cada método es siempre self
    def iniciar(self):
        respuesta = input("1. Ingresar jugadores/n 2.Jugar /n 3.Marque la opcion según lo que desee hacer")
        
        if(respuesta = 1 ):
            numeroJugadores = input("¿Cuantos jugadores van a ingresar/n")
            while(numeroJugadores = 0):
                color = input("¿Qué color será su ficha)/n")
                self.jugadores.append(Ficha(color))

    def jugar(self, jugador):
        for lugar in self.trampas:
            if(self.jugadores[jugador].posicion = lugar):
                #Lo que haga la trampa, porque no sé ni que hace
        for lugar in self.bonus:
            if (self.jugadores[jugador].posicion = lugar):
                 #Lo que haga la trampa, porque no sé ni que hace
        if(self.jugadores[jugador].posicion = final ):
            self.ganar()
        
    def ganar(self):
        print("Usted ha ganado")