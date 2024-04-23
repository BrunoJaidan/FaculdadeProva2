numeros = []

# Recebe os três primeiros números em ordem crescente
for i in range(3):
    num = float(input(f"Informe o {i+1}º número em ordem crescente: "))
    numeros.append(num)

# Recebe o quarto número
num_fora_ordem = float(input("Informe o quarto número: "))

# Adiciona o quarto número à lista
numeros.append(num_fora_ordem)

# Ordena a lista em ordem decrescente
numeros.sort(reverse=True)

# Mostra os números em ordem decrescente
print("Os números em ordem decrescente são:")
for num in numeros:
    print(num)
