from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')

bebida_suco = Bebida('Dell valle',5.00,'grande')
prato_pf = Prato('Parmegiana',30.00,'Parmegiana de frango com arroz')
sobremesa_bolo_chocolate = Sobremesa('Bolo de Chocolate',10.00,'Bolo')
sobremesa_manga = Sobremesa('Manga fresca',2.00,'Fruta')

bebida_suco.aplicar_desconto()
prato_pf.aplicar_desconto()
sobremesa_manga.aplicar_desconto()
sobremesa_bolo_chocolate.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pf)
restaurante_praca.adicionar_no_cardapio(sobremesa_bolo_chocolate)
restaurante_praca.adicionar_no_cardapio(sobremesa_manga)

def main():
    restaurante_praca.exibir_cardapio

# Bloco principal para executar o código
if __name__ == '__main__':
    main()