Tupla = ('Yo muy bien', 1245, 'genial')

Tupla = list(Tupla)
Tupla.remove('Yo muy bien')
Tupla.append("Me parece genial") 
ultimo_elemento = Tupla[0]
Tupla = tuple(Tupla)

print(Tupla)