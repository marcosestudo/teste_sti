# import para uso de expressões regulares
import re

def contaNome(arquivo, palavra):
    # abrindo arquivo
    arquivo =  open(arquivo, "r")

    # lendo texto e armazenando na variável
    texto = arquivo.read()

    # re.sub - removendo caracteres não alfanuméricos do texto
    # lower - convertendo todas palavras em lower case para acharmos independentemente de letras maiúculas
    # slpit - armazenando todas as palavra separadas por espaço em uma lista
    palavras = re.sub(r"\W+", " ", texto).lower().split()


    # fechando arquivo
    arquivo.close()

    # fazendo a busca com a palavra buscada em lower case
    palavra = palavra.lower()
    
    contador = 0
    
    for palavraListada in palavras:
        if palavraListada == palavra:
            contador += 1

    print(f'\nA palavra {palavra} aparece {contador} vezes no arquivo')

contaNome("exercicio_4.txt", "lorem")


# solução usando count
# a função count contabiliza a palavra buscada independentemente dela estar separada por espaços
# eu preferi fazer da forma acima para desenvolver um pouco melhor o raciocínio da questão
# descomentando o código abaixo usando a função count, vemos que o resultado das duas funções é o mesmo

# def contaNomeComCount(arquivo, palavra):
#     arquivo =  open(arquivo, "r")

#     texto = arquivo.read().lower()
#     arquivo.close()

#     print(f'Usando count: A palavra {palavra} aparece {texto.count(palavra.lower())} vezes no arquivo')

# contaNomeComCount("exercicio_4.txt", "Lorem")
