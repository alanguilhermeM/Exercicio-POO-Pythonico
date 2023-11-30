from src.livro.livro import Livro


def test_cria_livro():
    li = Livro('Harry Hotter', 'J.K.Roulins', 320)
    assert li.titulo == "Harry Hotter"
    assert li.autor == "J.K.Roulins"
    assert li.paginas == 320
