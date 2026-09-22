"""Exercício acadêmico de sequência e contagem com while."""

while True:
    try:
        n = int(input("Digite o número final (inteiro a partir de 1): "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        continue
    if n < 1:
        print("Digite um número maior ou igual a 1.")
        continue
    break

print("Sequência:")
count = 0
current = 1

while current <= n:
    print(current, end=" ")
    count += 1
    current += 1

print()
print("Quantidade:", count)
