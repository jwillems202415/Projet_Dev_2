from reservation import Reservation, Tables 
from client import Client
from table import Table
from horaire import Horaire

class Restaurant:
    """Classe représentant un restaurant et ses fonctionnalités de gestion.

    Cette classe permet de gérer les réservations, les tables disponibles,
    et les horaires d'ouverture du restaurant.

    Attributes:
        nom (str): Le nom du restaurant.
        tables (list[Table]): Liste des tables disponibles dans le restaurant.
        horaires (dict): Dictionnaire des horaires d'ouverture et de fermeture.
            Exemple: {"ouverture": "09:00", "fermeture": "22:00"} ou
            {"lundi": {"ouverture": "12:00", "fermeture": "14:30"}, ...}.
    """

    def __init__( self, nom: str, tables: dict, horaires: dict) -> None:
        """Initialise une instance de Restaurant.

        Args:
            nom: Le nom du restaurant.
            tables: Liste des tables disponibles dans le restaurant.
            horaires: Dictionnaire définissant les horaires d'ouverture.
        """
        self.__nom = nom
        self.__tables = tables
        self.__horaires = horaires

    
    
    
    def verifier_disponibilite(self, date: str, heure: str, nombre_personnes: int) -> bool:
        """Vérifie la disponibilité d'une table pour une réservation donnée.

        Args:
            date: La date de la réservation (format: "YYYY-MM-DD").
            heure: L'heure de la réservation (format: "HH:MM").
            nombre_personnes: Le nombre de personnes pour la réservation.

        Returns:
            bool: True si une table est disponible, False sinon.
        """
        return False  # À implémenter

    def ajouter_reservation(self, reservation: dict) -> bool:
        """Ajoute une nouvelle réservation pour le restaurant.

        Args:
            reservation: Dictionnaire contenant les détails de la réservation.
                Exemple: {"date": "2025-12-25", "heure": "20:00", "table": 2, "nom_client": "Dupont"}.

        Returns:
            bool: True si la réservation a été ajoutée avec succès, False en cas d'échec.
        """
        return False  # À implémenter

    def retirer_reservation(self, identifiant_reservation: str) -> bool:
        """Retire une réservation existante du système.

        Args:
            identifiant_reservation: L'identifiant unique de la réservation à retirer.

        Returns:
            bool: True si la réservation a été retirée avec succès, False en cas d'échec.
        """
        return False  # À implémenter

    def lister_reservations(self):
        """Liste l'ensemble des réservations enregistrées par le système.

        Returns:
            list: Une liste contenant toutes les réservations.
        """
        return False