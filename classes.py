class Document:
    def __init__(self, titre, auteur, id_document):
        self.titre = titre
        self.auteur = auteur
        self.id_document = id_document
        self.disponible = True

    def __str__(self):
        return f"{self.titre} par {self.auteur} (ID: {self.id_document}) - {'Disponible' if self.disponible else 'Emprunté'}"

    def afficher_details(self):
        # Méthode abstraite pour afficher les détails spécifiques du document
        raise NotImplementedError("La méthode afficher_details doit être redéfinie dans les sous-classes.")

class Livre(Document):
    def __init__(self, titre, auteur, isbn):
        # Initialise un objet Livre avec un titre, un auteur et un ISBN
        super().__init__(titre, auteur, isbn)
        self.__isbn = isbn

    def afficher_details(self):
        return f"Livre: {self.get_titre()} par {self.get_auteur()} (ISBN: {self.__isbn}) - {'Disponible' if self.get_disponible() else 'Emprunté'}"

    # Getter et Setter pour l'attribut ISBN
    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn


    def afficher_details(self):
        # Affiche les détails spécifiques d'un livre
        return f"Livre: {self.titre} par {self.auteur} (ISBN: {self.isbn}) - {'Disponible' if self.disponible else 'Emprunté'}"

class Membre:
    def __init__(self, nom, id_membre):
        self.nom = nom
        self.id_membre = id_membre
        self.documents_empruntes = []

    def emprunter_document(self, document):
        if document.disponible:
            self.documents_empruntes.append(document)
            document.disponible = False
            return True
        return False

    def retourner_document(self, document):
        if document in self.documents_empruntes:
            self.documents_empruntes.remove(document)
            document.disponible = True
            return True
        return False

    def __str__(self):
        return f"Membre: {self.nom} (ID: {self.id_membre}) - Documents empruntés: {[doc.titre for doc in self.documents_empruntes]}"

class Bibliotheque:
    def __init__(self):
        self.documents = []
        self.membres = []

    def ajouter_document(self, document):
        self.documents.append(document)

    def supprimer_document(self, id_document):
        self.documents = [doc for doc in self.documents if doc.id_document != id_document]

    def ajouter_membre(self, membre):
        self.membres.append(membre)

    def supprimer_membre(self, id_membre):
        self.membres = [membre for membre in self.membres if membre.id_membre != id_membre]

    def emprunter_document(self, id_membre, id_document):
        membre = next((m for m in self.membres if m.id_membre == id_membre), None)
        document = next((d for d in self.documents if d.id_document == id_document), None)
        if membre and document:
            return membre.emprunter_document(document)
        return False  # Retourne False si le membre ou le document n'existe pas

    def retourner_document(self, id_membre, id_document):
        membre = next((m for m in self.membres if m.id_membre == id_membre), None)
        document = next((d for d in self.documents if d.id_document == id_document), None)
        if membre and document:
            return membre.retourner_document(document)
        return False  # Retourne False si le membre ou le document n'existe pas

    def rechercher_document(self, titre):
        return [document for document in self.documents if titre.lower() in document.titre.lower()]

    def rechercher_membre(self, nom):
        return [membre for membre in self.membres if nom.lower() in membre.nom.lower()]

# Exemple d'utilisation
bibliotheque = Bibliotheque()

# Création de documents et d'un membre
livre1 = Livre("1984", "George Orwell", "360")
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
