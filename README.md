## Installation
  - Cloner le repo `$ git clone https://github.com/P0NE/sentryo-api.git`
  - Se mettre dans le répertoire `$ cd /sentryo-api`
  - Creér un environnement virtuel `$ python -m venv venv`
  - Installer les dépendances `$ pip install requirements.txt`
  - Créer un fichier `.env` avec :
      ```
      FLASK_ENV=development
      DATABASE_URL=sqlite:///../data/swapi.dat
      JWT_SECRET_KEY=bonjoursentryo
      ```
  - Démarrer l'app avec `python run.py`

## Explication
  - J'ai d'abord tenter le test technique en GO mais je me suis confronter à un problème en voulant utiliser GORM pour le mapping relationnel, notamment avec ce bout de code : 
    ```
    var peoples []People
	if err = db.Table("People").Joins("LEFT JOIN people_vehicles on people_vehicles.people=people.id").
		Joins("LEFT JOIN vehicles on vehicles.id=people_vehicles.vehicles").Preload("Vehicles").Find(&peoples).Error; err != nil {
		log.Fatal(err)
	}
    ```
    J'espère pouvoir en discuter avec vous.
    J'ai donc décidé de faire le projet dans un language que je maitrise mieux à l'heure actuelle: Python.
    Pour les APIs j'ai fait le choix d'utiliser `Flask-rest-plus` que je trouve très pratique et facile à utiliser pour ce genre de projet et pour le framework ORM j'ai choisi `SQLAlchemy`
    Je n'ai pas fini tout ce que je souhaitais faire à cause du temps. J'ai listé dans la partie d'après tout ce que je peux rajouter.

## TODOS
  - Ajouter la définition swagger pour les différents Endpoint.
  - Ajouter les TU pour tester les modèles et les views (request, response, status code...)
  - Ajouter une authentification par JWT
  - Ajouter la possibilité de lier un people avec un vehicle et un starship.
  - Modifier la base de données, notamment les types de certains champs et certaines colonnes de la table people (vehicles ?, Starships ?)