list=["a","b","c"]
string="".join(list)
print(string)


list=[1,2,3,4]
string=""
for i in list:
    string=string+str(i)+" "
print(string)


lista=["juan","camilo"]
string="".join(lista)
print(string)


string2="Yo amo a mi mamá "
list2=string2.split()
print(list2)


list=[]
for i in range(1,10):
    list.append(i)
print(list)
string=""
for x in list:
    string=string+str(x)+" "
print(string)