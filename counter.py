from collections import defaultdict, Counter

# Nesse arquivo será mostrado um exemplo de como o defaultdict instância automaticamente um objeto do
# tipo referenciado em sua definição.

class Conta:
    def __init__(self):
        print('Criando uma conta')

# Cria um defaultdict cujos elementos serão do tipo Conta

dicionario_contas = defaultdict(Conta)
# Ao identificar que a chave 12 não existe no dicionário, automaticamente defaultdict irá criar uma nova
# instância de Conta
dicionario_contas[12]

dicionario_contas[88] # Mesmo comportamento novamente.

# Existe um dicionário muito mais simples de ser utilizado para o cenário desse programa: Counter.
# Retornando ao exemplo de contar ocorrências de palavras em um texto, agora usando Counter. Por padrão,
# Counter inicia com valor zero.
meu_texto = "Sergei Vasilyevich Rachmaninoff[a][b] (1 April [O.S. 20 March] 1873 – 28 March 1943) was a Russian composer, virtuoso pianist, and conductor. Rachmaninoff is widely considered one of the finest pianists of his day and, as a composer, one of the last great representatives of Romanticism in Russian classical music. Early influences of Tchaikovsky, Rimsky-Korsakov, and other Russian composers gave way to a thoroughly personal idiom notable for its song-like melodicism, expressiveness and rich orchestral colours.[4] The piano is featured prominently in Rachmaninoff's compositional output and he made a point of using his skills as a performer to fully explore the expressive and technical possibilities of the instrument."

# Com Counter não há a necessidade de informar uma defaultfactory para inicializar os valores no dicionário.
ocorrencias = Counter()
for palavra in meu_texto.split():
  ocorrencias[palavra] += 1

# Com Counter o código pode tornar-se ainda mais simples já que ele aceita em seu Construtor um iterable.
# Então o código do bloco acima pode ser reduzido a apenas uma linha:
ocorrencias = Counter(meu_texto.split())
print(ocorrencias)