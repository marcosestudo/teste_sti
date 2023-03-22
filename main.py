import exercicio_1_ordenacao as ordenacao
import exercicio_2_fatorial as fatorial
import exercicio_3_fila as fila
import exercicio_4_busca_em_arquivo as busca

funcao = input("Deseja executar qual função?\n(1) fatorial não-recursivo\n(2) fatorial recursivo\nDigite o número da opção e tecle enter: ")

while funcao not in ["1", "2", "3", "4", "5"]:
    funcao = input("\nEscolha uma opçao válida\nDeseja executar qual função?\n(1) fatorial não-recursivo\n(2) fatorial recursivo\nDigite o número da opção e tecle enter: ")

if funcao == "1" or funcao == "2":
    # while começando com true para iniciar entrado no loop como se fosse um "do while", python não tem "do while"
    while True:
        try:
            # se não inserir um número inteiro, dá erro e cai no except
            num = int(input("Fatorial de: "))
            # se inserir um númro menor que 0, naõ sairá do loop e aparecerá a mensagem pedindo um número válido
            if num < 0:
                print("Digite um número inteiro maior ou igual a 0")
        except:
            # num recebe -1 pra reentrar no while e pedir um número válido
            num = -1
            print("Digite um número inteiro maior ou igual a 0") 
        # sendo inserido um número inteiro maior ou igual a 0, sai do loop
        if num >= 0:
            break
    if funcao == 1:
        print("\nExecutando funcão: fatorial_nao_recursivo")
        fat = fatorial.fatorial_nao_recursivo(num)
    else:
        print("\nExecutando funcão: fatorial_recursivo")
        fat = fatorial.fatorial_recursivo(num)
    print(f"O fatorial de {num} é {fat}")    

elif funcao == "3":
    print("trabalhando...")

elif funcao == "4":
    print("trabalhando...")

elif funcao == "5":
    print("trabalhando...")