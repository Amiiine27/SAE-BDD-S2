DROP SCHEMA IF EXISTS crypto CASCADE;
CREATE SCHEMA crypto;


CREATE TABLE crypto.cartes
(
    idCarte SERIAL PRIMARY KEY,
    hashrate FLOAT,
    consommationW INT,
    nomCarte VARCHAR,
    descriptionCarte VARCHAR,
    prixCarte DECIMAL,
    coutdAchat DECIMAL
);

CREATE TABLE crypto.boutique
(
    idBoutique SERIAL PRIMARY KEY,
    adresse VARCHAR
);

CREATE TABLE crypto.stocks
(
    idCarte INT REFERENCES crypto.cartes (idCarte),
    idBoutique INT REFERENCES crypto.boutique (idBoutique),
    quantite INT
);

CREATE TABLE crypto.cryptos
(
    idCrypto SERIAL PRIMARY KEY,
    nomCrypto VARCHAR,
    valEUR FLOAT,
    rendement FLOAT
);

CREATE TABLE crypto.rig
(
    idRig SERIAL PRIMARY KEY,
    modeleCarte INT REFERENCES crypto.cartes(idCarte),
    idSection INT,
    nbrCarte INT
);

CREATE TABLE crypto.miningPool
(   
    idPool SERIAL PRIMARY KEY,
    dateMinage date,
    rig INT REFERENCES crypto.rig(idRig),
    crypto INT REFERENCES crypto.cryptos (idCrypto)
);

CREATE TABLE crypto.transaction
(
    idTransaction SERIAL PRIMARY KEY,
    miningPool INT REFERENCES crypto.miningPool (idPool),
    montant DECIMAL
);







