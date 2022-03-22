import sys

def main():
    if len(sys.argv) < 4:
        print("Utilisation: python encrypt.py <nom_fichier_clair> <mot_de_passe> <nom_fichier_chiffre>", file=sys.stderr)
        sys.exit(1)
    
    nom_fichier_clair: str = sys.argv[1]
    mot_de_passe: str = sys.argv[2]
    nom_fichier_chiffre: str = sys.argv[3]
    # TODO Votre programme commence ici
    

if __name__ == "__main__":
    main()

