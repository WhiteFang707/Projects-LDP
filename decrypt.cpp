#include <iostream>
#include <string>
#include <cstring>
#include <fstream>

using namespace std;

int main(int argc, char *argv[]) {
    if (argc < 4) {
        cout << "Utilisation: ./decrypt <nom_fichier_chiffre> <mot_de_passe> <nom_fichier_dechiffre>" << endl;
        return 1;
    }
    
    string nom_fichier_chiffre = argv[1];
    string mot_de_passe = argv[2];
    string nom_fichier_dechiffre = argv[3];

    // TODO Votre programme commence ici
    ifstream nom_fichier_chiffre;
    












    return 0;
}
