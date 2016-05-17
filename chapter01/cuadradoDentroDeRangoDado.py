#!/usr/bin/env python

def main():
  def cuadr(num):
    return num * num

  def nom_cuad(num):
    return ("%d -> %d") % (num, cuadr(num))
  
  def promptCuadr():
    myNum1 = input("Enter num1: ")
    myNum2 = input("Enter num2: ")
    minimum = min(myNum1, myNum2)
    maximum = max(myNum1, myNum2)
    arr = [nom_cuad(x) for x in range(minimum, maximum) + [maximum]]
    multiline = "\n".join(arr)
    print multiline
  
  print "==== Mostrar el cuadrado de los numeros dentro del rango introducido ===="
  promptCuadr()
  print "Operacion finalizada"

main()
