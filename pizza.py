import mysql.connector
import os
from prettytable import PrettyTable


# Connexion à la base de données
cnx = mysql.connector.connect(user='root', password='mysql', host='127.0.0.1', database='pizzaplace')
# Création du curseur avec des résultats nommés
cursor = cnx.cursor(dictionary=True)


os.system('cls')
print("clients-pizzas")

input1 = input()
print()
if(input1 == "clients"):
    # Exécution de la requête
    query = "SELECT * FROM Clients;"
    cursor.execute(query)

    # Créer une instance de PrettyTable et définir les en-têtes du tableau
    table = PrettyTable()
    table.field_names = ["Nom", "#", "Adresse"]


    # Remplir le tableau avec les résultats de la requête
    for ligne in cursor:
        table.add_row([ligne["nom"], ligne["numero_telephone"], ligne["adresse"]])
    # Afficher le tableau
    print(table)
    input()

if(input1 == "pizzas"):
    # Exécution de la requête
    query = "SELECT * FROM Pizzas;"
    cursor.execute(query)

    # Créer une instance de PrettyTable et définir les en-têtes du tableau
    table = PrettyTable()
    table.field_names = ["Croute", "sauce", "Garniture 1", "Garniture 2", "Garniture 3", "Garniture 4"]

    # Remplir le tableau avec les résultats de la requête
    for ligne in cursor:
        table.add_row([ligne["croute"], ligne["sauce"], ligne["garniture1"], ligne["garniture2"], ligne["garniture3"], ligne["garniture4"]])
    # Afficher le tableau
    print(table)
    input()

# Fermeture du curseur et de la connexion
cursor.close()
cnx.close()

