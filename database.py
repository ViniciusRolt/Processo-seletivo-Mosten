import sqlite3

def create_db():
    conn = sqlite3.connect('filmes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            diretor TEXT,
            ano INTEGER,
            genero TEXT
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
    print("Banco e tabela criados com sucesso!")
