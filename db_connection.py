import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",
        database="nome_do_banco",
        user="seu_usuario",
        password="sua_senha"
    )
    return conn

def get_data_from_db(query):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data
