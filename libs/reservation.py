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
    
    midi = Horaire("12:00", "14:30")
    soir = Horaire("19:00", "22:30")
    
    
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
        commentaire: str    
    ):
           
        self.__identite_client = identite_client                  #str
        self.__identite_employe = identite_employe                #str
        self.__num_table = num_table                              #int
        self.__nombre_personnes = nombre_personnes                #int
        self.__type_reservation = type_reservation                #str
        self.__contraintes_alimentaires = contraintes_alimentaires    #str
        self.__nombre_enfants = nombre_enfants                    #int
        self.__commentaire = commentaire                          #str
        self.__date = datetime.now()                              #str
        self.__date_reservation = date_reservation                #str
        self.__service = service                                  #str
        self.__heure_debut = heure_debut                          #str
        self.__heure_fin = heure_fin                              #str
        
        
    @property    
    def identite_client(self) -> str:
        """Retourne l'identité du client."""
        return self.__identite_client
    
    @identite_client.setter
    def identite_client(self, identite_client: str) -> None:
        """Modifie l'identité du client."""
        self.__identite_client = identite_client
        
    @property
    def identite_employe(self) -> str:
        """Retourne l'identité de l'employé."""
        return self.__identite_employe
    
    @identite_employe.setter
    def identite_employe(self, identite_employe: str) -> None:
        """Modifie l'identité de l'employé."""
        self.__identite_employe = identite_employe
        
    @property
    def num_table(self) -> int: 
        """Retourne le numéro de la table réservée."""
        return self.__num_table

        
    @num_table.setter
    def num_table(self, num_table: int) -> None:
        """Modifie le numéro de la table réservée."""
        if num_table not in Reservation.Tables:
            raise ValueError(f"La table numéro {num_table} n'existe pas.")
        self.__num_table = num_table
        
    @property
    def nombre_personnes(self) -> int:  
        """Retourne le nombre de personnes pour la réservation."""
        return self.__nombre_personnes
    
    @nombre_personnes.setter
    def nombre_personnes(self, nombre_personnes: int) -> None:
        """Modifie le nombre de personnes pour la réservation."""
        capacite_table = Reservation.Tables[self.__num_table].capacite
        if nombre_personnes > capacite_table:
            raise ValueError(
                f"Le nombre de personnes ({nombre_personnes}) doit être inférieur ou égal à la capacité de la table {self.__num_table} ({capacite_table})."
            )
        if nombre_personnes < 1:
            raise ValueError("Le nombre de personnes doit être au moins 1.")
        self.__nombre_personnes = nombre_personnes
        

    @property
    def nombre_enfants(self) -> int:
        """Retourne le nombre d'enfants inclus dans la réservation."""
        return self.__nombre_enfants    
    
    @nombre_enfants.setter
    def nombre_enfants(self, nombre_enfants: int) -> None:
        """Modifie le nombre d'enfants inclus dans la réservation."""
        self.__nombre_enfants = nombre_enfants
        
    @property
    def contraintes_alimentaires(self) -> str:
        """Retourne les contraintes alimentaires spécifiques pour la réservation."""
        return self.__contraintes_alimentaires
    
    @contraintes_alimentaires.setter
    def contraintes_alimentaires(self, contraintes_alimentaires: str) -> None:  
        """Modifie les contraintes alimentaires spécifiques pour la réservation."""
        self.__contraintes_alimentaires = contraintes_alimentaires
    
    @property
    def date_reservation(self):
        return self.__date_reservation

    @date_reservation.setter
    def date_reservation(self, valeur: str):
        try:
            date_obj = datetime.strptime(valeur, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Format de date invalide. Utilisez 'YYYY-MM-DD'.")
    
        # Vérifier si le restaurant est fermé le lundi
        if date_obj.weekday() == 0:  # 0 = lundi
            raise ValueError("Le restaurant est fermé le lundi.")
    
        self.__date_reservation = date_obj
          
    @property
    def service(self) -> str:       
        """Retourne le service de la réservation."""
        return self.__service 
     
    @service.setter
    def service(self, service: str) -> None:    
        """Modifie le service de la réservation."""
        if service not in ["midi", "soir"]:
            raise ValueError("Le service doit être soit 'midi' soit 'soir'.")
        self.__service = service

    # Méthode statique pour convertir une chaîne en objet time
    @staticmethod
    def _str_to_time(s: str):
        """Convertit une chaîne 'HH:MM' en objet datetime.time."""
        return datetime.strptime(s, "%H:%M").time()

    @property
    def heure_debut(self) -> str:
        return self.__heure_debut

    @heure_debut.setter
    def heure_debut(self, valeur: str) -> None:
        heure = self._str_to_time(valeur)

        if self.__service == "midi":
            if heure >= Reservation.midi.ouverture:
                self.__heure_debut = valeur
            else:   
                raise ValueError(f"L'heure de début (RDB) {valeur} ne peut pas être avant l'ouverture de midi ({Reservation.midi.ouverture.strftime('%H:%M')}).")

        elif self.__service == "soir":
            if heure >= Reservation.soir.ouverture:
                self.__heure_debut = valeur
            else:
                raise ValueError(f"L'heure de début (RDB) {valeur} ne peut pas être avant l'ouverture du soir ({Reservation.soir.ouverture.strftime('%H:%M')}).")


    @property
    def heure_fin(self) -> str:
        return self.__heure_fin

    @heure_fin.setter
    def heure_fin(self, valeur: str) -> None:
        heure = self._str_to_time(valeur)

        if self.__service == "midi":
            if heure <= Reservation.midi.fermeture:
                self.__heure_fin = valeur
            else:
                raise ValueError(f"L'heure de fin (RF1) {valeur} ne peut pas être après la fermeture de midi ({Reservation.midi.fermeture.strftime('%H:%M')}).")

        elif self.__service == "soir":
            if heure <= Reservation.soir.fermeture:
                self.__heure_fin = valeur
            else:
                raise ValueError(f"L'heure de fin (RF1) {valeur} ne peut pas être après la fermeture du soir ({Reservation.soir.fermeture.strftime('%H:%M')}).")


    @property
    def type_reservation(self) -> str:
        """Retourne le type de réservation."""
        return self.__type_reservation
    
    @type_reservation.setter
    def type_reservation(self, type_reservation: str) -> None:  
        """Modifie le type de réservation."""
        self.__type_reservation = type_reservation
    
    @property
    def commentaire(self) -> str:
        """Retourne le commentaire additionnel concernant la réservation."""
        return self.__commentaire

    @commentaire.setter
    def commentaire(self, commentaire: str) -> None:
        """Modifie le commentaire additionnel concernant la réservation."""
        self.__commentaire = commentaire
    
    @property
    def date(self) -> str:
        """Retourne la date de création ou de modification de la réservation."""
        return self.__date.strftime("%Y-%m-%d %H:%M")

            
    def description(self) -> str:
        """Retourne une description détaillée de la réservation."""
        return (f"  Réservation de {self.__identite_client} pour le {self.__date_reservation} à {self.__heure_debut} sur la table {self.__num_table}.\n"
                f"  Nombre de personnes: {self.__nombre_personnes} (dont {self.__nombre_enfants} enfants).\n"
                f"  Contraintes alimentaires: {self.__contraintes_alimentaires}.\n  "
                f"  Type de réservation: {self.__type_reservation}.\n"    
                f"  Commentaire: {self.__commentaire}.\n"
                f"  Réservé par l'employé: {self.__identite_employe}.\n"
                f"  Date de création/modification: {self.date}.")
                      
                              

    def __del__(self) -> None:
       pass
    
    def __lt__(self, other) -> bool:
        pass
    
    def __gt__(self, other) -> bool:
        pass
    
    def __eq__(self, other) -> bool:
        pass
    
    def __str__(self) -> str:
        return f"Réservation de {self.__identite_client} pour le {self.__date_reservation} à {self.__heure_debut} sur la table {self.__num_table}."
           
    def __repr__(self) -> str:
        return f"Reservation('{self.__identite_client}', '{self.__identite_employe}', {self.__num_table}, {self.__nombre_personnes}, {self.__nombre_enfants}, '{self.__contraintes_alimentaires}', '{self.__date_reservation}', '{self.__service}', '{self.__heure_debut}', '{self.__heure_fin}', '{self.__type_reservation}', '{self.__commentaire}', '{self.__date.strftime('%Y-%m-%d %H:%M')}')"        
    
    if __name__ == "__main__":
        reservation = Reservation(
            "Jean Dupont",
            "Alice Martin",
            3,
            4,
            1,
            "Végétarien",
            "2025-12-25",
            "midi",
            "12:30",
            "14:00",
            "Anniversaire",
            "Pas de gâteau, merci.",
            "2024-06-15 10:00"
        )
        
        print(reservation)
        print(reservation.description())