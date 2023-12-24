from flask import Flask, request, jsonify
import logging
import http.client

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    client = http.client.HTTPConnection('localhost', 5000)
    client.request('GET', '/ip')
    response = client.getresponse()
    if response.status != 200:
        return jsonify({'error': 'internal error'}), 500
    data = response.read()
    return data.decode('utf-8')

@app.route('/ip', methods=['GET'])
def get_public_ip():
    try:
        logging.info('Request received from %s', request.remote_addr)

        client_ip = request.remote_addr
        return jsonify({'public_ip': client_ip})
    except Exception as e:
        logging.error('Error while retrieving public IP')
        logging.exception(e)
        return jsonify({'error': "internal error"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
