from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Datenbankinitialisierung
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Route für die Startseite
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        # Benutzername in die Datenbank speichern
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username) VALUES (?)', (username,))
        conn.commit()
        conn.close()
        return redirect(url_for('welcome', username=username))
    return render_template('index.html')

# Route für die Begrüßungsseite
@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
