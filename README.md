# Festival-API

Voor veel festivals hebben we veel werknemers nodig die op verschillende locaties werken.
Hiervoor heb ik een Festival-API gemaakt die het makkelijk maakt om users te koppelen aan festival en locaties aan festivals.
We kunnen Festivals, Locaties en Users aanmaken en deze terug ophalen.


# Authenticatie GET & POST users

Als eerste maken we een gebruiker aan met de POST user. Hier kunnen we de gegevens van de werknemer toevoegen die nodig zijn om het te koppelen aan een festival.
![image](https://github.com/bervoetshannes/API-python/assets/47882529/f617ba77-3f51-4397-9c3a-4fae57ad8e3c)
We geven deze 3 parameters: email, passwoord en is_active


Als we een werknemer terug willen vinden gebruiken we de GET user. Hieronder bevindt zich de GET van de users die aangemaakt zijn voor de authenticatie.
![image](https://github.com/bervoetshannes/API-python/assets/47882529/aef80b93-e170-4717-9485-9080f7e9b322)
Met behulp van skip en limit kunnen en we een exact aantal users laten zien.
Zelf heb ik een extra parameter active erbij gestoken voor het kijken of de gebruiker nog actief is.

# POST Locatie

Elk Festival zit op één bepaalde locatie, maar dit wilt niet zeggen dat elke locatie maar één festival heeft.
Daarom is het belangrijk om eerst de locaties aan te maken voordat een festival aangemaakt kan worden.
Bij een Locatie geven we 3 parameters terug: naam, lat en lon. 
De naam voor te weten hoe de locatie heet en de lat en lon voor de coördinatie van de locatie.

![image](https://github.com/bervoetshannes/API-python/assets/47882529/ec78f804-7547-48a5-97d5-10a9cb9ce9ed)

# GET Locatie

Hier vragen we de locaties voor de festivals
![image](https://github.com/bervoetshannes/API-python/assets/47882529/34bc1a19-9f59-46a7-8894-6aabdc5cb390)


# POST Festival
Bij het aanmaken van een festival hebben we  parameters: de naam van het festival, de locatie_id, begin datum en einddatum
We hebben hier alleen maar de id van de locatie nodig voor het terugkoppelen naar de andere gegevens
Hiervoor hebben we 2 classes voor festival, één voor de POST (CreateFestival) en één voor de GET (ListFestival).

![image](https://github.com/bervoetshannes/API-python/assets/47882529/bca88aad-380a-4d99-9a09-43dcef0a04e1)

# Get Festival

Eens we een festival hebben gemaakt willen we deze terug kunnen opvragen met de GET functie.

![image](https://github.com/bervoetshannes/API-python/assets/47882529/85c924a1-091f-4f30-9612-a80d0fb3e3e7)



# PUT Festival
Soms willen we aanpassingen maken in de naam van een fetsival, hiervoor wordt een PUT gebruikt.

![image](https://github.com/bervoetshannes/API-python/assets/47882529/6c073c90-d440-46e5-b593-2793709ad1c4)


# DELETE User
Als er een werknemer niet meer werkt op festivals gaan we deze Delete.
Dit doen we aan de hand van de user id
![image](https://github.com/bervoetshannes/API-python/assets/47882529/f51ba141-6435-4498-b9ea-2db36fd6e28a)

# Users linken aan Festivals

Voor het einddoel van deze API gaan we de werkenemers linken aan een festival.
Dit doen we met een extra POST functie.
We gebruiken de user_id en festival_id om deze samen in d-een schema te zetten.

![image](https://github.com/bervoetshannes/API-python/assets/47882529/72a7ab7e-b60d-4794-931c-947d7c55cd6a)

Als de POST goed gelukt is krijgen we een extra text met de user email en het gekoppelde festival.


![image](https://github.com/bervoetshannes/API-python/assets/47882529/8017a59c-72cb-4ff2-86dd-8f3658aadf7e)

Hierboven zien we een extra gemaakte schema om de 2 ids te koppelen met elkaar.


# FASTAPI Docs

![image](https://github.com/bervoetshannes/API-python/assets/47882529/27d06dc9-f1c9-429b-bbc3-3f4a97e3d5d2)

Hier staat een klein overzicht van al onze CRUD requests.
Bij het slot wordt een authenticatie gevraagd.

# Docker, Docker-Compose en Okteto
## Docker
![image](https://github.com/bervoetshannes/API-python/assets/47882529/142e357d-212e-4e99-ba2c-242b36b90493)
Hier ziet u mijn opgebouwde Dockerfile hoe deze wordt opgebouwd


## docker-compose
Met docker-compose builden we onze image vanzelf vanuit Docker.

![image](https://github.com/bervoetshannes/API-python/assets/47882529/446653b1-a883-44b7-beab-cc6748e67e55)

Hier zien we dat we de image r0695672/api-festival uit docker halen en deze hierna te builden.

## Okteto
Eens de repository gelinkt is met github langs docker-compose kunnen we deze verbinden met een okteto cloud account.