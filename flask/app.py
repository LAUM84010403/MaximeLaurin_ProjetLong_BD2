from flask import Flask, render_template, jsonify, request
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv('DATABASE_URL')

app = Flask(__name__)

dbHost = process.env.DB_HOST;
dbUser = process.env.DB_USER;
dbPass = process.env.DB_PASSWORD;
dbDatabase = process.env.DB_NAME;


# Configuration de la connexion à la base de données
def get_db_connection():
    return mysql.connector.connect(
        dbHost=DB_HOST,
        dbUser=DB_USER,
        dbPass=DB_PASSWORD,
        dbDatabase=DB_NAME
    )
    
#Afficher Index.html
@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT Clients.nom AS NomClient, Pizzas.sauce AS SaucePizza FROM Commandes INNER JOIN Clients ON Commandes.id_client = Clients.id INNER JOIN Pizzas ON Commandes.id_pizza = Pizzas.id;")
    data = cursor.fetchall()

    cursor.close()
    connection.close()
    return render_template('index.html', data=data)

#Afficher les clients
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

#Ajouter un client
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

    cursor.close()
    connection.close()
    return jsonify(success=True)

#Aafficher les commandes selon un utilisateurs
@app.route('/afficher_commande', methods=['POST'])
def afficher_commande():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    data = request.get_json()
    numero_client = data.get("numero_client")

    cursor.execute("SELECT Clients.id, Clients.nom, Pizzas.croute, Pizzas.sauce, Pizzas.garniture1, Pizzas.garniture2, Pizzas.garniture3, Pizzas.garniture4, COALESCE(Commandes_en_attente.statut, 'Terminé') statut FROM Commandes LEFT JOIN Clients ON Commandes.id_client = Clients.id LEFT JOIN Pizzas ON Commandes.id_pizza = Pizzas.id LEFT JOIN Commandes_en_attente ON Commandes.id = Commandes_en_attente.id WHERE Clients.id = %s", (numero_client,));
    commandes = cursor.fetchall()

    cursor.close()
    connection.close()
    return jsonify(commandes)

#Obtenir valeurs croute pour la liste déroulante
@app.route('/obtenir_valeurs_croute', methods=['GET'])
def obtenirValeursCroute():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SHOW COLUMNS FROM Pizzas LIKE 'croute'")
    result = cursor.fetchone()
    enum_values = result[1]
    
    enum_values = enum_values.replace("enum(", "").replace(")", "").replace("'", "")
    values_list = enum_values.split(",")

    cursor.close()
    connection.close()
    return jsonify(values_list)

#Obtenir valeurs sauce pour la liste déroulante
@app.route('/obtenir_valeurs_sauce', methods=['GET'])
def obtenirValeursSauce():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SHOW COLUMNS FROM Pizzas LIKE 'sauce'")
    result = cursor.fetchone()
    enum_values = result[1]
    
    enum_values = enum_values.replace("enum(", "").replace(")", "").replace("'", "")
    values_list = enum_values.split(",")

    cursor.close()
    connection.close()
    return jsonify(values_list)

#Obtenir valeurs garniture pour la liste déroulante
@app.route('/obtenir_valeurs_garniture', methods=['GET'])
def obtenirValeursGarniture():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SHOW COLUMNS FROM Pizzas LIKE 'garniture1'")
    result = cursor.fetchone()
    enum_values = result[1]
    
    enum_values = enum_values.replace("enum(", "").replace(")", "").replace("'", "")
    values_list = enum_values.split(",")

    cursor.close()
    connection.close()
    return jsonify(values_list)

#Afficher les commandes en attentes
@app.route('/afficher_attente', methods=['POST'])
def afficher_attente():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    data = request.get_json()
    id = data.get("numero_client")
    
    cursor.execute("SELECT Pizzas.croute, Pizzas.sauce, Pizzas.garniture1, Pizzas.garniture2, Pizzas.garniture3, Pizzas.garniture4 FROM Commandes LEFT JOIN Clients ON Commandes.id_client = Clients.id LEFT JOIN Pizzas ON Commandes.id_pizza = Pizzas.id LEFT JOIN Commandes_en_attente ON Commandes.id = Commandes_en_attente.id WHERE Clients.id = %s;", (id,));
    commandes = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return jsonify(commandes)

#Ajouter une pizza
@app.route('/ajouter_pizza', methods=['POST'])
def ajouter_pizza():
    data = request.get_json()
    croute = data.get("croute")
    sauce = data.get("sauce")
    garniture1 = data.get("garniture1")
    garniture2 = data.get("garniture2")
    garniture3 = data.get("garniture3")
    garniture4 = data.get("garniture4")

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Pizzas (croute, sauce, garniture1, garniture2, garniture3, garniture4) VALUES (%s, %s, %s, %s, %s, %s)", (croute, sauce, garniture1, garniture2, garniture3, garniture4))
    connection.commit()

    cursor.close()
    connection.close()
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(debug=True)
