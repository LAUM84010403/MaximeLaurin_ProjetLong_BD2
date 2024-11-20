from flask import Flask, render_template, jsonify, request
import mysql.connector

app = Flask(__name__)

# Configuration de la connexion à la base de données
def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.7",
        user="root",
        passwd="mysql",
        database="pizzaplace"
    )
    

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT Clients.nom AS NomClient, Pizzas.sauce AS SaucePizza FROM Commandes INNER JOIN Clients ON Commandes.id_client = Clients.id INNER JOIN Pizzas ON Commandes.id_pizza = Pizzas.id;")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', data=data)

@app.route('/afficher_clients')
def afficher_clients():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    # Récupérer toutes les lignes de la table Clients
    cursor.execute("SELECT * FROM Clients")
    clients = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return jsonify(clients)

@app.route('/ajouter_client', methods=['POST'])
def ajouter_client():
    connection = get_db_connection()
    data = request.get_json()
    nom = data['nom']
    numero_telephone = data['numero_telephone']
    adresse = data['adresse']
    
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Clients (nom, numero_telephone, adresse) VALUES (%s, %s, %s)", (nom, numero_telephone, adresse))
    connection.commit()
    
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)