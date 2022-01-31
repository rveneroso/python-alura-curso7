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