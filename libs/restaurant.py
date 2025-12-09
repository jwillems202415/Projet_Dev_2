from .reservation import Reservation

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

    def __init__(
        self,
        nom: str,
        tables: list['Table'],  # Supposons que `tables` est une liste d'instances de la classe `Table`
        horaires: dict,         # Structure flexible pour les horaires (à adapter selon tes besoins)
    ) -> None:
        """Initialise une instance de Restaurant.

        Args:
            nom: Le nom du restaurant.
            tables: Liste des tables disponibles dans le restaurant.
            horaires: Dictionnaire définissant les horaires d'ouverture.
        """
        self.nom = nom
        self.tables = tables
        self.horaires = horaires

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

    def ajouter_reservation(reservations):
        """Ajout d'une réservation."""

        # Récolte des informations.
        identite_client = input("Entrer le nom et le prénom du client :\nadd> ")
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

    def retirer_reservation(self, identifiant_reservation: str) -> bool:
        """Retire une réservation existante du système.

        Args:
            identifiant_reservation: L'identifiant unique de la réservation à retirer.

        Returns:
            bool: True si la réservation a été retirée avec succès, False en cas d'échec.
        """
        return False  # À implémenter

    def lister_reservations(reservations):
        """Liste l'ensemble des réservations enregistrées par le système.

        Returns:
            list: Une liste contenant toutes les réservations.
        """
        for index, reservation in enumerate(reservations, start=1):
            print(f"{index}. {reservation.identite_client}")