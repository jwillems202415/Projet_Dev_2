class Reservation:
    def __init__(
        self,
        identite_client: str,
        identite_employe: str,
        num_table: int,
        nombre_personnes: int,
        horodatage,
        type_reservation: str = "",
        contraintes_alimentaires: list["Aliment"] = [],
        nombre_enfants: int = 0,
        commentaire: str = "",
    ):
        self.identite_client = identite_client                  #str
        self.identite_employe = identite_employe                #str
        self.num_table = num_table                              #int
        self.nombre_personnes = nombre_personnes                #int
        self.horodatage = horodatage                                  #Datetime
        self.type_reservation = type_reservation                #str
        self.contraintes_alimentaires = contraintes_alimentaires    #str
        self.nombre_enfants = nombre_enfants                    #int
        self.commentaire = commentaire                          #str

    def description(self):
        """Affiche une description détaillée de la réservation."""
        print("\n" + "=" * 50)
        print("DÉTAILS DE LA RÉSERVATION")
        print("=" * 50)
        print(f"Client : {self.identite_client}")
        print(f"Employé : {self.identite_employe}")
        print(f"Table : {self.num_table}")
        print(f"Nombre de personnes : {self.nombre_personnes} (dont {self.nombre_enfants} enfant(s))")
        print(f"Date et heure : {self.horodatage}")
        if self.type_reservation:
            print(f"Type de réservation : {self.type_reservation}")
        if self.contraintes_alimentaires:
            print(f"Contraintes alimentaires : {', '.join(self.contraintes_alimentaires)}")
        if self.commentaire:
            print(f"Commentaire : {self.commentaire}")
        print("=" * 50 + "\n")


    def annuler(self):
        return

    def confirmer(self):
        return
