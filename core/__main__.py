from flask import Flask, request, Response
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_public_ip():
    try:
        logging.info("Request received from %s", request.remote_addr)

        client_ip = request.remote_addr
        return Response(client_ip, mimetype="text/plain")
    except Exception as e:
        logging.error("Error while retrieving public IP")
        logging.exception(e)
        return Response("Internal error", status=500, mimetype="text/plain")

@app.route("/health", methods=["GET"])
def health_check():
    try:
        return Response("OK", mimetype="text/plain")
    except Exception as e:
        logging.error("Error while checking health")
        logging.exception(e)
        return Response("Internal error", status=500, mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)