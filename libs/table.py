class Table:
    """Classe représentant une table dans un restaurant.

    Cette classe permet de gérer les informations et l'état d'occupation d'une table,
    incluant sa réservation et sa libération.

    Attributes:
        nom (str): Le nom de la table (ex: "Table impressionniste").
        numero (int): Le numéro unique de la table dans le restaurant.
        capacite (int): Le nombre de places disponibles à cette table.
    """

    def __init__(
        self,
        nom: str,
        numero: int,
        capacite: int,
        emplacement: str
    ) -> None:
        """Initialise une instance de Table.

        Args:
            nom: Le nom de la table.
            numero: Le numéro unique de la table.
            capacite: Le nombre de places disponibles.
        """
        self.__nom = nom                  # str
        self.__numero = numero            # int
        self.__capacite = capacite        # int
        self.__emplacement = emplacement  # str
        
    @property
    def nom(self) -> str:
        """Retourne le nom de la table."""
        return self.__nom
    
    @property
    def numero(self) -> int:
        """Retourne le numéro de la table."""
        return self.__numero
    
    
    @property
    def capacite(self) -> int:
        """Retourne la capacité de la table."""
        return self.__capacite
    
    @property
    def emplacement(self) -> str:
        """Retourne l'emplacement de la table."""
        return self.__emplacement
    
    def __str__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    if __name__ == "__main__": 
        table = Table("Table impressionniste", 1, 4)
        print(table)
        print(table.nom)
        print(table.numero)
        print(table.capacite)