print("Iniciando app.py")
#from test_pFcomFaturas import TestPFcomFaturas
print("Importação feita com sucesso")

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/busca_fatura', methods=['POST'])
def busca_fatura():
    data = request.json
    uc = data.get('uc')
    ano_mes = data.get('ano_mes')
    documento = data.get('documento')
    nome = data.get('nome')
    data_nascimento = data.get('data_nascimento')
    try:
        test = TestPFcomFaturas()
        test.setup_method(None)
        test.test_pFcomFaturas(uc, ano_mes, documento, nome, data_nascimento)
        test.teardown_method(None)
        return jsonify({"status": "Fatura processada com sucesso"}), 200
    except Exception as e:
        return jsonify({"status": "Erro ao processar fatura", "erro": str(e)}), 400

@app.route('/')
def home():
    return "API Busca Fatura ativa!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)