
import os

lista_clientes = []
lista_receitas = []
global receitas
global continuar
global tamanho_arquivo_clientes
tamanho_arquivo_clientes = os.path.getsize("clientes.txt")
continuar = 's'
receitas = 0.0
despesas = 0.0
saldo = receitas - despesas




def cadastrar_cliente():


  if tamanho_arquivo_clientes == 0:
    with open('clientes.txt', 'w') as arquivo_clientes:
      #depois adicionar loop de clientes
      continuar = 's'
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
  
        arquivo_clientes.write(str(cliente))

        #lista_clientes.append(cliente)
  
        continuar = input("continuar? ")
  else:
    with open('clientes.txt', 'a') as arquivo_clientes:
      #loop_clientes() --> depois adicionar loop clientes
      continuar = 's'
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

        arquivo_clientes.write("\n\n" + str(cliente))

        #lista_clientes.append(cliente)

        continuar = input("\ncontinuar? ")
  
  

'''def loop_clientes():
  continuar = 's'
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

    arquivo_clientes.write()
    lista_clientes.append(cliente)

    continuar = input("continuar? ")
'''
  
def cadastrar_receita():
  global continuar
  global receitas
  
  while(continuar == 's'):
    
    print("\nCadastro de Receita")
    input("Nome do cliente: ")
    float(input("Valor da venda: "))
    input("Data de hoje: ")
    input("Data em que o valor será recebido: ")
    
  
    
    import json
    
    if tamanho_arquivo_clientes != 0:

      #verifica se na lista_clientes, entre os dicionarios de cliente, há algum nome igual ao que foi digitado
      with open('clientes.txt', 'r') as arquivo_clientes:
        clientes_cadastrados = arquivo_clientes.readlines()


        for cliente in clientes_cadastrados:
          #cliente_dict = dict(cliente)
          cliente_dict = json.loads(cliente.replace(" \' "," \" "))
          print(type(cliente_dict))
          print(cliente)
          print("\n")
          print(cliente_dict)
        '''    
        if any(cliente["nome"] == nome_cliente for cliente in clientes_cadastrados):
          lista_receitas.append(receita)
          print(lista_receitas)
          receitas += valor_venda
          print(receitas)
          print("Cadastro realizado com sucesso!")
        else: 
          print("Não existe esse cliente")
          '''
    else:
      print("Não existe nenhum cliente cadastrado!")
        
        

    continuar = input("continuar? ")




while True:
  print("\n==== Menu ====")
  print("1. Cadastrar Cliente")
  print("2. Cadastrar Receita")
  print("3. Cadastrar Despesa")
  print("4. Atestar Recebimento de Receita")
  print("5. Pagar Conta")
  print("6. Exibir relatórios financeiros")
  print("0. Sair")
  '''
  print("6. Listar Receitas Recebidas")
  print("7. Listar Despesas Recebidas")
  print("8. Listar Despesas a Receber")
  print("9. Listar Clientes que Melhor Impactaram o Financeiro")
  print("10. Listar Despesas Mais Caras por Tipo")
  print("11. Listar Despesas por Categoria (Interna/Externa)")
  print("12. Comparar Períodos (por Lucro)")
  print("13. Exibir Saldo Atual")
  print("0. Sair")'''

  escolha = input("Escolha uma opção: ")

  if escolha == "0":
    break
  elif escolha == "1":
    cadastrar_cliente()
  elif escolha == "2":
    cadastrar_receita()
  else:
    print("Opção inválida. Tente novamente.")
  '''elif escolha == "3":
      cadastrar_despesa()
  elif escolha == "4":
      atestar_recebimento_receita()
  elif escolha == "5":
      pagar_conta()
  elif escolha == "6":
      relatorios_financeiros()'''

