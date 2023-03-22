class Fila:
    # método construtor
    def __init__(self):
        self.elementos = []

    def insere(self, elem):
        self.elementos.append(elem)

    def remove(self):
        if len(self.elementos) != 0:
            return self.elementos.pop(0)
        else:
            print("A fila está vazia")
            return None

    def tam(self):
        print(f"A fila tem {len(self.elementos)} elemento(s)")

    def proximo(self):
        if len(self.elementos) != 0:
            print(f"O próximo elmento a sair da fila é: {self.elementos[0]}")
        else:
            print("A fila está vazia")



print("Qual operação deseja realizar na fila?\n(1) inserir elemento\n(2) remover elemento\n(3) Ver quantos elementos a fila possui\n(4) Ver qualé o próximo elemento a sair da fila")
