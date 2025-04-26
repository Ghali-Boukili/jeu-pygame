# -*- coding: utf-8 -*-

import pygame

pygame.init() # initialisation du module "pygame" 

fenetre = pygame.display.set_mode( (600,600) ) # Création d'une fenêtre graphique de taille 600x600 pixels
pygame.display.set_caption("Space Invader") # Définit le titre de la fenêtre


# Chargement des images:
#    On définit et affecte les variables qui contiendront les images du vaisseau ou de l'alien
imageAlien = pygame.image.load("alien.png")
imageVaisseau = pygame.image.load("vaisseau.png")
imageVaisseau = pygame.transform.scale(imageVaisseau, (64, 64)) # On redimensionne l'image du vaisseau à une taille de 64x64 pixels

# On définit les variables qui contiendront les positions des différents éléments (vaisseau, alien, projectile)
# Chaque position est un couple de valeur '(x,y)'
positionVaisseau = (300,525)
positionAlien = (300,10)
projectile = (-1, -1)


# Fonction en charge de dessiner tous les éléments sur notre fenêtre graphique.
# Cette fonction sera appelée depuis notre boucle infinie
def dessiner():
    global imageAlien, imageVaisseau, fenetre, projectile
    # On remplit complètement notre fenêtre avec la couleur noire: (0,0,0)
    # Ceci permet de 'nettoyer' notre fenêtre avant de la dessiner
    fenetre.fill( (0,0,0) )    
    fenetre.blit(imageVaisseau, positionVaisseau) # On dessine l'image du vaisseau à sa position
    fenetre.blit(imageAlien, positionAlien)  # On dessine l'image du vaisseau à sa position
    if projectile != (-1, -1):
        pygame.draw.circle(fenetre, (255,255,255), projectile, 5) # On dessine le projectile (un simple petit cercle)
    pygame.display.flip() # Rafraichissement complet de la fenêtre avec les dernières opérations de dessin


# Fonction en charge de gérer les évènements clavier (ou souris)
# Cette fonction sera appelée depuis notre boucle infinie
def gererClavierEtSouris():
    global continuer, positionVaisseau, projectile
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
            continuer = 0
    # Gestion du clavier: Quelles touches sont pressées ?
    touchesPressees = pygame.key.get_pressed() 
    if touchesPressees[pygame.K_SPACE] == True:
        projectile = (positionVaisseau[0],positionVaisseau[1])
    if touchesPressees[pygame.K_RIGHT] == True:
        positionVaisseau = ( positionVaisseau[0] + 5 , positionVaisseau[1] )
    if touchesPressees[pygame.K_LEFT] == True:
        print("Le vaisseau doit faire un 'pas' vers la gauche")


# On crée une nouvelle horloge qui nous permettra de fixer la vitesse de rafraichissement de notre fenêtre
clock = pygame.time.Clock()

# La boucle infinie de pygame:
# On va continuellement dessiner sur la fenêtre, gérer les évènements et calculer certains déplacements
continuer = 1
while continuer==1:
    # pygame permet de fixer la vitesse de notre boucle:
    # ici on déclare 50 tours par secondes soit une animation à 50 images par secondes
    clock.tick(50) 

    dessiner()
    gererClavierEtSouris()

    # On fait avancer le projectile (si il existe)
    if projectile != (-1, -1):
        projectile = (projectile[0], projectile[1] - 5) # le projectile "monte" vers le haut de la fenêtre



## A la fin, lorsque l'on sortira de la boucle, on demandera à Pygame de quitter proprement
pygame.quit()
