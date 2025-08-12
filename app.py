from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_mexicano = Restaurante('Mexican food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('camila', 5)
restaurante_praca.receber_avaliacao('felipe', 7)



restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()