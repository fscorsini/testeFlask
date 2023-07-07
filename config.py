SECRET_KEY = 'Corsini'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'senha',
        servidor = 'bdjogos',
        database = 'jogoteca'
    )