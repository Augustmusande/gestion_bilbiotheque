class Livre:
    def __init__(self, titre, auteur, isbn):
        # Initialise un objet Livre avec un titre, un auteur et un ISBN
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.disponible = True  # Par défaut, un livre est disponible

    def __str__(self):
        # Retourne une chaîne de caractères décrivant le livre
        return f"{self.titre} par {self.auteur} (ISBN: {self.isbn}) - {'Disponible' if self.disponible else 'Emprunté'}"

class Membre:
    def __init__(self, nom, id_membre):
        # Initialise un objet Membre avec un nom et un identifiant unique
        self.nom = nom
        self.id_membre = id_membre
        self.livres_empruntes = []  # Liste des livres empruntés par le membre

    def emprunter_livre(self, livre):
        # Permet à un membre d'emprunter un livre s'il est disponible
        if livre.disponible:
            self.livres_empruntes.append(livre)  # Ajoute le livre à la liste des livres empruntés
            livre.disponible = False  # Marque le livre comme non disponible
            return True  # Retourne True pour indiquer que l'emprunt a réussi
        return False  # Retourne False si le livre n'est pas disponible

    def retourner_livre(self, livre):
        # Permet à un membre de retourner un livre emprunté
        if livre in self.livres_empruntes:
            self.livres_empruntes.remove(livre)  # Retire le livre de la liste des livres empruntés
            livre.disponible = True  # Marque le livre comme disponible
            return True  # Retourne True pour indiquer que le retour a réussi
        return False  # Retourne False si le livre n'est pas dans la liste des livres empruntés

    def __str__(self):
        # Retourne une chaîne de caractères décrivant le membre et les livres empruntés
        return f"Membre: {self.nom} (ID: {self.id_membre}) - Livres empruntés: {[livre.titre for livre in self.livres_empruntes]}"

class Bibliotheque:
    def __init__(self):
        # Initialise une bibliothèque avec des listes vides pour les livres et les membres
        self.livres = []
        self.membres = []

    def ajouter_livre(self, livre):
        # Ajoute un livre à la bibliothèque
        self.livres.append(livre)

    def supprimer_livre(self, isbn):
        # Supprime un livre de la bibliothèque en utilisant son ISBN
        self.livres = [livre for livre in self.livres if livre.isbn != isbn]

    def ajouter_membre(self, membre):
        # Ajoute un membre à la bibliothèque
        self.membres.append(membre)

    def supprimer_membre(self, id_membre):
        # Supprime un membre de la bibliothèque en utilisant son identifiant unique
        self.membres = [membre for membre in self.membres if membre.id_membre != id_membre]

    def emprunter_livre(self, id_membre, isbn):
        # Permet à un membre d'emprunter un livre s'il est disponible
        # Trouve le membre par son identifiant
        membre = next((m for m in self.membres if m.id_membre == id_membre), None)
        # Trouve le livre par son ISBN
        livre = next((l for l in self.livres if l.isbn == isbn), None)
        # Si le membre et le livre existent, tente l'emprunt
        if membre and livre:
            return membre.emprunter_livre(livre)
        return False  # Retourne False si le membre ou le livre n'existe pas

    def retourner_livre(self, id_membre, isbn):
        # Permet à un membre de retourner un livre emprunté
        # Trouve le membre par son identifiant
        membre = next((m for m in self.membres if m.id_membre == id_membre), None)
        # Trouve le livre par son ISBN
        livre = next((l for l in self.livres if l.isbn == isbn), None)
        # Si le membre et le livre existent, tente le retour
        if membre and livre:
            return membre.retourner_livre(livre)
        return False  # Retourne False si le membre ou le livre n'existe pas

    def rechercher_livre(self, titre):
        # Recherche des livres par titre (insensible à la casse)
        return [livre for livre in self.livres if titre.lower() in livre.titre.lower()]

    def rechercher_membre(self, nom):
        # Recherche des membres par nom (insensible à la casse)
        return [membre for membre in self.membres if nom.lower() in membre.nom.lower()]

# Exemple d'utilisation
bibliotheque = Bibliotheque()

# Création de livres et d'un membre
livre1 = Livre("1984", "George bouche", "360")
livre2 = Livre("Le Meilleur des Mondes", "Exaudie", "360")
membre1 = Membre("August", 1)

# Ajout des livres et du membre à la bibliothèque
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_membre(membre1)

# Affichage d'un livre et d'un membre
print(livre1)  # Affiche les détails du livre 1
print(membre1)  # Affiche les détails du membre 1

# Emprunt d'un livre par le membre
bibliotheque.emprunter_livre(1, "360")
print(livre1)  # Le livre 1 est maintenant marqué comme emprunté
print(membre1)  # Le membre 1 a maintenant le livre 1 dans sa liste de livres empruntés

# Retour d'un livre par le membre
bibliotheque.retourner_livre(1, "369")
print(livre1)  # Le livre 1 est maintenant marqué comme disponible
print(membre1)  # Le membre 1 n'a plus de livres empruntés
