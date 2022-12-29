from sqlalchemy import Column, Integer, REAL, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MusicLibrary(Base):
    __tablename__ = 'music_library'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    duration = Column(REAL, nullable=False)

