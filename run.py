from infra.configs.connection import DBConnectionHandler
from infra.repository.atores_repository import AtoresRepository
from infra.repository.filmes_repository import FilmesRepository

repo = AtoresRepository()
data = repo.select()
print(data)


repo2 = FilmesRepository(DBConnectionHandler)
response = repo2.select()
filme = response[0]
print(response)
