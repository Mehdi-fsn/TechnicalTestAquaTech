import random
from datetime import datetime, timedelta


def generatorEau():
    ### Valeur de réglages du générateur ###
    vMin = 0
    vMax = 300  # cm
    vCurrent = 150  # Niveau actuel

    upDown = 1  # 0 = phase reduction du niveau, 1 = phase d'augmentation du niveau
    time = 0  # 1 à 120 minutes (durée de phase)
    step = 0  # 0.0 à 1.0 (step entre chaque données)

    date = datetime(2022, 11, 27, 23, 59)

    count = 0  # Compteur de données
    countBlock = 0  # Compteur pour éviter les blocages au min et max plus de 120 minutes
    ########################################

    # System
    while (count < 10080):
        upDown = random.randint(0, 1)
        time = random.randint(1, 120)

        for t in range(time):
            step = round(random.uniform(0, 1), 2)

            #  Config de la date
            date += timedelta(minutes=1)

            #  Config de la donnée de niveau Eau
            vCurrent = setCurrentValue(upDown, step, vCurrent, vMin, vMax, 2)
            
            #  Renvoi de la donnée avec un générateurs pour ne pas utiliser la mémoire interne 
            yield {
                "date" : date,
                "vCurrent" : vCurrent
            }

            # Permet d'éviter le blocage à la valeur max ou min plus de 120 minutes
            countBlock = stopBlock(vCurrent, vMin, vMax,
                                   countBlock, upDown).get("countBlock")
            upDown = stopBlock(vCurrent, vMin, vMax,
                               countBlock, upDown).get("upDown")

            count += 1
            if (count == 10080):
                break


def generatorPression():
    ### Valeur de réglages du générateur ###
    vMin = 1
    vMax = 4  # bar
    vCurrent = 2.5  # Pression actuel

    upDown = 1  # 0 = phase reduction du niveau, 1 = phase d'augmentation du niveau
    time = 0  # 1 à 120 minutes (durée de phase)
    step = 0  # 0.0 à 0.01 (step entre chaque données)

    date = datetime(2022, 11, 27, 23, 59)

    count = 0  # Compteur de données
    countBlock = 0  # Compteur pour éviter les blocages au min et max plus de 120 minutes
    ########################################

    # System
    while (count < 10080):
        upDown = random.randint(0, 1)
        time = random.randint(1, 120)

        for t in range(time):
            step = round(random.uniform(0, 0.01), 5)

            #  Config de la date
            date += timedelta(minutes=1)

            #  Config de la donnée pression
            vCurrent = setCurrentValue(upDown, step, vCurrent, vMin, vMax, 5)
            
            #  Renvoi de la donnée
            yield {
                "date" : date,
                "vCurrent" : vCurrent
            }

            # Permet d'éviter le blocage à la valeur max ou min plus de 120 minutes
            countBlock = stopBlock(vCurrent, vMin, vMax,
                                   countBlock, upDown).get("countBlock")
            upDown = stopBlock(vCurrent, vMin, vMax,
                               countBlock, upDown).get("upDown")

            count += 1
            if (count == 10080):
                break


#  Configuration de la donnée actuelle
def setCurrentValue(upDown, step, vCurrent, vMin, vMax, arroundValue):
    match upDown:
        case 0:
            vCurrent -= step
        case 1:
            vCurrent += step

    if (vCurrent < vMin):
        vCurrent = vMin
    if (vCurrent > vMax):
        vCurrent = vMax

    return round(vCurrent, arroundValue)

# Permet d'éviter le blocage à la valeur max ou min plus de 120 minutes
def stopBlock(vCurrent, vMin, vMax, countBlock, upDown):
    if (vCurrent == vMin or vCurrent == vMax):
        countBlock += 1
        if (countBlock == 120):
            countBlock = 0
            match upDown:
                case 0:
                    upDown = 1
                case 1:
                    upDown = 0
    else:
        countBlock = 0

    return {
        "countBlock": countBlock,
        "upDown": upDown
    }


