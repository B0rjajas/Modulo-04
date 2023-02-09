Lista = ['Hola','Que tal?','Muy bien']

Tupla = ('Yo muy bien', 1245, 'genial')

numero = 12.44
integer = 16
decimal = 18,932

diccionario = {
    "Juan" : "joven",
    "edad" : 3, 
    "sexo" : "binario",
    "Actividad" : "trabajando"
    }


#01
redondear_alza = round(numero)
print (redondear_alza)


# 02
import math
raiz_cuadrada = math.sqrt(numero)
print (raiz_cuadrada)

#03

seleccion = diccionario.get('Actividad')

print (seleccion)


#04
Lista += ['Y tú?']
print(Lista)

#05
seleccion_tupla = Tupla[1]

print(seleccion_tupla)


#06

Lista.append("Me parece genial") 
ultimo_elemento = Lista[-1]

#07

Lista[0] = 'Buenas noches'
 
print(Lista)

#08 
Lista.sort()

print(Lista)


#09 

Tupla = list(Tupla)
Tupla.remove('published')
Tupla = tuple(Tupla)

print(Tupla)

