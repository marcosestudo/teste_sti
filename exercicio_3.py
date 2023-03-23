class Fila:
    # método construtor
    def __init__(self):
        self.elementos = []

    def insere(self, elem):
        self.elementos.append(elem)

    def remove(self):
        if len(self.elementos) != 0:
            removido = self.elementos.pop(0)
            print(f"\nElemento removido: {removido}")
            return removido
        else:
            print("A fila está vazia")
            return None

    def tam(self):
        print(f"\nA fila tem {len(self.elementos)} elemento(s)")

    def proximo(self):
        if len(self.elementos) > 0:
            print(f"\nO próximo elmento a sair da fila é: {self.elementos[0]}")
        else:
            print("A fila está vazia")



# instanciando a fila
nossaFila = Fila()



def operacoes_fila(fila):
    # operacao iniciando com -1 para entra no loop perguntando a sua opcao simulando ofuncionamento de um "do while", python não tem "do while"
    operacao = -1

    while operacao not in ["1", "2", "3", "4", "5"]:
        print("\nQual operação deseja realizar na fila?")
        print("(1) inserir elemento")
        print("(2) remover elemento")
        print("(3) Ver quantos elementos a fila possui")
        print("(4) Ver qual é o próximo elemento a sair da fila")
        print("(5) Sair")
        operacao = input("\nDigite o número da opção e tecle enter: ")
        
        if operacao not in ["1", "2", "3", "4", "5"]:
            print("Opção inválida")

        if operacao == "1":
            elem = input("\nDigite o elemento que será inserido na fila e tecle enter: ")
            fila.insere(elem)

        elif operacao == "2":
            fila.remove()

        elif operacao == "3":
            fila.tam()

        elif operacao == "4":
            fila.proximo()

        elif operacao == "5":
            break
        
        confirmacao = -1

        while confirmacao not in ["1", "2"]:
            confirmacao = input("\nDeseja fazer outra operação na fila\n(1) Sim\n(2) Não\nDigite a opção e tecle enter: ")
            if confirmacao not in ["1", "2"]:
                print("Opção inválida")
                           
        # se a opção da confirmação for 1, confirmação continua sendo -1 para cair no loop das opções no início do código
        # se a opção for 2, sai do loop e encerra o programa
        if confirmacao == "2":
            break



operacoes_fila(nossaFila)