from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,

)


from config import MYSQL_URL


engine = create_engine(MYSQL_URL)
meta = MetaData()



class TVShowsManager():
    def __init__(self, engine) -> None:
        self.engine = engine
        self.shows = self.get_shows_schema()

    def get_shows_schema(self):
        shows = Table(
            'tvshows', meta,
            Column('id', Integer, primary_key=True),
            Column('place', Integer),
            Column('title', String(255)),
            Column('year', String(10)),
            Column('rating', String(10)),
            Column('link', String(255))
        )
        return shows

    def create_table(self):
        meta.create_all(self.engine, checkfirst=True)
        print('таблица успешно создана')

    def insert_show(self, data):
        ins = self.shows.insert().values(
            **data
        )
        with self.engine.connect() as connect:
            connect.execute(ins)
            connect.commit()

    def delete_table(self):
        self.shows.drop(self.engine, checkfirst=True)
        print('таблица успешно удалена')