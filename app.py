import sqlite3

from flask import Flask, request, jsonify, app
from flask import render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

zaehlerstand = dict()
test = "test"
strom_aktuell = dict()

@app.route('/', methods=['GET', 'POST', 'PUT'])
def hello_world():  # put application's code here
    conn = get_db_connection()
    stand = conn.execute('SELECT * FROM zaehlerstaende WHERE id=3').fetchone()["stand"]
    conn.close()
    return render_template('index.html', name='John', stand=stand)


@app.route('/post/data/<uuid>', methods=["POST"])
def receive_data(uuid):
    input_json = request.get_json(force=True)
    i = request.get_data(as_text=True)
    print(i)
    stand = i.split(" ")[3].split(".")[0]
    conn = get_db_connection()
    conn.execute("INSERT INTO zaehlerstaende (uuid, stand) VALUES (?, ?)",
            (uuid, stand)
            )
    conn.commit()
    conn.close()
    return '{success: "True",}'


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, use_debugger=False, use_realoder=False)
