class Avaliacao:
    """
    Representa uma avaliação feita por um cliente para um restaurante.
    """
    def __init__(self, cliente, nota):
        """
        Inicializa uma instância de Avaliacao.

        Args:
            cliente (str): O nome do cliente que fez a avaliação.
            nota (float): A nota atribuída à avaliação.
        """
        self._cliente = cliente  # O nome do cliente que avaliou
        self._nota = nota  # A nota dada pelo cliente
    