class Table:
    """Classe représentant une table dans un restaurant.

    Cette classe permet de gérer les informations et l'état d'occupation d'une table,
    incluant sa réservation et sa libération.

    Attributes:
        nom (str): Le nom de la table (ex: "Table impressionniste").
        numero (int): Le numéro unique de la table dans le restaurant.
        capacite (int): Le nombre de places disponibles à cette table.
        est_occupe (bool): Indique si la table est actuellement occupée (True) ou libre (False).
    """

    def __init__(
        self,
        nom: str,
        numero: int,
        capacite: int,
        est_occup: bool,
    ) -> None:
        """Initialise une instance de Table.

        Args:
            nom: Le nom de la table.
            numero: Le numéro unique de la table.
            capacite: Le nombre de places disponibles.
            est_occup: L'état d'occupation initial de la table.
        """
        self.nom = nom                  # str
        self.numero = numero            # int
        self.capacite = capacite        # int
        self.est_occupe = est_occup    # bool

    def reserver(self) -> None:
        """Marque la table comme occupée.

        Met à jour l'attribut `est_occupe` à True pour indiquer que la table est réservée.
        """
        self.est_occupe = True

    def liberer(self) -> None:
        """Marque la table comme libre.

        Met à jour l'attribut `est_occupe` à False pour indiquer que la table est disponible.
        """
        self.est_occupe = False
