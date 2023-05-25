/* Deklarasi Library */
#include <bits/stdc++.h>
#include "detail.cpp"

using namespace std;

int main()
{
    /* Deklarasi variabel iterator */
    int n = 2;
    int i;

    /* Membuat array objek */
    detail tim[n];

    /* Input data */
    tim[0].setTeam("Manchester United");
    tim[0].setNation("England");
    tim[0].setFound(1876);
    tim[0].setPlayer("GK-De Gea, RB-Dalot, CB-Varane, CB-Maguire, LB-Shaw, CM-Pogba, CM-Van de Beek, CAM-Bruno, LW-Rashford, RW-Sancho, ST-Ronaldo");

    tim[1].setTeam("Manchester City");
    tim[1].setNation("England");
    tim[1].setFound(1880);
    tim[1].setPlayer("GK-Ederson, RB-Walker, CB-Stones, CB-Dias, LB-Cancelo, CM-Fernandinho, CM-Gundongan, CAM-De Bruyne, LW-Sterling, RW-Benardo, ST-Jesus");

    /* Menampilkan data */
    for (i = 0; i < n; i++)
    {
        cout << "Tim " << i + 1 << endl;
        cout << "==============================" << endl;
        cout << "Nama Tim           : " << tim[i].getTeam() << endl;
        cout << "Asal Negara Tim    : " << tim[i].getNation() << endl;
        cout << "Tahun Berdiri      : " << tim[i].getFound() << endl;
        cout << "==============================" << endl;
        cout << "Detail Pemain" << endl;
        cout << "==============================" << endl;
        cout << tim[i].getPlayer() << endl;

        cout << "\n";
    }

    /* Menghentikan operasi */
    return 0;
}