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
        contact: str,
    ) -> None:
        """Initialise une instance de Client.

        Args:
            identite: Le nom complet du client.
            preference_table: Le numéro de la table préférée du client.
            contact: Le numéro de téléphone du client.
        """
        self.__identite = identite
        self.__preference_table = preference_table
        self.__contact = contact

    
    @property
    def identite(self) -> str:
        """Retourne le nom complet du client."""
        return self.__identite
    
    @identite.setter
    def identite(self, valeur: str) -> None:
        """Modifie le nom complet du client."""
        if valeur.isdigit():
            raise ValueError("L'identité ne peut pas contenir de chiffres.")
        self.__identite = valeur
    
    @property
    def preference_table(self) -> int:  
        """Retourne le numéro de la table préférée du client."""
        return self.__preference_table      
    
    
    @preference_table.setter
    def preference_table(self, valeur: int) -> None:
        """Modifie le numéro de la table préférée du client."""
        if valeur < 1:
            raise ValueError("La préférence de table ne peut pas être inférieure à 1.")
        elif valeur > 12:
            raise ValueError("La préférence de table ne peut pas être supérieure à 12.")
        
        self.__preference_table = valeur
    
    
    @property
    def contact(self) -> str:
        """Retourne le numéro de téléphone du client."""
        return self.__contact
        
        
    @contact.setter
    def contact(self, valeur: str) -> None:
        """Modifie le numéro de téléphone du client."""
        if not isinstance(valeur, str):
            raise TypeError("Le contact doit être une chaîne de caractères.")
        if not valeur.isdigit() or len(valeur) != 10:
            raise ValueError("Le numéro de téléphone doit contenir exactement 10 chiffres.")
        if not valeur.startswith("04"):
            raise ValueError("Le numéro de téléphone belge doit commencer par '04'.")
        self.__contact = valeur
             
    def __str__(self):
        return f"Client(identite={self.__identite}, preference_table={self.__preference_table}, contact={self.__contact})"
    
    def __repr__(self):
        return f"Client(identite='{self.__identite}', preference_table='{self.__preference_table}', contact='{self.__contact}')"
    

    if __name__ == "__main__": 
        client = Client("Jean Dupont", 5, "0478123456")
        print(client)  