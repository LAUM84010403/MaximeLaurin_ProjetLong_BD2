USE pizzaplace;

INSERT INTO Clients(nom, numero_telephone, adresse) VALUES ("Max IME", "555-555-5555", "5 rue du lointain");
INSERT INTO Clients(nom, numero_telephone, adresse) VALUES ("Xavier", "666-666-6666", "6 rue de Nicko");
INSERT INTO Clients(nom, numero_telephone, adresse) VALUES ("Tophe", "777-777-7777", "32 rue du pkm");
INSERT INTO Clients(nom, numero_telephone, adresse) VALUES ("Francis", "888-888-8888", "93 rue de l'odorat");
INSERT INTO Clients(nom, numero_telephone, adresse) VALUES ("Le nain", "999-999-9999", "411 rue de la taille");
INSERT INTO Clients(nom, numero_telephone, adresse) VALUES ("4", "453-534-5434", "454 rue de la trentaine");

INSERT INTO Pizzas (croute, sauce, garniture1, garniture2, garniture3, garniture4)
VALUES ('Classique', 'Tomate', 'Pepperoni', 'Champignons', 'Fromage', 'Olives');
INSERT INTO Pizzas (croute, sauce, garniture1, garniture2, garniture3, garniture4)
VALUES ('Mince', 'Spaghetti', 'Oignons', 'Champignons', 'Anchois', 'Olives');
INSERT INTO Pizzas (croute, sauce, garniture1, garniture2, garniture3, garniture4)
VALUES ('Épaisse', 'Alfredo', 'Aucun', 'Aucun', 'Aucun', 'Olives');
INSERT INTO Pizzas (croute, sauce, garniture1, garniture2, garniture3, garniture4)
VALUES ('Classique', 'Tomate', 'Bacon', 'Bacon', 'Poulet', 'Poulet');

SHOW CREATE TABLE Commandes;


INSERT INTO Commandes(id_client, id_pizza) VALUES (1, 2);
INSERT INTO Commandes (id_client, id_pizza)
VALUES (3, 2);
INSERT INTO Commandes (id_client, id_pizza)
VALUES (1, 4);
INSERT INTO Commandes (id_client, id_pizza)
VALUES (3, 3);
INSERT INTO Commandes (id_client, id_pizza)
VALUES (5, 1);