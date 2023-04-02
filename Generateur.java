import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Generateur {

    public static void main(String[] args) {
        int numberOfRigs = 4;
        int numberOfCryptos = 23;
        LocalDate startDate = LocalDate.of(2023, 1, 1);
        LocalDate endDate = LocalDate.of(2023, 4, 7);
        String outputFile = "miningPoolInserts.sql";

        generateMiningPoolData(numberOfRigs, numberOfCryptos, startDate, endDate, outputFile);
    }

    private static void generateMiningPoolData(int numberOfRigs, int numberOfCryptos, LocalDate startDate, LocalDate endDate, String outputFile) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile))) {
            writer.write("-- Insertion des données pour la table Miningpool\n");
            writer.write("INSERT INTO crypto.miningPool (dateMinage, rig, crypto)\n");
            writer.write("VALUES\n");

            List<String> insertValues = new ArrayList<>();

            for (int rig = 1; rig <= numberOfRigs; rig++) {
                LocalDate currentDate = startDate;
                int crypto = (rig - 1) % numberOfCryptos + 1;

                while (!currentDate.isAfter(endDate)) {
                    insertValues.add(String.format("    ('%s', %d, %d)", currentDate, rig, crypto));
                    currentDate = currentDate.plusDays(1);
                    crypto = (crypto % numberOfCryptos) + 1;
                }
            }

            writer.write(String.join(",\n", insertValues) + ";\n");
        } catch (IOException e) {
            System.err.println("Erreur lors de l'écriture du fichier : " + e.getMessage());
        }
    }
}
