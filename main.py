'''
#ejercicio1
print("Hola Mundo")
cadena = "Hola Mundo"
print(cadena)

#ejercicio2
nombre =input("nombre ")
print("hola"+" "+nombre)

#ejercicio4
print(((3+2)/(2*5))**2)

#ejercicio5
horas= float(input("número de horas trabajadas "))
pago= float(input("costo de la hora "))
print(pago*horas)

#ejercicio6
n=int(input("número "))
suma=(n*(n+1)/2)
print(suma)

#ejercicio7
peso=float(input("peso en kg "))
estatura=float(input("peso en metros "))
imc=(peso/estatura**2)
print(round(imc,2))


#ejercicio8
num1=int(input("dato 1 "))
num2=int(input("dato 2 "))
cociente=(num1//num2)
print(cociente)
resto=(num1%num2)
print(resto)

#ejercicio9
c=float(input("cantidad a invertir "))
i=float(input("tasa de interés anual "))
año=float(input("número de años  "))
cap=(c*(i/100+1)**año)
print(round(cap,2))

#ejercicio10
payasos=float(input("número de payasos "))
muñecas=float(input("número de muñecas "))
total=(payasos*112)+(muñecas*75)
print("el peso total es ", total)

#2
num1=int(input("dato 1 "))
num2=int(input("dato 2 "))
cociente=(num1//num2)
print(cociente)
resto=(num1%num2)
print(resto)
if c<1:
  print("El divisor es mayor que el dividendo")
else
  print("El divisor es mayor que el divisor")
'''
#ejercicio3
inv=float(input("ingresa la cantidad a invertir"))
int=float(input("ingresa el interes anual"))
años=float(input("ingresa el número de años: "))
fórmula=(inv*((int/100)+1)**años)
if formula <100000:
  print("baja rentabilidad")
elif 100000<formula>100000:
  print("rentabilidad baja")
else:
  print("es una buena inversión") 