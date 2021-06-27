# Simple API for Adverts

## How to run
- Clone repo 
- Activate env ``` source env/bin/activate ```
- Install all requirements ``` pip install -r requirements.txt ```
- Come to project directory ``` cd advert/ ```
- Run project on 8000 port ``` python manage.py runserver 8000 ```

See all adverts: http://127.0.0.1:8000/ads/

See advert by id: http://127.0.0.1:8000/ads/2

# Response structure
```json
[
{
"id": 1,
"subject": "bil till salu",
"body": "det ar min alsklig bil",
"price": "0.00",
"email": "asd@assd.asd"
},
{
"id": 2,
"subject": "basta bord",
"body": "nu saljar jag min bord",
"price": "0.00",
"email": "adddd@as33d.com"
},
...
```