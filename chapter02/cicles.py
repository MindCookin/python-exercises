#!/usr/bin/env python

print "Escribir un ciclo definido para imprimir por pantalla todos los numeros entre 10 y 20."
print [x for x in range(10, 20)]

print "Escribir un ciclo definido que salude por pantalla a sus cinco mejores amigos/as."
print [amigo for amigo in ['Lola', 'Dolores', 'Quique', 'Manuel', 'Manolo']]

print "Escribir un programa que use un ciclo definido con rango numerico, que pregunte los nombres de sus cinco mejores amigos/as, y los salude."
for i in range(5):
  amigo = raw_input('Escribe el nombre de tu {0} amigo: '.format(i + 1))
  print 'Hola {0}'.format(amigo)

print "Escribir un programa que use un ciclo definido con rango numerico, que pregunte los nombres de sus seis mejores amigos/as, y los salude."
for i in range(6):
  amigo = raw_input('Escribe el nombre de tu {0} amigo: '.format(i + 1))
  print 'Hola {0}'.format(amigo)

print "Escribir un programa que use un ciclo definido con rango numerico, que averigue a cuantos amigos quieren saludar, les pregunte los nombres de esos amigos/as, y los salude." 
num = input("A cuantos amigos quieres saludar?")
for i in range(num):
  amigo = raw_input('Escribe el nombre de tu {0} amigo: '.format(i + 1))
  print 'Hola {0}'.format(amigo)
