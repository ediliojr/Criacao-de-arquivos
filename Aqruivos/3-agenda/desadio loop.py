AGENDA = {'Tulio': '3333-3333'}
my_dict={}
i=0
def adicionar_contato():
  # TODO: Neste método você deverá adicionar um item na agenda

  nome=input("Digite o nome: ")
  num=input("Digite o numero: ")

  my_dict = {nome : num}
  AGENDA.update(my_dict)

def remover_contato():
  # TODO: Neste método você deverá ser capaz de remover um contato da agenda.
  nome=input("Digite o nome: ")
  AGENDA.pop(nome)
  pass
  print('Agenda aberta')

# TODO: Criar aqui um menu com as opções conforme exemplo.

  print('Agenda fechada')


def start():

  print("Escolha uma opção:\n1. Exibir agenda\n2. Adicionar um novo contato\n3. Remover um contato")
  print("4. Sair")
  n=int(input("Digite um numero:"))

  while n<5 and n>0:
    if n==1:
      nomes=AGENDA.keys()
      valores=AGENDA.values()
      for i in nomes:
        print("Contato:", i,"telefone",AGENDA[i])
      return start()
    if n==2:
      adicionar_contato()
      return start()
    if n==3:
      remover_contato()
      return start()
    if n==4:
      break
    break
  print("\nNumero invalido\n")
  return start()

start()
