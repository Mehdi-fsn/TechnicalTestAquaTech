from sqlalchemy import DATETIME, FLOAT, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class capteurNiveauEau(Base):
    __tablename__ = "capteurNiveauEau"

    date = Column(DATETIME, primary_key=True,default=None)
    cm = Column(FLOAT, default=None)

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


class capteurPression(Base):
    __tablename__ = "capteurPression"

    date = Column(DATETIME, primary_key=True, default=None)
    bar = Column(FLOAT, default=None)

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}