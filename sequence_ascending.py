n = int(input("Digite o número final: "))

print("Sequência:")
count = 0
current = 1

while current <= n:
    print(current, end=" ")
    count += 1
    current += 1

print()
print("Quantidade:", count)
