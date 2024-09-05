import matplotlib.pyplot as plt
import random

# Função para gerar vendas diárias
def gerar_vendas_diarias():
    vendas_calabresa = []
    vendas_mussarela = []
    vendas_portuguesa = []

    for _ in range(7):
        vendas_calabresa.append(random.randint(10, 50))
        vendas_mussarela.append(random.randint(10, 50))
        vendas_portuguesa.append(random.randint(10, 50))

    return vendas_calabresa, vendas_mussarela, vendas_portuguesa

# Função para criar gráfico de barras
def grafico_barras(vendas_calabresa, vendas_mussarela, vendas_portuguesa, pizzaria):
    dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
    
    plt.bar(dias, vendas_calabresa, label='Calabresa', color='red')
    plt.bar(dias, vendas_mussarela, bottom=vendas_calabresa, label='Mussarela', color='yellow')
    plt.bar(dias, vendas_portuguesa, bottom=[vendas_calabresa[i] + vendas_mussarela[i] for i in range(7)], label='Portuguesa', color='green')

    plt.title(f"Vendas Semanais - {pizzaria}")
    plt.xlabel("Dias da Semana")
    plt.ylabel("Pizzas Vendidas")
    plt.legend()
    plt.show()

# Função para criar gráfico de pizza
def grafico_pizza(vendas_calabresa, vendas_mussarela, vendas_portuguesa, pizzaria):
    total_calabresa = sum(vendas_calabresa)
    total_mussarela = sum(vendas_mussarela)
    total_portuguesa = sum(vendas_portuguesa)
    totais = [total_calabresa, total_mussarela, total_portuguesa]
    sabores = ['Calabresa', 'Mussarela', 'Portuguesa']

    plt.pie(totais, labels=sabores, autopct='%1.1f%%', colors=['red', 'yellow', 'green'])
    plt.title(f"Distribuição de Vendas - {pizzaria}")
    plt.show()

# Função para criar gráfico de linha
def grafico_linha(vendas_calabresa, vendas_mussarela, vendas_portuguesa, pizzaria):
    dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
    
    plt.plot(dias, vendas_calabresa, marker='o', label='Calabresa', color='red')
    plt.plot(dias, vendas_mussarela, marker='o', label='Mussarela', color='yellow')
    plt.plot(dias, vendas_portuguesa, marker='o', label='Portuguesa', color='green')

    plt.title(f"Evolução das Vendas Semanais - {pizzaria}")
    plt.xlabel("Dias da Semana")
    plt.ylabel("Pizzas Vendidas")
    plt.legend()
    plt.show()

# Função principal
def main():
    pizzaria = input("Digite o nome da pizzaria: ")

    # Gerar vendas aleatórias de forma simplificada
    vendas_calabresa, vendas_mussarela, vendas_portuguesa = gerar_vendas_diarias()

    # Interagir com o usuário para escolher o gráfico
    print("\nQual gráfico você deseja visualizar?")
    print("1. Gráfico de Barras")
    print("2. Gráfico de Pizza")
    print("3. Gráfico de Linha")

    opcao = input("Digite o número da sua escolha: ")

    if opcao == '1':
        grafico_barras(vendas_calabresa, vendas_mussarela, vendas_portuguesa, pizzaria)
    elif opcao == '2':
        grafico_pizza(vendas_calabresa, vendas_mussarela, vendas_portuguesa, pizzaria)
    elif opcao == '3':
        grafico_linha(vendas_calabresa, vendas_mussarela, vendas_portuguesa, pizzaria)
    else:
        print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
