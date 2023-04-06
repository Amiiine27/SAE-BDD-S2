DROP SCHEMA IF EXISTS shopInfo CASCADE;
CREATE SCHEMA shopInfo;



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


CREATE TABLE shopInfo.periode
(
    idPeriode INT PRIMARY KEY,
    mensualite date
);


CREATE TABLE shopInfo.depenses
(
    idDepense SERIAL,
    montant DECIMAL,
    nomPosteDeDepense VARCHAR(50)

) INHERITS (shopInfo.periode);


CREATE TABLE shopInfo.recettes
(
    idRecette SERIAL,
    montant DECIMAL

) INHERITS (shopInfo.periode);


CREATE TABLE shopInfo.bilan(
	montantDuBilan DECIMAL

) INHERITS (shopInfo.periode);


-- On stock nos 100 valeurs dans cette table et elle ne fait donc pas partie des tables que l'on utilise dans l'intitulé de la sae
CREATE TABLE shopInfo.valeurs
(   
    idVal SERIAL PRIMARY KEY,
    valeur DECIMAL,
    
);
