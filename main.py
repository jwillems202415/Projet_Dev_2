def action_add():
    """Action pour ajouter une réservation."""
    print("Action 'add' : Ajout d'une réservation...")
    # Ajoute ici ton code pour l'action "add"

def action_delete():
    """Action pour supprimer une réservation."""
    print("Action 'delete' : Suppression d'une réservation...")
    # Ajoute ici ton code pour l'action "delete"

def action_list():
    """Action pour lister les réservations."""
    print("Action 'list' : Liste des réservations...")
    # Ajoute ici ton code pour l'action "list"

def action_help():
    """Affiche l'aide des commandes disponibles."""
    print("Commandes disponibles :")
    print("  add    - Ajouter une réservation")
    print("  delete - Supprimer une réservation")
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
