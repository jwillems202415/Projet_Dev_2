from datetime import datetime
from table import Table
from horaire import Horaire

class Reservation:
    """Classe représentant une réservation dans un restaurant. 
    Cette classe permet de gérer les informations relatives à une réservation,
    incluant les détails du client, de l'employé, de la table, et
    les spécificités de la réservation elle-même.
    Attributes:
        identite_client (str): L'identité du client ayant effectué la réservation.  
        identite_employe (str): L'identité de l'employé ayant pris la réservation.
        num_table (int): Le numéro de la table réservée.
        nombre_personnes (int): Le nombre de personnes pour la réservation.
        nombre_enfants (int): Le nombre d'enfants inclus dans la réservation.
        contraintes_alimentaires (str): Les contraintes alimentaires spécifiques pour la réservation.   
        date_reservation (str): La date de la réservation (format: "YYYY-MM-DD").
        service (str): Le service de la réservation (ex: "midi", "soir").
        heure_debut (str): L'heure de début de la réservation (format: "HH:MM").
        heure_fin (str): L'heure de fin de la réservation (format: "HH:MM").
        type_reservation (str): Le type de réservation (ex: "standard", "anniversaire").
        commentaire (str): Un commentaire additionnel concernant la réservation.
        date (str): La date de création ou de modification de la réservation.   
    """
    
    Tables = {
        1: Table("la table des amoureux", 1, 2, "Baie vitrée"),
        2: Table("Les Tourtereaux", 2, 2, "Baie vitrée"),
        3: Table("La Conviviale", 3, 4, "Baie vitrée"),
        4: Table("La Famille Martin", 4, 4, "Baie vitrée"),
        5: Table("Grands Appétits", 5, 6, "Centre"),
        6: Table("Grands Appétits", 6, 6, "Centre"),
        7: Table("Grands Appétits", 7, 6, "Centre"),
        8: Table("Grands Appétits", 8, 6, "Centre"),  
        9: Table("La Confidence", 9, 3, "Fond"),
        10: Table("L’Ombre du Chêne", 10, 3, "Fond"),
        11: Table("Le Coin du Chef", 11, 3, "Fond"),
        12: Table("La Douce Nuit", 12, 3, "Fond")  
    }
    
    
    def __init__(
        self,
        identite_client: str,
        identite_employe: str,
        num_table: int,
        nombre_personnes: int,
        nombre_enfants: int,
        contraintes_alimentaires: str,
        date_reservation: str,
        service: str,
        heure_debut: str,
        heure_fin: str, 
        type_reservation: str, 
        commentaire: str,
        date: str
    ):
           
        self.__identite_client = identite_client                  #str
        self.__identite_employe = identite_employe                #str
        self.__num_table = num_table                              #int
        self.__nombre_personnes = nombre_personnes                #int
        self.__type_reservation = type_reservation                #str
        self.__contraintes_alimentaires = contraintes_alimentaires    #str
        self.__nombre_enfants = nombre_enfants                    #int
        self.__commentaire = commentaire                          #str
        self.__date = date                                        #str
        self.__date_reservation = date_reservation                #str
        self.__service = service                                  #str
        self.__heure_debut = heure_debut                          #str
        self.__heure_fin = heure_fin                              #str
        
        
    @property    
    def identite_client(self) -> str:
        """Retourne l'identité du client."""
        return self.__identite_client
    
    @property
    def identite_employe(self) -> str:
        """Retourne l'identité de l'employé."""
        return self.__identite_employe
    
    
    @property
    def num_table(self) -> int: 
        """Retourne le numéro de la table réservée."""
        return self.__num_table

        
    @property
    def nombre_personnes(self) -> int:  
        """Retourne le nombre de personnes pour la réservation."""
        return self.__nombre_personnes
    
    @property
    def nombre_enfants(self) -> int:
        """Retourne le nombre d'enfants inclus dans la réservation."""
        return self.__nombre_enfants    
    
    @property
    def contraintes_alimentaires(self) -> str:
        """Retourne les contraintes alimentaires spécifiques pour la réservation."""
        return self.__contraintes_alimentaires
    
    @property
    def date_reservation(self) -> str:  
        """Retourne la date de la réservation."""
        return self.__date_reservation
    
    
    @property
    def service(self) -> str:       
        """Retourne le service de la réservation."""
        return self.__service   

    @property
    def heure_debut(self) -> str:
        """Retourne l'heure de début de la réservation."""
        return self.__heure_debut   
    
    
    @property
    def heure_fin(self) -> str:
        """Retourne l'heure de fin de la réservation."""
        return self.__heure_fin
    
    @property
    def type_reservation(self) -> str:
        """Retourne le type de réservation."""
        return self.__type_reservation
    
    @property
    def commentaire(self) -> str:
        """Retourne le commentaire additionnel concernant la réservation."""
        return self.__commentaire
    
    @property
    def date(self) -> str:
        """Retourne la date de création ou de modification de la réservation."""
        return self.__date

            
    def description(self) -> str:
        """Retourne une description détaillée de la réservation."""
        return (
            f"Réservation pour {self.__identite_client} "
            f"par {self.__identite_employe} "
            f"le {self.__date_reservation} "
            f"du {self.__service} "
            f"de {self.__heure_debut} à {self.__heure_fin} "
            f"sur la table {self.__num_table} "
            f"pour {self.__nombre_personnes} personnes "
            f"({self.__nombre_enfants} enfants) "
            f"avec les contraintes alimentaires : {self.__contraintes_alimentaires} "
            f"Type de réservation : {self.__type_reservation} "
            f"Commentaire : {self.__commentaire} "
            f"Créée le {self.__date}"
        )

    def __del__(self) -> None:
        """Supprime l'instance de la réservation."""
        return f"La réservation pour {self.__identite_client} a été supprimée."
    
    def __lt__(self, other) -> bool:
        pass
    
    def __gt__(self, other) -> bool:
        pass
    
    def __eq__(self, other) -> bool:
        pass
    
    def __str__(self) -> str:
        pass
           
    def __repr__(self) -> str:
        pass
    
    if __name__ == "__main__":
        pass