# Função para calcular a média dos alunos
def calcular_media():
 # Entrada: Recebe as notas dos alunos
    notas = []
    qtd_notas = int(input("Quantas notas deseja inserir? "))
    
    for i in range(qtd_notas):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)

# Processo: Calcula a média aritmética
    media = sum(notas) / len(notas)

# Saída: Exibe o resultado
    print(f"A média das notas é: {media:.2f}")

# Chama a função para executar o programa
calcular_media()

# Função para calcular a média dos alunos e verificar aprovação
def calcular_media():
    # Entrada: Recebe as notas dos alunos
    notas = []
    qtd_notas = int(input("Quantas notas deseja inserir? "))
    
    for i in range(qtd_notas):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)

    # Processo: Calcula a média aritmética
    media = sum(notas) / len(notas)
    
    # Saída: Exibe o resultado da média
    print(f"A média das notas é: {media:.2f}")

    # Verifica se o aluno foi aprovado ou reprovado
    if media >= 6:
        print("Aprovado")
    else:
        print("Reprovado")

# Chama a função para executar o programa
calcular_media()

# Função para calcular a média dos alunos e verificar aprovação, recuperação ou reprovação
def calcular_media():
    # Entrada: Recebe as notas dos alunos
    notas = []
    qtd_notas = int(input("Quantas notas deseja inserir? "))
    
    for i in range(qtd_notas):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)

    # Processo: Calcula a média aritmética
    media = sum(notas) / len(notas)
    
    # Saída: Exibe o resultado da média
    print(f"A média das notas é: {media:.2f}")

    # Verifica a situação do aluno baseado na média
    if media >= 6:
        print("Aprovado")
    elif 5.0 < media < 6.0:
        print("Recuperação!!!")
    else:
        print("Reprovado kkkkkk")

# Chama a função para executar o programa
calcular_media()

