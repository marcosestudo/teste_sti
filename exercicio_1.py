def ordena(lista):
    listaOrdenada = []
    for nome in lista:
        # busca sequencial pra saber se o próximo nome a ser inserido já existe na lista ordenada pra evitar repetição
        proximo = busca_sequencial(listaOrdenada, nome)
        if proximo != None:
            # busca binária para encontrar o índice da lista onde o próximo nome deve ser inserido de forma ordenada
            posicao = busca_binaria(listaOrdenada, proximo)
            listaOrdenada.insert(posicao, proximo)
    return listaOrdenada



def busca_sequencial(listaOrdenada, nome):
    for nomeOrdenado in listaOrdenada:
        # se o nome já existir na lista ordenada, não retorna nada
        if nome == nomeOrdenado:
            return None
    # se ainda não existir na lista ordenada, retorna o nome a ser inserido
    return nome



def busca_binaria(lista, nome):
    esquerda, direita = 0, len(lista)
    while esquerda < direita:
        meio = (esquerda + direita) // 2
        # aqui não tem a checagem pra saber se o elemento foi encontrado, pois já sabemos que ele não pertence à lista
        if lista[meio] < nome:
            esquerda = meio + 1
        else:
            direita = meio
    # na busca binária, se o elemento não for encontrado, retorna None ou -1, aqui retorna o índice onde o próximo nome será inserido
    return esquerda



# listas pra testes

# lista sem repetições 
# lista = ["Breno Azevedo Souza", "Caua Melo Alves", "Vitoria Cavalcanti Lima", "Andre Cunha Fernandes", "Aline Ferreira Barros"]

# lista com repetições
lista = ["Breno Azevedo Souza", "Caua Melo Alves", "Aline Ferreira Barros", "Vitoria Cavalcanti Lima", "Aline Ferreira Barros", "Caua Melo Alves", "Aline Ferreira Barros", "Vitoria Cavalcanti Lima", "Andre Cunha Fernandes", "Andre Cunha Fernandes",  "Caua Melo Alves"]

print(ordena(lista))