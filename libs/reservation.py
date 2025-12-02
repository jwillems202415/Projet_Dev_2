class Reservation:
    def __init__(
        self,
        identite_client: str,
        identite_employe: str,
        num_table: int,
        nombre_personnes: int,
        horaire,
        type_reservation: str = "",
        contrainte_alimentaire: list["Aliment"] = [],
        nombre_enfants: int = 0,
        commentaire: str = "",
    ):
        self.identite_client = identite_client                  #str
        self.identite_employe = identite_employe                #str
        self.num_table = num_table                              #int
        self.nombre_personnes = nombre_personnes                #int
        self.horaire = horaire                                  #Datetime
        self.type_reservation = type_reservation                #str
        self.contrainte_alimentaire = contrainte_alimentaire    #str
        self.nombre_enfants = nombre_enfants                    #int
        self.commentaire = commentaire                          #str

    def description(self):
        print("")

    def annuler(self):
        return

    def confirmer(self):
        return
