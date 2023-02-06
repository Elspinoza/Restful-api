#  Importations
import pymysql
from app import app
from conf import mysql
from flask import request, render_template, jsonify

@app.route("/user/add", methods=['POST'])
def add_user():
    try:

        json = request.json
        #id = json['id']
        nom = json['nom']
        prenom = json['prenom']
        tel = json['tel']
        password = json['password']
        email = json['email']
        login = json['login']
    
        #if nom and prenom and request.method =='POST':
        if nom and prenom and tel and password and email and login and request.method =='POST':
            con = mysql.connect()
            cursor = con.cursor(pymysql.cursors.DictCursor)
            query = 'insert into user(nom,prenom,login,password,tel,email)VALUES(%s,%s,%s,%s,%s,%s)'
            bind_data = (nom,prenom,login,password,tel,email)
            #bindData = (nom,prenom)
            cursor.execute(query,bind_data)
            con.commit()
            response = jsonify('Utilisateur ajouté avec succès')
            response.status_code = 200
            return response
        else:
            message = {'status':404, 'message':'Entrée(s) invalide'}
            response = jsonify(message)
            response.status_code = 404
            return response
    except Exception as e:
        print(e) 
        message = {'status':404, 'message':'error please '}
        return message

    finally:
        cursor.close()
        con.close()


@app.route("/login")
def login():
   return render_template("login.html",name= __name__)

@app.route("/user/get/<int:id>")
def get_user(id):
    con = mysql.connect()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    query = 'insert into user(nom,prenom,login,password,tel,email)VALUES(%s,%s,%s,%s,%s,%s)'
    bind_data = (nom,prenom,login,password,tel,email)
            #bindData = (nom,prenom)
    cursor.execute(query,bind_data)
    return jsonify({"id":id})
    

if(__name__ == '__main__'):
    app.run()
