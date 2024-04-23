# Recebe os três primeiros números em ordem crescente
numeros = []
for i in range(3):
    num = float(input(f"Informe o {i+1}º número em ordem crescente: "))
    if i == 0:
        numeros = [num]
    elif num < numeros[0]:
        numeros = [num] + numeros
    elif num > numeros[-1]:
        numeros = numeros + [num]
    else:
        for j in range(len(numeros) - 1):
            if num > numeros[j] and num < numeros[j + 1]:
                numeros = numeros[:j+1] + [num] + numeros[j+1:]
                break

# Recebe o quarto número
num_fora_ordem = float(input("Informe o quarto número: "))

# Adiciona o quarto número à lista
if num_fora_ordem < numeros[0]:
    numeros = [num_fora_ordem] + numeros
elif num_fora_ordem > numeros[-1]:
    numeros = numeros + [num_fora_ordem]
else:
    for i in range(len(numeros) - 1):
        if num_fora_ordem > numeros[i] and num_fora_ordem < numeros[i + 1]:
            numeros = numeros[:i+1] + [num_fora_ordem] + numeros[i+1:]
            break

# Mostra os números em ordem decrescente
print("Os números em ordem decrescente são:")
for num in reversed(numeros):
    print(num)