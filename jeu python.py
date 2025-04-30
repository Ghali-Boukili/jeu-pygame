# -*- coding: utf-8 -*-

import pygame

pygame.init() # initialisation du module "pygame" 

fenetre = pygame.display.set_mode( (600,600) ) # Création d'une fenêtre graphique de taille 600x600 pixels
pygame.display.set_caption("Space Invader") # Définit le titre de la fenêtre





## A la fin, lorsque l'on sortira de la boucle, on demandera à Pygame de quitter proprement
pygame.quit()
