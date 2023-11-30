from src.livro.livro import Livro


def test_descricao_livro():
    livro = Livro('Harry Hotter', 'J.K.Roulins', 320)
    expected_description = "O livro Harry Hotter de J.K.Roulins possui " \
                           "320 páginas."
    assert livro.__repr__() == expected_description

