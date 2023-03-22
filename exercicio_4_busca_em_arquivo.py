def contaNome(arquivo, nome):
    # abrindo arquivo
    arquivo =  open(arquivo, "r")

    # lendo linhas do arquivo
    linhas = arquivo.readlines()

    # fechando arquivo
    arquivo.close()

    # criando lista vazia pra receber as palavras do arquivo
    palavras = []

    # inserindo todos as palavras do arquivo na lista para que possamos contar quantas vezes o nome buscado aparece
    for linha in linhas:
        palavras.extend(linha.split())

    print(palavras)

    return palavras.count(nome)       


print(contaNome("exercicio_4.txt", "Sophia"))