def calcular_media(lista_notas):
    soma = sum(lista_notas)
    quantidade = len(lista_notas)
    media = soma / quantidade
    return media


notas_aluno = [8.0, 9.0, 7.5, 8.5]

resultado_media = calcular_media(notas_aluno)

print(f"Média final: {resultado_media:.2f}")