#ajout de la classe document
class Document:
    def __init__(self, titre, auteur, id_document):
        # Initialise un objet Document avec un titre, un auteur et un identifiant unique
        self.titre = titre
        self.auteur = auteur
        self.id_document = id_document
        self.disponible = True  # Par défaut, un document est disponible

    def __str__(self):
        # Retourne une chaîne de caractères décrivant le document
        return f"{self.titre} par {self.auteur} (ID: {self.id_document}) - {'Disponible' if self.disponible else 'Emprunté'}"

class Livre(Document):
    def __init__(self, titre, auteur, isbn):
        # Initialise un objet Livre en appelant le constructeur de Document
        super().__init__(titre, auteur, isbn)
        self.isbn = isbn

    def __str__(self):
        # Retourne une chaîne de caractères décrivant le livre
        return f"{self.titre} par {self.auteur} (ISBN: {self.isbn}) - {'Disponible' if self.disponible else 'Emprunté'}"



class Personne:
    def __init__(self, nom, id_personne):
        # Initialise un objet Personne avec un nom et un identifiant unique
        self.nom = nom
        self.id_personne = id_personne

    def __str__(self):
        # Retourne une chaîne de caractères décrivant la personne
        return f"Personne: {self.nom} (ID: {self.id_personne})"
        
#Modification de la classe Membre pour prendre en charge la surcharge
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
        # Initialise une bibliothèque avec des listes vides pour les documents et les membres
        self.documents = []
        self.membres = []

    def ajouter_document(self, document):
        # Ajoute un document à la bibliothèque
        self.documents.append(document)

    def supprimer_document(self, id_document):
        # Supprime un document de la bibliothèque en utilisant son identifiant unique
        self.documents = [doc for doc in self.documents if doc.id_document != id_document]

    def ajouter_membre(self, membre):
        # Ajoute un membre à la bibliothèque
        self.membres.append(membre)

    def supprimer_membre(self, id_membre):
        # Supprime un membre de la bibliothèque en utilisant son identifiant unique
        self.membres = [membre for membre in self.membres if membre.id_personne != id_membre]

    def emprunter_document(self, id_membre, id_document):
        # Permet à un membre d'emprunter un document s'il est disponible
        # Trouve le membre par son identifiant
        membre = next((m for m in self.membres if m.id_personne == id_membre), None)
        # Trouve le document par son identifiant
        document = next((d for d in self.documents if d.id_document == id_document), None)
        # Si le membre et le document existent, tente l'emprunt
        if membre and document:
            return membre.emprunter_livre(document)
        return False  # Retourne False si le membre ou le document n'existe pas

    def retourner_document(self, id_membre, id_document):
        # Permet à un membre de retourner un document emprunté
        # Trouve le membre par son identifiant
        membre = next((m for m in self.membres if m.id_personne == id_membre), None)
        # Trouve le document par son identifiant
        document = next((d for d in self.documents if d.id_document == id_document), None)
        # Si le membre et le document existent, tente le retour
        if membre and document:
            return membre.retourner_livre(document)
        return False  # Retourne False si le membre ou le document n'existe pas

    def rechercher_document(self, titre):
        # Recherche des documents par titre (insensible à la casse)
        return [doc for doc in self.documents if titre.lower() in doc.titre.lower()]

    def rechercher_membre(self, nom):
        # Recherche des membres par nom (insensible à la casse)
        return [membre for membre in self.membres if nom.lower() in membre.nom.lower()]

# Exemple d'utilisation
bibliotheque = Bibliotheque()

# Création de livres et d'un membre
livre1 = Livre("2004", "exowan", "360")
livre2 = Livre("Le Meilleur des Mondes", "ingid", "987")
membre1 = Membre("gentine", 1)

# Ajout des livres et du membre à la bibliothèque
bibliotheque.ajouter_document(livre1)
bibliotheque.ajouter_document(livre2)
bibliotheque.ajouter_membre(membre1)

# Affichage d'un livre et d'un membre
print(livre1)  # Affiche les détails du livre 1
print(membre1)  # Affiche les détails du membre 1

# Emprunt d'un livre par le membre
bibliotheque.emprunter_document(1, "360")
print(livre1)  # Le livre 1 est maintenant marqué comme emprunté
print(membre1)  # Le membre 1 a maintenant le livre 1 dans sa liste de livres empruntés

# Retour d'un livre par le membre
bibliotheque.retourner_document(1, "987")
print(livre1)  # Le livre 1 est maintenant marqué comme disponible
print(membre1)  # Le membre 1 n'a plus de livres empruntés

