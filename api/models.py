from sqlalchemy import Column, Integer, String, Text

from .database import Base


class Analise(Base):

    __tablename__ = "analises"

    id = Column(Integer, primary_key=True, index=True)
    cidade = Column(String, nullable=False)
    relatorio = Column(Text, nullable=False)