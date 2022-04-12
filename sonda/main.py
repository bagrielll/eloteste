from flask import Flask, request
from func import main
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_sondas():
    request_data = request.get_json()
    maxCords = request_data['maxCords']
    sondas = request_data['sondas']
    return main(maxCords, sondas)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=port)