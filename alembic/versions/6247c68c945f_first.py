"""first

Revision ID: 6247c68c945f
Revises: 
Create Date: 2023-07-05 17:34:04.481969

"""
import sqlalchemy as sa

from alembic import op
from infra.repository.filmes_repository import FilmesRepository

# revision identifiers, used by Alembic.
revision = '6247c68c945f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(titulo, genero, ano) -> None:
    # TODO: tornar dinâmico
    filmes_repo = FilmesRepository()
    filmes_repo.insert(titulo, genero, ano)


def downgrade(titulo) -> None:
    filmes_repo = FilmesRepository()
    filmes_repo.delete(titulo)
