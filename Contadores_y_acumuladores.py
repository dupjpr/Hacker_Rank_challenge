contador -------------
list=["q","w","q","w","q","w","q","w","q","w","q","w","q","w","q"]
cuenta=0

for i in list:
    if i == "q":
        cuenta=cuenta+1
        rest= len(list)-cuenta


print(f"In the list there are {cuenta} q elements and {rest} w elements")

acumulador ------------

total=0
for i in range (5):
    total=total+i

print(f"El total es {total}")
