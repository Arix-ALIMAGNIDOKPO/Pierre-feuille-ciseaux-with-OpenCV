# Jeu de pierre-feuille-ciseaux avec IA

Ce projet utilise la bibliothèque opencv-python pour recréer le célèbre jeu de pierre-feuille-ciseaux de manière interactive avec l'Intelligence Artificielle (IA). Ce jeu utilise la vision par ordinateur pour reconnaître la main et les différents signes de l'utilisateur, et affiche le résultat du duel entre l'utilisateur et l'IA. Les règles du jeu sont simples : la pierre bat les ciseaux, les ciseaux battent la feuille et la feuille bat la pierre. 

## Installation

Pour installer les dépendances nécessaires, vous devez avoir python 3.9 ou 3.10 installé sur votre machine. Ensuite, vous pouvez exécuter la commande suivante dans le répertoire du projet :

`pip install -r requirements.txt`

Cette commande va installer les packages suivants :

- opencv-python
- cvzone
- mediapipe

## Utilisation

Pour lancer le jeu, vous devez exécuter le fichier main.py avec la commande suivante :

`python main.py`

Une fenêtre va s'ouvrir avec la caméra de votre ordinateur. Appuyez sur la touche S de votre clavier pour lancer un tour. Vous devez placer votre main devant la caméra et faire un signe de pierre, de feuille ou de ciseaux avant la fin du décompte de 3 secondes. L'IA va faire un signe aléatoire et le comparer au vôtre. Le score de chaque joueur s'actualise après chaque tour. Le premier joueur qui atteint 10 points remporte le jeu.