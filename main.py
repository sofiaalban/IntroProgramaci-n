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
'''
#ejercicio10
payasos=float(input("número de payasos "))
muñecas=float(input("número de muñecas "))
total=(payasos*112)+(muñecas*75)
print("el peso total es ", total)
