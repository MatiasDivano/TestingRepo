# repaso de usos de listas y de for

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def elevar_al_cuadrado(x):
    return x**2

out = ""

for i in lista:
    out = out + str(elevar_al_cuadrado(i))
    if i < len(lista):
        out = out + " "

print(out)
