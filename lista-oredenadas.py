# lista desordenada NOME, MAtRICULA, ANO
lista = [
    ("joao", 105, 2023),
    ("maria", 201, 2024),
    ("pedro", 50, 2021),
    ("ana", 150, 2022),
    ("carlos", 88, 2020),
    ("lucas", 302, 2019),
    ("julia", 12, 2015),
    ("fernanda", 250, 2018)
]

# Ordena a lista com base no ano (último elemento de cada tupla)
lista_ordenado = sorted(lista, key=lambda x: x[2])

# Imprime a lista ordenada de forma formatada
print("\nLista ordenada por ano:")
print("-" * 55)
for nome, matricula, ano in lista_ordenado:
    print(f"Nome: {nome.title():<10} matricula: {matricula:<5} Ano Admissão: {ano}")







