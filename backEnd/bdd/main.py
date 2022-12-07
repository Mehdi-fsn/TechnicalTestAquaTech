from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Engine qui permet la connexion à la base de données (user:mdp@host/base)
engine = create_engine("mysql+mysqldb://userdb:root@localhost/TestTechniqueAquaTech?charset=utf8mb4")

# Création d'une session pour l'éxecution des requêtes
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)