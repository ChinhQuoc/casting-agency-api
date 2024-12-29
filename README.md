# Backend - Casting Agency

## Setting up the Backend

### Install Dependencies

1. **Python 3.7**

2. Open terminal and run command:

```bash
pip install -r requirements.txt
```

### Set up the Database

With Postgres running, create a `casting_agency` database:

```bash
createdb casting_agency
```

Populate the database using the `casting_agency.psql` file provided. Open terminal run:

```bash
psql casting_agency < casting_agency.psql
```

### Run the Server

On the folder project, Open terminal and run:

```bash
python app.py
```

## Documenting your Endpoints

`GET '/movies'`

- Get list movies
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `movies`: A list of question objects, each containing `id`, `releaseDate`, and `title`.

```json
{
  "movies": [
    {
      "id": 2,
      "releaseDate": "Tue, 24 Dec 2024 00:00:00 GMT",
      "title": "ggi uu kiguf"
    },
    {
      "id": 1,
      "releaseDate": "Wed, 20 May 2020 00:00:00 GMT",
      "title": "Bad Boys for Life update"
    }
  ],
  "success": true
}
```

`GET '/actors'`

- Get list actor
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `actors`: A list of question objects, each containing `id`, `age`, `gender`, and `name`.

```json
{
  "actors": [
    {
      "age": 57,
      "gender": "male",
      "id": 1,
      "name": "Johnny Depp"
    },
    {
      "age": 5,
      "gender": "female",
      "id": 3,
      "name": "fwe Anna"
    },
    {
      "age": 13,
      "gender": "male",
      "id": 4,
      "name": "Gta de fff"
    },
    {
      "age": 9,
      "gender": "female",
      "id": 6,
      "name": "hgf uuy 1"
    }
  ],
  "success": true
}
```

`GET '/movies/<int:id>'`

- Get a specific movie identified by its unique id.
- URL Parameters:
  - `id`: An integer representing the unique identifier of the movie to be deleted.
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `movie`: A object movie and along with the corresponding actor list, each containing `id`, `releaseDate`, `title`, and a list of `actors`.

```json
{
  "movie": {
    "actors": [
      {
        "age": 5,
        "gender": "female",
        "id": 3,
        "name": "fwe Anna"
      },
      {
        "age": 13,
        "gender": "male",
        "id": 4,
        "name": "Gta de fff"
      }
    ],
    "id": 2,
    "releaseDate": "Tue, 24 Dec 2024 00:00:00 GMT",
    "title": "ggi uu kiguf"
  },
  "success": true
}
```

`GET '/actors/<int:id>'`

- Get a specific actor identified by its unique id.
- URL Parameters:
  - `id`: An integer representing the unique identifier of the actor to be deleted.
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `actor`: A object actor and along with the corresponding actor list, each containing `id`, `age`, `gender`, `name` and a list of `movies`.

```json
{
  "actor": {
    "age": 13,
    "gender": "male",
    "id": 4,
    "movies": [
      {
        "id": 2,
        "releaseDate": "Tue, 24 Dec 2024 00:00:00 GMT",
        "title": "ggi uu kiguf"
      }
    ],
    "name": "Gta de fff"
  },
  "success": true
}
```

`DELETE '/movies/<int:id>'`

- Delete a specific movie identified by its unique id.
- URL Parameters:
  - `id`: An integer representing the unique identifier of the movie to be deleted.
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `delete`: An id of the movie is deleted
- Possible Responses:
  - Returns a `404` status if the movie's id is not match any ids movie in the database.

```json
{
  "delete": 1,
  "success": true
}
```

`DELETE '/actors/<int:id>'`

- Delete a specific actor identified by its unique id.
- URL Parameters:
  - `id`: An integer representing the unique identifier of the actor to be deleted.
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `delete`: An id of the actor is deleted
- Possible Responses:
  - Returns a `404` status if the actor's id is not match any ids actor in the database.

```json
{
  "delete": 1,
  "success": true
}
```

`POST '/movies'`

- Create a movie based on the payload Webapp request to.
- Request Body: A JSON object containing:
  - `title`: A string representing the title.
  - `releaseDate`: A string representing the release date.
  - `idsActor`: An array representing the ids actor.
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `movie`: An object representing the selected question, containing `id`, `title`, and `releaseDate`.
- Possible Responses:

  - Returns a `422` status if title or releaseDate isn't contained in body.

- Body

```json
{
  "title": "iphone",
  "releaseDate": "2024-12-23T18:10:28.596Z",
  "idsActor": [1, 3]
}
```

`POST '/actors'`

- Create an actor based on the payload Webapp rquest to.
- Request Body: A JSON object containing:
  - `name`: A string representing the name.
  - `age`: A number representing the age.
  - `gender`: A number representing the gender.
  - `idsMovie`: An array representing the ids movie.
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `movie`: An object representing the selected question, containing `id`, `name`, `age`, and `gender`.
- Possible Responses:

  - Returns a `422` status if name isn't contained in body.

- Body

```json
{
  "name": "test actor",
  "age": 6,
  "gender": "male",
  "idsMovie": [1, 3]
}
```

`PATCH '/movies/<int:id>'`

- Update a specific movie identified by its unique id.
- Request Body: A JSON object containing:
  - `id`: A number representing the id.
  - `releaseDate`: A string representing the releaseDate.
  - `idsActor`: An array representing the ids actor.
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `movie`: An object representing the selected question, containing `title`, and `releaseDate`.
- Possible Responses:

  - Returns a `404` status if the movie's id is not match any ids movie in the database.
  - Returns a `422` status if title or release isn't contained in body.

- Body

```json
{
  "title": "ggi uu kiguf",
  "releaseDate": "2024-12-26T17:00:00.000Z",
  "idsActor": [3, 4, 7, 8, 9, 10]
}
```

`PATCH '/actors/<int:id>'`

- Update a specific actor identified by its unique id.
- Request Body: A JSON object containing:
  - `name`: A string representing the name.
  - `age`: A number representing the age.
  - `gender`: A number representing the gender.
  - `idsMovie`: An array representing the ids movie.
- Returns: An object with the following keys:
  - `success`: A boolean indicating the request status.
  - `actor`: An object representing the selected question, containing `id`, `name`, `age`, and `gender`.
- Possible Responses:

  - Returns a `404` status if the actor's id is not match any ids actor in the database.
  - Returns a `422` status if name isn't contained in body.

- Body

```json
{
  "id": 1,
  "name": "test actor",
  "age": 6,
  "gender": "male",
  "idsMovie": [1, 3]
}
```
