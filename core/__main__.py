from flask import Flask, request, jsonify
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/', methods=['GET'])
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
