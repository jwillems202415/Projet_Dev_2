class Restaurant:
    def __init__(self, nom, tables, horaires):
        self.nom = nom                  #str
        self.tables = tables            #int
        self.horaires = horaires        #Datetime

    def verifier_disponibilite(self):
        return

    def ajouter_reservation(self):
        return

    def retirer_reservation(self):
        return


class Table:
    def __init__(self, nom, numero, capacite, est_occupe):
        self.nom = nom                  #str
        self.numero = numero            #int
        self.capacite = capacite        #int
        self.est_occupe = est_occupe    #bool

    def reserver(self):
        return

    def liberer(self):
        return


class Horaire:
    def __init__(self, jour, periode, ouverture, fermeture):
        self.jour = jour                #str
        self.periode = periode          #str
        self.ouverture = ouverture      #Time
        self.fermeture = fermeture      #Time


class Client:
    def __init__(self, identite, preferenceTable, contact):
        self.identite = identite                #str
        self.preferenceTable = preferenceTable  #int
        self.contact = contact                  #int

    def reserver(self):
        return


class Reservation:
    def __init__(self,identite_client,identite_employe,num_table,nombre_personnes,horaire,type_reservation,contrainte_alimentaire,nombre_enfants,commentaire: str):
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
        return

    def annuler(self):
        return

    def confirmer(self):
        return