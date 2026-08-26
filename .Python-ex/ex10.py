while True:
    nome = input("Digite o nome do aluno: ").strip()

    if nome and not nome.isdigit():
        break

    print("Nome inválido. Digite um nome válido.")

notas = []

for i in range(1, 4):
    while True:
        try:
            nota = float(input(f"Digite a {i}ª nota: "))

            if nota < 0 or nota > 10:
                print("A nota deve estar entre 0 e 10.")
                continue

            notas.append(nota)
            break

        except ValueError:
            print("Nota inválida. Digite apenas números.")

media = sum(notas) / len(notas)

print(f"O aluno {nome} ficou com média {media:.2f}.")
