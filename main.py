from flask import Flask, request, jsonify, redirect
from database_functions import *

app = Flask(__name__)

@app.route('/create-short-url/<path:url>', methods=['GET'])
def insert(url):
    print(url)
    return 'localhost:5000/short-url/{}'.format(insert_url(url))

@app.route('/short-url/<url_id>')
def forwardurl(url_id):
    return redirect(find_url(url_id))


if __name__ == '__main__':
    app.run(debug=True)