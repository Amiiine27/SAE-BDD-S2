CREATE TABLE crypto.depenses
(
    idDepense SERIAL PRIMARY KEY,
    dateDepense DATE,
    montant DECIMAL
);



WITH recettes_moyenne AS (
    SELECT AVG(montant) AS moyenne_montant
    FROM crypto.recettes
)
SELECT r.idRecette, r.dateRecette, r.montant, r.montant - recettes_moyenne.moyenne_montant AS difference_moyenne
FROM crypto.recettes r, recettes_moyenne
ORDER BY r.dateRecette;





