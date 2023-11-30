class Produto:
    def __init__(
        self, nome: str, codigo: str, preco: float, quantidade: int
    ) -> None:
        self.__nome = nome
        self.__codigo = codigo
        self.__preco = preco
        self.__quantidade = quantidade

    def get_preco(self) -> float:
        return self.__preco

    def get_quantidade(self) -> int:
        return self.__quantidade

    def atualizar_preco_do_produto(self, novo_preco: float) -> None:
        if novo_preco < 0:
            raise ValueError("Preço não pode ser negativo")

        self.__preco = novo_preco

    def adicionar_estoque_do_produto(self, quantidade: int) -> None:
        if self.__quantidade < 0:
            raise ValueError("Quantidade não pode ser negativo")

        self.__quantidade += quantidade

    def remover_estoque_do_produto(self, quantidade: int) -> None:
        if self.__quantidade < quantidade:
            raise ValueError(f'Estoque insuficiente: {self.__quantidade}')

        self.__quantidade -= quantidade


instance = Produto('Notebook', 'A3dh4', 2, 1)
print(instance.atualizar_preco_do_produto(2))
