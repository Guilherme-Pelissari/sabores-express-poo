from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    """
    Representa um restaurante e suas características.
    """
    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Args:
            nome (str): O nome do restaurante.
            categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()  
        self._categoria = categoria.upper() 
        self._ativo = False 
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)   

    def __str__(self):
        """
        Retorna uma representação em string do objeto Restaurante.
        """
        return f'{self._nome} | {self._categoria}'

    @classmethod 
    def listar_restaurantes(cls):
        """
        Exibe uma lista formatada de todos os restaurantes registrados.
        """
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}")
        print("-" * 80)
        for restaurante in cls.restaurantes:
            # Imprime os detalhes de cada restaurante, incluindo nome, categoria, avaliação média e status
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """
        Retorna um emoji que representa o status do restaurante (ativo ou inativo).
        """
        return '✅' if self._ativo else '❎' 

    def alternar_estado(self):
        """
        Alterna o estado de atividade do restaurante.
        """
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Recebe uma avaliação e a adiciona à lista de avaliações do restaurante.

        Args:
            cliente (str): O nome do cliente que fez a avaliação.
            nota (float): A nota dada pelo cliente (de 1 a 5).
        """
        # Verifica se a nota está dentro do intervalo válido (entre 0 e 5)
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """
        Calcula e retorna a média das avaliações do restaurante.
        """
        if not self._avaliacao:
            return '-'  # Retorna '-' se não houver avaliações
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)  # Calcula a média e arredonda para uma casa decimal
        return media
    

    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item,'descricao'):
                mensagem_prato = f'{i} Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i} Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)