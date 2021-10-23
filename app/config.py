class Config(object):
    """
    class Config to store credential information
    """
    SECRET_KEY = '\xce\xcc\x9eV\x978\xafpbdO@J\x92\xcc\x80\xa8\xc5\xa0\xbbu&\x84\xba'
    DB_USERNAME = 'postgres'
    DB_PASSWORD = 'postgres'
    DB = 'delman'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/delman'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
