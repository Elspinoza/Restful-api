#  Importations
import pymysql
from app import app
from conf import mysql
from flask import jsonify
from flask import Flask, request, render_template,flash

@app.route("/add", methods=['POST'])
def add_user():
    try:
        print('1111111111111111111111')
        #con = mysql.connect()
        #cursor = con.cursor(pymysql.cursors.DictCursor)
        conn = pymysql.connect(cursorclass=pymysql.cursors.DictCursor)
        print('222222222222222222222222222222')
        with conn.cursor() as cursor:

            json = request.json
            #id = json['id']
            nom = json["nom"]
            prenom = json['prenom']
            tel = json['tel']
            pasword = json['pasword']
            email = json['email']
            login = json['login']

            print('3333333333333333333333333333')
            print('****************************')
            print(nom)
            print('****************************')
    
        if nom and prenom and request.method == 'POST':
            cursor.execute("INSERT INTO user (nom,prenom)VALUES(%,%)",(nom,prenom))
            conn.commit()
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
        return jsonify(e)

    #finally:
     #   cursor.close()
      #  conn.close()


@app.route("/login")
def login():
   return render_template("login.html",name= __name__)

if(__name__ == '__main__'):
    app.run()
