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

#ejercicio1
n=int(input("dato 1 "))
m=int(input("dato 2 "))
def suma (n,m):
  sum=n+m
  return sum
print(suma(n, m))

#ejercicio2
n=int(input("dato 1 "))
m=int(input("dato 2 "))
def resta (n,m):
  operación=n-m
  return operación 
print(resta(n, m))
  
#ejercicio3
n=int(input("dato 1 "))
m=int(input("dato 2 "))
def división(n,m):
  if m==0:
    return "no se puede dividir entre 0"
  else:
    operación=(n/m)
  return operación 
print(división(n, m))

#ejercicio4
n=int(input("dato 1 "))
m=int(input("dato 2 "))
op=str(input("¿que operación deseas realizar?"))

if op=="suma":
  def suma (n,m):
    sum=n+m
    return sum
  print(suma(n, m))

elif op == "resta":
  def resta (n,m):
    operación=n-m
    return operación 
  print(resta(n, m))

elif op=="multiplicación":
  def multiplicación (n,m):
    operación=n*m
    return operación 
  print(multiplicación(n, m))

elif op=="división":
   if m==0:
    print ("no se puede dividir entre 0")
   else:
     def división(n,m):
      operación=(n/m)
      return operación 
   print(división(n, m))

else:
  print("ah")

def marca(m,b):
  m=x
  b=y
if marca.lower==nosy:
  desc=(pe*(5/100))
  return desc
else:
  return pe
  pe=input(float("ingrese el precio del estereo "))
  marca=input(str("ingrese la marca que sea del estereo"))
  marca(m)
  
if pe>=2000000:
  desc=(pe*(10/100))
  valor=(pe-desc)
else:
  precio=pe
 '''
import random
def adivina():
  numero_secreto = random.randint(1, 100)
  adivinado = False

while not adivinado:
  intento = int(input("adivina el número"))