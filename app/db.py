from sqlalchemy import create_engine, text

engine = create_engine('postgresql://postgres:postgres@localhost:5432/delman')

# with engine.connect() as connection:
#     result = connection.execute(text("select username from employees"))
#     for row in result:
#         print("username:", row['username'])

def connect_db():
    try:
        engine.connect()
        return engine
    except:
        print('failed connecto to db')

# connect_db()