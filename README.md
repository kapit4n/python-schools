# school-events-dj


## run project
### with docker
- `docker-compose up`

### with conda
- `conda create --name my_env python=3`
- `conda activate my_env`
- `python manage.py runserver`

## login
POST http://localhost:8000/api-auth/login

## resources
```
{
    "heroes": "http://localhost:8000/heroes/",
    "projects": "http://localhost:8000/projects/",
    "roles": "http://localhost:8000/roles/",
    "employees": "http://localhost:8000/employees/",
    "teams": "http://localhost:8000/teams/",
    "members": "http://localhost:8000/members/"
}
```
## create new user
- ``` docker-compose run app python manage.py createsuperuser ```

## mofify models and run
- ```docker-compose run app python manage.py makemigrations```
- ```docker-compose run app python manage.py migrate```

## 
