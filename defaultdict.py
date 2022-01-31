from collections import defaultdict

meu_texto = "Sergei Vasilyevich Rachmaninoff[a][b] (1 April [O.S. 20 March] 1873 – 28 March 1943) was a Russian composer, virtuoso pianist, and conductor. Rachmaninoff is widely considered one of the finest pianists of his day and, as a composer, one of the last great representatives of Romanticism in Russian classical music. Early influences of Tchaikovsky, Rimsky-Korsakov, and other Russian composers gave way to a thoroughly personal idiom notable for its song-like melodicism, expressiveness and rich orchestral colours.[4] The piano is featured prominently in Rachmaninoff's compositional output and he made a point of using his skills as a performer to fully explore the expressive and technical possibilities of the instrument."

# Cria um dicionário que define um valor default para quando uma chave não for localizada. Na prática o construtor
# de defaultdict espera uma defaultfactory que é basicamente uma função ou algo capaz de retornar um valor que
# sirva como default. No exemplo abaixo está sendo usado o tipo int porque int() retorna 0 quando nenhum valor é
# passado à função. Portanto, int() serve como defaultfactory para o defaultdict.
ocorrencias = defaultdict(int)

for palavra in meu_texto.split():
  ocorrencias[palavra] += 1 # Reduzindo o código da versão anterior

for palavra, numero_ocorrencias in ocorrencias.items():
    print(f'A palavra {palavra} ocorre {numero_ocorrencias} no texto')
