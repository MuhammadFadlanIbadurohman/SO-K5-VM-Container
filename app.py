from flask import Flask, jsonify
import sqlite3, datetime, socket

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('presensi.db')
    conn.execute('CREATE TABLE IF NOT EXISTS log (id INTEGER PRIMARY KEY, waktu TEXT)')
    conn.execute('INSERT INTO log (waktu) VALUES (?)', (str(datetime.datetime.now()),))
    conn.commit()
    count = conn.execute('SELECT COUNT(*) FROM log').fetchone()[0]
    return jsonify({'layanan': 'Presensi Kampus', 'host': socket.gethostname(), 'total_presensi': count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
