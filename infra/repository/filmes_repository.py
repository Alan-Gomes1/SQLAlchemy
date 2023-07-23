from sqlalchemy.orm.exc import NoResultFound

from infra.entities.filmes import Filmes


class FilmesRepository:
    def __init__(self, ConnectionHandler):
        self.__ConnectionHandler = ConnectionHandler

    def select(self):
        with self.__ConnectionHandler() as db:
            try:
                data = db.session.query(Filmes).all()
                return data
            except NoResultFound:
                return None

    def insert(self, titulo, genero, ano):
        with self.__ConnectionHandler() as db:
            try:
                data = Filmes(titulo=titulo, genero=genero, ano=ano)
                db.session.add(data)
                db.session.commit()
                return data
            except Exception as e:
                db.session.rollback()
                raise e

    def update(self, titulo):
        with self.__ConnectionHandler() as db:
            try:
                db.session.query(Filmes).filter(
                    Filmes.titulo == titulo).update({"titulo": titulo})
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e

    def delete(self, titulo):
        with self.__ConnectionHandler() as db:
            try:
                db.session.query(Filmes).filter(
                    Filmes.titulo == titulo).delete()
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
