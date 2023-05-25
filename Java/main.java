import java.util.*;

public class main {
    public static void main(String[] args){

        //inisialisasi
        int n=0, m=0;
        int i=0, j=0;

        //input banyak tim
        System.out.println("Masukkan banyak tim :");
        Scanner sc = new Scanner(System.in);
        try{
            n = sc.nextInt(); //masukan ke n
        }catch(Exception e){}
        
        //masukkan banyak pemain
        System.out.println("Masukkan banyak pemain :");
        try{
            m = sc.nextInt(); //masukan ke n
        }catch(Exception e){}
        
        //deklarasi array kelas
        tim timsb[] = new tim[n]; //buat array tim

        //variabel sementara
        String namatimm="";
        String asalm="";
        int tahunm=0;
        String[] pemainm= new String[m];
        //input variabel sementara dan panggil kelas
        for(i=0; i<n; i++){
            System.out.println("Nama Tim " + (i+1) + " :");
            try{
                namatimm = sc.nextLine();
            }catch(Exception e){}
            System.out.println("Asal :");
            try{
                asalm = sc.nextLine();
            }catch(Exception e){}
            System.out.println("Tahun :");
            try{
                tahunm = sc.nextInt();
            }catch(Exception e){}
            System.out.println(m + " Pemain :");
            for(j=0; j<m; j++){
                try{
                    pemainm[j] = sc.nextLine();
                }catch(Exception e){}
            }
            timsb[i] = new tim(namatimm, asalm, tahunm, pemainm, m);
        }

        for(i=0; i<=n; i++){
            System.out.println("Tim Sepak Bola ke-" + i + " : ");
            System.out.println("Nama : " + timsb[i].getnamatim());
            System.out.println("Asal : " + timsb[i].getasal());
            System.out.println("Tahun : " + timsb[i].gettahun());
            System.out.println("Pemain : ");
            for(j=0; j<m; j++){
                System.out.println("- " + timsb[i].getpemain(j));
            }
            // System.out.println("Pemain : " + timsb[i].getpemain());
            System.out.println("");
        }
    }
}