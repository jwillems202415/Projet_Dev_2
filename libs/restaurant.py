# restaurant.py
import json
from .client import Client
from .reservation import Reservation
from .table import Table

class Restaurant:
    _nom = "La Bonne Fourchette"
    _chef = "Gaston"

    def __init__(self, fichier_reservations="reservations.json"):
        self.fichier_reservations = fichier_reservations
        self.clients = []
        self.tables = []  # Liste de tables dans le restaurant
        self.reservations = []

        # Charger les réservations depuis JSON
        try:
            with open(self.fichier_reservations, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    reservation = Reservation(
                        item["identite_client"],
                        item["identite_employe"],
                        item["num_table"],
                        item["nombre_personnes"],
                        item["nombre_enfants"],
                        item["contraintes_alimentaires"],
                        item["date_reservation"],
                        item["service"],
                        item["heure_debut"],
                        item["heure_fin"],
                        item["type_reservation"],
                        item.get("commentaire", "")
                    )
                    reservation.id = item["id"]  # conserver l'ID existant
                    self.reservations.append(reservation)
        except (FileNotFoundError, json.JSONDecodeError):
            print("❗ Le fichier « reservations.json » est inexistant.")

    def nom(self):
        return self._nom

    def chef(self):
        return self._chef

    # Clients
    def ajouter_client(self, client: Client):
        self.clients.append(client)

    # Tables
    def ajouter_table(self, table: Table):
        self.tables.append(table)

    def afficher_tables(self):
        for table in self.tables:
            print(f"Table {table.num_table}: {table.nom}, Capacité: {table.capacite}, Emplacement: {table.emplacement}")

    # Réservations
    def ajouter_reservation(self, reservation: Reservation):
        self.reservations.append(reservation)
        self._sauvegarder_reservations()

    def supprimer_reservation(self, reservation: Reservation):
        if reservation in self.reservations:
            self.reservations.remove(reservation)
            self._sauvegarder_reservations()
            print(f"Réservation de {reservation.identite_client} supprimée.")
        else:
            print("Réservation introuvable.")

    def afficher_reservations(self):
        """Affiche résumé des réservations"""
        for res in self.reservations:
            print(res)

    def voir_reservation(self, reservation_id):
        """Affiche les détails complets d'une réservation via ID"""
        for res in self.reservations:
            if res.id == reservation_id:
                print(res.description())
                return
        print(f"Aucune réservation trouvée avec l'ID {reservation_id}")

    # Sauvegarde JSON
    def _sauvegarder_reservations(self):
        data = []
        for res in self.reservations:
            data.append({
                "id": res.id,
                "identite_client": res.identite_client,
                "identite_employe": res.identite_employe,
                "num_table": res.num_table,
                "nombre_personnes": res.nombre_personnes,
                "nombre_enfants": res.nombre_enfants,
                "contraintes_alimentaires": res.contraintes_alimentaires,
                "date_reservation": str(res.date_reservation),
                "service": res.service,
                "heure_debut": res.heure_debut,
                "heure_fin": res.heure_fin,
                "type_reservation": res.type_reservation,
                "commentaire": res.commentaire,
                "date_creation": res.date_creation
            })
        with open(self.fichier_reservations, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)    

    if __name__ == "__main__":
        pass