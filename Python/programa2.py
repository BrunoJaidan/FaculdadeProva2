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
    
    
    
    
    
    
    
    
    
    
    
    function calculateTotal() {
  var quantity1 = parseFloat(document.getElementById('quantity1').value);
  var value1 = parseFloat(document.getElementById('value1').value);
  var quantity2 = parseFloat(document.getElementById('quantity2').value);
  var value2 = parseFloat(document.getElementById('value2').value);
  var quantity3 = parseFloat(document.getElementById('quantity3').value);
  var value3 = parseFloat(document.getElementById('value3').value);

  var subtotal1 = quantity1 * value1;
  var subtotal2 = quantity2 * value2;
  var subtotal3 = quantity3 * value3;

  var total = subtotal1 + subtotal2 + subtotal3;

  var resultDiv = document.getElementById('result');
  resultDiv.innerHTML = `
    <p>Subtotal 1: R$ ${subtotal1.toFixed(2)}</p>
    <p>Subtotal 2: R$ ${subtotal2.toFixed(2)}</p>
    <p>Subtotal 3: R$ ${subtotal3.toFixed(2)}</p>
    <h2>Total: R$ ${total.toFixed(2)}</h2>
  `;
}




body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  margin: 0;
  padding: 0;
}

.container {
  max-width: 600px;
  margin: 50px auto;
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.form label,
.form input,
.form button {
  margin-bottom: 10px;
}

.result {
  margin-top: 20px;
}


    