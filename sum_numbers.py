n = int(input("Entrez un nombre entier: "))

result = 0

for i in range(1, n + 1):
    result += i

print("La somme des nombres de 1 à", n, "est:", result)
