# TODO: Crie um método que irá ler o arquivo "pares.txt" e irá salvar no arquivo "multiplos.txt" todos os múltiplos de 3, um número por linha.
# IMPORTANTE: Este exercício não tem teste (pytest).

def leitura_escrita_arquivo():
  with open("pares","r") as arquivo:
    numero=int(arquivo.readlines().pop("\n"))
  if numero%3 == 0:

        arquivo=open("multiplos","a")
        arquivo.write(str(numero)+"\n")
  print(numero)

leitura_escrita_arquivo()
