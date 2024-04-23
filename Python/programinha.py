total_aprovados = 0
total_exame = 0
total_reprovados = 0
soma_notas = 0

for i in range(6):
    nota1 = float(input(f"Informe a primeira nota do aluno {i+1}: "))
    nota2 = float(input(f"Informe a segunda nota do aluno {i+1}: "))
    
    media = (nota1 + nota2) / 2
    soma_notas += media
    
    if media < 3.0:
        total_reprovados += 1
        mensagem = "Reprovado"
    elif media >= 3.0 and media < 7.0:
        total_exame += 1
        mensagem = "Exame"
    else:
        total_aprovados += 1
        mensagem = "Aprovado"
    
    print(f"Média aritmética do aluno {i+1}: {media:.2f} - {mensagem}")

media_classe = soma_notas / 6
print(f"\nTotal de alunos aprovados: {total_aprovados}")
print(f"Total de alunos em exame: {total_exame}")
print(f"Total de alunos reprovados: {total_reprovados}")
print(f"Média da classe: {media_classe:.2f}")
