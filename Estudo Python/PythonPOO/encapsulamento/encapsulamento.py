class BaseDedados:
    def __init__(self):
        # Variavéis/metodos com um _ (underline), não deve ser acessada, é um private "mais fraco", ainda assim é possível acessar
        # Com dois __ (underline), não é possível acessar/modificar
        self._dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self._dados['clientes'][id]

bd = BaseDedados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Thamires')
bd.inserir_cliente(3, 'Marina')
bd.apaga_cliente(1)
bd.lista_clientes()
