import sys
from pathlib import Path

# Ajouter le dossier libs au path pour que Python trouve les modules
sys.path.insert(0, str(Path(__file__).parent / "libs"))

# Imports des classes depuis libs (sans préfixe 'libs.')
from client import Client
from reservation import Reservation
from restaurant import Restaurant

def menu():
    print("\n=== La Bonne Fourchette - CLI ===")
    print("1. Afficher les tables")
    print("2. Ajouter un client")
    print("3. Afficher les clients")
    print("4. Ajouter une réservation")
    print("5. Supprimer une réservation")
    print("6. Voir toutes les réservations")
    print("7. Quitter")
    return input("Votre choix: ")

def main():
    resto = Restaurant()  # Initialise le restaurant

    global reservations
    reservations = load_reservations()

    while True:
        choix = menu()

        if choix == "1":
            resto.afficher_tables()

        elif choix == "2":
            nom = input("Nom complet: ")
            table_pref = int(input("Table préférée (1-12): "))
            contact = input("Numéro de téléphone: ")
            client = Client(nom, table_pref, contact)
            resto.ajouter_client(client)
            print(f"Client {nom} ajouté.")

        elif choix == "3":
            resto.afficher_clients()

        elif choix == "4":
            identite_client = input("Nom du client: ")
            identite_employe = input("Nom de l'employé: ")
            num_table = int(input("Numéro de table: "))
            nombre_personnes = int(input("Nombre de personnes: "))
            nombre_enfants = int(input("Nombre d'enfants: "))
            contraintes = input("Contraintes alimentaires: ")
            date_res = input("Date (YYYY-MM-DD): ")
            service = input("Service (midi/soir): ")
            heure_debut = input("Heure début (HH:MM): ")
            heure_fin = input("Heure fin (HH:MM): ")
            type_res = input("Type de réservation: ")
            commentaire = input("Commentaire: ")

            reservation = Reservation(
                identite_client,
                identite_employe,
                num_table,
                nombre_personnes,
                nombre_enfants,
                contraintes,
                date_res,
                service,
                heure_debut,
                heure_fin,
                type_res,
                commentaire
            )
            resto.ajouter_reservation(reservation)
            print("Réservation ajoutée.")

        elif choix == "5":
            nom_client = input("Nom du client à supprimer: ")
            res_a_supprimer = next((r for r in resto.reservations if r.identite_client == nom_client), None)
            if res_a_supprimer:
                resto.supprimer_reservation(res_a_supprimer)
            else:
                print("Aucune réservation trouvée pour ce client.")

        elif choix == "6":
            for desc in resto.voir_reservations():
                print(desc)

        elif choix == "7":
            print("Au revoir !")
            break

        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
