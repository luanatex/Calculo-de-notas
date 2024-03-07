aprovados = 0
reprovados = 0
totalalunos = 3

# FOR para criar a sequencia de input de cada aluno

for aluno in range(1,totalalunos + 1):
  print('Notas do Aluno', aluno)

# WHILE em cada atividade para limitar o valor da nota do input

  while True:
    aop1 = float(input('Digite a nota da Atividade Pontuada 1 (AOP1): '))
    if 0 <= aop1 <= 1:
      break
    else:
      print('Erro\nA nota inserida deve ser entre 0 e 1')
  while True:
    aop2 = float(input('Digite a nota da Atividade Pontuada 2 (AOP2): '))
    if 0 <= aop2 <= 2:
      break
    else:
      print('Erro\nA nota inserida deve ser entre 0 e 2')
  while True:
    aop3 = float(input('Digite a nota da Atividade Pontuada 3 (AOP3): '))
    if 0 <= aop3 <= 1:
      break
    else:
      print('Erro\nA nota inserida deve ser entre 0 e 1')
  while True:
    prova = float(input('Digite a nota da Prova Regular: '))
    if 0 <= prova <= 6:
      break
    else:
      print('Erro\n A nota inserida deve ser entre 0 e 6')

# Soma do Modulo (sm) = soma de todas as atividades anteriores

  sm = aop1 + aop2 + aop3 + prova
  if sm < 7:
    print('Status do Aluno:\nProva de Recuperação')
    while True:
      recuperação = float(input('Digite a nota da Prova de Recuperação: '))
      if 0 <= recuperação <= 10:
        break
      else:
        print('Erro\nA nota inserida deve ser entre 0 e 10')

#Calcular da nota final e exibir status do aluno
    final = (sm + recuperação)/2
    if final < 5:
      reprovados += 1
      print('Status do Aluno:\nReprovado')
    else:
      aprovados += 1
      print('Status do Aluno:\nAprovado')
  else:
    aprovados += 1
    print('Status do Aluno:\nAprovado')

#Calcular a porcentagem de alunos aprovados e reprovados

porcentagemaprov = round(aprovados/(totalalunos/100))
porcentagemreprov = round(reprovados/(totalalunos/100))
print('Status da Turma:')
print(f'{porcentagemaprov}% dos alunos foram Aprovados')
print(f'{porcentagemreprov}% dos alunos foram Reprovados')
