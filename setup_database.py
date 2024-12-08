import sqlite3

# Conecta o banco de dados
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    tipo TEXT CHECK(tipo IN ('admin', 'comum')) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS especialistas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS perguntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    pergunta TEXT NOT NULL,
    info_perguntas TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS respostas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pergunta INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    resumo TEXT NOT NULL,
    recomendacao TEXT,
    explicacao TEXT,
    FOREIGN KEY (id_pergunta) REFERENCES perguntas(id),
    FOREIGN KEY (user_id) REFERENCES usuarios(id)
)
''')

conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")
