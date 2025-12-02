from libs.reservation import Reservation

reservations = []

def action_add():
    """Action pour ajouter une réservation."""
    print("Action 'add' : Ajout d'une réservation...")

    # Récolte des informations.
    identite_client = input("Entrer le NOM et le Prénom du client :\nadd> ")
    print(identite_client)

    identite_employe = input("Entrer le nom de l'employé :\nadd> ")
    print(identite_employe)

    num_table = input("Entrer le numéro de la table :\nadd> ")
    print(num_table)

    nombre_personnes = input("Entrer le nombre de convives :\nadd> ")
    print(nombre_personnes)

    horodatage = input("Entrer la date et l'heure :\nadd> ")
    print(horodatage)

    type_reservation = input("S'il s'agit d'une occasion particulière, merci de le préciser :\nadd> ")
    print(type_reservation)

    contraintes_alimentaires = []
    while True:
        allergie = input("Spécifier les aliments auxquels le client est allergique (ou appuyer sur Entrée pour terminer) :\nadd-allergic> ").strip()

        # Si l'utilisateur appuie sur Entrée sans rien écrire, on sort de la boucle
        if not allergie:
            break

        # Ajoute l'allergie à la liste
        contraintes_alimentaires.append(allergie)
        print(allergie)
    print(contraintes_alimentaires)
    
    nombre_enfants = input("Entrer le nombre d'enfants :\nadd> ")
    print(nombre_enfants)

    commentaire = input("Entrer un éventuel commentaire :\nadd> ") 
    print(commentaire)

    # Création d'une instance
    reservation = Reservation(
        identite_client=identite_client,
        identite_employe=identite_employe,
        num_table=num_table,
        nombre_personnes=nombre_personnes,
        horodatage=horodatage,
        type_reservation=type_reservation,
        contraintes_alimentaires=contraintes_alimentaires,
        nombre_enfants=nombre_enfants,
        commentaire=commentaire,
    )

    reservations.append(reservation)


def action_delete():
    """Action pour supprimer une réservation."""
    print("Action 'delete' : Suppression d'une réservation...")
    # Ajoute ici ton code pour l'action "delete"

def action_detail(id_reservation):
    """Action pour afficher le détail d'une réservation."""
    # utiliser la méthode description. Il faut utiliser le numéro pour identifier la réservation dans le gros array des réservations.

def action_list():
    """Action pour lister les réservations."""
    print("Action 'list' : Liste des réservations...")
    for index, reservation in enumerate(reservations, start=1):
        print(f"{index}. {reservation.identite_client}")
    # Ajoute ici ton code pour l'action "list"

def action_help():
    """Affiche l'aide des commandes disponibles."""
    print("Commandes disponibles :")
    print("  add    - Ajouter une réservation")
    print("  delete - Supprimer une réservation")
    print("  detail - Afficher le détail d'une réservation")
    print("  list   - Lister les réservations")
    print("  help   - Afficher cette aide")
    print("  exit   - Quitter le programme")

def main():
    print("Bienvenue dans le système de gestion des réservations !")
    print("Tapez 'help' pour voir les commandes disponibles.")

    while True:
        # Demande à l'utilisateur de saisir une commande
        user_input = input("\n> ").strip().lower()

        # Exécute l'action correspondante
        if user_input == "add":
            action_add()
        elif user_input == "delete":
            action_delete()
        elif user_input == "list":
            action_list()
        elif user_input == "help":
            action_help()
        elif user_input == "exit":
            print("Au revoir !")
            break
        else:
            print(f"Commande inconnue : '{user_input}'. Tapez 'help' pour voir les commandes disponibles.")

if __name__ == "__main__":
    main()
