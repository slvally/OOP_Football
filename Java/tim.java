public class tim{

    private String namatim;
    private String asal;
    private int tahun;
    //private String pemain;
    private String[] pemain;
    int x = 0;

    public tim(){

    }

    public tim(String namatim, String asal, int tahun, String[] pemain, int m){
        this.namatim = namatim;
        this.asal = asal;
        this.tahun = tahun;
        for(x=0; x<m; x++){
            this.pemain[x]=pemain[x];
        }
    }

    public String getnamatim(){
        return namatim;
    }
    public void setnamatim(String namatim){
        this.namatim = namatim;
    }

    public String getasal(){
        return asal;
    }
    public void setasal(String asal){
        this.asal = asal;
    }
    public int gettahun(){
        return tahun;
    }
    public void settahun(int tahun){
        this.tahun = tahun;
    }
    public String getpemain(int x){
        return pemain[x];
    }
    public void setpemain(String[] pemain, int m){
        for(x=0; x<m; x++){
            this.pemain[x]=pemain[x];
        }
    }


}