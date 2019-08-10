# string = "q w e r t y u i o p a s d f g h j k l z x c v b n m Q W E R T Y U I O P A S D F G H J K L Z X C V B N M"
#
# lista = string.split()
#
# list1 = []
# for i in lista:
#     if len(i) > 0:
#         string2 = i
#         string3 = string2[0].upper()
#         string4 = string2[1:len(i)].lower()
#         final = string3 + string4
#         list1.append(final)
#
# resul = " ".join(list1)
#
# print(resul)

def my_capitalize(str):

    ar1 = str.split()
    ar2 = []
    output = ' '
    for i in ar1:
        num = i[0].isdigit()
        if num:
            ar2.append(i)
        else:
            ar2.append(i.capitalize())


    print(ar2)
    return output.join(ar2)

str = "alpha beta 5mega"
print(my_capitalize(str))

