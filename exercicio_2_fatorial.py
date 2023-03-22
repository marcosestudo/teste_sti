# fatorial náo recursivo
def fatorial_nao_recursivo(num):
    cont = 1
    fat = 1

    while cont <= num:
        fat *= cont
        cont += 1

    return fat


# fatorial recursivo
def fatorial_recursivo(num):
    if num == 0 or num == 1:
        return 1
    return num * fatorial_recursivo(num - 1)