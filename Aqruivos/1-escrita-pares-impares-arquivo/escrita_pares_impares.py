# TODO: Crie um método que irá gravar os números de 0 a 100 em dois arquivos, no arquivo "impares.txt" grave os números ímpares e
# no arquivo "pares.txt" grave os números pares.
# IMPORTANTE: Este exercício não tem teste (pytest).



def escrever_pares_impares():
  for number in range (101):
    if number%2 ==0:
      arquivo=open("pares","a")
      arquivo.write(str(number)+"\n")
      arquivo.close()
    else:
      arquivo=open("impares","a")
      arquivo.write(str(number)+"\n")
      arquivo.close()
escrever_pares_impares()
