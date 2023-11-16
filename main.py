lista_clientes = []
lista_receitas = []
global receitas, continuar
continuar = 's'
receitas = 0.0
despesas = 0.0
saldo = receitas - despesas


def cadastroCliente():
  continuar = 's'
  print(continuar)
  while(continuar == 's'):
    
    print("\nCadastro de Cliente")
    nome = input("Nome: ")
    cpf_cnpj = input("CPF ou CNPJ: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
  
    cliente = {
      "nome": nome,
      "cpf_cnpj": cpf_cnpj,
      "telefone": telefone,
      "endereco": endereco
    }
    lista_clientes.append(cliente)
    print(cliente)
    print(lista_clientes)

    continuar = input("continuar? ")

  cadastroReceita()
  
def cadastroReceita():
  global receitas,continuar
  while(continuar == 's'):
    
    print("\nCadastro de Receita")
    nome = input("Nome do cliente: ")
    valor_venda = float(input("Valor da venda: "))
    data_atual = input("Data de hoje: ")
    data_recebimento = input("Data em que o valor será recebido: ")
    
  
    receita = {
      "nome": nome,
      "valor_venda": valor_venda,
      "data_atual": data_atual,
      "data_recebimento": data_recebimento
    }
    if lista_clientes != []:

      #verifica se na lista_clientes, entre os dicionarios de cliente, há algum nome igual ao que foi digitado
      if any(cliente['nome'] == nome for cliente in lista_clientes):
        lista_receitas.append(receita)
        print(lista_receitas)
        receitas += valor_venda
        print(receitas)
        print("Cadastro realizado com sucesso!")
      else: 
        print("Não existe esse cliente")
    else:
      print("Não existe nenhum cliente cadastrado!")

    continuar = input("continuar? ")


'''a = int(input("esc: "))




if a == 1:
  cadastroCliente()
elif a == 2:
  cadastroReceita()
else:
  print(":((((")'''
