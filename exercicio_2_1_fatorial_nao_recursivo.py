def fatorial_nao_recursivo(num):
    cont = 1
    fat = 1

    while cont <= num:
        fat *= cont
        cont += 1

    return fat
