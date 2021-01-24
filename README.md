# Casting Agency
Casting Agency is a company that is responsible for creating movies and managing movies and assigning actors with different roles. there are three different roles which are Assistant role, Director Role and Producer role,all have different permissions to perform actions on database

Here is hosted heroku [Link]()

## Motivation for project 

This is the capstone project for Full Stack Nano Degree program by Udacity


```

## Project Dependencies

#### Python 3 

Install letest version of python3 [here] (https://www.python.org/downloads/)

#### Virtual Enviornment


You can create python virtual environment.Instruction for create virtual enviornment is [here] (https://docs.python.org/3/tutorial/venv.html)

Example in my code :

conda create -n myenv python=3.6

source activate myenv

For python virtual enviornment setup you can do following in your terminal

python3 -m venv env source env/bin/activate

for more details check [this] (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


After creating virtual environment hit following command to install project requirements.

```
pip install -r requirements.txt

```




#### Run server      

```
 python3 app.py 
```

### Task for Setup Auth0 

1. Create a new Auth0 Account
2. Select a unique tenant domain 
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    
    - `get:actors`
    - `get:movies`
    - `post:actors`
    - `post:movies`
    - `patch:actors`
    - `patch:movies`
    - `delete:actors`
    - `delete:movies`
    

6. Create new roles for:
    - Assistant
      - Can view all actors and all movies

    - Casting Director
        - All permissions a Casting Assistant has and…
        - Add or delete an actor from the database
        - Modify actors or movies

    - Executive Producer
        - All permissions a Casting Director has and…
        - Add or delete a movie from the database

7. Endpoints



## Authentication

The API has three registered users:

1. Assistant

```
email: assistant@hotmail.com
password: Assistant@41
```

2. Director

```
email: director.casting@hotmail.com
password: Director@41
```

3. Producer

```
email: executive.producer@hotmail.com
password: Executive@41
```

The Auth0 domain and api audience can be found in `setup.sh`.



# Endpoints

GET
POST
PATCH
DELETE


```
GET ‘/movies’ 
 
- get a List of all Available Movies

http://0.0.0.0:8080/movies

Response:
{
  "movies": [
    {
      "id": 1,
      "release_date": "Sun, 24 Jan 2021 00:00:00 GMT",
      "title": "Suit"
    },
    {
      "id": 2,
      "release_date": "Sun, 24 Jan 2021 2020 00:00:00 GMT",
      "title": "Lost"
    },
    {
      "id": 3,
      "release_date": "Sun, 24 Jan 2021 00:00:00 GMT",
      "title": "Last of us"
    },
    {
      "id": 4,
      "release_date": "Sun, 24 Jan 2021 00:00:00 GMT",
      "title": "Game of End"
    }
  ],
  "status_code": 200,
  "success": true,
  "total_record": 4
}



GET ‘/actors’

- Get a List of all Available Actors

Request : 

http://0.0.0.0:8080/actors

Response:

{
  "actors": [
    {
      "age": 31,
      "gender": "Male",
      "id": 1,
      "name": "Abdulaziz MS"
    },
    {
      "age": 40,
      "gender": "Male",
      "id": 2,
      "name": "Talal Ahmad"
    },
    {
      "age": 45,
      "gender": "Male",
      "id": 3,
      "name": "Bader Khaled"
    },
    {
      "age": 60,
      "gender": "Male",
      "id": 4,
      "name": "Tomy Tomy"
    }
  ],
  "status_code": 200,
  "success": true,
  "total_record": 4
}




DELETE ‘/movies/<int:movie_id>’

- Delete Movie with specific Movie id

Request :

http://0.0.0.0:8080/movies/1

Response :

{
   "movie_id": 1,
   "status_code": 200,
   "success": true
}


DELETE ‘/actors/<int:actor_id>’
- Delete Actor with specific Actor id

Request  :

http://0.0.0.0:8080/actors/1

Response :

{
   "actor_id": 1,
   "status_code": 200,
   "success": true
}


POST '/actors'
- This endpoint is used for creating new actor

Request body:
{
  "name":"kahled tlal",
  "age":30,
  "gender": "Male"
}
Give Authorization : 'Bearer TOKEN'
    
Returns:

  {
    "actor": {
      "age": 30,
      "gender": "Male",
      "id": 5,
      "name": "kahled tlal"
    },
    "message": "kahled tlal created",
    "status_code": 200,
    "success": true
  }
  


```



    
   






