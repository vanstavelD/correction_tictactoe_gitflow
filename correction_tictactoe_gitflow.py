def jouer_coup(plateau:dict, joueur:str, coup:str) -> None:
    """Fonction qui joue un coup (Ne vérifie pas si le coup est valide)
    Args:
        plateau (dict): Le plateau de jeu
        joueur (str): "O" ou "X"
        coup (str): Coordonnées de la forme "A1"
    """
    plateau[coup[0].upper()][int(coup[1])] = joueur

def afficher_grille(plateau:dict) -> None:
    """Fonction qui affiche la grille du morpion
    Args:
        plateau (dict): Un plateau de jeu
    """
    os.system("clear")
    print(" \t|\t0\t|\t1\t|\t2\t|")
    print("---------------------------------------------------------")
    for cle in plateau:
        print(cle, end="\t|\t")
        for elt in plateau[cle]:
            if elt == None:
                print(" ", end="\t|\t")
            else:
                print(elt, end="\t|\t")
        print("\n---------------------------------------------------------")
        
def est_coup_valide(plateau:dict, coup:str) -> bool:
    """Fonction qui vérifie si un coup est valide
    Args:
        plateau (dict): Le plateau de jeu
        coup (str): Un coup de la forme "A1" avec le premier caractere entre A et C et le second entre 0 et 2 
    Returns:
        bool: True si le coup est valide, False sinon
    """
    
    # On vérifie si le coup est une case qui existe
    if coup[0].upper() not in ["A", "B", "C"]:
        return False
    if coup[1] not in ["0", "1", "2"]:
        return False
    
    # On vérifie si la case est vide
    if plateau[coup[0].upper()][int(coup[1])] == None:
        return True
    else:
        return False       
    
    
    def est_pleine(plateau:dict) -> bool:
        """Fonction qui permet de savoir si la grille est pleine
    Args:
        plateau (dict): Un plateau de jeu
    Returns:
        bool: True si la grille est pleine, False sinon
    """
    
    for cle in plateau:
        for case in plateau[cle]:
            if case == None:
                return False
    return True

plateau = {
    "A" : [None for _ in range(3)],
    "B" : [None for _ in range(3)],
    "C" : [None for _ in range(3)]
}

termine = False
joueur = "X"

while not termine:
    afficher_grille(plateau)
    
    coup = input("Entrez un coup : (Joueur = " + joueur + " ) ")
    # On vérifie si le coup est valide, sinon on redemande un coup
    while not est_coup_valide(plateau, coup):
        coup = input("Entrez un coup (Valide cette fois): ")
    
    jouer_coup(plateau, joueur, coup)
    
    pleine = est_pleine(plateau)
    gagnante = est_gagnante(plateau)
    termine = pleine or gagnante
    
    if gagnante:
        afficher_grille(plateau)
        print("Félicitations joueur ", joueur)
    elif pleine:
        afficher_grille(plateau)
        print("Égalité")
    else:
        if joueur == "X":
            joueur = "O"
        else:
            joueur = "X"