class Client:
    """Classe représentant un client du restaurant.

    Cette classe permet de gérer les informations d'un client,
    ses préférences et ses réservations.

    Attributes:
        identite (str): Le nom complet du client (ex: "Jean Dupont").
        preference_table (int): Le numéro de la table préférée du client.
        contact (int): Le numéro de téléphone du client.
    """

    def __init__(
        self,
        identite: str,
        preference_table: int,
        contact: int,
    ) -> None:
        """Initialise une instance de Client.

        Args:
            identite: Le nom complet du client.
            preference_table: Le numéro de la table préférée du client.
            contact: Le numéro de téléphone du client.
        """
        self.identite = identite
        self.preference_table = preference_table
        self.contact = contact

    def reserver(self, restaurant: 'Restaurant', date: str, heure: str, nombre_personnes: int) -> bool:
        """Effectue une réservation pour le client dans un restaurant donné.

        Args:
            restaurant: L'instance du restaurant où le client souhaite réserver.
            date: La date de la réservation (format: "YYYY-MM-DD").
            heure: L'heure de la réservation (format: "HH:MM").
            nombre_personnes: Le nombre de personnes pour la réservation.

        Returns:
            bool: True si la réservation a été effectuée avec succès, False sinon.
        """
        return False  # À implémenter
