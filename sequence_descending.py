n = int(input("Digite o número inicial: "))

print("Sequência:")
count = 0
current = n

while current >= 0:
    print(current, end=" ")
    count += 1
    current -= 1

print()
print("Quantidade:", count)
