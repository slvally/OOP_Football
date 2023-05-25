#include <iostream>
#include <string>

using namespace std;

class detail
{
private:
    /* Deklarasi atribut */
    string name;
    string nation;
    int found;
    string player;

public:
    /* Membuat constructor */
    detail()
    {
        this->found = 0;
        this->name = this->nation = this->player = "";
    }

    detail(string name, string nation, int found, string player)
    {
        this->name = name;
        this->nation = nation;
        this->found = found;
        this->player = player;
    }

    /*Set dan Get data nama tim sepakbola */
    void setTeam(string name)
    {
        this->name = name;
    }
    string getTeam()
    {
        return this->name;
    }

    /*Set dan Get data asal negara tim sepakbola */
    void setNation(string nation)
    {
        this->nation = nation;
    }
    string getNation()
    {
        return this->nation;
    }

    /*Set dan Get data tahun berdiri tim sepakbola */
    void setFound(int found)
    {
        this->found = found;
    }
    int getFound()
    {
        return this->found;
    }

    /*Set dan Get data nama pemain tim sepakbola */
    void setPlayer(string player)
    {
        this->player = player;
    }
    string getPlayer()
    {
        return this->player;
    }
};