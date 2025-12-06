import re
class Horaire:
    def __init__(self, ouverture: str, fermeture: str) -> None:
        """  Initialise une instance de Horaire.
        Args:
            ouverture: L'heure d'ouverture (format: "HH:MM").
            fermeture: L'heure de fermeture (format: "HH:MM").
        """
        self.__ouverture = ouverture      
        self.__fermeture = fermeture      

    pattern = r"^([01]\d|2[0-3]):[0-5]\d$"
    
    @property
    def ouverture(self) -> str:
        """Retourne l'heure d'ouverture."""
        return self.__ouverture
    
    @ouverture.setter
    def ouverture(self, valeur: str) -> None:
        """Modifie l'heure d'ouverture."""
        if not re.match(self.pattern, valeur):
            raise ValueError("Format d'heure invalide. Utilisez HH:MM.")
        elif not isinstance(valeur, str):
            raise TypeError("L'heure doit être une chaîne de caractères au format 'HH:MM'.")
        self.__ouverture = valeur
    
    @property
    def fermeture(self) -> str:
        """Retourne l'heure de fermeture."""
        return self.__fermeture
    
    @fermeture.setter
    def fermeture(self, valeur: str) -> None:   
        """Modifie l'heure de fermeture."""
        if not re.match(self.pattern, valeur):
            raise ValueError("Format d'heure invalide. Utilisez HH:MM.")
        elif not isinstance(valeur, str):
            raise TypeError("L'heure doit être une chaîne de caractères au format 'HH:MM'.")
        self.__fermeture = valeur
        
    def __str__(self) -> str:
        pass
    
    def __repr__(self) -> str:
        pass
    
    if __name__ == "__main__": 
        horaire = Horaire("09:00", "22:00")
        print(horaire)
        print(horaire.ouverture)
        print(horaire.fermeture)