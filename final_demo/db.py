from sqlalchemy import create_engine

engine = create_engine('postgresql://admin:admin@mydb/music', echo=True)
# engine = create_engine('sqlite:///db.sqlite3', echo=True)
