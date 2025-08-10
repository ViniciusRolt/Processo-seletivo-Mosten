from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Libera acesso CORS para o front-end

DB_NAME = "filmes.db"

# --- FUNÇÕES DE BANCO DE DADOS ---

def criar_tabela():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT NOT NULL,
            descricao TEXT,
            imagem TEXT NOT NULL,
            gostei INTEGER DEFAULT 0,
            naoGostei INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def listar_filmes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM filmes")
    rows = cursor.fetchall()
    conn.close()
    filmes = []
    for r in rows:
        filmes.append({
            "id": r[0],
            "titulo": r[1],
            "genero": r[2],
            "descricao": r[3],
            "imagem": r[4],
            "gostei": r[5],
            "naoGostei": r[6]
        })
    return filmes

def inserir_filme(titulo, genero, descricao, imagem):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO filmes (titulo, genero, descricao, imagem) VALUES (?, ?, ?, ?)",
        (titulo, genero, descricao, imagem)
    )
    conn.commit()
    conn.close()

def votar(id, tipo):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    if tipo == "gostei":
        cursor.execute("UPDATE filmes SET gostei = gostei + 1 WHERE id = ?", (id,))
    elif tipo == "naoGostei":
        cursor.execute("UPDATE filmes SET naoGostei = naoGostei + 1 WHERE id = ?", (id,))
    else:
        conn.close()
        return False
    conn.commit()
    conn.close()
    return True

def totais_gerais():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(gostei), SUM(naoGostei) FROM filmes")
    res = cursor.fetchone()
    conn.close()
    return {
        "total_gostei": res[0] or 0,
        "total_naoGostei": res[1] or 0
    }

# --- ROTAS ---

@app.route("/api/filmes", methods=["GET"])
def api_listar_filmes():
    filmes = listar_filmes()
    return jsonify(filmes)

@app.route("/api/filmes", methods=["POST"])
def api_cadastrar_filme():
    data = request.json
    titulo = data.get("titulo")
    genero = data.get("genero")
    descricao = data.get("descricao", "")
    imagem = data.get("imagem")

    if not titulo or not genero or not imagem:
        return jsonify({"erro": "Campos obrigatórios faltando"}), 400

    inserir_filme(titulo, genero, descricao, imagem)
    return jsonify({"mensagem": "Filme cadastrado com sucesso"}), 201

@app.route("/api/filmes/<int:id>/voto", methods=["POST"])
def api_votar(id):
    data = request.json
    tipo = data.get("tipo")  # "gostei" ou "naoGostei"
    if not tipo or tipo not in ["gostei", "naoGostei"]:
        return jsonify({"erro": "Tipo de voto inválido"}), 400

    success = votar(id, tipo)
    if not success:
        return jsonify({"erro": "Erro ao registrar voto"}), 400

    return jsonify({"mensagem": "Voto registrado com sucesso"})

@app.route("/api/totais", methods=["GET"])
def api_totais():
    totais = totais_gerais()
    return jsonify(totais)

# --- MAIN ---

if __name__ == "__main__":
    criar_tabela()  # Cria tabela se não existir
    app.run(debug=True)
