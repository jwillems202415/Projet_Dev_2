from datetime import datetime, time

class Horaire:
    """
    Représente un horaire d'ouverture et de fermeture (heures uniquement).
    """

    def __init__(self, ouverture: str, fermeture: str) -> None:
        """
        Initialise une instance de Horaire.

        Args:
            ouverture (str): Heure d'ouverture au format "HH:MM".
            fermeture (str): Heure de fermeture au format "HH:MM".
        """
        self.__ouverture = datetime.strptime(ouverture, "%H:%M").time()
        self.__fermeture = datetime.strptime(fermeture, "%H:%M").time()
    # ----------- Méthodes internes -----------

    @staticmethod
    def _convertir_en_time(valeur: str) -> time:
        """
        Convertit une chaîne 'HH:MM' en objet datetime.time.
        """
        try:
            heure = datetime.strptime(valeur, "%H:%M").time()
            return heure
        except ValueError:
            raise ValueError("Format d'heure invalide. Utilisez 'HH:MM'.")

    # ----------- Propriétés -----------

    @property
    def ouverture(self) -> time:
        return self.__ouverture

    @ouverture.setter
    def ouverture(self, valeur: str) -> None:
        if not isinstance(valeur, str):
            raise TypeError("L'heure doit être une chaîne de caractères dans le format 'HH:MM'.")
        self.__ouverture = self._convertir_en_time(valeur)

    @property
    def fermeture(self) -> time:
        return self.__fermeture

    @fermeture.setter
    def fermeture(self, valeur: str) -> None:
        if not isinstance(valeur, str):
            raise TypeError("L'heure doit être une chaîne de caractères dans le format 'HH:MM'.")
        self.__fermeture = self._convertir_en_time(valeur)

    # ----------- Affichage -----------

    def __str__(self) -> str:
        return f"Ouverture : {self.ouverture.strftime('%H:%M')} | Fermeture : {self.fermeture.strftime('%H:%M')}"

    def __repr__(self) -> str:
        return f"Horaire('{self.ouverture.strftime('%H:%M')}', '{self.fermeture.strftime('%H:%M')}')"


# Exemple d'utilisation
if __name__ == "__main__":
    horaire = Horaire("09:15", "22:30")
    print(horaire)
    print("Ouverture :", horaire.ouverture)
    print("Fermeture :", horaire.fermeture)
