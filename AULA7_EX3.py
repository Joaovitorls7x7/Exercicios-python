catalogo = {
    "Nome": "Caderno",
    "codigo": 1,
    "Preco": 18.50,
    "Quantidade": 12,
    }

valor_total_estoque = (float(catalogo["Preco"] * catalogo["Quantidade"]))

print("--- Dados do produto ---")
print(f"Produto: {catalogo['Nome']}")
print(f"Preço: {catalogo['Preco']:.2f}")
print(f"Quantidade: {catalogo['Quantidade']}")
print(f"Valor total em estoque: {valor_total_estoque:.2f}")