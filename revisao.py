peso = 50

print(peso)

peso = "dsda"

print(peso)

lista = [1, 2, 3, 4, 5]

print(lista)

lista = [1, 2, 3, 4, 2.5, 3.6, 'ajh', 'b']

print(lista)

obj = {
    "cor": "azul"
}

obj['nome'] = "teste"
obj['idade'] = 15

print(obj['cor'])

inteiros = [1, 2, 3, "asd", 5]

for elemento in inteiros:
    print(elemento)

print(" ")

for i in range(len(inteiros)):
    print("Indice {} Valor {}".format(i, inteiros[i]))
