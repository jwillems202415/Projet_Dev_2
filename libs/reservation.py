from datetime import datetime

class Reservation:
    """Classe représentant une réservation avec un ID unique."""

    _dernier_id = 0  # compteur global pour les ID uniques

    def __init__(self, identite_client, identite_employe, num_table, nombre_personnes,
                 nombre_enfants, contraintes_alimentaires, date_reservation,
                 service, heure_debut, heure_fin, type_reservation, commentaire=""):
        self.__id = Reservation._generer_id()
        self.__identite_client = identite_client
        self.__identite_employe = identite_employe
        self.__num_table = num_table
        self.__nombre_personnes = nombre_personnes
        self.__nombre_enfants = nombre_enfants
        self.__contraintes_alimentaires = contraintes_alimentaires
        self.__date_reservation = date_reservation
        self.__service = service
        self.__heure_debut = heure_debut
        self.__heure_fin = heure_fin
        self.__type_reservation = type_reservation
        self.__commentaire = commentaire
        self.__date_creation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def _generer_id():
        Reservation._dernier_id += 1
        return f"{Reservation._dernier_id:04d}"

    # Affichage résumé
    def __str__(self):
        return f"[{self.id}] {self.identite_client} - Table {self.num_table} - {self.date_reservation} ({self.type_reservation})"

    # Affichage complet
    def description(self):
        return {
            "ID": self.id,
            "Client": self.identite_client,
            "Employé": self.identite_employe,
            "Table": self.num_table,
            "Nombre de personnes": self.nombre_personnes,
            "Nombre d'enfants": self.nombre_enfants,
            "Contraintes alimentaires": self.contraintes_alimentaires,
            "Date réservation": self.date_reservation,
            "Service": self.service,
            "Heure début": self.heure_debut,
            "Heure fin": self.heure_fin,
            "Type réservation": self.type_reservation,
            "Commentaire": self.commentaire,
            "Date création": self.date_creation
        }

    if __name__ == "__main__":
       pass