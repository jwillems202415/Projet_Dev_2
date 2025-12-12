# Dans ce fichier se trouvent toutes les fonctions actionnées lorsqu'une commande particulière est exécutée en console.

from datetime import time, datetime
import re
from libs.reservation import Reservation

def action_help():
    print(
        "add  - Encoder une réservation\n"
        "list - Lister les réservations du jour\n"
        "del  - Supprimer une réservation\n"
        "plus - Autres commandes\n"
        "exit - Quitter l'application\n"
    )

def action_add(restaurant):
    # Horodatage ---------------------------------------------------------------
    while True:
        print(f"Horodatage (YYYY-MM-DD HH:MM) (laisser blanc pour « {datetime.now().strftime("%Y-%m-%d %H:%M")} ») :")
        date_res_input = input("add> ")
        if not date_res_input:
            date_res = datetime.now().replace(hour=20, minute=0, second=0, microsecond=0)
            break
        else:
            try:
                date_res = datetime.strptime(date_res_input, "%Y-%m-%d %H:%M")
                break
            except:
                print("❗ Format invalide. Utilisez le format YYYY-MM-DD HH:MM.\n")

    print(f"✔️ Horodatage : {date_res.strftime("%Y-%m-%d %H:%M")}\n")

    # Nombre de convives -------------------------------------------------------
    while True:
        print("Nombre de convives : (laisser blanc pour « 2 »)")
        try:
            nbr_conv = input("add> ")
            if not nbr_conv:
                nbr_conv = 2
            nbr_conv = int(nbr_conv)
            break
        except ValueError:
            print("❗ Format invalide. Veuillez entrer un nombre.\n")

    print(f"✔️ Nombre de convives : {nbr_conv}\n")

    # Identité client ----------------------------------------------------------
    while True:
        print("Nom et prénom du client :")
        id_client = input("add> ")
        if not id_client:
            print("❗ Ce champ est obligatoire et ne peut pas être vide.\n")
        elif len(id_client) == 1:
            print("❗ Ce champ ne peut pas contenir qu'un seul caractère.\n")
        elif not re.fullmatch(r"^[A-Za-zÀ-ÖØ-öø-ÿ' -]+$", id_client): #🐱
            print("❗ Ce champ ne peut contenir que des lettres, tirets, apostrophes ou espaces.\n")
        else:
            break

    print(f"✔️ Identité du client : {id_client}\n")
    # 💡 Rajouter ici un truc qui récupère les clients, regarde s'il existe déjà et offre de l'enregistrer ou non.

    print(f"ℹ️ Si la réservation se fait par téléphone, vous pouvez raccrocher à partir de ce point. Les questions suivantes demanderont des informations complémentaires et spécifiques que le client aurait de toute façon précisées auparavant, dès lors sa présence n'est plus requise.\n")

    # Contraintes alimentaires -------------------------------------------------
    # 💡 Ajouter ici le code pour encoder les contraintes alimentaires
    contr_alim = []
    print("Lister les contraintes alimentaires : (laisser blanc si aucune)")
    while True:
        in_alim = input("add-alim> ")
        if not in_alim:
            break
        elif len(in_alim) == 1:
            print("❗ Ce champ ne peut pas contenir qu'un seul caractère.\n")
        elif not re.fullmatch(r"^[A-Za-zÀ-ÖØ-öø-ÿ' -]+$", in_alim): #🐱
            print("❗ Ce champ ne peut contenir que des lettres, tirets, apostrophes ou espaces.\n")
        else:
            contr_alim.append(in_alim)
    
    print(f"✔️ Contraintes alimentaires : {contr_alim} :\n")

    # Nombre chaises hautes ----------------------------------------------------
    while True:
        print("Nombre de chaises hautes requises pour des enfants : (laisser blanc pour 0)")
        try:
            nbr_chaises_h = input("add> ")
            if not nbr_chaises_h:
                nbr_chaises_h = 0
            nbr_chaises_h = int(nbr_chaises_h)
            break
        except ValueError:
            print("❗ Format invalide. Veuillez entrer un nombre.\n")

    print(f"✔️ Nombre de chaises hautes requises : {nbr_chaises_h}\n")

    # Identité de l'employé ----------------------------------------------------
    while True:
        print("Prénom de l'employé enregistrant cette réservation : (laisser blanc pour « Gaston »)")
        id_empl = input("add> ")
        if not id_empl:
            id_empl = "Gaston"
            break
        elif len(id_empl) == 1:
            print("❗ Ce champ ne peut pas contenir qu'un seul caractère.\n")
        elif not re.fullmatch(r"^[A-Za-zÀ-ÖØ-öø-ÿ' -]+$", id_empl): #🐱
            print("❗ Ce champ ne peut contenir que des lettres, tirets, apostrophes ou espaces.\n")
        else:
            break
    # 💡 Ajouter un système qui vérifie que l'employé est bien dans la liste.
    print(f"✔️ Prénom de l'employé enregistrant : {id_empl}\n")

    # Numéro de table assigné --------------------------------------------------
    while True:
        print("Numéro de table :")
        try:
            num_table = input("add> ")
            if not num_table:
                num_table = 0
            num_table = int(num_table)
            break
        except ValueError:
            print("❗ Format invalide. Veuillez entrer un nombre.\n")

    print(f"✔️ Numéro de table assigné : {num_table}\n")

    # Type de réservation ------------------------------------------------------
    while True:
        print("Entrez le type d'occasion (Anniversaire, demande en marriage…) : (laisser blanc pour « Normale »)")
        type_reserv = input("add> ")
        if not type_reserv:
            type_reserv = "Normale"
            break
        elif len(type_reserv) == 1:
            print("❗ Ce champ ne peut pas contenir qu'un seul caractère.\n")
        elif not re.fullmatch(r"^[A-Za-zÀ-ÖØ-öø-ÿ' -]+$", type_reserv): #🐱
            print("❗ Ce champ ne peut contenir que des lettres, tirets, apostrophes ou espaces.\n")
        else:
            break

    print(f"✔️ Type de réservation : {type_reserv}\n")

    # Commentaire --------------------------------------------------------------
    print("Commentaire éventuel : (laisser blanc si aucun)")
    commentaire = input("add> ")

    # Autres données dispensables ----------------------------------------------

    heure_res = date_res.time() # Cette p* de ligne m'a bien cassé les c*.

    if time(12, 0) <= heure_res <= time(14, 30):
        serv = "midi"
        heure_fin = "14:30"
    elif time(19, 0) <= heure_res <= time(23, 0):
        serv = "soir"
        heure_fin = "23:00"
    else:
        print("❗ Hors des horaires de service.")
        serv = None
        heure_fin = None

    if serv:
        print(f"Service : {serv}, Heure de fin : {heure_fin}")

    reservation = Reservation(
        identite_client = id_client,
        identite_employe = id_empl,
        num_table = num_table,
        nombre_personnes = nbr_conv,
        nombre_enfants = nbr_chaises_h,
        contraintes_alimentaires = contr_alim,
        date_reservation = date_res.date().strftime("%Y-%m-%d"),
        service = serv,
        heure_debut = heure_res,
        heure_fin = heure_fin,
        type_reservation = type_reserv,
        commentaire = commentaire,
    )

    restaurant.ajouter_reservation(reservation)
    print("✅ Réservation ajoutée. Merci.\n")

def action_list(restaurant):
    restaurant.voir_reservations()

def action_del(restaurant):
    restaurant.supprimer_reservation()

def action_plus():
    print("plus")

def action_exit():
    with open(reservations_data_file, "w", encoding="utf-8") as f:
        json.dump(reservations, f, ensure_ascii=False, indent=4)
    print("Données sauvegardées dans reservations.json.\n:) AU REVOIR")
