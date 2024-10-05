from modelos.restaurante import Restaurante

# Criando instâncias da classe Restaurante
restaurante_hotdog = Restaurante('HotDog', 'Cachorro Quente')
restaurante_hotdog.receber_avaliacao('marcelo', 1)  # Nota como número
restaurante_hotdog.receber_avaliacao('lais', 1)
restaurante_hotdog.receber_avaliacao('leo', 1)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
