# Dans ce fichier se trouvent toutes les fonctions actionnées lorsqu'une commande particulière est exécutée en console.

import re
from libs.reservation import Reservation
from datetime import datetime, timedelta, time

def action_help():
    print(
        "add     - Encoder une réservation\n"
        "list    - Lister les réservations\n"
        "detail  - Afficher le détail d'une réservation\n"
        "modif   - Modifier une réservation\n"
        "del     - Supprimer une réservation\n"
        "exit    - Quitter l'application\n"
    )


def action_add(restaurant):
    # Horodatage ---------------------------------------------------------------
    while True:
        print(f"Horodatage (YYYY-MM-DD HH:MM) (laisser blanc pour « {datetime.now().strftime("%Y-%m-%d")} 20:00 ») :")
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

    
    # Nombre de convives -------------------------------------------------------
    while True:
        print("Nombre de convives : (laisser blanc pour « 2 »)")
        nbr_conv = input("add> ")

        if not nbr_conv:
            nbr_conv = 2
            break

        try:
            nbr_conv = int(nbr_conv)
            if nbr_conv < 1:
                print("❗ Cette valeur ne peut pas être inférieure à 1.\n")
            else:
                break
        except ValueError:
            print("❗ Format invalide. Veuillez entrer un nombre.\n")

    print(f"✔️ Nombre de convives : {nbr_conv}\n")
    
    # Nombre d'enfants ------------------------------------------------------------
    while True:
        print("Nombre d'enfants : (laisser blanc pour 0)")
        nbr_enfants = input("add> ")

        if not nbr_enfants:
            nbr_enfants = 0
            break

        try:
            nbr_enfants = int(nbr_enfants)
            if nbr_enfants < 0:
                print("❗ Cette valeur ne peut pas être négative.\n")
            else:
                break
        except ValueError:
            print("❗ Format invalide. Veuillez entrer un nombre.\n")


    print(f"✔️ Nombre d'enfants : {nbr_enfants}\n")

    # Chaise haute ---------------------------------------------------------------
    chaise_haute = "Non"
    if nbr_enfants > 0:
        while True:
            print("Faut-il prévoir une chaise haute ? (oui / non) :")
            rep = input("add> ").lower()
            if rep in ["oui", "non"]:
                chaise_haute = rep.capitalize()
                break
            else:
                print("❗ Répondez par 'oui' ou 'non'.\n")

    print(f"✔️ Chaise haute : {chaise_haute}\n")
    
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

    # Numéro de table assigné --------------------------------------------------
    while True:
        print("Numéro de table :")
        try:
            num_table = input("add> ")
            num_table = int(num_table)
            if not num_table:
                print("❗ Ce champ ne peut pas être vide.\n")
            elif num_table == 0:
                print("❗ Un numéro de table ne peut pas être nul.\n")
            elif num_table > 12:
                print("❗ Il n'y a que douze tables dans le restaurant, toute valeur supérieure à 12 est invalide.\n")
            else:
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
    commentaire = ""
    if chaise_haute == "Oui":
        commentaire = "[Chaise haute requise] "
    user_commentaire = input("Commentaire éventuel : (laisser blanc si aucun)\nadd> ")
    commentaire += user_commentaire
    print(f"✔️ Commentaire : {commentaire}\n")

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
        nombre_enfants = nbr_enfants,
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
    if not restaurant.reservations:
        print("Aucune réservation enregistrée.\n")
        return

    print("\n--- LISTE DES RÉSERVATIONS ---")
    for i, res in enumerate(restaurant.reservations, start=1):
        print(
            f"{i}. {res.identite_client} | "
            f"{res.date_reservation} {res.heure_debut}"
        )
    print("------------------------------\n")


def action_detail(restaurant):
    """Afficher le détail d'une réservation et permettre d'enchaîner sur d'autres."""
    if not restaurant.reservations:
        print("Aucune réservation à afficher.\n")
        return

    afficher_autre = True
    while afficher_autre:
        print("\n--- LISTE DES RÉSERVATIONS ---")
        for i, res in enumerate(restaurant.reservations, start=1):
            print(f"{i}. {res.identite_client} | {res.date_reservation} {res.heure_debut}")
        print("------------------------------\n")

        while True:
            try:
                choix = int(input("Numéro de la réservation à afficher (0 pour annuler) : "))
                if choix == 0:
                    print("\nTapez 'help' pour voir les commandes disponibles.\n")
                    return
                if 1 <= choix <= len(restaurant.reservations):
                    res = restaurant.reservations[choix - 1]
                    break
                else:
                    print("❗ Veuillez entrer un numéro valide.\n")
            except ValueError:
                print("❗ Veuillez entrer un nombre.\n")


        print("\n======== DÉTAIL DE LA RÉSERVATION ========")
        print(f"Nom et prénom du client : {res.identite_client}")
        print(f"Date et heure           : {res.date_reservation} {res.heure_debut}")
        print(f"Nombre de convives      : {res.nombre_personnes}")
        print(f"Nombre d'enfants        : {res.nombre_enfants}")
        print(f"Table souhaitée         : {res.num_table}")
        print(f"Occasion particulière   : {res.type_reservation}")
        print(f"Allergies / contraintes : {res.contraintes_alimentaires}")
        print(f"Note du staff           : {res.commentaire}")
        print(f"Réservation encodée par : {res.identite_employe}")
        print("=========================================")

        
        while True:
            rep = input("\nVoulez-vous afficher les détails d'une autre réservation ? (oui/non) : ").strip().lower()
            if rep in ["oui", "o"]:
                break
            elif rep in ["non", "n"]:
                afficher_autre = False
                print("\nTapez 'help' pour voir les commandes disponibles.\n")
                break
            else:
                print("❗ Veuillez répondre par 'oui' ou 'non'.")


