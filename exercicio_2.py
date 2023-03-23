def fatorial_nao_recursivo(num):
    cont = 1
    fat = 1

    while cont <= num:
        fat *= cont
        cont += 1

    return fat



while True:
    try:
        # se não inserir um número inteiro, dá erro e cai no except
        num = int(input("Digite um número inteiro maior ou igual a 0: "))
        # se inserir um númro menor que 0, naõ sairá do loop e aparecerá a mensagem pedindo um número válido
        if num < 0:
            print("Número inválido")
    except:
        # num recebe -1 pra reentrar no while e pedir um número válido
        num = -1
        print("Número inválido") 
    # sendo inserido um número inteiro maior ou igual a 0, sai do loop
    if num >= 0:
        break



print(f"O fatorial de {num} é {fatorial_nao_recursivo(num)}")
