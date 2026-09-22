"""Exercício acadêmico de sequência e contagem com while."""

while True:
    try:
        n = int(input("Digite o número inicial (inteiro a partir de 0): "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        continue
    if n < 0:
        print("Digite um número maior ou igual a 0.")
        continue
    break

print("Sequência:")
count = 0
current = n

while current >= 0:
    print(current, end=" ")
    count += 1
    current -= 1

print()
print("Quantidade:", count)
