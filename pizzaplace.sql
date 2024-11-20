DROP DATABASE IF EXISTS pizzaplace;
CREATE DATABASE pizzaplace;
USE pizzaplace;

CREATE TABLE Clients(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50),
    numero_telephone VARCHAR(20),
    adresse VARCHAR(255)
);

CREATE TABLE Pizza(
	id INT AUTO_INCREMENT PRIMARY KEY,
	croute ENUM("Classique", "Mince", "Épaisse"),
    sauce ENUM("Tomate", "Spaghetti", "Alfredo"),
    garniture1 ENUM("Aucun", "Pepperoni", "Champignons", "Oignons", "Poivrons", "Olives", "Anchois", "Bacon", "Poulet", "Maïs", "Fromage", "Piments forts"),
    garniture2 ENUM("Aucun", "Pepperoni", "Champignons", "Oignons", "Poivrons", "Olives", "Anchois", "Bacon", "Poulet", "Maïs", "Fromage", "Piments forts"),
    garniture3 ENUM("Aucun", "Pepperoni", "Champignons", "Oignons", "Poivrons", "Olives", "Anchois", "Bacon", "Poulet", "Maïs", "Fromage", "Piments forts"),
    garniture4 ENUM("Aucun", "Pepperoni", "Champignons", "Oignons", "Poivrons", "Olives", "Anchois", "Bacon", "Poulet", "Maïs", "Fromage", "Piments forts")
);