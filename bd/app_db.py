from sqlalchemy import create_engine

def create_db(name):
    bd = create_engine(f'sqlite:///{name}.db')
    return bd
