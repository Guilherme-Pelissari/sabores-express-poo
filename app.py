from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_praca = Restaurante('praça', 'Gourmet')

bebida_suco = Bebida('Dell valle',5.00,'grande')
prato_pf = Prato('Parmegiana',30.00,'Parmegiana de frango com arroz')
bebida_suco.aplicar_desconto()
prato_pf.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pf)

def main():
    restaurante_praca.exibir_cardapio

# Bloco principal para executar o código
if __name__ == '__main__':
    main()