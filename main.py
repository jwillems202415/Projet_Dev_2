from libs.reservation import Reservation
from libs.restaurant import Restaurant

reservations = [] # Il faudra stocker ça dans un JSON et le charger un beau jour

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
            print("Action 'add' : Ajout d'une réservation...")
            Restaurant.ajouter_reservation(reservations)
        elif user_input == "delete":
            action_delete()
        elif user_input == "list":
            print("Action 'list' : Liste des réservations...")
            Restaurant.lister_reservations(reservations)
        elif user_input == "help":
            action_help()
        elif user_input == "exit":
            print("Au revoir !")
            break
        else:
            print(f"Commande inconnue : '{user_input}'. Tapez 'help' pour voir les commandes disponibles.")

if __name__ == "__main__":
    main()
