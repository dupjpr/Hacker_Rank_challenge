n = int(input(">"))
matrix = []
for i in range(n):
 matrix.append([])
 for x in range(1):
     matrix[i].append(input(">>"))
     matrix[i].append((float(input("#"))))

lista = []

for index in range(len(matrix)):
    val = matrix[index][1]
    lista.append(val)

uniq_ranks = set(lista)
lista = list(uniq_ranks)
lista.sort()
matrix.sort()
for item in matrix:
    if item[1] == lista[1]:
        print(item[0])

---- with function ---- 

def nested_lists(matrix):
    lista = []

    for index in range(len(matrix)):
        val = matrix[index][1]
        lista.append(val)

    uniq_ranks = set(lista)
    lista = list(uniq_ranks)
    lista.sort()
    matrix.sort()
    for item in matrix:
        if item[1] == lista[1]:
            print(item[0])


array = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
nested_lists(array)
# Berry
# Harry

