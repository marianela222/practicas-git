#pedir al usuario dos numeros de punto flotante
numero1= float(input("ingrese el primer numero:"))
numero2= float(input("ingrese el segundo numero:"))

#calcular el promedio
promedio= (numero1+numero2)/2

#muestro el promedio
print("el promedio es:", promedio)

#decidir si aprobo o desaprobo
if promedio>7:
    print("aprobo")
else:
    print("desaprobo")