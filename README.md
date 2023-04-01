# Technical Test For AquaTech

Update : I was hired !!

The test was conducted as part of an application to AquaTech. The aim is to create a data generator simulating data from two different sensors (water level and pressure sensor). In order to analyze these data, it was necessary to display them as a graph. To do this, I had to create a frontend and a backend in order to retrieve and display them.

## Les technologies 

#### Database - MySQL
> The database was selected based on 3 factors: speed, ease of use and experience. Indeed, a relational database is not necessarily necessary, but the 3 criteria mentioned above led me to this choice.

### Data Generator - Python 
> To make the data generator, I chose the python language. The biggest factor was that the language had to be able to use the generators in order not to store the data between the time it is generated and when it is stored in the DB (this is the case with `yield`). Moreover, thanks to its ease of learning, my experience with this language and its versatility have strengthened my choice.

### BackEnd - Flask (SQLAlchemy)
> The backend followed logically since I wanted to integrate the generator with it. The fact that flask allows to create clear and well defined APIs and its documentation is well supplied was important. Moreover, it is a rather light framework in itself with simplified routing. I chose to also use the SQLAlchemy ORM to secure the database from any external and potentially malicious interactions.

### Frontend - VueJS
> Light and minimalist at the base, the ability to add even the necessary tools makes it a flexible framework for each project. Its small size does not mean a lower speed and its detailed documentation is a big +. 'Chartjs', a graphics creation module also tipped the scales. Having already an experience with it, but also due to the fact that it is a great future ahead of it, I chose to continue to progress on it.

## Get Started

Thanks to docker, a single command line is needed to install the project under Linux: 

- With docker compose v2 => ```docker compose up```
- Avec docker compose v1 => ```docker-compose up```

> Docker v19.03.0 or more is required

Once containers launch, in your browser enter ```localhost:3080``` then click on **Générer les données**.

## Explaination of data generator

The generator works thanks to a random phase system (decrease, stability and increase). Each phase lasts between 1 and 120 minutes randomly. Between each data, each minute, a step is randomly defined in a range specific to each sensor (0.0 - 1.0 for the water level sensor and 0.00 - 0.01 for the pressure sensor). Finally, a system to avoid blocking more than 120 minutes at the min and max values of each sensor has been put in place.

## Bonus 

You can regenerate data at your convenience with the button **Refresh**.

## Realised by
- [@Mehdi-fsn](https://github.com/Mehdi-fsn)# Technical Test AquaTech
