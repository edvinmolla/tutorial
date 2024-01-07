
lista = {
    0: "Bli buke",
    1: "Laj rrobat",
    2: "Lexo",
}

lista.update({3:"Fli gjume"})

for key, value in lista.items():
    print(key, value)