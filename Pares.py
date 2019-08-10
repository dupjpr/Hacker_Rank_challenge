----- Infinito-------------
print ("Números pares e impares")
print("___"*30)
a=0
while a == 0:
    numbers = int(input("Escriba un número entero: "))
    n = numbers % 2
    if n == 0:
        print(f"{numbers} Número par")
    else:
        print(f"{numbers} Número impar")
----------------------------------------------------------

------5 intentos ----------

print ("Números pares e impares")
print("___"*30)
a=0
while a < 5:
    a=a+1
    numbers = int(input("Escriba un número entero: "))
    n = numbers % 2
    if n == 0:
        print(f"{numbers} Número par")
    else:
        print(f"{numbers} Número impar")

----- bucle for-----------
print ("Números pares e impares")
print("___"*30)
for i in range(10):
    n = i % 2
    if n == 0:
        print(f"{i} Número par.")
    else:
        print(f"{i} Número primo.")
