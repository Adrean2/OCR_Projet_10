# OCR_Projet_10

## Création de l'environnement virtuel
### Pipenv
Il faudra installer Pipenv sur votre machine afin de créer un environnement virtuel avec la commande: <br>
```pip install pipenv```

### Placez-vous ensuite dans le répertoire SoftDesk puis activez l'environnement virtuelle avec : <br>```pipenv shell```
![pipenvshell](https://puu.sh/IGZWY/ea4dd7b48b.png)

## Requirements
Cette API utilise Django Rest Framework (DRF), l'authentification simplejwt ainsi que drf-nested-routers afin de répondre aux exigences du projet.<br>
Pour installer les requirements, l'environnement virtuel activé et toujours placé dans le répertoire SoftDesk utilisez la commande: <br>
``` pip install -r requirements.txt```

## Utilisation de l'API
### Démarrer le serveur
Une fois l'environnement virtuel activé,toujours placé dans le répertoire SoftDesk, démarrez le serveur avec la commande : <br>```python manage.py runserver```<br>
![runserver](https://puu.sh/IGZX3/80973f0f9e.png)<br>
Ca y est, vous avez accès à l'API! Il ne reste plus qu'à suivre la documentation des point de terminaisons.

###	Point de terminaison d'API	Méthode HTTP	URI
![endpoints1](https://puu.sh/IGZPc/9869e55d43.png)<br>
![endpoints2](https://puu.sh/IGZPl/b2ae6b52d5.png)

### Postman
Vous pouvez accéder à toute la documentation postman [ici](https://documenter.getpostman.com/view/18150156/UVeGqkr4).
