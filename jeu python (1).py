# -*- coding: utf-8 -*-
import sys
import pygame

pygame.init()  # Initialisation du module "pygame"

# Création de la fenêtre
fenetre = pygame.display.set_mode((850, 600))
pygame.display.set_caption("Jeu Game")

# Chargement de l'image de fond
background_image = pygame.image.load("Background.png").convert()
background_image = pygame.transform.scale(background_image, (850, 600))  # Redimensionnement si nécessaire
bg_width = background_image.get_width()

score = 0
niveau= 0


# Position horizontale de l’image de fond
bg_x = 0
bg_speed = 4  # Vitesse de défilement (pixels par frame)


def dessiner():
    global bg_x

    # Mise à jour de la position
    bg_x += bg_speed
    if bg_x >= bg_width:
        bg_x = 0  # Réinitialisation quand l'image a complètement défilé

    # Affichage des deux images pour effet de boucle
    fenetre.blit(background_image, (-bg_x, 0))
    fenetre.blit(background_image, (bg_width - bg_x, 0))



    # Mise à jour de l'écran
    pygame.display.flip()

# Fonction pour gérer les événements clavier et souris
def gererClavierEtSouris():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Horloge pour gérer le temps
clock = pygame.time.Clock()

# Boucle principale
continuer = True
while continuer:
    clock.tick(50)  # 50 FPS
    dessiner()
    gererClavierEtSouris()

# Fin propre
pygame.quit()
sys.exit()