def action_modif(restaurant):
    if not restaurant.reservations:
        print("Aucune réservation à modifier.\n")
        return

    # Afficher la liste des réservations
    print("\n--- LISTE DES RÉSERVATIONS ---")
    for i, res in enumerate(restaurant.reservations, start=1):
        print(f"{i}. {res.identite_client} | {res.date_reservation} {res.heure_debut}")
    print("------------------------------\n")

    # Choix de la réservation
    while True:
        try:
            choix = int(input("Numéro de la réservation à modifier : "))
            if 1 <= choix <= len(restaurant.reservations):
                reservation = restaurant.reservations[choix - 1]
                break
            else:
                print("❗ Sélection invalide. Veuillez réessayer.")
        except ValueError:
            print("❗ Veuillez entrer un nombre valide.")

    # Menu des champs modifiables
    print(
        "Que souhaitez-vous modifier ?\n"
        "1. Date / heure\n"
        "2. Nombre de convives\n"
        "3. Nombre d'enfants\n"
        "4. Table\n"
        "5. Type de réservation\n"
        "6. Commentaire"
    )

    champ = input("add> ").strip()

    # Modifier en fonction du choix
    if champ == "1":
        nouvelle_date = input("Nouvelle date (YYYY-MM-DD) : ").strip()
        nouvelle_heure = input("Nouvelle heure (HH:MM) : ").strip()
        try:
            reservation.date_reservation = nouvelle_date
            reservation.heure_debut = nouvelle_heure
        except Exception:
            print("❗ Format de date/heure invalide, modification annulée.")
            return
    elif champ == "2":
        while True:
            valeur = input("Nouveau nombre de convives : ").strip()
            if valeur.isdigit():
                reservation.nombre_personnes = int(valeur)
                break
            else:
                print("❗ Veuillez entrer un chiffre.")
    elif champ == "3":
        while True:
            valeur = input("Nouveau nombre d'enfants : ").strip()
            if valeur.isdigit():
                reservation.nombre_enfants = int(valeur)
                break
            else:
                print("❗ Veuillez entrer un chiffre.")
    elif champ == "4":
        while True:
            valeur = input("Nouvelle table : ").strip()
            if valeur.isdigit():
                reservation.num_table = int(valeur)
                break
            else:
                print("❗ Veuillez entrer un chiffre.")
    elif champ == "5":
        reservation.type_reservation = input("Nouveau type de réservation : ").strip()
    elif champ == "6":
        reservation.commentaire = input("Nouveau commentaire : ").strip()
    else:
        print("❗ Choix invalide, modification annulée.")
        return

    print("✔️ Réservation mise à jour avec succès.\n")


def action_del(restaurant):
    if not restaurant.reservations:
        print("Aucune réservation à supprimer.\n")
        return

   
    print("\n--- LISTE DES RÉSERVATIONS ---")
    for i, res in enumerate(restaurant.reservations, start=1):
        print(f"{i}. {res.identite_client} | {res.date_reservation} {res.heure_debut}")
    print("------------------------------\n")

   
    while True:
        try:
            choix = int(input("Numéro de la réservation à supprimer (0 pour annuler) : "))
            if choix == 0:
                print("❌ Suppression annulée.\n")
                return
            if 1 <= choix <= len(restaurant.reservations):
                res = restaurant.reservations[choix - 1]
                break
            else:
                print("❗ Veuillez entrer un numéro valide.\n")
        except ValueError:
            print("❗ Veuillez entrer un nombre.\n")

    while True:
        confirm = input(f"Êtes-vous sûr de vouloir supprimer la réservation de {res.identite_client} ? (oui/non) : ").strip().lower()
        if confirm in ["oui", "o"]:
            restaurant.reservations.pop(choix - 1)
            print(f"✅ Réservation de {res.identite_client} supprimée.\n")
            break
        elif confirm in ["non", "n"]:
            print("❌ Suppression annulée.\n")
            break
        else:
            print("❗ Veuillez répondre par 'oui' ou 'non'.")


def action_plus():
    print("plus")
    # il y a quoi a mettre en plus lol ??

def action_exit():
    print(":) AU REVOIR")
    exit()