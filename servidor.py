from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # ← AGORA VAI USAR A PASTA templates

@app.route('/receber-dados', methods=['POST'])
def receber_dados():
    nome = request.form.get('user_name')
    email = request.form.get('user_email')

    if nome and email:
        conn = sqlite3.connect('dados_ebook.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO inscricoes (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Dados salvos com sucesso!"})
    else:
        return jsonify({"erro": "Dados incompletos"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
