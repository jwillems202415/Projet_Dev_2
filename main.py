from libs.reservation import Reservation
from libs.restaurant import Restaurant
import json

# SAUVEGARDE DES DONNÉES -------------------------------------------------------

RESERVATIONS_FILE = "reservations.json"

def load_reservations():
    """Load reservations from the JSON file."""
    try:
        with open(RESERVATIONS_FILE, "r") as file:
            data = json.load(file)
            return [Reservation(**item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_reservations(reservations):
    """Save reservations to the JSON file."""
    with open(RESERVATIONS_FILE, "w") as file:
        json.dump([reservation.__dict__ for reservation in reservations], file, indent=4)

# ------------------------------------------------------------------------------

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
    print(r"""
    _            ____
    | |    __ _  | __ )  ___  _ __  _ __   ___
    | |   / _` | |  _ \ / _ \| '_ \| '_ \ / _ \
    | |__| (_| | | |_) | (_) | | | | | | |  __/
    |_____\__,_| |____/ \___/|_| |_|_| |_|\___|
    |  ___|__  _   _ _ __ ___| |__   ___| |_| |_ ___
    | |_ / _ \| | | | '__/ __| '_ \ / _ \ __| __/ _ \
    |  _| (_) | |_| | | | (__| | | |  __/ |_| ||  __/
    |_|  \___/ \__,_|_|  \___|_| |_|\___|\__|\__\___|
    version 0.2
    """)

    print("Bienvenue dans le système de gestion des réservations !")
    print("Tapez 'help' pour voir les commandes disponibles.")

    global reservations
    reservations = load_reservations()

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
            print("⏳ Enregistrement des réservations…")
            save_reservations(reservations)
            print("✅ Enregistrement terminé !")
            print("Au revoir !")
            break
        else:
            print(f"Commande inconnue : '{user_input}'. Tapez 'help' pour voir les commandes disponibles.")

if __name__ == "__main__":
    main()
