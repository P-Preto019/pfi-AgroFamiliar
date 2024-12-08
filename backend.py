from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

CORS(app)

@app.route('/api/cotacao-soja', methods=['GET'])
def get_cotacao_soja():
    url1 = "https://www.noticiasagricolas.com.br/cotacoes/soja"
    response = requests.get(url1)
    
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        cotacaos = soup.find_all("td")
        for i, cotacaoSoja in enumerate(cotacaos, start=1):
            if i == 2: 
                return jsonify({'cotacaoSoja': cotacaoSoja.text.strip()})

    return jsonify({'error': 'Falha ao obter a cotação'}), 500

@app.route('/api/cotacao-milho', methods=['GET'])
def get_cotacao_milho():
    url2 = "https://www.noticiasagricolas.com.br/cotacoes/milho"
    response = requests.get(url2)
    
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        cotacaos = soup.find_all("td")
        for i, cotacaoMilho in enumerate(cotacaos, start=1):
            if i == 2: 
                return jsonify({'cotacaoMilho': cotacaoMilho.text.strip()})

    return jsonify({'error': 'Falha ao obter a cotação'}), 500

@app.route('/api/cotacao-trigo', methods=['GET'])
def get_cotacao_trigo():
    url3 = "https://www.noticiasagricolas.com.br/cotacoes/trigo"
    response = requests.get(url3)
    
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        cotacaos = soup.find_all("td")
        for i, cotacaoTrigo in enumerate(cotacaos, start=1):
            if i == 3: 
                return jsonify({'cotacaoTrigo': cotacaoTrigo.text.strip()})

    return jsonify({'error': 'Falha ao obter a cotação'}), 500

@app.route('/api/cotacao-feijao', methods=['GET'])
def get_cotacao_feijao():
    url4 = "https://www.noticiasagricolas.com.br/cotacoes/feijao"
    response = requests.get(url4)
    
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        cotacaos = soup.find_all("td")
        for i, cotacaoFeijao in enumerate(cotacaos, start=1):
            if i == 2: 
                return jsonify({'cotacaoFeijao': cotacaoFeijao.text.strip()})

    return jsonify({'error': 'Falha ao obter a cotação'}), 500

@app.route('/api/cotacao-suinos', methods=['GET'])
def get_cotacao_suinos():
    url4 = "https://www.noticiasagricolas.com.br/cotacoes/suinos"
    response = requests.get(url4)
    
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        cotacaos = soup.find_all("td")
        for i, cotacaoSuinos in enumerate(cotacaos, start=1):
            if i == 3:  
                return jsonify({'cotacaoSuinos': cotacaoSuinos.text.strip()})

    return jsonify({'error': 'Falha ao obter a cotação'}), 500

@app.route('/api/cotacao-boigordo', methods=['GET'])
def get_cotacao_boigordo():
    url4 = "https://www.noticiasagricolas.com.br/cotacoes/boi-gordo"
    response = requests.get(url4)
    
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        cotacaos = soup.find_all("td")
        for i, cotacaoBoigordo in enumerate(cotacaos, start=1):
            if i == 2:  
                return jsonify({'cotacaoBoigordo': cotacaoBoigordo.text.strip()})

    return jsonify({'error': 'Falha ao obter a cotação'}), 500

if __name__ == '__main__':
    app.run(debug=True)

