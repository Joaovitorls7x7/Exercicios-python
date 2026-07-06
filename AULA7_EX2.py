Lista_produtos = ["Suco", "Pão de Queijo", "Sanduíche", "Café", "Bolo"]

print("--- Produtos Disponíveis --- ")

for indice, produtos in enumerate(Lista_produtos, start = 1):
    print(f"{indice} - {produtos}")