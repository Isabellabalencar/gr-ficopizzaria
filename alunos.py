import matplotlib.pyplot as plt

# Dados de exemplo (nomes dos alunos e notas)
alunos = ['Aluno 1', 'Aluno 2', 'Aluno 3', 'Aluno 4']
notas_matematica = [8, 7, 9, 6]
notas_ciencias = [7, 8, 6, 9]

# Criar gráfico de barras individuais para Matemática e Ciências
plt.bar(alunos, notas_matematica, label='Matemática', color='blue', width=0.4, align='center')
plt.bar(alunos, notas_ciencias, label='Ciências', color='orange', width=0.2, align='edge')

# Configurações do gráfico
plt.xlabel("Alunos")
plt.ylabel("Notas")
plt.title("Comparação de Desempenho Acadêmico")
plt.legend()

# Exibir o gráfico
plt.show()
