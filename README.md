# pythonclassmates
Pythonclassmates est un site communautaire dédié aux étudiants et mentor du parcours développeur d'application python de openclassrooms.

## Besoin identifié
Ce projet est né de la volonté de mon mentor Thierry Chappuis de créer une plateforme communautaire à même de centraliser l'information et favoriser l'échange et le partage de connaissance. Ayant la chance d'avoir une communauté très active sur le DA python, nous avons tout de même soulevé quelques problèmes, que ce site à court, moyen et long terme souhaite modestement régler. En voici une  liste non exhaustive : 
* Les personnes souhaitant créer un webinaire non aucun moyen de connaître le nombre de participant à l'avance
* Discord étant ce qu'il est, l'information y est vite noyée par les conversations et nouveaux sujets, ce qui rend la promotion d'événement compliquée, et les solutions et aides techniques très éphémères.
* Difficulté de retrouver les informations pertinentes sur discord (même une fois épinglées).
* Difficulté pour toucher l'ensemble des étudiants lors de la promotion d'un webinaire.
* Impossibilité d'agréger l'information.
* Répétition de l'information.

L'idée derrière cette plateforme pourrait se résumer en trois parties : la création et la communication autour d'événement, la création d'un blog participatif, et la centralisation de toutes les ressources utiles en un seul et même endroit. La communauté openclassrooms python étant très active sur le discord d'application python, ce site y serait étroitement lié. C'est pourquoi, une des volontés de ce projet est de pouvoir aussi bien récupérer des ressources proposées sur le DA python pour les exporter / agréger sur notre site communautaire, qu'à l'inverse publier des informations du site sur DA python, notamment les événements comme les webinaires. 

## Objectif à court terme (MVP)
* Partie event :
  * Système d'événement pour les webinaires
  * Inscription des participants
* Partie ressources : 
  * Insérer une ressource
* Partie blog :
  * Création d'article
  * Création d'une série d'article
* Système de tag (commun aux trois parties : event, blog et ressource)
* Système de catégorie (commun au trois parties : event, blog et ressource)

## Objectifs à moyen terme
* Partie event :
  * Publication d'évènement automatique et répété sur le channel général de discord (utilisation API wagtail)
  * Envoie de mails aux inscrits
* Partie Blog :
  * Commentaires sur les articles
* Partie ressources:
  * Récupération automatique des webinaires passés

## Objectifs à long terme
* Gamification du site avec un système de niveau en fonction de points gagnés par la participation à la vie du site (animer un webinaire = 20 points, créer un article = 10 points, laisser un commentaire = 1 point, etc...)
* Partie event :
  * Intégration des vidéos directement sur la plateforme ?
* Partie Blog : ... 
* Partie ressources :
  * Créer un bot pour récupérer automatiquement les ressources proposé sur les channels DA python et les intégrer sur le site (nécessite un bot discord + API wagtail)

## Solution technique
* **langage** : python
* **librairie de test** : django.test, wagatail.test
* **framework** : django
* **cms** : wagtail
* **serveur de base de données** : postgresql
