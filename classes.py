class Document:
    def __init__(self, titre, auteur, id_document):
        # Initialise un objet Document avec un titre, un auteur et un identifiant de document
        self.__titre = titre
        self.__auteur = auteur
        self.__id_document = id_document
        self.__disponible = True

    def __str__(self):
        # Retourne une chaîne de caractères représentant l'objet Document
        return f"{self.__titre} par {self.__auteur} (ID: {self.__id_document}) - {'Disponible' if self.__disponible else 'Emprunté'}"

    def afficher_details(self):
        # Méthode abstraite pour afficher les détails spécifiques du document
        raise NotImplementedError("La méthode afficher_details doit être redéfinie dans les sous-classes.")

    # Getters et Setters
    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_id_document(self):
        return self.__id_document

    def set_id_document(self, id_document):
        self.__id_document = id_document

    def get_disponible(self):
        return self.__disponible

    def set_disponible(self, disponible):
        self.__disponible = disponible


class Livre(Document):
    def __init__(self, titre, auteur, isbn):
        # Initialise un objet Livre avec un titre, un auteur et un ISBN
        super().__init__(titre, auteur, isbn)
        self.__isbn = isbn

    def afficher_details(self):
        # Affiche les détails spécifiques d'un livre
        return f"Livre: {self.get_titre()} par {self.get_auteur()} (ISBN: {self.__isbn}) - {'Disponible' if self.get_disponible() else 'Emprunté'}"

    # Getter et Setter pour l'attribut ISBN
    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn


class Membre:
    def __init__(self, nom, id_membre):
        # Initialise un objet Membre avec un nom et un identifiant unique
        self.__nom = nom
        self.__id_membre = id_membre
        self.__documents_empruntes = []

    def emprunter_document(self, document):
        # Permet à un membre d'emprunter un document s'il est disponible
        if document.get_disponible():
            self.__documents_empruntes.append(document)
            document.set_disponible(False)
            return True
        return False

    def retourner_document(self, document):
        # Permet à un membre de retourner un document emprunté
        if document in self.__documents_empruntes:
            self.__documents_empruntes.remove(document)
            document.set_disponible(True)
            return True
        return False

    def __str__(self):
        # Retourne une chaîne de caractères représentant l'objet Membre
        return f"Membre: {self.__nom} (ID: {self.__id_membre}) - Documents empruntés: {[doc.get_titre() for doc in self.__documents_empruntes]}"

    # Getters et Setters
    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_id_membre(self):
        return self.__id_membre

    def set_id_membre(self, id_membre):
        self.__id_membre = id_membre

    def get_documents_empruntes(self):
        return self.__documents_empruntes


class Bibliotheque:
    def __init__(self):
        # Initialise une bibliothèque avec des listes de documents et de membres
        self.__documents = []
        self.__membres = []

    def ajouter_document(self, document):
        # Ajoute un document à la bibliothèque
        self.__documents.append(document)

    def supprimer_document(self, id_document):
        # Supprime un document de la bibliothèque par son identifiant
        self.__documents = [doc for doc in self.__documents if doc.get_id_document() != id_document]

    def ajouter_membre(self, membre):
        # Ajoute un membre à la bibliothèque
        self.__membres.append(membre)

    def supprimer_membre(self, id_membre):
        # Supprime un membre de la bibliothèque par son identifiant
        self.__membres = [membre for membre in self.__membres if membre.get_id_membre() != id_membre]

    def emprunter_document(self, id_membre, id_document):
        # Permet à un membre d'emprunter un document de la bibliothèque
        membre = next((m for m in self.__membres if m.get_id_membre() == id_membre), None)
        document = next((d for d in self.__documents if d.get_id_document() == id_document), None)
        if membre and document:
            return membre.emprunter_document(document)
        return False  # Retourne False si le membre ou le document n'existe pas

    def retourner_document(self, id_membre, id_document):
        # Permet à un membre de retourner un document emprunté
        membre = next((m for m in self.__membres if m.get_id_membre() == id_membre), None)
        document = next((d for d in self.__documents if d.get_id_document() == id_document), None)
        if membre and document:
            return membre.retourner_document(document)
        return False  # Retourne False si le membre ou le document n'existe pas

    def rechercher_document(self, titre):
        # Recherche des documents par titre (insensible à la casse)
        return [document for document in self.__documents if titre.lower() in document.get_titre().lower()]

    def rechercher_membre(self, nom):
        # Recherche des membres par nom (insensible à la casse)
        return [membre for membre in self.__membres if nom.lower() in membre.get_nom().lower()]

    # Getters pour les attributs privés
    def get_documents(self):
        return self.__documents

    def get_membres(self):
        return self.__membres


# Exemple d'utilisation
bibliotheque = Bibliotheque()

# Création de documents et d'un membre
livre1 = Livre("La guerre de 100", "George Orwell", "360")
livre2 = Livre("Le Meilleur des Mondes", "Aldous Huxley", "361")
membre1 = Membre("August", 1)

# Ajout des documents et du membre à la bibliothèque
bibliotheque.ajouter_document(livre1)
bibliotheque.ajouter_document(livre2)
bibliotheque.ajouter_membre(membre1)

# Affichage d'un document et d'un membre
print(livre1)
print(membre1)

# Emprunt d'un document par le membre
bibliotheque.emprunter_document(1, "360")
print(livre1)  # Le livre 1 est maintenant marqué comme emprunté
print(membre1)  # Le membre 1 a maintenant le livre 1 dans sa liste de documents empruntés

# Retour d'un document par le membre
bibliotheque.retourner_document(1, "360")
print(livre1)  # Le livre 1 est maintenant marqué comme disponible
print(membre1)  # Le membre 1 n'a plus de documents empruntés
