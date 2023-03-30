import java.util.ArrayList;
import java.util.Scanner;

public class Gros {


    public static ArrayList<String> insertions(){
        ArrayList<Double> values = new ArrayList<Double>();
        values.add(-2.127);
        values.add(-0.274);
        values.add(-0.938);
        values.add(-0.972);
        values.add(1.394);
        values.add(-1.787);
        values.add(0.451);
        values.add(-0.027);
        values.add(-2.358);
        values.add(0.825);
        values.add(2.042);
        values.add(-1.618);
        values.add(0.338);
        values.add(1.333);
        values.add(1.421);
        values.add(-1.796);
        values.add(2.193);
        values.add(-0.282);
        values.add(0.336);
        values.add(2.357);
        values.add(1.384);
        values.add(-0.318);
        values.add(-0.93);
        values.add(0.75);
        values.add(2.06);
        values.add(-1.918);
        values.add(-0.043);
        values.add(-2.044);
        values.add(-0.257);
        values.add(-2.095);
        values.add(-1.849);
        values.add(1.659);
        values.add(-1.196);
        values.add(-1.134);
        values.add(-0.75);
        values.add(0.123);
        values.add(-2.384);
        values.add(2.236);
        values.add(1.121);
        values.add(0.584);
        values.add(1.11);
        values.add(-0.312);
        values.add(1.641);
        values.add(2.382);
        values.add(-1.344);
        values.add(-1.83);
        values.add(-1.276);
        values.add(2.079);
        values.add(-1.534);
        values.add(-1.017);
        values.add(0.356);
        values.add(-1.877);
        values.add(-1.657);
        values.add(-0.621);
        values.add(1.675);
        values.add(2.393);
        values.add(1.166);
        values.add(-1.876);
        values.add(0.484);
        values.add(-1.464);
        values.add(-2.419);
        values.add(0.601);
        values.add(0.578);
        values.add(2.015);
        values.add(1.748);
        values.add(-1.764);
        values.add(1.496);
        values.add(-2.068);
        values.add(-0.468);
        values.add(2.427);
        values.add(-0.999);
        values.add(-0.65);
        values.add(0.338);
        values.add(0.749);
        values.add(0.117);
        values.add(2.379);
        values.add(-0.189);
        values.add(-0.259);
        values.add(-1.391);
        values.add(0.642);
        values.add(-1.822);
        values.add(-0.317);
        values.add(-2.015);
        values.add(2.342);
        values.add(-0.68);
        values.add(-2.462);
        values.add(-1.045);
        values.add(-2.318);
        values.add(2.396);
        values.add(-2.203);
        values.add(1.366);
        values.add(2.132);
        values.add(-1.082);
        values.add(-1.474);
        values.add(-1.85);
        values.add(1.475);
        values.add(0.156);
        values.add(-0.695);
        values.add(0.674);
        values.add(2.184);
        ArrayList<String> liste=new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        for (int i=0; i<values.size(); i++){
            liste.add("("+(i+1)+ ", '', "+ values.get(i)+")");
        }
        return liste;
    }

    public static void affichage(ArrayList<String> l){
        for (String s : l){
            System.out.println(s);
        }
    }

    public static void main(String[] args) {
        affichage(insertions());
    }
}
