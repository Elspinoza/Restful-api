from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'host'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'database'

mysql = MySQL(app)
@app.route('/users', methods=['GET'])
def get_all_users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM users''')
    rv = cur.fetchall()
    return jsonify(rv)
@app.route('/add', methods=['POST'])
def add_user():
    cur = mysql.connection.cursor()
    name = request.json['name']
    email = request.json['email']
    cur.execute('''INSERT INTO users (name, email) VALUES (%s, %s)''', (name, email))
    mysql.connection.commit()
    result = {'name': name, 'email': email}
    return jsonify({'result': result})
if __name__ == '__main__':
    app.run(debug=True)
