class Document:
    def __init__(self, titre, auteur, id_document):
        # Initialise un objet Document avec un titre, un auteur et un identifiant de document
        self.titre = titre
        self.auteur = auteur
        self.id_document = id_document
        self.disponible = True  # Par défaut, le document est disponible

    def __str__(self):
        # Retourne une chaîne de caractères décrivant le document
        return f"{self.titre} par {self.auteur} (ID: {self.id_document}) - {'Disponible' if self.disponible else 'Emprunté'}"

    def afficher_details(self):
        # Méthode abstraite pour afficher les détails spécifiques du document
        raise NotImplementedError("La méthode afficher_details doit être redéfinie dans les sous-classes.")

class Livre(Document):
    def __init__(self, titre, auteur, isbn):
        # Initialise un objet Livre avec un titre, un auteur et un ISBN
        super().__init__(titre, auteur, isbn)
        self.isbn = isbn

    def afficher_details(self):
        # Affiche les détails spécifiques d'un livre
        return f"Livre: {self.titre} par {self.auteur} (ISBN: {self.isbn}) - {'Disponible' if self.disponible else 'Emprunté'}"

class Membre:
    def __init__(self, nom, id_membre):
        # Initialise un objet Membre avec un nom et un identifiant unique
        self.nom = nom
        self.id_membre = id_membre
        self.documents_empruntes = []  # Liste des documents empruntés par le membre

    def emprunter_document(self, document):
        # Permet à un membre d'emprunter un document s'il est disponible
        if document.disponible:
            self.documents_empruntes.append(document)  # Ajoute le document à la liste des documents empruntés
            document.disponible = False  # Marque le document comme non disponible
            return True  # Retourne True pour indiquer que l'emprunt a réussi
        return False  # Retourne False si le document n'est pas disponible

    def retourner_document(self, document):
        # Permet à un membre de retourner un document emprunté
        if document in self.documents_empruntes:
            self.documents_empruntes.remove(document)  # Retire le document de la liste des documents empruntés
            document.disponible = True  # Marque le document comme disponible
            return True  # Retourne True pour indiquer que le retour a réussi
        return False  # Retourne False si le document n'est pas dans la liste des documents empruntés

    def __str__(self):
        # Retourne une chaîne de caractères décrivant le membre et les documents empruntés
        return f"Membre: {self.nom} (ID: {self.id_membre}) - Documents empruntés: {[doc.titre for doc in self.documents_empruntes]}"

    def afficher_details(self):
        # Affiche les détails du membre et les documents empruntés
        return f"Membre: {self.nom} (ID: {self.id_membre}) - Documents empruntés: {[doc.titre for doc in self.documents_empruntes]}"

class Bibliotheque:
    def __init__(self):
        # Initialise une bibliothèque avec des listes vides pour les documents et les membres
        self.documents = []
        self.membres = []

    def ajouter_document(self, document):
        # Ajoute un document à la bibliothèque
        self.documents.append(document)

    def supprimer_document(self, id_document):
        # Supprime un document de la bibliothèque en utilisant son identifiant
        self.documents = [doc for doc in self.documents if doc.id_document != id_document]

    def ajouter_membre(self, membre):
        # Ajoute un membre à la bibliothèque
        self.membres.append(membre)

    def supprimer_membre(self, id_membre):
        # Supprime un membre de la bibliothèque en utilisant son identifiant unique
        self.membres = [membre for membre in self.membres if membre.id_membre != id_membre]

    def emprunter_document(self, id_membre, id_document):
        # Permet à un membre d'emprunter un document s'il est disponible
        # Trouve le membre par son identifiant
        membre = next((m for m in self.membres if m.id_membre == id_membre), None)
        # Trouve le document par son identifiant
        document = next((d for d in self.documents if d.id_document == id_document), None)
        # Si le membre et le document existent, tente l'emprunt
        if membre and document:
            return membre.emprunter_document(document)
        return False  # Retourne False si le membre ou le document n'existe pas

    def retourner_document(self, id_membre, id_document):
        # Permet à un membre de retourner un document emprunté
        # Trouve le membre par son identifiant
        membre = next((m for m in self.membres if m.id_membre == id_membre), None)
        # Trouve le document par son identifiant
        document = next((d for d in self.documents if d.id_document == id_document), None)
        # Si le membre et le document existent, tente le retour
        if membre and document:
            return membre.retourner_document(document)
        return False  # Retourne False si le membre ou le document n'existe pas

    def rechercher_document(self, titre):
        # Recherche des documents par titre (insensible à la casse)
        return [document for document in self.documents if titre.lower() in document.titre.lower()]

    def rechercher_membre(self, nom):
        # Recherche des membres par nom (insensible à la casse)
        return [membre for membre in self.membres if nom.lower() in membre.nom.lower()]

# Exemple d'utilisation
bibliotheque = Bibliotheque()

# Création de documents et d'un membre
livre1 = Livre("1984", "prince", "360")
livre2 = Livre("Le Monde et ses merveilles", "john muller", "36")
membre1 = Membre("waridi", 5)

# Ajout des documents et du membre à la bibliothèque
bibliotheque.ajouter_document(livre1)
bibliotheque.ajouter_document(livre2)
bibliotheque.ajouter_membre(membre1)

# Affichage d'un document et d'un
print(livre1)
print(membre1)

# Emprunt d'un document par le membre
bibliotheque.emprunter_document(5, "360")
print(livre1)  # Le livre 1 est maintenant marqué comme emprunté
print(membre1)  # Le membre 1 a maintenant le livre 1 dans sa liste de documents empruntés

# Retour d'un document par le membre
bibliotheque.retourner_document(5, "360")
print(livre1)  # Le livre 1 est maintenant marqué comme disponible
print(membre1)  # Le membre 1 n'a plus de documents empruntés
