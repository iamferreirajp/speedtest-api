import os
from flask import Flask, jsonify, request
from requests import Request

app = Flask(__name__)

@app.route('/get_files', methods=['GET'])
def get_files():
    """
    Pega a lista de arquivos na Caixa Postal
    """
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')