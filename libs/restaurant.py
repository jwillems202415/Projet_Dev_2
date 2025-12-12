import json
from .client import Client
from .reservation import Reservation
from .table import Table

class Restaurant:
    """Classe représentant le restaurant 'La Bonne Fourchette' avec son chef Gaston."""

    _nom = "La Bonne Fourchette"
    _chef = "Gaston"

    def __init__(self, fichier_reservations="reservations.json"):
        self.fichier_reservations = fichier_reservations
        self.clients = []        # Liste d'objets Client
        self.tables = Reservation.Tables  # Tables existantes
        # Charger les réservations depuis le fichier JSON
        try:
            with open(self.fichier_reservations, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.reservations = []
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
                        item["commentaire"]
                    )
                    self.reservations.append(reservation)
        except (FileNotFoundError, json.JSONDecodeError):
            print("❗ Le fichier « reservations.json » est inexistant.")
            self.reservations = []

    # Méthodes fixes
    def nom(self) -> str:
        return self._nom

    def chef(self) -> str:
        return self._chef

    # Ajouter un client
    def ajouter_client(self, client: Client) -> None:
        self.clients.append(client)

    # Ajouter une réservation
    def ajouter_reservation(self, reservation: Reservation) -> None:
        self.reservations.append(reservation)
        # self._sauvegarder_reservations() # fonctionne pas pour le moment et clc

    # Supprimer une réservation
    def supprimer_reservation(self, reservation: Reservation) -> None:
        if reservation in self.reservations:
            self.reservations.remove(reservation)
            self._sauvegarder_reservations()
            print(f"Réservation de {reservation.identite_client} supprimée.")
        else:
            print("Réservation introuvable.")

    # Voir toutes les réservations
    def voir_reservations(self):
        return [r.description() for r in self.reservations]

    # Sauvegarder les réservations dans un fichier JSON
    def _sauvegarder_reservations(self) -> None:
        data = []
        for res in self.reservations:
            data.append({
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
                "date_creation": res.date
            })
        with open(self.fichier_reservations, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    # Afficher les tables disponibles
    def afficher_tables(self):
        for num, table in self.tables.items():
            print(f"Table {num}: {table.nom}, Capacité: {table.capacite}, Emplacement: {table.emplacement}")

    # Afficher tous les clients
    def afficher_clients(self):
        for client in self.clients:
            print(client)

    # Afficher toutes les réservations
    def afficher_reservations(self):
        for res in self.reservations:
            print(res)

    def __str__(self):
        return f"Restaurant {self._nom} géré par {self._chef}"
    
    def __repr__(self):
        return f"Restaurant('{self._nom}', '{self._chef}')"



if __name__ == "__main__":
    resto = Restaurant()

    # Ajouter un client
    client1 = Client("Jean Dupont", 5, "0478123456")
    resto.ajouter_client(client1)

    # Ajouter une réservation
    reservation1 = Reservation(
        identite_client=client1.identite,
        identite_employe="Alice Martin",
        num_table=3,
        nombre_personnes=4,
        nombre_enfants=1,
        contraintes_alimentaires="Végétarien",
        date_reservation="2025-12-25",
        service="midi",
        heure_debut="12:30",
        heure_fin="14:00",
        type_reservation="Anniversaire",
        commentaire="Pas de gâteau, merci."
    )
    resto.ajouter_reservation(reservation1)

    # Affichage
    print("Nom du restaurant:", resto.nom())
    print("Chef du restaurant:", resto.chef())
    print("\nTables disponibles:")
    resto.afficher_tables()
    print("\nClients:")
    resto.afficher_clients()
    print("\nRéservations:")
    resto.afficher_reservations()

    # Supprimer une réservation
    resto.supprimer_reservation(reservation1)
    print("\nRéservations après suppression:")
    resto.afficher_reservations()
