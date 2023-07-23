from unittest import mock
from infra.repository.filmes_repository import FilmesRepository
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from infra.entities.filmes import Filmes


class ConnectionHandlerMock:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                  [mock.call.query(Filmes)],
                  [Filmes(titulo="Novo", genero="drama", ano=2024)]
                ),
                (
                    [
                        mock.call.query(Filmes),
                        mock.call.filter(Filmes.titulo == "Teste"),
                    ],
                    [Filmes(titulo="Teste", genero="qualquer", ano=2023)]
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, tb):
        self.session.close()


def test_select():
    repo = FilmesRepository(ConnectionHandlerMock)
    response = repo.select()
    assert isinstance(response, list)


def test_select_drama_filmes():
    filme_repo = FilmesRepository(ConnectionHandlerMock)
    response = filme_repo.select()
    assert isinstance(response[0], Filmes)
    assert response[0].genero == "drama"


def teste_insert():
    repo = FilmesRepository(ConnectionHandlerMock)
    response = repo.insert("antigo", "romance", 1900)
    assert str(response) == 'Filme [titulo=antigo, ano=1900]'
