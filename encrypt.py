import sys

def chiffrement(lettre, password):
    return (((ord(lettre) - ord("A")) + \
            (ord(password) - ord("A"))) % 26) + ord("A") 


def main():
    if len(sys.argv) < 4:
        print("Utilisation: python encrypt.py <nom_fichier_clair> <mot_de_passe> <nom_fichier_chiffre>", file=sys.stderr)
        sys.exit(1)
    
    nom_fichier_clair: str = sys.argv[1]
    mot_de_passe: str = sys.argv[2]
    nom_fichier_chiffre: str = sys.argv[3]

    #Recolt des donnés
    t = open(nom_fichier_clair)
    texte = [x.strip().upper() for x in t.readlines()]
    taille_de_mot_d_passe = len(mot_de_passe)

    #crypté les donnés
    f = open(nom_fichier_chiffre, 'w')
    x = 0
    for phrase in texte:
        phrases = str()
        
        for letter in phrase:
            if ord('Z') >= ord(letter) >= ord('A'):
                phrases = phrases + chr(chiffrement(letter, mot_de_passe[x].upper()))
                x = (x + 1) % taille_de_mot_d_passe

            else: phrases = phrases + letter

        f.write(phrases + "\n")    


if __name__ == "__main__":
    main()

