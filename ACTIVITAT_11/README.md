# ACTIVITAT_11

## Base de dades

### Disseny Base de Dades

![Resultat](./images/Penjat_BD.drawio.png)

### Base de Dades creada a Postgresql
#### He afegit una taula amb els intents per a registrar cada vegada que el jugador usa una lletra

![Resultat](./images/tables_created.png)

### Taula Attempt
#### Aquesta taula té els següents camps:

![Resultat](./images/updated_bd.png)

#### Amb el is_correct podem després treure els errors que ha fet en la partida corresponent.

### Taula Log_Record
#### He afegit el camp "best_game_points" i he modificat el nom del camp "best_game" a "best_game_date":

![Resultat](./images/new_field.png)

### Ho he modificat ja que abans tenía només la data al camp, no guardaba els millors punts que habia aconseguit en la partida

## Endpoints amb Swagger

### GET /penjat/start-game

#### Aquest endpoint serveix per a l'endpoint 1 i 2 demanats ja que retorna el mateix text recollint-lo de la base de dades

![Resultat](./images/start_game.png)

### GET /penjat/errors/{log_id}
#### Retorna el nombre d'errors
![Resultat](./images/errors.png)

### POST /penjat/attempts
#### Per Insertar un intent
![Resultat](./images/post_attempts.png)

### GET /penjat/alphabet/{lang}
#### Agafar l'abecedari corresponent
![Resultat](./images/alphabet.png)

### GET /penjat/game/{log_id}
#### Agafar les estadístiques del jugador
![Resultat](./images/player_record.png)