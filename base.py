#
# Exemplos de operações envolvendo coleções
#
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

usuarios_a_serem_notificados = usuarios_data_science.copy()
# Observação sobre o método copy(): em se tratando de objetos, a coleção de destino não receberá os objetos
# inteiros. Receberá tão somente uma referência para o objeto presente na coleção original (shallow copy).
usuarios_a_serem_notificados.extend(usuarios_machine_learning)
print(usuarios_a_serem_notificados)

# O objeto usuarios_a_serem_notificados é uma lista e como tal, aceita repetições. Se não queremos que um objeto
# ou um valor ocorra mais de uma vez dentro da coleção, devemos usar set. Set aceita como argumento um iterável e
# não somente listas.
usuarios_a_serem_notificados = set(usuarios_a_serem_notificados)
print(usuarios_a_serem_notificados) # Será impresso {23, 56, 42, 43, 13, 15}

# Coleções do tipo set não preservam a posição dos elementos. Portanto, não é possível acessar um elemento qualquer
# do conjunto através de seu índice. A linha abaixo, por exemplo, resulta no erro
# TypeError: 'set' object is not subscriptable
# print(usuarios_a_serem_notificados[2])

# Iterando sobre um set
for usuario in usuarios_a_serem_notificados:
    print(usuario)

# Redefinindo as listas iniciais do programa como set
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

# Aplicar a operação or (|) sobre dois conjuntos devolve a união de ambos:
usuarios_finais = usuarios_data_science | usuarios_machine_learning
print(f'Resultado do operador | sobre os dois conjuntos {usuarios_finais}')

# Já a intersecção de 2 conjuntos pode ser obtida através do operador and (&)
usuarios_dois_cursos = usuarios_data_science & usuarios_machine_learning
print(f'Resultado do operador & sobre os dois conjuntos {usuarios_dois_cursos}')

# Se for necessário saber quais elementos estão presentes em um conjunto e não estão presentes no
# outro deve-se usar o operador de menos (-)
usuarios_que_nao_fizeram_machine_learning = usuarios_data_science - usuarios_machine_learning
print(f'Resultado do operador - sobre os dois conjuntos {usuarios_que_nao_fizeram_machine_learning}')

# Para saber os usuários que só fizeram data science ou só fizeram machine learning, deve-se
# utilizar o operador ^ (ou exclusivo)
so_ds_ou_so_ml = usuarios_data_science ^ usuarios_machine_learning
print(so_ds_ou_so_ml)

# Pode-se adicionar elementos a um conjunto com o método add(). Caso o elemento a ser inserido já
# exista no conjunto ele não será adicionado mas essa operação não levanta nenhum erro. Convém
# lembrar que não é possível determinar a posição em que o novo elemento será inserido no conjunto.
usuarios = {8, 32, 27, 54, 5, 2012}
print(usuarios)
usuarios.add(2012) # O elemento já existe e nada será feito.
print(usuarios)
usuarios.add(1967)
print(usuarios)

# Por padrão, sets são objetos mutáveis em Python. Caso seja necessário tornar um set imutável
# deve-se utilizar o método frozenset:
usuarios = frozenset(usuarios)
# usuarios.add(666) # Resulta no erro AttributeError: 'frozenset' object has no attribute 'add'