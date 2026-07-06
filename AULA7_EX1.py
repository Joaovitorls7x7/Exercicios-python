notas_aluno = []

for i in range(1,5):
    nota = float(input(f"Digite a Nota: {i}: "))
    notas_aluno.append(nota)

media_notas = sum(notas_aluno) / len(notas_aluno)

print("\n--- Notas Armazenadas na Lista ---")
for indice, nota in enumerate(notas_aluno, start=1):
    print(f"Nota {indice}: {nota}")
print(f"A media das notas é: {media_notas: .2f}")
