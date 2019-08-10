n=int(input("Number of students: "))
dic={}
list=[]
list2=[]
for i in range(n):
    a=input("Name:")
    list2 = a.split(" ")
    dic[list2[0]] = list2[1:]

x=dic[input("name:")]
list=x
a=0
for x in list:
    a=a+float(x)
    promedio=a/len(list)
txt="{:.2f}"
print(txt.format(promedio))
