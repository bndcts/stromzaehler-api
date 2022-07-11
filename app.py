import datetime
import sqlite3

from datetime import datetime
from flask import Flask, request, jsonify, app
from flask import render_template
import db as db

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST', 'PUT'])
def hello_world():  # put application's code here
    stand = db.query_db('SELECT * FROM zaehlerstaende WHERE id=?', [3], True)
    return render_template('index.html', name='John', stand=stand)


@app.route('/post/data/<uuid>', methods=["POST"])
def receive_data(uuid):
    input_json = request.get_json(force=True)
    i = request.get_data(as_text=True)
    print(i)
    uuid = uuid.split('.')[0]
    stand = i.split(" ")[3].split(".")[0]
    date = datetime.now()
    db.insert_into_db("INSERT INTO werte (uuid, stand, date) VALUES (?, ?, ?)",
                      (uuid, stand, date))
    return '{success: "True",}'


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, use_debugger=False, use_realoder=False)
