from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__) # create an instance of this class

@app.route("/", methods=["GET"])
def get_my_ip():
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr), 200
#    return jsonify({'ip': request.remote_addr}), 200

   