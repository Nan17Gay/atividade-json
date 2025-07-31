import json

ARQUIVO = "tbbt.json"

with open(ARQUIVO, "a+") as arquivo:
    arquivo.seek(0)
    try:
        json.load(arquivo)
    except:
        arquivo.write("[]")

def carregar():
    with open(ARQUIVO, "r") as arquivo:
        return json.load(arquivo)
    
def listar():
    dados = carregar()
    for p in dados:
        print(p)

def criar():
    nome = input("Nome: ")
    idade = input("Idade: ")
    profissao = input("Profissao: ")
    conjuge = input("Conjuge: ")

    dados = carregar()
    dados.append({
        "nome": nome, 
        "idade": idade, 
        "profissao": profissao, 
        "conjuge": conjuge
        })
    salvar(dados)
    print("Salvo!")

def atualizar():
    nome = input("Nome para atualizar: ")
    dados = carregar()
    for linha in dados:
        if linha["nome"] == nome:
            linha["idade"] = input("Nova idade: ")
            linha["profissao"] = input("Nova profissao: ")
            salvar(dados)
            print("Atualizado!")
            return
    print("Nome não encontrado.")

def salvar(dados):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def deletar():
    nome = input("Nome para deletar: ")
    dados = carregar()
    for linha in dados:
        if linha["nome"] == nome:
            dados.remove(linha)
            salvar(dados)
            print("\n\n ❌ Deletado! \n\n")
            return
    print("Nome não encontrado.")

def menu():
    opcao = 0 # jeito gambiarra kk
    while opcao !=5:
        print("\n1 - Criar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("5 - Sair")
        opcao = int(input("Escolha: "))
        if opcao == 1:
            criar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        elif opcao == 5:
            break

menu()