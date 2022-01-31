# Dicionários são estruturas de dados que assumem a forma chave : valor
aparicoes = {
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}
print(type(aparicoes))

# Para obter o valor para uma determinada chave deve-se fazer:
palavra = "Guilherme"
print("A palavra {} ocorre {} veze(s) no dicionário".format(palavra, aparicoes[palavra]))

# Se se tentar obter o valor para uma chave que não existe ocorrerá um erro do tipo KeyError
# print(aparicoes["ovomaltine"]) # KeyError: 'ovomaltine'

# Em se tratando de números é possível usar uma alternativa na busca por ocorrências de um termo no
# dicionário que é através do método get(). Por exemplo:
palavra = "guilhotina"
# O zero na sintaxe abaixo funciona como um valor default caso a chave não seja encontrada
print("A palavra {} ocorre {} veze(s) no dicionário".format(palavra, aparicoes.get(palavra, 0)))

palavra = "cachorro"
# Se a chave for encontrada o número de ocorrência retornará normalmente.
print("A palavra {} ocorre {} veze(s) no dicionário".format(palavra, aparicoes.get(palavra, 0)))

# É possível também criar dicionários de outro forma como no exemplo abaixo:
dias_da_semana = dict(Domingo = 1, Segunda = 2, Terça = 3, Quarta = 4, Quinta = 5, Sexta = 6, Sábado = 7)
print(dias_da_semana)

# Para adicionar um elemento a um dicionário já existente:
aparicoes["Ovomaltine"] = 5
print(aparicoes)

# Reatribuir um valor a uma chave já existente simplesmente substitui o valor existente.
aparicoes["Ovomaltine"] = 3
print(aparicoes)

# Para remover um item já existente no dicionário usamos del:
del aparicoes["Ovomaltine"]
print(aparicoes)

# Tentar remover um elemento cuja chave não existe resulta em KeyError
# del aparicoes["Ovomaltine"]
# print(aparicoes)

# Para verificar se uma determinada chave ocorre no dicionário podemos usar in
print("cachorro" in aparicoes)

# É possível iterar sobre um dicionário imprimindo suas chaves.
for elemento in aparicoes:
    print(elemento)

# Outra forma de iterar sobre as chaves de um dicionário
for elemento in aparicoes.keys():
    print(elemento)

# Também é possível iterar sobre os valores de um dicionário
for valor in aparicoes.values():
    print(valor)

# Para iterar simultâneamente sobre as chaves e os valores de um dicionário
for item in aparicoes.items():
    print(item)

for key, value in aparicoes.items():
    print(f'No dicionário a palavra {key} ocorre {value} vez(es)')