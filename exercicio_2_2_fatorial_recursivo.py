def fatorial_recursivo(num):
    if num == 0 or num == 1:
        return 1
    return num * fatorial_recursivo(num - 1)

