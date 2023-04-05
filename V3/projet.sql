DROP SCHEMA IF EXISTS shopInfo CASCADE;
CREATE SCHEMA shopInfo;


CREATE TABLE shopInfo.boutique
(
    idBoutique SERIAL PRIMARY KEY,
    adresse VARCHAR
);

CREATE TABLE shopInfo.produit
(
    idProduit SERIAL PRIMARY KEY,
    prix FLOAT,
    description VARCHAR,
    nom VARCHAR
    
);


CREATE TABLE shopInfo.stocks
(
    idProduit INT,
    idBoutique INT,
    quantite INT,
    PRIMARY KEY (idProduit, idBoutique),
    CONSTRAINT fk_stocks_produit FOREIGN KEY (idProduit) REFERENCES shopInfo.produit(idProduit),
    CONSTRAINT fk_stocks_boutique FOREIGN KEY (idBoutique) REFERENCES shopInfo.boutique(idBoutique)
);



CREATE TABLE shopInfo.valeurs
(   
    idVal SERIAL,
    valeur DECIMAL,
    PRIMARY KEY (idVal, valeur)
);

CREATE TABLE shopInfo.posteDeDepense
(
    idPoste SERIAL PRIMARY KEY,
    intitule VARCHAR
);

CREATE TABLE shopInfo.periode
(
    periode date PRIMARY KEY
);

CREATE TABLE shopInfo.depenses
(
    idDepense SERIAL PRIMARY KEY,
    montant DECIMAL,
    posteDeDepense INT REFERENCES shopInfo.posteDeDepense(idPoste)

) INHERITS (shopInfo.periode);

CREATE TABLE shopInfo.recettes
(
    idRecette SERIAL PRIMARY KEY,
    montant DECIMAL

) INHERITS (shopInfo.periode);









