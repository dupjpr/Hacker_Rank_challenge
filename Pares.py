----- Infinito-------------
print ("N�meros pares e impares")
print("___"*30)
a=0
while a == 0:
    numbers = int(input("Escriba un n�mero entero: "))
    n = numbers % 2
    if n == 0:
        print(f"{numbers} N�mero par")
    else:
        print(f"{numbers} N�mero impar")
----------------------------------------------------------

------5 intentos ----------

print ("N�meros pares e impares")
print("___"*30)
a=0
while a < 5:
    a=a+1
    numbers = int(input("Escriba un n�mero entero: "))
    n = numbers % 2
    if n == 0:
        print(f"{numbers} N�mero par")
    else:
        print(f"{numbers} N�mero impar")

----- bucle for-----------
print ("N�meros pares e impares")
print("___"*30)
for i in range(10):
    n = i % 2
    if n == 0:
        print(f"{i} N�mero par.")
    else:
        print(f"{i} N�mero primo.")
