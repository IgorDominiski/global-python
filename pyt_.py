import matplotlib.pyplot as plt

def menu():
    print("\n=== Sistema Futuro do Trabalho ===")
    print("1. Cadastrar habilidade")
    print("2. Listar habilidades")
    print("3. Criar tabela de rendimento")
    print("4. Gerar gráfico da tabela")
    print("5. Sair")

def cadastrar_habilidade(banco):
    nome = input("Nome da habilidade: ").strip()
    if not nome:
        print("Entrada inválida.")
        return
    try:
        nivel = int(input("Nível da habilidade (0 a 10): "))
        if nivel < 0 or nivel > 10:
            print("Valor fora do intervalo.")
            return
    except:
        print("Entrada inválida.")
        return
    banco[nome] = nivel
    print("Habilidade cadastrada.")

def listar_habilidades(banco):
    if not banco:
        print("Nenhuma habilidade cadastrada.")
        return
    print("\nHabilidades cadastradas:")
    for k, v in banco.items():
        print(f"{k}: {v}")

def criar_tabela_rendimento(tabela):
    tabela.clear()
    print("\nDigite os dados da tabela. Para parar, deixe o nome vazio.")
    while True:
        nome = input("Nome da habilidade: ").strip()
        if nome == "":
            break
        try:
            valor = float(input("Rendimento (0 a 10): "))
        except:
            print("Entrada inválida.")
            continue
        tabela[nome] = valor
    print("Tabela criada.")

def gerar_grafico(tabela):
    if not tabela:
        print("A tabela está vazia.")
        return
    nomes = list(tabela.keys())
    valores = list(tabela.values())

    plt.figure(figsize=(8, 5))
    plt.bar(nomes, valores)
    plt.title("Tabela de Rendimento")
    plt.xlabel("Habilidade")
    plt.ylabel("Rendimento")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()

def main():
    habilidades = {}
    tabela_rendimento = {}

    while True:
        menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_habilidade(habilidades)
        elif opc == "2":
            listar_habilidades(habilidades)
        elif opc == "3":
            criar_tabela_rendimento(tabela_rendimento)
        elif opc == "4":
            gerar_grafico(tabela_rendimento)
        elif opc == "5":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida.")

main()
