from modelos.restaurante import Restaurante

# Criação de instâncias da classe Restaurante
restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_mexicano = Restaurante('Mexican food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

# Exemplo de uso do método receber_avaliacao para o restaurante_praca
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('camila', 5) 
restaurante_praca.receber_avaliacao('felipe', 7) 

# Exemplo de uso do método alternar_estado para o restaurante_mexicano
restaurante_mexicano.alternar_estado()

def main():
    """
    Função principal que executa a listagem dos restaurantes.
    """
    Restaurante.listar_restaurantes()

# Bloco principal para executar o código
if __name__ == '__main__':
    main()